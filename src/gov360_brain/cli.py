from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import jsonschema
import yaml

from .adapters import get_default_registry
from .domains import DomainManager
from .llm import OpenAICompatibleClient, OpenAISettings
from .context import ContextBuilder
from .orchestration.approval import ApprovalManager
from .orchestration.ingestion import IngestionOrchestrator
from .orchestration.pipeline import KnowledgePipeline
from .orchestration.state import RunJournal, SourceCatalog
from .project import ProjectPaths
from .utils import atomic_write_json, read_jsonl
from .vault import VaultAuditor, VaultPublisher, normalize_note_file


def _json(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))


def _profile(paths: ProjectPaths, name: str) -> dict[str, Any]:
    path = paths.root / "config" / "profiles" / f"{name}.yaml"
    if not path.exists():
        raise ValueError(f"Unknown profile: {name}")
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    schema = json.loads((paths.root / "config" / "schemas" / "profile.schema.json").read_text(encoding="utf-8"))
    jsonschema.validate(value, schema)
    return value


def _domain_rows(paths: ProjectPaths, domain_id: str) -> list[dict[str, Any]]:
    return [row for row in read_jsonl(paths.state / "source_manifest.jsonl") if domain_id in row.get("domains", [])]


def _execute_run(paths: ProjectPaths, domain: str, profile_name: str) -> dict[str, Any]:
    profile = _profile(paths, profile_name)
    domains = DomainManager(paths)
    pack = domains.load(domain)
    initial_status = pack.status
    if initial_status == "DRAFT":
        pack = domains.set_status(pack.slug, "INGESTING")
    journal = RunJournal.create(paths, domain_id=pack.domain_id, profile=profile_name)
    try:
        registry = get_default_registry()
        ingestion = IngestionOrchestrator(paths, registry, light_workers=int(profile.get("max_light_workers", 2)))
        discovered = ingestion.inventory(pack, journal)
        normalized = ingestion.ingest(pack, discovered, profile=profile_name, journal=journal)
        records = _domain_rows(paths, pack.domain_id)
        source_ids = {str(row["source_id"]) for row in records if row.get("status") not in {"QUARANTINED", "RETIRED", "SUPERSEDED"}}
        validation = ingestion.validate_existing(source_ids)
        invalid = sum(1 for item in validation if not item.get("valid"))
        summary: dict[str, Any] = {
            "run_id": journal.run_id,
            "domain_id": pack.domain_id,
            "profile": profile_name,
            "discovered_sources": len(discovered),
            "normalized": sum(1 for item in normalized if item.get("status") == "NORMALIZED"),
            "normalization_noop": sum(1 for item in normalized if item.get("status") == "NOOP"),
            "quarantined": sum(1 for row in records if row.get("status") == "QUARANTINED"),
            "normalization_failed": sum(1 for item in normalized if item.get("status") == "FAILED"),
            "invalid_ingest": invalid,
            "llm_calls": 0,
        }
        if invalid or summary["normalization_failed"]:
            journal.finish("FAILED", **summary)
            return {**summary, "status": "FAILED"}
        # `run` is deliberately the source-to-Markdown boundary. It never
        # constructs an LLM client; `generate` is the separate downstream stage.
        status = "SUCCEEDED"
        if initial_status == "DRAFT":
            domains.set_status(pack.slug, "REVIEW_REQUIRED")
        _rebuild_vault_index(paths)
        journal.finish(status, **summary)
        return {**summary, "status": status}
    except Exception:
        journal.finish("FAILED")
        if initial_status == "DRAFT":
            domains.set_status(pack.slug, "REVIEW_REQUIRED")
        raise


def _rebuild_vault_index(paths: ProjectPaths) -> bool:
    """Keep the historical indexer away from the active Markdown vault."""

    if (paths.vault / "SCHEMA.md").exists():
        return False
    VaultPublisher(paths).rebuild_index()
    return True


