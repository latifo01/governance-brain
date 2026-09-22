from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import jsonschema
import yaml

from ..domains import DomainManager
from ..project import ProjectPaths
from ..utils import atomic_write_json, read_jsonl, sha256_file
from .publisher import VaultPublisher
from .frontmatter import parse_note, validation_errors


class VaultAuditor:
    def __init__(self, paths: ProjectPaths):
        self.paths = paths

    def run(self, domain_id: str | None = None) -> dict[str, Any]:
        findings: list[dict[str, str]] = []

        def add(severity: str, code: str, artifact: str, remediation: str) -> None:
            findings.append({"severity": severity, "code": code, "artifact": artifact, "remediation": remediation})

        schemas = self.paths.root / "config" / "schemas"
        try:
            domain_schema = self._schema(schemas / "domain-pack.schema.json")
            for path in sorted(self.paths.domain_packs.glob("*/domain.yaml")):
                try:
                    jsonschema.validate(yaml.safe_load(path.read_text(encoding="utf-8")), domain_schema)
                except Exception:
                    add("ERROR", "INVALID_DOMAIN_PACK", path.relative_to(self.paths.root).as_posix(), "Validate the Domain Pack against schema_version 1.")
            DomainManager(self.paths).list()
        except Exception:
            add("ERROR", "DOMAIN_REGISTRY_INVALID", "domain_packs", "Resolve duplicate or invalid stable domain identifiers.")

        manifest_schema = self._schema(schemas / "source-manifest.schema.json")
        manifest = read_jsonl(self.paths.state / "source_manifest.jsonl")
        for row in manifest:
            if domain_id and domain_id not in row.get("domains", []):
                continue
            source_id = str(row.get("source_id", "unknown"))
            try:
                jsonschema.validate(row, manifest_schema)
            except Exception:
                add("ERROR", "INVALID_SOURCE_MANIFEST", source_id, "Repair the manifest record without changing the immutable source.")
            for relative in row.get("relative_paths", []):
                source_path = self.paths.root / str(relative)
                if source_path.exists() and sha256_file(source_path) != row.get("source_sha256"):
                    add("CRITICAL", "SOURCE_HASH_CHANGED", source_id, "Restore the original or register the changed file as a new source version.")

        unit_schema = self._schema(schemas / "ingested-unit.schema.json")
        valid_units: set[tuple[str, str, str]] = set()
        for document_path in sorted(self.paths.ingest.glob("SRC-*/document.json")):
            source_id = document_path.parent.name
            try:
                document = json.loads(document_path.read_text(encoding="utf-8"))
            except Exception:
                add("ERROR", "INVALID_DOCUMENT_JSON", source_id, "Regenerate normalization atomically.")
                continue
            manifest_row = next((row for row in manifest if row.get("source_id") == source_id), None)
            if not manifest_row or document.get("source_sha256") != manifest_row.get("source_sha256"):
                add("ERROR", "LINEAGE_MISMATCH", source_id, "Regenerate from the registered immutable source hash.")
            for unit in document.get("units", []):
                path = document_path.parent / str(unit.get("filename", ""))
                try:
                    text = path.read_text(encoding="utf-8")
                    metadata = self._frontmatter(text)
                    jsonschema.validate(metadata, unit_schema)
                    if sha256_file(path) != unit.get("file_sha256"):
                        raise ValueError
                    valid_units.add((source_id, str(unit.get("locator")), str(unit.get("content_sha256"))))
                except Exception:
                    add("ERROR", "INVALID_INGEST_UNIT", f"{source_id}/{unit.get('filename')}", "Regenerate and validate the normalized unit.")

        receipt_schema = self._schema(schemas / "receipt.schema.json")
        for receipt in sorted((self.paths.state / "runs").glob("*/receipts/*.json")):
            try:
                jsonschema.validate(json.loads(receipt.read_text(encoding="utf-8")), receipt_schema)
            except Exception:
                add("ERROR", "INVALID_RECEIPT", receipt.relative_to(self.paths.root).as_posix(), "Regenerate the immutable job receipt.")

        evidence = read_jsonl(self.paths.state / "evidence_registry.jsonl")
        verified_keys: set[tuple[str, str, str]] = set()
        for item in evidence:
            key = (str(item.get("source_id")), str(item.get("locator")), str(item.get("unit_content_sha256")))
            if item.get("status") == "VERIFIED":
                if key not in valid_units:
                    add("ERROR", "ORPHAN_EVIDENCE", str(item.get("evidence_ref")), "Re-audit against a valid unit hash and locator.")
                verified_keys.add((key[0], str(item.get("source_sha256")), key[1]))

        question_schema = self._schema(schemas / "questionnaire.schema.json")
        questions = read_jsonl(self.paths.state / "question_registry.jsonl")
        approvals = read_jsonl(self.paths.state / "approvals.jsonl")
        for question in questions:
            qid = str(question.get("question_id", "unknown"))
            try:
                candidate = dict(question)
                if candidate.get("status") == "PUBLISHED":
                    candidate["status"] = "PROPOSED"
                jsonschema.validate(candidate, question_schema)
            except Exception:
                add("ERROR", "INVALID_QUESTION", qid, "Repair the bilingual question and its conditional logic.")
            for ref in question.get("evidence_refs", []):
                key = (str(ref.get("source_id")), str(ref.get("source_sha256")), str(ref.get("locator"))) if isinstance(ref, dict) else ("", "", "")
                if key not in verified_keys:
                    add("ERROR", "UNVERIFIED_QUESTION_EVIDENCE", qid, "Attach at least one currently verified evidence locator.")
            if question.get("status") == "PUBLISHED" and not any(row.get("domain_id") == question.get("domain") and row.get("stage") == "questionnaires" for row in approvals):
                add("CRITICAL", "MISSING_APPROVAL", qid, "Record explicit questionnaire approval before publication.")
        try:
            VaultPublisher._assert_acyclic({str(item.get("question_id")): item for item in questions})
        except ValueError:
            add("ERROR", "QUESTION_DEPENDENCY_CYCLE", "question_registry.jsonl", "Remove the cyclic dependency before publication.")

        # Relations are a separate, controlled registry.  Validate both the
        # public shape and the resolved endpoints so a syntactically valid
        # relation cannot silently create a dangling graph edge.
        relation_schema_path = schemas / "relation.schema.json"
        relation_rows = read_jsonl(self.paths.state / "relations.jsonl")
        relation_schema = self._schema(relation_schema_path) if relation_schema_path.exists() else None
        verified_evidence = {
            str(item.get("evidence_ref")): item
            for item in evidence
            if item.get("status") == "VERIFIED"
        }
        relation_ids: set[str] = set()
        targets = VaultPublisher(self.paths)._target_index()
        for relation in relation_rows:
            relation_id = str(relation.get("relation_id", "unknown"))
            if relation_id in relation_ids:
                add("ERROR", "DUPLICATE_RELATION_ID", relation_id, "Keep one deterministic record for each relation identity.")
            relation_ids.add(relation_id)
            try:
                if relation_schema:
                    jsonschema.validate(relation, relation_schema)
                VaultPublisher._validate_relation_candidates([relation], verified_evidence)
            except Exception:
                add("ERROR", "INVALID_RELATION", relation_id, "Repair the relation against the controlled vocabulary and verified evidence.")
                continue
            subject_id = str(relation.get("subject_id"))
            target_id = str(relation.get("target_id"))
            if relation.get("status") == "UNRESOLVED":
                add("ERROR", "UNRESOLVED_RELATION", relation_id, "Publish or correct both reviewed relation endpoints before publication.")
            elif relation.get("status") == "PUBLISHED":
                if subject_id not in targets or target_id not in targets:
                    add("ERROR", "PUBLISHED_RELATION_UNRESOLVED", relation_id, "Reconcile the relation after both target notes exist.")
                for key in ("subject_path", "target_path"):
                    if not relation.get(key):
                        add("ERROR", "RELATION_PATH_MISSING", relation_id, "Rebuild the resolved relation paths.")
            for key in ("subject_path", "target_path"):
                path_text = relation.get(key)
                if not path_text:
                    continue
                path = self.paths.vault / (str(path_text) + ".md")
                if not path.exists():
                    add("ERROR", "RELATION_NOTE_MISSING", relation_id, "Reconcile relation paths against the current vault.")
                    continue
                metadata = self._frontmatter(path.read_text(encoding="utf-8"))
                relation_metadata_ids = {
                    str(item.get("relation_id")) if isinstance(item, dict) else str(item)
                    for item in metadata.get("relations", metadata.get("relation_ids", []))
                }
                if relation_id not in relation_metadata_ids:
                    add("ERROR", "RELATION_FRONTMATTER_MISSING", relation_id, "Rebuild the note relation_ids frontmatter field.")

        vault_pages = sorted(self.paths.vault.rglob("*.md"))
        for page in vault_pages:
            text = page.read_text(encoding="utf-8")
            # Every vault note participates in the same graph contract.  The
            # parser infers the legacy system/audit family from its location,
            # then reports actionable schema defects without exposing body
            # content in the audit report.
            inferred_type = "audit" if "90_Audit" in page.relative_to(self.paths.vault).parts else ("system" if "00_System" in page.relative_to(self.paths.vault).parts else None)
            try:
                note = parse_note(text, validate=False, canonical=True, note_type=inferred_type)
                errors = validation_errors(note.metadata)
                if errors:
                    add("ERROR", "INVALID_VAULT_FRONTMATTER", page.relative_to(self.paths.vault).as_posix(), "Normalize the note frontmatter against config/schemas/vault-frontmatter.schema.json.")
            except Exception:
                add("ERROR", "INVALID_VAULT_FRONTMATTER", page.relative_to(self.paths.vault).as_posix(), "Add a valid unified YAML frontmatter block.")
            for target in re.findall(r"\[\[([^\]|#]+)", text):
                normalized = target.replace("\\", "/").strip()
                candidates = (
                    self.paths.vault / f"{normalized}.md",
                    self.paths.vault / normalized,
                    page.parent / f"{normalized}.md",
                    page.parent / normalized,
                )
                if not any(candidate.exists() for candidate in candidates):
                    add("ERROR", "BROKEN_WIKI_LINK", page.relative_to(self.paths.vault).as_posix(), f"Create or correct the reviewed target: {target}")

        findings.sort(key=lambda item: (item["severity"], item["code"], item["artifact"]))
        result = {
            "schema_version": 1,
            "domain_id": domain_id,
            "status": "BLOCKED" if any(item["severity"] in {"CRITICAL", "ERROR"} for item in findings) else "READY_FOR_HUMAN_APPROVAL",
            "counts": {
                "sources": len(manifest),
                "ingest_units": len(valid_units),
                "verified_evidence": sum(1 for item in evidence if item.get("status") == "VERIFIED"),
                "questions": len(questions),
                "relations": len(relation_rows),
                "findings": len(findings),
            },
            "findings": findings,
        }
        atomic_write_json(self.paths.state / "audit_report.json", result)
        VaultPublisher(self.paths).write_audit()
        return result

    @staticmethod
    def _schema(path: Path) -> dict[str, Any]:
        return json.loads(path.read_text(encoding="utf-8"))

    @staticmethod
    def _frontmatter(text: str) -> dict[str, Any]:
        if not text.startswith("---\n"):
            raise ValueError("missing frontmatter")
        end = text.find("\n---\n", 4)
        if end < 0:
            raise ValueError("unterminated frontmatter")
        value = yaml.safe_load(text[4:end])
        if not isinstance(value, dict):
            raise ValueError("frontmatter must be a mapping")
        return value
