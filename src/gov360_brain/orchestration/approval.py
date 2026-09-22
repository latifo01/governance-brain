from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from ..domains import DomainManager
from ..project import ProjectPaths
from ..utils import append_jsonl, atomic_write_text, canonical_json, read_jsonl, sha256_text
from ..vault import VaultPublisher


def _now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


class ApprovalManager:
    def __init__(self, paths: ProjectPaths):
        self.paths = paths
        self.domains = DomainManager(paths)
        self.publisher = VaultPublisher(paths)

    def approve(self, domain: str, stage: str, *, run_id: str | None = None) -> dict[str, Any]:
        pack = self.domains.load(domain)
        if stage == "domain":
            updated = self.domains.set_status(pack.slug, "ACTIVE")
            record = self._record(updated.domain_id, stage, "DOMAIN_PACK", sha256_text(canonical_json(updated.to_mapping())))
            self._log(record)
            return record
        if pack.status != "ACTIVE":
            raise ValueError("Knowledge and questionnaires require an ACTIVE domain")
        run_dir = self._proposal_run(pack.domain_id, stage, run_id)
        review = json.loads((run_dir / "proposals" / "review.json").read_text(encoding="utf-8"))
        if review.get("status") == "BLOCKED":
            raise ValueError("The latest vault review is blocked")
        proposal_name = "knowledge.json" if stage == "knowledge" else "questionnaires.json"
        proposal_path = run_dir / "proposals" / proposal_name
        proposal = json.loads(proposal_path.read_text(encoding="utf-8"))
        proposal_hash = sha256_text(canonical_json(proposal))
        expected_hash = review.get("knowledge_sha256" if stage == "knowledge" else "questionnaires_sha256")
        if expected_hash and expected_hash != proposal_hash:
            raise ValueError("Proposal changed after its review; run the generation stage again")
        effective_run_id = run_dir.name
        existing = [
            row for row in read_jsonl(self.paths.state / "approvals.jsonl")
            if row.get("domain_id") == pack.domain_id and row.get("stage") == stage and row.get("run_id") == effective_run_id and row.get("proposal_sha256") == proposal_hash
        ]
        if existing:
            return existing[-1]

        published: list[Path] = []
        if stage == "knowledge":
            published.extend(self.publisher.publish_knowledge(pack, proposal))
            manifest = {str(row.get("source_id")): row for row in read_jsonl(self.paths.state / "source_manifest.jsonl")}
            evidence = [row for row in read_jsonl(self.paths.state / "evidence_registry.jsonl") if row.get("status") == "VERIFIED" and pack.domain_id in row.get("domains", [])]
            for source_id in sorted({str(row["source_id"]) for row in evidence}):
                source = manifest.get(source_id)
                document_path = self.paths.ingest / source_id / "document.json"
                if source and document_path.exists():
                    document = json.loads(document_path.read_text(encoding="utf-8"))
                    published.append(self.publisher.publish_source_note(source, document, [row for row in evidence if row["source_id"] == source_id], status="VERIFIED"))
        elif stage == "questionnaires":
            approvals = read_jsonl(self.paths.state / "approvals.jsonl")
            if not any(row.get("domain_id") == pack.domain_id and row.get("stage") == "knowledge" and row.get("run_id") == effective_run_id for row in approvals):
                raise ValueError("Approve the knowledge stage for the same run first")
            published.extend(self.publisher.publish_questionnaires(pack, proposal))
        else:
            raise ValueError("stage must be domain, knowledge, or questionnaires")

        self.publisher.rebuild_index()
        self.publisher.write_audit()
        record = self._record(pack.domain_id, stage, effective_run_id, proposal_hash, published_count=len(published))
        self._log(record)
        return record

    def _proposal_run(self, domain_id: str, stage: str, run_id: str | None) -> Path:
        filename = "knowledge.json" if stage == "knowledge" else "questionnaires.json" if stage == "questionnaires" else ""
        candidates: list[Path] = []
        for run_json in sorted((self.paths.state / "runs").glob("*/run.json")):
            try:
                run = json.loads(run_json.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            if run.get("domain_id") == domain_id and (run_id is None or run.get("run_id") == run_id) and (run_json.parent / "proposals" / filename).exists():
                candidates.append(run_json.parent)
        if not candidates:
            raise FileNotFoundError("No reviewable proposal run was found")
        return candidates[-1]

    def _record(self, domain_id: str, stage: str, run_id: str, proposal_hash: str, *, published_count: int = 0) -> dict[str, Any]:
        record = {"schema_version": 1, "approval_id": "APR-" + sha256_text(f"{domain_id}:{stage}:{run_id}:{proposal_hash}")[:20].upper(), "domain_id": domain_id, "stage": stage, "run_id": run_id, "proposal_sha256": proposal_hash, "approved_at": _now(), "published_count": published_count, "approval_source": "explicit_cli_action"}
        append_jsonl(self.paths.state / "approvals.jsonl", record)
        return record

    def _log(self, record: dict[str, Any]) -> None:
        path = self.paths.vault / "00_System" / "Log.md"
        existing = path.read_text(encoding="utf-8") if path.exists() else "# Governance Brain Log\n"
        line = f"- {record['approved_at']} — {record['approval_id']} — {record['domain_id']} — {record['stage']} — run `{record['run_id']}`\n"
        if line not in existing:
            atomic_write_text(path, existing.rstrip() + "\n" + line)