def _execute_generate(paths: ProjectPaths, domain: str, profile_name: str) -> dict[str, Any]:
    if profile_name == "codex-direct":
        pack = DomainManager(paths).load(domain)
        journal = RunJournal.create(paths, domain_id=pack.domain_id, profile=profile_name)
        records = _domain_rows(paths, pack.domain_id)
        units = []
        for row in records:
            document_path = paths.ingest / str(row["source_id"]) / "document.json"
            if not document_path.exists():
                continue
            document = json.loads(document_path.read_text(encoding="utf-8"))
            if document.get("validation", {}).get("valid") is True and document.get("source_sha256") == row.get("source_sha256"):
                units.append({"source_id": row["source_id"], "source_sha256": row["source_sha256"], "unit_count": len(document.get("units", [])), "ingest_path": f"ingest/{row['source_id']}/units"})
        packet = {"schema_version": 1, "mode": "codex-direct", "domain_id": pack.domain_id, "domain_slug": pack.slug, "source_units": units, "instructions": "Read only the validated Markdown units listed above. Return typed proposal JSON; do not publish. Every claim requires audited evidence."}
        packet_path = journal.run_dir / "codex_handoff.json"
        atomic_write_json(packet_path, packet)
        journal.finish("REVIEW_REQUIRED", handoff_path=packet_path.relative_to(paths.root).as_posix(), source_count=len(units), unit_count=sum(item["unit_count"] for item in units), llm_calls=0)
        return {"run_id": journal.run_id, "domain_id": pack.domain_id, "profile": profile_name, "status": "CODEX_HANDOFF_READY", "handoff_path": packet_path.relative_to(paths.root).as_posix(), "source_count": len(units), "unit_count": sum(item["unit_count"] for item in units), "llm_calls": 0}
    profile = _profile(paths, profile_name)
    if not bool(profile.get("llm_enabled")):
        raise ValueError("The generate stage requires strict-local or approved-remote; use run for no-llm ingestion")
    pack = DomainManager(paths).load(domain)
    journal = RunJournal.create(paths, domain_id=pack.domain_id, profile=profile_name)
    try:
        records = _domain_rows(paths, pack.domain_id)
        client = OpenAICompatibleClient(OpenAISettings.from_env(profile=profile_name))
        summary = KnowledgePipeline(paths, client, workers=int(profile.get("max_llm_workers", 1))).run(pack, records, journal)
        status = "REVIEW_REQUIRED" if summary.get("review_status") != "BLOCKED" else "FAILED"
        journal.finish(status, **summary)
        return {"run_id": journal.run_id, "domain_id": pack.domain_id, "profile": profile_name, **summary, "status": status}
    except Exception:
        journal.finish("FAILED")
        raise


def _snapshot(paths: ProjectPaths, pack: Any, require_ready: bool) -> dict[str, tuple[int, int]]:
    values: dict[str, tuple[int, int]] = {}
    for root_value in (*pack.source_roots, "sources/_shared"):
        root = paths.root / root_value
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.name.startswith("~$") or path.name.endswith(".ready"):
                continue
            if require_ready and not path.with_name(path.name + ".ready").exists():
                continue
            stat = path.stat()
            values[path.relative_to(paths.root).as_posix()] = (stat.st_size, stat.st_mtime_ns)
    return values


def _cmd_domain(args: argparse.Namespace, paths: ProjectPaths) -> dict[str, Any]:
    manager = DomainManager(paths)
    if args.domain_command == "list":
        return {"domains": [pack.to_mapping() for pack in manager.list()]}
    pack = manager.init(args.slug, name_en=args.name_en, name_fr=args.name_fr, question_prefix=args.question_prefix, description=args.description or "", domain_id=args.domain_id)
    return pack.to_mapping()


def _cmd_inventory(args: argparse.Namespace, paths: ProjectPaths) -> dict[str, Any]:
    pack = DomainManager(paths).load(args.domain)
    rows = IngestionOrchestrator(paths, get_default_registry()).inventory(pack)
    return {"domain_id": pack.domain_id, "source_count": len(rows), "sources": [{"source_id": row["source_id"], "source_sha256": row["source_sha256"], "source_format": row["source_format"], "status": row["status"]} for row in rows]}


