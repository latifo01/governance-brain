"""Deterministic, fail-closed exports and local source reconstruction.

No function in this module publishes remotely or writes an original source.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import tempfile
import tomllib
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import quote

import yaml

from ..utils import sha256_file

OKF_SPEC = {
    "version": "0.2",
    "revision": "0b87c52c6ef999286c745e19998fdfcd03d5dbee",
    "sha256": "26aa5da029278939f914e578107242d9607d4f2dc5fe153272b82f9ed1030101",
    "url": "https://raw.githubusercontent.com/GoogleCloudPlatform/open-knowledge-format/0b87c52c6ef999286c745e19998fdfcd03d5dbee/SPEC.md",
}
_SHA = re.compile(r"^[a-f0-9]{64}$")
_ID = re.compile(r"^SRC-[0-9]{4,}$")
# A policy cannot override these boundaries, even by adding an explicit grant.
_FORBIDDEN = {"sources", "ingest", "state", "brain wiki", ".git", ".venv", ".obsidian", ".opencode", ".codex", "__pycache__"}


def _frontmatter(value: dict[str, Any]) -> str:
    return "---\n" + yaml.safe_dump(value, sort_keys=True, allow_unicode=True) + "---\n\n"


def _json(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def _relative(value: str) -> PurePosixPath:
    path = PurePosixPath(value)
    if not value or "\\" in value or path.is_absolute() or ".." in path.parts or ":" in path.parts[0]:
        raise ValueError("UNSAFE_RELATIVE_PATH")
    return path


def _safe(root: Path, relative: str) -> Path:
    path = root.joinpath(*_relative(relative).parts)
    current = root
    if root.is_symlink():
        raise ValueError("SYMLINK_ROOT")
    for part in _relative(relative).parts:
        current = current / part
        if current.is_symlink():
            raise ValueError("SYMLINK_PATH")
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError("PATH_OUTSIDE_ROOT")
    return path


def _load(path: Path, default: Any = None) -> Any:
    return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else default


def _rows(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _policy(root: Path) -> dict[str, Any]:
    value = _load(_safe(root, "config/redistribution-policy.json"), {})
    if value.get("schema_version") != 1 or value.get("default") != "deny":
        raise ValueError("INVALID_REDISTRIBUTION_POLICY")
    return value


def _destination(root: Path, output: Path | str | None, default: str) -> Path:
    target = Path(output) if output is not None else Path("dist") / default
    if target.is_absolute():
        try:
            target = target.relative_to(root)
        except ValueError as exc:
            raise ValueError("OUTPUT_MUST_BE_UNDER_REPOSITORY_DIST") from exc
    checked = _relative(target.as_posix())
    if len(checked.parts) < 2 or checked.parts[0] != "dist":
        raise ValueError("OUTPUT_MUST_BE_UNDER_REPOSITORY_DIST")
    return _safe(root, checked.as_posix())


def _bundle(root: Path, output: Path | str | None, default: str, files: dict[str, bytes], manifest: dict[str, Any], *, write: bool,
            manifest_name: str = "brain-release.json") -> dict[str, Any]:
    """Stage the complete bundle, then replace only a recognized owned bundle."""
    destination = _destination(root, output, default)
    records = [{"path": name, "sha256": hashlib.sha256(body).hexdigest(), "size": len(body)} for name, body in sorted(files.items())]
    manifest = {"schema_version": 1, **manifest, "files": records}
    files = {**files, manifest_name: _json(manifest)}
    current = False
    if destination.exists():
        if not destination.is_dir() or not (destination / manifest_name).is_file():
            raise ValueError("OUTPUT_NOT_AN_OWNED_BUNDLE")
        existing = {}
        for path in destination.rglob("*"):
            if ".git" in path.relative_to(destination).parts:
                continue
            if path.is_symlink():
                raise ValueError("SYMLINK_IN_OUTPUT")
            if path.is_file():
                existing[path.relative_to(destination).as_posix()] = path.read_bytes()
        old = _load(destination / manifest_name, {})
        if old.get("kind") != manifest.get("kind"):
            raise ValueError("OUTPUT_BUNDLE_KIND_MISMATCH")
        expected_old = {r["path"]: r["sha256"] for r in old.get("files", [])}
        actual_old = {p: hashlib.sha256(b).hexdigest() for p, b in existing.items() if p != manifest_name}
        if expected_old != actual_old:
            raise ValueError("OUTPUT_HAS_UNMANAGED_OR_MODIFIED_FILES")
        current = existing == files
    if write and not current:
        destination.parent.mkdir(parents=True, exist_ok=True)
        stage = Path(tempfile.mkdtemp(prefix=".brain-bundle-", dir=destination.parent))
        backup = None
        try:
            for relative, body in sorted(files.items()):
                target = _safe(stage, relative)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(body)
            for record in records:
                if sha256_file(_safe(stage, record["path"])) != record["sha256"]:
                    raise ValueError("STAGED_HASH_MISMATCH")
            if destination.exists():
                backup = Path(tempfile.mkdtemp(prefix=".brain-backup-", dir=destination.parent))
                backup.rmdir()
                os.replace(destination, backup)
            try:
                os.replace(stage, destination)
            except BaseException:
                if backup is not None:
                    os.replace(backup, destination)
                    backup = None
                raise
        finally:
            if stage.exists():
                shutil.rmtree(stage)
            if backup is not None and backup.exists():
                shutil.rmtree(backup)
    return {"valid": True, "kind": manifest["kind"], "output": destination.relative_to(root).as_posix(), "current": current, "written": write and not current, "file_count": len(files), "manifest": manifest}


def _anchor(value: str) -> str:
    return quote(re.sub(r"[^\w\- ]", "", value.lower()).replace(" ", "-"), safe="-_")


def _wiki_links(body: str, lookup: dict[str, str], current: str, gaps: list[dict[str, Any]]) -> str:
    """Convert links outside fenced/inline code; retain unresolved labels."""
    fence = None
    result = []
    for line in body.splitlines(keepends=True):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            result.append(line)
            continue
        if fence is not None:
            result.append(line)
            continue
        def convert(match: re.Match[str]) -> str:
            target, _, label = match[1].partition("|")
            note, separator, anchor = target.partition("#")
            if not note:
                path = current
            else:
                path = lookup.get(note) or lookup.get(note.removesuffix(".md"))
            display = (label or target).replace("[", "\\[").replace("]", "\\]")
            if path is None:
                gaps.append({"code": "UNRESOLVED_OR_EXCLUDED_LINK", "from": current, "target": note})
                return display
            suffix = "#" + _anchor(anchor) if separator else ""
            return f"[{display}](/{quote(path, safe='/')}{suffix})"
        chunks = re.split(r"(`+[^`]*`+)", line)
        result.append("".join(chunk if i % 2 else re.sub(r"!?\[\[([^\]\n]+)\]\]", convert, chunk) for i, chunk in enumerate(chunks)))
    return "".join(result)


def _publication_log(root: Path, included_paths: set[str]) -> tuple[str, list[dict[str, Any]]]:
    entries = []
    undated = []
    base = _safe(root, "state/workshop/proposals")
    for receipt_path in sorted(base.glob("*/review/integration-report.json")) if base.exists() else []:
        receipt = _load(_safe(root, receipt_path.relative_to(root).as_posix()), {})
        manifest_path = receipt_path.parent.parent / "manifest.json"
        manifest = _load(_safe(root, manifest_path.relative_to(root).as_posix()), {})
        if receipt.get("valid") is not True or manifest.get("status") != "INTEGRATED":
            continue
        selected = [r for r in receipt.get("files", []) if "brain wiki/" + r.get("path", "") in included_paths]
        if not selected:
            continue
        approval_path = receipt_path.parent / "approval.md"
        approval = _safe(root, approval_path.relative_to(root).as_posix()).read_text(encoding="utf-8") if approval_path.exists() else ""
        # An approval date is not an integration timestamp. Preserve that label.
        date = re.search(r"(?im)^- Decision date:\s*(\d{4}-\d{2}-\d{2})\s*$", approval)
        row = {"proposal_id": manifest.get("proposal_id", receipt_path.parent.parent.name), "receipt_sha256": sha256_file(receipt_path), "candidate_sha256": receipt.get("candidate_sha256"), "file_count": len(selected)}
        if date:
            entries.append((date[1], row))
        else:
            undated.append(row)
    lines = ["# Publication receipt history", "", "Dates below are recorded approval dates, not inferred integration times.", ""]
    last = None
    for date, row in sorted(entries, key=lambda pair: (pair[0], pair[1]["proposal_id"]), reverse=True):
        if date != last:
            lines += [f"## {date}", ""]
            last = date
        lines.append(f"- Approval recorded for `{row['proposal_id']}`; integrated receipt `{row['receipt_sha256']}` ({row['file_count']} included files).")
    if not entries:
        lines.append("No dated publication receipt is available for included concepts.")
    return "\n".join(lines) + "\n", undated


def export_okf(root: Path, output: Path | str | None = None, *, public: bool = False, write: bool = True) -> dict[str, Any]:
    from .catalogue import compile_brain
    root = Path(root).resolve()
    data = compile_brain(root)
    policy = _policy(root) if public else {"content_grants": []}
    grants = {r.get("path"): r for r in policy.get("content_grants", []) if r.get("permission") == "redistribute" and r.get("license") and r.get("review_record") and _SHA.fullmatch(str(r.get("sha256", "")))}
    notes, gaps = [], []
    for note in data["notes"]:
        if public:
            grant = grants.get(note["path"], {})
            if grant.get("sha256") != note["sha256"]:
                gaps.append({"code": "REDISTRIBUTION_NOT_AUTHORIZED", "note_id": note["id"]})
                continue
        notes.append(note)
    mapping = {n["id"]: "concepts/" + n["id"] + ".md" for n in notes}
    lookup: dict[str, str] = {}
    ambiguous = set()
    for note in notes:
        relative = note["path"].removeprefix("brain wiki/")
        for key in {note["id"], note["title"], relative, relative.removesuffix(".md"), *note.get("aliases", [])}:
            if key in lookup and lookup[key] != mapping[note["id"]]:
                ambiguous.add(key)
            lookup[key] = mapping[note["id"]]
    for key in ambiguous:
        lookup.pop(key, None)
    files: dict[str, bytes] = {}
    for note in notes:
        metadata = dict(note.get("metadata", {}))
        # No source/trust fields are inferred from publication or note status.
        for key in ("sources", "verified", "generated", "stale_after"):
            metadata.pop(key, None)
        metadata.update({"type": note["type"], "title": note["title"], "status": "deprecated" if note.get("status") == "deprecated" else "stable", "brain_id": note["id"], "brain_sha256": note["sha256"]})
        refs, annotations = [], []
        body = note["body"]
        cursor = 0
        for section in data.get("sections", []):
            if section.get("note_id") != note["id"]:
                continue
            text = section.get("text", "")
            start = body.find(text, cursor) if text else -1
            if start >= 0:
                cursor = start + len(text)
            if section.get("evidence_status") != "REVIEWED":
                continue
            labels = []
            for citation in section.get("citations", []):
                if not isinstance(citation, dict) or citation.get("evidence_status") != "REVIEWED":
                    continue
                source_id = citation.get("source_id")
                source_hash = citation.get("source_sha256")
                if not (_ID.fullmatch(str(source_id)) and _SHA.fullmatch(str(source_hash))):
                    continue
                ref_id = "brain-" + hashlib.sha256(str(citation.get("evidence_ref", source_id)).encode()).hexdigest()[:16]
                descriptor = "references/" + source_id.lower() + "-" + source_hash + ".md"
                # Metadata descriptors contain no original or ingested text.
                descriptor_meta = {"type": "Reference", "title": source_id,
                    "resource": f"urn:sha256:{source_hash}", "brain_source_id": source_id,
                    "brain_source_sha256": source_hash}
                files[descriptor] = (_frontmatter(descriptor_meta) + "# Source identity\n\nThis descriptor records identity only. Supply the original locally and resolve its hash against the source seed.\n").encode("utf-8")
                ref = {"id": ref_id, "resource": "/" + descriptor, "brain_source_id": source_id,
                    **{k: citation[k] for k in ("evidence_ref", "unit_path", "unit_sha256", "unit_file_sha256", "locator", "authority") if k in citation}}
                if ref not in refs:
                    refs.append(ref)
                labels.append(ref_id)
            if labels and start >= 0:
                annotations.append((cursor, "\n\nSection evidence: " + " ".join(f"[^{label}]" for label in sorted(set(labels)))))
            elif labels:
                gaps.append({"code": "SECTION_ATTRIBUTION_UNRESOLVED", "note_id": note["id"], "section_id": section.get("section_id")})
        if refs:
            metadata["sources"] = sorted(refs, key=lambda row: row["id"])
            for offset, annotation in reversed(annotations):
                body = body[:offset] + annotation + body[offset:]
            body += "\n\n" + "\n".join(f"[^{ref['id']}]: [{ref['brain_source_id']}]({ref['resource']}); locator: {str(ref.get('locator', 'unknown')).replace(chr(10), ' ')}." for ref in metadata["sources"]) + "\n"
        else:
            gaps.append({"code": "SOURCE_PROVENANCE_UNRESOLVED", "note_id": note["id"]})
        body = _wiki_links(body, lookup, mapping[note["id"]], gaps)
        files[mapping[note["id"]]] = (_frontmatter(metadata) + body).encode("utf-8")
    files["index.md"] = ("---\nokf_version: '0.2'\n---\n\n# Governance Brain\n\n" + "\n".join(f"- [{n['title']}](/{'concepts/' + n['id'] + '.md'})" for n in notes) + "\n").encode("utf-8")
    log, undated = _publication_log(root, {n["path"] for n in notes})
    files["log.md"] = log.encode("utf-8")
    return _bundle(root, output, "okf-public" if public else "okf", files, {"kind": "okf", "public": public, "specification": OKF_SPEC, "mapping": mapping, "gaps": gaps, "undated_publication_receipts": undated}, write=write)


def _sanitize_seed_record(record: dict[str, Any]) -> dict[str, Any]:
    import jsonschema
    keys = ("source_id", "source_sha256", "relative_paths", "source_format", "source_kind", "domains", "primary_domain", "adapter_id", "adapter_version")
    result = {k: record[k] for k in keys if k in record}
    schema = _load(Path(__file__).resolve().parents[3] / "config/schemas/source-manifest.schema.json")
    jsonschema.validate({"schema_version": 1, "status": "DISCOVERED", **result}, schema)
    for value in result["relative_paths"]:
        if _relative(value).parts[0] != "sources":
            raise ValueError("INVALID_SOURCE_PATH")
    units = []
    for unit in record.get("expected_units", []):
        if _relative(unit["filename"]).parts[0] != "units" or not _SHA.fullmatch(unit["file_sha256"]):
            raise ValueError("INVALID_UNIT_RECORD")
        units.append({k: unit[k] for k in ("filename", "file_sha256", "locator", "locator_kind")})
    result["expected_units"] = units
    result["reconstruction"] = "expected" if units else "unavailable"
    return result


def _source_seed(root: Path) -> dict[str, Any]:
    existing_seed = _load(_safe(root, "config/source-seed.json"), {})
    records = {row["source_id"]: _sanitize_seed_record(row) for row in existing_seed.get("sources", [])}
    if len(records) != len(existing_seed.get("sources", [])):
        raise ValueError("DUPLICATE_SEEDED_SOURCE_ID")
    # A kit can itself emit a kit without losing its reconstruction baseline.

    for row in _rows(_safe(root, "state/source_manifest.jsonl")):
        source_id = row["source_id"]
        if not _ID.fullmatch(source_id) or not _SHA.fullmatch(row["source_sha256"]):
            raise ValueError("INVALID_SOURCE_ID_OR_HASH")
        paths = []
        for value in row.get("relative_paths", []):
            path = _relative(value)
            if path.parts[0] != "sources" or len(path.parts) < 2:
                raise ValueError("INVALID_SOURCE_PATH")
            paths.append(path.as_posix())
        document = _load(_safe(root, f"ingest/{source_id}/document.json"), {})
        expected = []
        if document and document.get("source_sha256") != row["source_sha256"]:
            raise ValueError("SOURCE_DOCUMENT_HASH_MISMATCH")
        for unit in document.get("units", []):
            path = _relative(unit["filename"])
            if path.parts[0] != "units" or not _SHA.fullmatch(unit["file_sha256"]):
                raise ValueError("INVALID_UNIT_RECORD")
            expected.append({k: unit[k] for k in ("filename", "file_sha256", "locator", "locator_kind")})
        prior = records.get(source_id, {})
        if not document and prior.get("source_sha256") == row["source_sha256"]:
            expected = prior.get("expected_units", [])
        records[source_id] = {"source_id": source_id, "source_sha256": row["source_sha256"], "relative_paths": sorted(paths), "adapter_id": document.get("adapter_id", row.get("adapter_id")), "adapter_version": document.get("adapter_version", row.get("adapter_version", "unknown")), "source_format": row.get("source_format"), "source_kind": row.get("source_kind"), "domains": row.get("domains", []), "primary_domain": row.get("primary_domain"), "expected_units": expected, "reconstruction": "expected" if expected else "unavailable"}
    return {"schema_version": 1, "sources": [_sanitize_seed_record(row) for row in sorted(records.values(), key=lambda row: row["source_id"])], "notice": "Hashes establish identity only; this seed grants no evidence review or publication approval."}


def release_kit(root: Path, output: Path | str | None = None, *, write: bool = True) -> dict[str, Any]:
    root = Path(root).resolve()
    policy = _policy(root)
    files, gaps = {}, []
    for relative in sorted(set(policy.get("original_files", []))):
        path = _relative(relative)
        agent_template = (len(path.parts) == 3 and path.parts[0] in {".codex", ".opencode"}
                          and ((path.parts[1] == "agents" and path.suffix in {".toml", ".md"})
                               or (path.parts[0] == ".opencode" and path.parts[1] == "commands" and path.suffix == ".md")))
        contract_document = relative == "brain wiki/SCHEMA.md"
        if (any(part in _FORBIDDEN for part in path.parts) and not agent_template and not contract_document) or relative in {"opencode.json", "opencode.jsonc", "auth.json"} or path.name.startswith(".env") or path.suffix in {".key", ".pem", ".pyc"}:
            raise ValueError("KIT_ALLOWLIST_CONTAINS_FORBIDDEN_PATH")
        target = _safe(root, relative)
        if not target.is_file():
            gaps.append({"code": "ALLOWLIST_FILE_MISSING", "path": relative})
            continue
        body = target.read_bytes()
        if re.search(rb"(?i)(?:\bsk-(?:or-v1-)?[a-z0-9_-]{20,}|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----)", body):
            raise ValueError("POSSIBLE_SECRET_IN_KIT_FILE")
        if path.parts[0] == ".opencode" and path.suffix == ".md":
            # Recipient chooses its provider/model locally; preserve role prose,
            # permissions and command routing without copied provider pins.
            text = body.decode("utf-8")
            match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, re.S)
            if match:
                metadata = yaml.safe_load(match[1])
                if isinstance(metadata, dict) and "model" in metadata:
                    metadata.pop("model")
                    body = (_frontmatter(metadata) + text[match.end():]).encode("utf-8")
        files[relative] = body
    codex_agents = []
    for name, body in sorted(files.items()):
        if name.startswith(".codex/agents/") and name.endswith(".toml"):
            metadata = tomllib.loads(body.decode("utf-8"))
            agent_id = PurePosixPath(name).stem
            if not re.fullmatch(r"[a-z][a-z0-9_]*", agent_id):
                raise ValueError("INVALID_CODEX_AGENT_ID")
            codex_agents.extend([f"[agents.{agent_id}]",
                "description = " + json.dumps(str(metadata.get("description", agent_id)), ensure_ascii=False),
                "config_file = " + json.dumps("agents/" + PurePosixPath(name).name), ""])
    if codex_agents:
        files[".codex/config.toml"] = ("[agents]\nmax_concurrent_threads_per_session = 3\n\n" + "\n".join(codex_agents)).encode("utf-8")
    files["opencode.json"] = _json({
        "$schema": "https://opencode.ai/config.json", "share": "disabled",
        "instructions": ["AGENTS.md", "WORKSHOP.md"],
        "permission": {"read": {"*": "allow", ".env*": "deny", "**/.env*": "deny", "sources/**": "deny", "ingest/**": "ask"},
                       "edit": {"*": "ask", "sources/**": "deny"}, "bash": "ask", "external_directory": "deny"},
    })
    seed = _source_seed(root)
    files["config/source-seed.json"] = _json(seed)
    files["KIT.md"] = ("# Governance Brain reconstruction kit\n\nThis directory has no source corpus, extracted text, prior Git history, or publication approvals.\n\n1. Run `uv sync --frozen --extra dev`.\n2. Place lawfully held originals below `sources/`; hashes in `config/source-seed.json` identify expected files.\n3. Preview `uv run gov360 brain bootstrap`, then run `uv run gov360 brain bootstrap --apply` to reconstruct matching units.\n4. Review reconstruction gaps before extracting evidence or drafting knowledge.\n5. Run `uv run pytest -q`; the kit carries only synthetic technical tests.\n6. Configure OpenCode provider credentials and models locally; the kit keeps agents, commands and skills but removes wrapper model pins. Open `opencode` and use `/brain-next` or `/brain-build <release>`. Select strict-local operation, or explicitly authorise approved-remote endpoint and material before transmitting ingest.\n\nAdapter/version/hash divergence blocks the affected reconstruction. LLM-written notes are not reproducible from source bytes alone. Code licensing does not grant rights to original or derived third-party content.\n").encode("utf-8")
    return _bundle(root, output, "release-kit", files, {"kind": "release-kit", "public": True, "original_code_license": "Apache-2.0", "source_count": len(seed["sources"]), "gaps": gaps, "history_included": False, "transforms": ["remove_opencode_wrapper_model_pins", "generate_model_free_opencode_config", "register_allowlisted_codex_agents"]}, write=write)


def _private_handoff_policy(root: Path) -> dict[str, Any]:
    import jsonschema

    policy_path = _safe(root, "config/private-handoff-policy.json")
    schema_path = _safe(root, "config/schemas/private-handoff.schema.json")
    policy = _load(policy_path, {})
    schema = _load(schema_path, {})
    try:
        jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(policy)
    except jsonschema.ValidationError as exc:
        field = ".".join(str(part) for part in exc.absolute_path) or "policy"
        raise ValueError("INVALID_PRIVATE_HANDOFF_POLICY:" + field) from None
    required_scope = {"sources/**", "ingest/**", "brain wiki/**", "state/**", "dist/**"}
    if set(policy["authorization"]["scope"]) != required_scope:
        raise ValueError("PRIVATE_HANDOFF_SCOPE_INCOMPLETE")
    return policy


def _prefix_match(relative: str, excluded: str) -> bool:
    normalized = _relative(excluded).as_posix()
    return relative == normalized or relative.startswith(normalized + "/")


def _verify_private_corpus(root: Path) -> dict[str, int]:
    """Verify identities and normalized units without logging document bodies."""
    from .ingest_reader import source_document, validated_unit

    rows = _rows(_safe(root, "state/source_manifest.jsonl"))
    if len({row.get("source_id") for row in rows}) != len(rows):
        raise ValueError("DUPLICATE_SOURCE_ID")
    source_files = 0
    validated_units = 0
    ready_sources = 0
    for row in rows:
        source_id = row.get("source_id")
        expected = row.get("source_sha256")
        if not _ID.fullmatch(str(source_id)) or not _SHA.fullmatch(str(expected)):
            raise ValueError("INVALID_SOURCE_ID_OR_HASH")
        paths = row.get("relative_paths", [])
        if not isinstance(paths, list) or not paths:
            raise ValueError("SOURCE_PATH_REQUIRED")
        for relative in paths:
            candidate = _safe(root, str(relative))
            if _relative(str(relative)).parts[0] != "sources" or not candidate.is_file():
                raise ValueError("SOURCE_FILE_MISSING")
            if sha256_file(candidate) != expected:
                raise ValueError("SOURCE_FILE_HASH_MISMATCH")
            source_files += 1
        if row.get("status") == "READY_FOR_LLM":
            source, document = source_document(root, source_id)
            for unit in document["units"]:
                validated_unit(root, source, document, unit["filename"])
                validated_units += 1
            ready_sources += 1
    return {"logical_sources": len(rows), "source_files": source_files,
            "ready_sources": ready_sources, "validated_units": validated_units}


def private_handoff(root: Path, output: Path | str | None = None, *, write: bool = True) -> dict[str, Any]:
    """Build the operator-authorized private CDO continuation snapshot.

    This is distinct from ``release_kit``: it includes the immutable corpus,
    normalized units, active vault, workshop state and local derived outputs.
    It never initializes Git or publishes remotely.
    """
    root = Path(root).resolve()
    policy = _private_handoff_policy(root)
    destination = _destination(root, output, "cdo-handoff")
    excluded = list(policy["exclude_paths"])
    try:
        excluded.append(destination.relative_to(root).as_posix())
    except ValueError as exc:
        raise ValueError("OUTPUT_MUST_BE_UNDER_REPOSITORY_DIST") from exc
    files: dict[str, bytes] = {}
    for name in sorted(policy["include_files"]):
        path = _safe(root, name)
        if not path.is_file():
            raise ValueError("HANDOFF_REQUIRED_FILE_MISSING")
        files[name] = path.read_bytes()
    for root_name in sorted(policy["include_roots"]):
        base = _safe(root, root_name)
        if not base.is_dir():
            raise ValueError("HANDOFF_REQUIRED_ROOT_MISSING")
        for path in sorted(base.rglob("*")):
            relative = path.relative_to(root).as_posix()
            if any(_prefix_match(relative, item) for item in excluded):
                continue
            parts = PurePosixPath(relative).parts
            if parts[0] not in {"sources", "ingest"}:
                if any(part in {"__pycache__", ".pytest_cache", ".pytest_tmp"} for part in parts):
                    continue
                if path.suffix == ".pyc" or path.name in {".DS_Store", "Thumbs.db", "workspace.json", "workspace-mobile.json"}:
                    continue
            if path.is_symlink():
                raise ValueError("SYMLINK_IN_PRIVATE_HANDOFF")
            if path.is_file():
                files[relative] = path.read_bytes()
    operational = {name: body for name, body in files.items()
                   if not name.startswith(("sources/", "ingest/"))
                   and PurePosixPath(name).suffix.lower() not in {".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx", ".png", ".jpg", ".jpeg", ".gif"}}
    secret = re.compile(rb"(?i)(?:\bsk-(?:or-v1-)?[a-z0-9_-]{20,}|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----)")
    if any(secret.search(body) for body in operational.values()):
        raise ValueError("POSSIBLE_SECRET_IN_PRIVATE_HANDOFF")
    corpus = _verify_private_corpus(root)
    policy_sha256 = sha256_file(_safe(root, "config/private-handoff-policy.json"))
    files["HANDOFF.md"] = (
        "# CDO private continuation repository\n\n"
        "This private snapshot contains the immutable source corpus, validated ingest, active Obsidian vault, "
        "workshop state and derived outputs. It does not authorize public redistribution.\n\n"
        "1. Read `AGENTS.md`, `README.md`, `WORKSHOP.md`, `ROADMAP.md`, `brain wiki/SCHEMA.md`, and `manuel.md`.\n"
        "2. Run `uv sync --frozen --extra dev`, then `uv run pytest -q`.\n"
        "3. Run `uv run gov360 brain validate`, `uv run gov360 brain build --check`, and the derived checks.\n"
        "4. Open `brain wiki/` in Obsidian and start OpenCode from the repository root.\n"
        "5. Add new originals; never modify or delete an existing file below `sources/`.\n\n"
        "See `docs/windows-setup.md` for the Windows path and `manuel.md` for the complete evidence-first workflow.\n"
    ).encode("utf-8")
    manifest = {
        "kind": "private-cdo-handoff", "public": False, "history_included": False,
        "handoff_id": policy["handoff_id"], "target": policy["target"],
        "authorization": policy["authorization"], "authorization_policy_sha256": policy_sha256,
        "corpus": corpus,
        "notice": "Private transfer authorization is not a public redistribution licence or a knowledge approval.",
    }
    return _bundle(root, output, "cdo-handoff", files, manifest, write=write,
                   manifest_name="cdo-handoff-manifest.json")


def bootstrap(root: Path, source_root: Path | str | None = None, *, apply: bool = False) -> dict[str, Any]:
    """Reconstruct only missing ingest directories, with preserved seeded IDs.

    A supplied source_root must remain below sources/. No source is copied.
    Unsupported/missing inputs are per-source gaps. A reconstructed mismatch is
    rejected before installing that source and never overwrites existing ingest.
    """
    from ..adapters.registry import get_default_registry
    from ..contracts import NormalizationContext
    from ..orchestration.ingestion import IngestionOrchestrator
    from ..project import ProjectPaths
    root = Path(root).resolve()
    seed = _load(_safe(root, "config/source-seed.json"))
    if not isinstance(seed, dict) or seed.get("schema_version") != 1:
        raise ValueError("SOURCE_SEED_REQUIRED")
    supplied = Path(source_root) if source_root is not None else Path("sources")
    if supplied.is_absolute():
        try:
            supplied = supplied.relative_to(root)
        except ValueError as exc:
            raise ValueError("SOURCE_ROOT_MUST_BE_BENEATH_SOURCES") from exc
    relative = _relative(supplied.as_posix())
    if relative.parts[0] != "sources":
        raise ValueError("SOURCE_ROOT_MUST_BE_BENEATH_SOURCES")
    source_dir = _safe(root, relative.as_posix())
    matches: dict[str, list[Path]] = {}
    if source_dir.exists():
        for path in sorted(source_dir.rglob("*")):
            if path.is_symlink():
                raise ValueError("SYMLINK_SOURCE")
            if path.is_file():
                matches.setdefault(sha256_file(path), []).append(path)
    records = seed.get("sources", [])
    if len({r.get("source_id") for r in records}) != len(records):
        raise ValueError("DUPLICATE_SEEDED_SOURCE_ID")
    registry = get_default_registry()
    rows = []
    tasks = []
    for record in records:
        sid, digest = record.get("source_id", ""), record.get("source_sha256", "")
        if not _ID.fullmatch(sid) or not _SHA.fullmatch(digest):
            raise ValueError("INVALID_SOURCE_ID_OR_HASH")
        for value in record.get("relative_paths", []):
            candidate = _relative(value)
            if candidate.parts[0] != "sources":
                raise ValueError("INVALID_SOURCE_PATH")
        expected = record.get("expected_units", [])
        for unit in expected:
            candidate = _relative(unit["filename"])
            if candidate.parts[0] != "units" or not _SHA.fullmatch(unit["file_sha256"]):
                raise ValueError("INVALID_UNIT_RECORD")
        if len({u["filename"] for u in expected}) != len(expected):
            raise ValueError("DUPLICATE_EXPECTED_UNIT")
        row = {"source_id": sid, "source_sha256": digest, "status": "MISSING_SOURCE"}
        paths = matches.get(digest, [])
        if not expected:
            row["status"] = "NO_RECONSTRUCTION_BASELINE"
        elif paths:
            source = paths[0]
            row["relative_source_path"] = source.relative_to(root).as_posix()
            final = _safe(root, "ingest/" + sid)
            if final.exists():
                document = _load(_safe(root, f"ingest/{sid}/document.json"), {})
                valid = document.get("source_sha256") == digest and document.get("validation", {}).get("valid") is True
                actual = {u.get("filename"): u.get("file_sha256") for u in document.get("units", [])}
                valid = valid and actual == {u["filename"]: u["file_sha256"] for u in expected}
                valid = valid and all(_safe(final, u["filename"]).is_file() and sha256_file(_safe(final, u["filename"])) == u["file_sha256"] for u in expected)
                row["status"] = "NOOP" if valid else "EXISTING_INGEST_CONFLICT"
            else:
                try:
                    adapter = registry.select(source)
                except Exception:
                    row["status"] = "ADAPTER_UNAVAILABLE"
                else:
                    if adapter.adapter_id != record.get("adapter_id") or adapter.adapter_version != record.get("adapter_version"):
                        row["status"] = "ADAPTER_VERSION_MISMATCH"
                    else:
                        row["status"] = "READY"
                        tasks.append((record, source, adapter, row))
        rows.append(row)
    manifest_path = _safe(root, "state/source_manifest.jsonl")
    old_manifest = manifest_path.read_bytes() if manifest_path.is_file() else None
    existing_manifest = {r["source_id"]: r for r in _rows(manifest_path)}
    for record in records:
        prior = existing_manifest.get(record["source_id"])
        if prior and prior["source_sha256"] != record["source_sha256"]:
            raise ValueError("SEEDED_SOURCE_MANIFEST_CONFLICT")
        if any(r["source_sha256"] == record["source_sha256"] and sid != record["source_id"] for sid, r in existing_manifest.items()):
            raise ValueError("SEEDED_SOURCE_HASH_ID_CONFLICT")
    installed = []
    staged = []
    if apply and tasks:
        ingest = _safe(root, "ingest")
        ingest.mkdir(parents=True, exist_ok=True)
        for record, source, adapter, row in tasks:
            sid = record["source_id"]
            stage = Path(tempfile.mkdtemp(prefix=".bootstrap-", dir=ingest))
            try:
                context = NormalizationContext(project_root=root, source_id=sid, source_sha256=record["source_sha256"], relative_source_path=row["relative_source_path"], domain_slugs=tuple(record.get("domains", [])), output_dir=stage, profile="strict-local")
                result = adapter.normalize(source, context)
                report = adapter.validate(result, context)
                if not report.valid or sha256_file(source) != record["source_sha256"]:
                    raise ValueError("RECONSTRUCTION_INVALID")
                orchestrator = IngestionOrchestrator(ProjectPaths(root), registry)
                source_row = {**record, "relative_paths": [row["relative_source_path"]]}
                document = orchestrator._write_result(stage, source_row, context, result, report)
                orchestrator._validate_directory(stage, document)
                expected = {u["filename"]: u["file_sha256"] for u in record["expected_units"]}
                if {u["filename"]: u["file_sha256"] for u in document["units"]} != expected:
                    row["status"] = "RECONSTRUCTION_HASH_MISMATCH"
                    continue
                destination = _safe(root, "ingest/" + sid)
                if destination.exists():
                    row["status"] = "EXISTING_INGEST_CONFLICT"
                    continue
                staged.append((stage, destination, row))
                stage = None
            except Exception:
                row["status"] = "RECONSTRUCTION_FAILED"
            finally:
                if stage is not None and stage.exists():
                    shutil.rmtree(stage)
    if apply:
        import jsonschema
        updated = dict(existing_manifest)
        schema = _load(_safe(root, "config/schemas/source-manifest.schema.json"))
        if schema is None:
            schema = _load(Path(__file__).resolve().parents[3] / "config/schemas/source-manifest.schema.json")
        try:
            for record, row in zip(records, rows):
                sid = record["source_id"]
                prior = existing_manifest.get(sid)
                item = dict(prior) if prior else {
                    "schema_version": 1,
                    **{k: record[k] for k in ("source_id", "source_sha256", "relative_paths", "source_format", "source_kind", "domains", "primary_domain")},
                    "adapter_id": record.get("adapter_id"),
                    "adapter_version": record.get("adapter_version", "unknown"),
                    "status": "DISCOVERED", "normativity": "UNCLASSIFIED", "unit_count": 0,
                }
                if row.get("relative_source_path"):
                    item["relative_paths"] = sorted(set(item["relative_paths"]) | {row["relative_source_path"]})
                success = row["status"] in {"READY", "NOOP"}
                if row["status"] == "READY" and not any(r is row for _, _, r in staged):
                    success = False
                if success:
                    if not prior or prior.get("status") not in {"RETIRED", "SUPERSEDED", "QUARANTINED", "EXTRACTED", "AUDITED", "VERIFIED"}:
                        item["status"] = "READY_FOR_LLM"
                    item["unit_count"] = len(record["expected_units"])
                elif not prior:
                    item["status"] = "DISCOVERED" if row["status"] == "MISSING_SOURCE" else "QUARANTINED"
                jsonschema.validate(item, schema)
                updated[sid] = item
            body = b"".join((json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8") for _, r in sorted(updated.items()))
            manifest_path.parent.mkdir(parents=True, exist_ok=True)
            fd, temp = tempfile.mkstemp(prefix=".source-manifest-", dir=manifest_path.parent)
            temp_path = Path(temp)
            try:
                with os.fdopen(fd, "wb") as stream:
                    stream.write(body)
                if (manifest_path.read_bytes() if manifest_path.exists() else None) != old_manifest:
                    raise ValueError("SOURCE_MANIFEST_CHANGED_DURING_BOOTSTRAP")
                for stage, destination, row in staged:
                    if destination.exists():
                        raise ValueError("INGEST_CHANGED_DURING_BOOTSTRAP")
                    os.replace(stage, destination)
                    installed.append(destination)
                if body != old_manifest:
                    os.replace(temp_path, manifest_path)
                for _, _, row in staged:
                    row["status"] = "RECONSTRUCTED"
            finally:
                temp_path.unlink(missing_ok=True)
        except BaseException:
            # Only directories created in this transaction can be rolled back.
            for directory in installed:
                shutil.rmtree(directory)
            raise
        finally:
            for stage, _, _ in staged:
                if stage.exists():
                    shutil.rmtree(stage)
    # New metadata establishes identity and extraction state, never authority,
    # fidelity, evidence review, publication approval or invented timestamps.
    return {"schema_version": 1, "valid": all(r["status"] in {"READY", "NOOP", "RECONSTRUCTED"} for r in rows), "apply": apply, "sources": rows, "reconstructed": sum(r["status"] == "RECONSTRUCTED" for r in rows), "gaps": sum(r["status"] not in {"READY", "NOOP", "RECONSTRUCTED"} for r in rows)}