def _cmd_status(paths: ProjectPaths) -> dict[str, Any]:
    manifest = read_jsonl(paths.state / "source_manifest.jsonl")
    states: dict[str, int] = {}
    for row in manifest:
        states[str(row.get("status", "UNKNOWN"))] = states.get(str(row.get("status", "UNKNOWN")), 0) + 1
    registry = get_default_registry()
    return {
        "project_root": str(paths.root),
        "domains": len(DomainManager(paths).list()),
        "sources": len(manifest),
        "source_states": states,
        "adapters": [
            {
                "adapter_id": adapter.adapter_id,
                "adapter_version": adapter.adapter_version,
                "heavy": bool(getattr(adapter, "heavy", False)),
                "capabilities": getattr(adapter, "capabilities", {}),
            }
            for adapter in registry.adapters
        ],
        "latest_run": RunJournal.latest(paths),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="gov360", description="Local-first evidence governance knowledge pipeline")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status", help="Show identifiers, counts, and the latest run")

    domain = sub.add_parser("domain", help="Manage configuration-only Domain Packs")
    domain_sub = domain.add_subparsers(dest="domain_command", required=True)
    domain_sub.add_parser("list")
    init = domain_sub.add_parser("init")
    init.add_argument("slug")
    init.add_argument("--name-en", required=True)
    init.add_argument("--name-fr", required=True)
    init.add_argument("--question-prefix", required=True)
    init.add_argument("--description")
    init.add_argument("--domain-id")

    inventory = sub.add_parser("inventory")
    inventory.add_argument("--domain", required=True)
    source = sub.add_parser("source", help="Record reviewed source metadata")
    source_sub = source.add_subparsers(dest="source_command", required=True)
    classify = source_sub.add_parser("classify", help="Assign a reviewed authority class without changing the source")
    classify.add_argument("source_id")
    classify.add_argument("--normativity", required=True, choices=["BINDING", "GUIDANCE", "STANDARD", "FRAMEWORK", "DATASET", "RESEARCH", "UNCLASSIFIED"])
    classify.add_argument("--reviewer", required=True)
    run = sub.add_parser("run")
    run.add_argument("--domain", required=True)
    run.add_argument("--profile", default="no-llm", choices=["strict-local", "approved-remote", "no-llm"], help="Ingestion/runtime profile; no LLM is called by this command")
    normalize = sub.add_parser("normalize", help="Alias for the source-to-Markdown run stage")
    normalize.add_argument("--domain", required=True)
    normalize.add_argument("--profile", default="no-llm", choices=["strict-local", "approved-remote", "no-llm"])
    generate = sub.add_parser("generate", help="Use validated Markdown in a separate LLM/wiki proposal stage")
    generate.add_argument("--domain", required=True)
    generate.add_argument("--profile", default="strict-local", choices=["strict-local", "approved-remote", "codex-direct"], help="LLM backend: local, approved API, or Codex handoff without an endpoint")
    validate = sub.add_parser("validate-ingest")
    validate.add_argument("--domain", required=True)
    normalize_vault = sub.add_parser("normalize-vault", help="Migrate all vault notes to the unified frontmatter contract")
    approve = sub.add_parser("approve")
    approve.add_argument("--domain", required=True)
    approve.add_argument("--stage", required=True, choices=["domain", "knowledge", "questionnaires"])
    approve.add_argument("--run-id")
    audit = sub.add_parser("audit")
    audit.add_argument("--domain")
    retire = sub.add_parser("retire")
    retire.add_argument("--source-id", required=True)
    watch = sub.add_parser("watch")
    watch.add_argument("--domain", required=True)
    watch.add_argument("--profile", default="strict-local", choices=["strict-local", "approved-remote", "no-llm"])
    watch.add_argument("--interval", type=float, default=5.0)
    watch.add_argument("--require-ready", action="store_true")
    watch.add_argument("--once", action="store_true", help="Run one stable-file check and exit")
    context = sub.add_parser("context", help="Build a deterministic local context packet for an assistant")
    context.add_argument("--query", required=True, help="Question or retrieval query")
    context.add_argument("--domain", action="append", dest="domains", help="Restrict retrieval to one or more domain IDs")
    context.add_argument("--authority", action="append", dest="authorities", help="Restrict source authority (for example BINDING)")
    context.add_argument("--release", default="CURRENT", dest="release_id")
    context.add_argument("--token-budget", type=int, default=2048)
    context.add_argument("--project-context", default="{}", help="JSON object with applicability context")
    context.add_argument("--access-scope", default="{}", help="JSON object with local access restrictions")
    from .brain.cli import add_parser
    add_parser(sub)
    return parser


def _json_object(value: str, flag: str) -> dict[str, Any]:
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{flag} must be a JSON object") from exc
    if not isinstance(parsed, dict):
        raise ValueError(f"{flag} must be a JSON object")
    return parsed


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == 'brain':
        from .brain.cli import run
        return run(args)
    if (Path.cwd() / 'brain wiki' / 'SCHEMA.md').exists() and args.command in {'generate', 'approve', 'normalize-vault', 'audit'}:
        parser.error('Legacy vault writer disabled for Governance 360 Markdown contract. See WORKSHOP.md and python -m gov360_brain.workshop.')
    paths = ProjectPaths.discover()
    paths.ensure_layout()
    DomainManager(paths).rebuild_registry()
    try:
        if args.command == "status":
            result = _cmd_status(paths)
        elif args.command == "domain":
            result = _cmd_domain(args, paths)
        elif args.command == "inventory":
            result = _cmd_inventory(args, paths)
        elif args.command == "source":
            if args.source_command == "classify":
                result = SourceCatalog(paths).classify(args.source_id, normativity=args.normativity, reviewer=args.reviewer)
            else:
                raise ValueError("Unknown source command")
        elif args.command in {"run", "normalize"}:
            result = _execute_run(paths, args.domain, args.profile)
        elif args.command == "generate":
            result = _execute_generate(paths, args.domain, args.profile)
        elif args.command == "validate-ingest":
            pack = DomainManager(paths).load(args.domain)
            source_ids = {str(row["source_id"]) for row in _domain_rows(paths, pack.domain_id)}
            checks = IngestionOrchestrator(paths, get_default_registry()).validate_existing(source_ids)
            result = {"domain_id": pack.domain_id, "valid": all(item.get("valid") for item in checks), "checks": checks}
        elif args.command == "normalize-vault":
            notes = sorted(paths.vault.rglob("*.md"))
            for note in notes:
                normalize_note_file(note)
            result = {"status": "SUCCEEDED", "notes": len(notes), "vault": str(paths.vault)}
        elif args.command == "approve":
            result = ApprovalManager(paths).approve(args.domain, args.stage, run_id=args.run_id)
        elif args.command == "audit":
            domain_id = DomainManager(paths).load(args.domain).domain_id if args.domain else None
            result = VaultAuditor(paths).run(domain_id)
        elif args.command == "retire":
            SourceCatalog(paths).update(args.source_id, status="RETIRED", retired_at=datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"))
            result = {"source_id": args.source_id, "status": "RETIRED", "original_retained": True}
        elif args.command == "watch":
            pack = DomainManager(paths).load(args.domain)
            previous = _snapshot(paths, pack, args.require_ready)
            while True:
                time.sleep(max(0.05, args.interval))
                current = _snapshot(paths, pack, args.require_ready)
                if current == previous:
                    result = _execute_run(paths, args.domain, args.profile)
                    if args.once:
                        break
                previous = current
        elif args.command == "context":
            project_context = _json_object(args.project_context, "--project-context")
            access_scope = _json_object(args.access_scope, "--access-scope")
            if args.domains:
                project_context["domains"] = [str(item).upper() for item in args.domains]
            if args.authorities:
                project_context["authorities"] = [str(item).upper() for item in args.authorities]
            result = ContextBuilder(paths).build_context(
                query=args.query,
                project_context=project_context,
                access_scope=access_scope,
                release_id=args.release_id,
                token_budget=args.token_budget,
            )
        else:
            parser.error("unknown command")
            return 2
        _json(result)
        return 0 if result.get("status") not in {"FAILED", "BLOCKED"} and result.get("valid") is not False else 1
    except Exception as exc:
        safe_messages = {"DomainPackError", "LLMConfigurationError", "FileNotFoundError", "ValueError"}
        payload = {"status": "FAILED", "error": {"type": type(exc).__name__, "code": "COMMAND_FAILED"}}
        if type(exc).__name__ in safe_messages:
            payload["error"]["message"] = str(exc)
        _json(payload)
        return 2


if __name__ == "__main__":
    sys.exit(main())
