from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml

from ..domains import DomainPack
from ..project import ProjectPaths
from ..utils import atomic_write_text, read_jsonl, safe_filename, sha256_text, write_jsonl, yaml_scalar
from .frontmatter import render_note


RELATION_TYPES = frozenset(
    {
        "defines",
        "requires",
        "applies_to",
        "exception_to",
        "depends_on",
        "conflicts_with",
        "supersedes",
        "related_to",
    }
)
NOTE_TYPES = frozenset({"SOURCE", "CONCEPT", "RULE", "DOMAIN", "QUESTION", "MAP"})

# This is deliberately stricter than the schema's endpoint enums.  It prevents
# a relation that is syntactically valid from becoming a semantically invalid
# edge in the graph.  ``related_to`` and ``conflicts_with`` are intentionally
# broad; their evidence and labels still make the distinction visible.
RELATION_ENDPOINTS: dict[str, frozenset[tuple[str, str]]] = {
    "defines": frozenset(
        {
            ("SOURCE", "CONCEPT"),
            ("SOURCE", "RULE"),
            ("SOURCE", "DOMAIN"),
            ("DOMAIN", "CONCEPT"),
            ("DOMAIN", "RULE"),
            ("CONCEPT", "CONCEPT"),
            ("CONCEPT", "RULE"),
            ("RULE", "CONCEPT"),
            ("RULE", "RULE"),
        }
    ),
    "requires": frozenset(
        {
            (subject, target)
            for subject in ("DOMAIN", "CONCEPT", "RULE")
            for target in ("CONCEPT", "RULE", "QUESTION")
        }
    ),
    "applies_to": frozenset(
        {
            ("CONCEPT", "DOMAIN"),
            ("CONCEPT", "QUESTION"),
            ("RULE", "DOMAIN"),
            ("RULE", "QUESTION"),
        }
    ),
    "exception_to": frozenset(
        {
            (subject, target)
            for subject in ("CONCEPT", "RULE")
            for target in ("CONCEPT", "RULE")
        }
    ),
    "depends_on": frozenset(
        {
            (subject, target)
            for subject in ("CONCEPT", "RULE", "QUESTION")
            for target in ("CONCEPT", "RULE", "QUESTION")
        }
    ),
    "conflicts_with": frozenset((subject, target) for subject in NOTE_TYPES for target in NOTE_TYPES),
    "supersedes": frozenset((kind, kind) for kind in NOTE_TYPES),
    "related_to": frozenset((subject, target) for subject in NOTE_TYPES for target in NOTE_TYPES),
}


class VaultPublisher:
    def __init__(self, paths: ProjectPaths):
        self.paths = paths

    def ensure_layout(self) -> None:
        for name in (
            "00_System",
            "10_Sources",
            "20_Concepts",
            "30_Domains",
            "40_Rules",
            "50_Questionnaires",
            "60_Maps",
            "90_Audit",
            "_assets",
        ):
            (self.paths.vault / name).mkdir(parents=True, exist_ok=True)

    def publish_source_note(
        self,
        source: dict[str, Any],
        document: dict[str, Any],
        evidence: list[dict[str, Any]],
        *,
        status: str,
    ) -> Path:
        self.ensure_layout()
        source_id = str(source["source_id"])
        source_name = Path(str(source.get("relative_paths", [source_id])[0])).name
        filename = safe_filename(f"{source_id} - {Path(source_name).stem}", ".md")
        path = self.paths.vault / "10_Sources" / filename
        domains = sorted(str(item) for item in source.get("domains", []))
        accepted = [item for item in evidence if item.get("status") == "VERIFIED"]
        metadata = {
            "type": "source",
            "schema_version": 1,
            "stable_id": source_id,
            "source_id": source_id,
            "revision": 1,
            "title": f"{source_id} — {source_name}",
            "aliases": [source_name],
            "domains": domains,
            "status": status,
            "source_sha256": str(source.get("source_sha256", "")),
            "source_format": str(document.get("source_format") or "unknown").lower(),
            "source_kind": str(source.get("source_kind", "document")),
            "normativity": str(source.get("normativity", "UNCLASSIFIED")),
            "evidence_refs": sorted(str(item.get("evidence_ref")) for item in accepted if item.get("evidence_ref")),
            "relations": [],
            "provenance": {
                "source_id": source_id,
                "source_sha256": str(source.get("source_sha256", "")),
                "source_ids": [source_id],
                "locators": sorted(str(item.get("locator")) for item in accepted if item.get("locator")),
                "adapter_id": str(document.get("adapter_id", "")),
                "adapter_version": str(document.get("adapter_version", "")),
            },
        }
        lines = [
            f"# {source_id} — {source_name}",
            "",
            f"Normalized units: {len(document.get('units', []))}. Evidence status: `{status}`.",
            "",
            "## Provenance",
            "",
            f"- Immutable source hash: `{source['source_sha256']}`",
            f"- Adapter: `{document.get('adapter_id')}@{document.get('adapter_version')}`",
            "",
            "## Evidence",
            "",
        ]
        if not accepted:
            lines.append("No verified claims are available. Human review is required.")
        else:
            for item in sorted(accepted, key=lambda value: (str(value.get("locator")), str(value.get("claim_id")))):
                lines.extend([
                    f"### {item.get('claim_id')} — {item.get('locator')}",
                    "",
                    str(item.get("claim", "")).strip(),
                    "",
                    f"Evidence: `{item.get('evidence_ref')}`",
                    "",
                ])
        lines.extend(["## Unit coverage", ""])
        for unit in document.get("units", []):
            lines.append(f"- `{unit.get('locator')}` → `ingest/{source_id}/{unit.get('filename')}`")
        atomic_write_text(path, render_note(metadata, "\n".join(lines), validate=True))
        self.reconcile_relations()
        return path

    def publish_knowledge(self, pack: DomainPack, proposal: dict[str, Any]) -> list[Path]:
        """Materialize an approved typed change set; never infer approval here."""

        self.ensure_layout()
        verified = {
            str(row.get("evidence_ref")): row
            for row in read_jsonl(self.paths.state / "evidence_registry.jsonl")
            if row.get("status") == "VERIFIED"
        }
        relation_candidates = self._relation_candidates(proposal)
        # Validate the shape and evidence before writing any knowledge note so
        # an invalid relation cannot leave a half-materialized approval behind.
        self._validate_relation_candidates(relation_candidates, verified, pack)
        registry_path = self.paths.state / "knowledge_registry.jsonl"
        registry = {str(row.get("stable_id")): row for row in read_jsonl(registry_path)}
        output: list[Path] = []
        for change in proposal.get("changes", []):
            if change.get("change_type") == "NOOP":
                continue
            stable_id = str(change.get("stable_id", ""))
            refs = [str(item) for item in change.get("evidence_refs", [])]
            if not stable_id or not refs or any(item not in verified for item in refs):
                raise ValueError(f"Knowledge change lacks verified evidence: {stable_id or '<missing>'}")
            modality = str(change.get("modality", "context"))
            if modality in {"obligation", "prohibition"}:
                manifest = {str(row.get("source_id")): row for row in read_jsonl(self.paths.state / "source_manifest.jsonl")}
                if any(manifest.get(str(verified[ref].get("source_id")), {}).get("normativity") != "BINDING" for ref in refs):
                    raise ValueError(f"Non-binding evidence cannot publish {modality}: {stable_id}")
            kind = str(change.get("artifact_type", "CONCEPT"))
            folder = "20_Concepts" if kind == "CONCEPT" else "40_Rules"
            affected_domains = sorted(set(str(item).upper() for item in change.get("affected_domains", [])) | {pack.domain_id})
            evidence_rows = [verified[ref] for ref in sorted(set(refs))]
            row = {
                "schema_version": 1,
                "stable_id": stable_id,
                "artifact_type": kind,
                "title": str(change.get("title", "")),
                "statement": str(change.get("statement", "")),
                "modality": modality,
                "evidence_refs": sorted(set(refs)),
                "affected_domains": affected_domains,
                "status": "PUBLISHED",
            }
            registry[stable_id] = row
            metadata = {
                "type": kind.lower(),
                "schema_version": 1,
                "stable_id": stable_id,
                "revision": int(change.get("revision", 1)),
                "title": row["title"],
                "aliases": [str(item) for item in change.get("aliases", [])],
                "domains": affected_domains,
                "affected_domains": affected_domains,
                "status": "PUBLISHED",
                "artifact_type": kind,
                "modality": modality,
                "statement": row["statement"],
                "evidence_refs": sorted(set(refs)),
                "relations": [],
                "provenance": {
                    "source_ids": sorted({str(item.get("source_id")) for item in evidence_rows}),
                    "source_sha256s": sorted({str(item.get("source_sha256")) for item in evidence_rows}),
                    "locators": sorted({str(item.get("locator")) for item in evidence_rows}),
                    "evidence_refs": sorted(set(refs)),
                    "generated_by": "knowledge_architect",
                },
            }
            lines = [
                f"# {row['title']}",
                "",
                row["statement"],
                "",
                "## Evidence",
                "",
                *(f"- `{item}` — {verified[item]['source_id']}, {verified[item]['locator']}" for item in row["evidence_refs"]),
            ]
            path = self.paths.vault / folder / f"{safe_filename(stable_id)}.md"
            atomic_write_text(path, render_note(metadata, "\n".join(lines), validate=True))
            output.append(path)
        write_jsonl(registry_path, [registry[key] for key in sorted(registry)])
        self.publish_relations({"relations": relation_candidates, "domain_id": pack.domain_id}, verified=verified)
        return output

    @staticmethod
    def _relation_candidates(proposal: dict[str, Any]) -> list[dict[str, Any]]:
        """Accept both names used by early and current change-set drafts."""

        values = proposal.get("relations")
        if values is None:
            values = proposal.get("relation_changes", [])
        if values is None:
            return []
        if not isinstance(values, list):
            raise ValueError("Relation change set must be an array")
        return [item for item in values if isinstance(item, dict)]

    @classmethod
    def _validate_relation_candidates(
        cls,
        candidates: list[dict[str, Any]],
        verified: dict[str, dict[str, Any]],
        pack: DomainPack | None = None,
    ) -> None:
        seen: set[str] = set()
        for candidate in candidates:
            relation_type = str(candidate.get("relation_type", candidate.get("type", ""))).lower()
            subject_type = str(candidate.get("subject_type", "")).upper()
            target_type = str(candidate.get("target_type", "")).upper()
            subject_id = str(candidate.get("subject_id", "")).strip()
            target_id = str(candidate.get("target_id", "")).strip()
            if relation_type not in RELATION_TYPES:
                raise ValueError(f"Unsupported relation type: {relation_type or '<missing>'}")
            if subject_type not in NOTE_TYPES or target_type not in NOTE_TYPES:
                raise ValueError(f"Unsupported relation endpoint type: {subject_type or '<missing>'} -> {target_type or '<missing>'}")
            if (subject_type, target_type) not in RELATION_ENDPOINTS[relation_type]:
                raise ValueError(f"Relation endpoint is not allowed: {relation_type} {subject_type} -> {target_type}")
            if not subject_id or not target_id:
                raise ValueError("Relation subject_id and target_id are required")
            evidence_refs = candidate.get("evidence_refs", [])
            if not isinstance(evidence_refs, list) or not evidence_refs:
                raise ValueError(f"Relation lacks evidence: {subject_id} -> {target_id}")
            refs = {
                str(item.get("evidence_ref")) if isinstance(item, dict) else str(item)
                for item in evidence_refs
            }
            if not refs or any(ref not in verified for ref in refs):
                raise ValueError(f"Relation uses unverified evidence: {subject_id} -> {target_id}")
            relation_id = str(candidate.get("relation_id", ""))
            if relation_id:
                if not re.fullmatch(r"REL-[A-F0-9]{16,64}", relation_id):
                    raise ValueError(f"Invalid relation_id: {relation_id}")
                if relation_id in seen:
                    raise ValueError(f"Duplicate relation_id: {relation_id}")
                seen.add(relation_id)
            affected = candidate.get("affected_domains", [])
            if affected is None:
                affected = []
            if not isinstance(affected, list):
                raise ValueError("Relation affected_domains must be an array")
            if pack and pack.domain_id not in affected:
                # Domain membership is added during normalization.  This is
                # intentionally not an error for proposals authored globally.
                continue

    @staticmethod
    def _relation_id(candidate: dict[str, Any], refs: list[str]) -> str:
        explicit = str(candidate.get("relation_id", "")).strip()
        if explicit:
            return explicit
        seed = {
            "relation_type": str(candidate.get("relation_type", candidate.get("type", ""))).lower(),
            "subject_id": str(candidate.get("subject_id", "")),
            "subject_type": str(candidate.get("subject_type", "")).upper(),
            "target_id": str(candidate.get("target_id", "")),
            "target_type": str(candidate.get("target_type", "")).upper(),
            "evidence_refs": sorted(refs),
        }
        return "REL-" + sha256_text(json.dumps(seed, ensure_ascii=False, sort_keys=True, separators=(",", ":")))[:20].upper()

    def publish_relations(
        self,
        proposal: dict[str, Any] | None = None,
        *,
        verified: dict[str, dict[str, Any]] | None = None,
    ) -> list[Path]:
        """Resolve and materialize an approved relation change set.

        Relation records are prepared independently from note rendering.  The
        complete target table is built only after all notes in the batch have
        been written, which makes the result independent of worker completion
        order.  Missing targets remain explicit ``UNRESOLVED`` records and do
        not create placeholder notes.
        """

        self.ensure_layout()
        proposal = proposal or {}
        relation_candidates = self._relation_candidates(proposal)
        if verified is None:
            verified = {
                str(row.get("evidence_ref")): row
                for row in read_jsonl(self.paths.state / "evidence_registry.jsonl")
                if row.get("status") == "VERIFIED"
            }
        self._validate_relation_candidates(relation_candidates, verified)

        registry_path = self.paths.state / "relations.jsonl"
        registry = {
            str(row.get("relation_id")): row
            for row in read_jsonl(registry_path)
            if row.get("relation_id")
        }
        default_domain = str(proposal.get("domain_id", "")).upper()
        for candidate in relation_candidates:
            refs = sorted(
                {
                    str(item.get("evidence_ref")) if isinstance(item, dict) else str(item)
                    for item in candidate.get("evidence_refs", [])
                }
            )
            relation_id = self._relation_id(candidate, refs)
            affected = sorted(
                {
                    str(item).upper()
                    for item in candidate.get("affected_domains", [])
                    if str(item).strip()
                }
                | ({default_domain} if default_domain else set())
            )
            registry[relation_id] = {
                "schema_version": 1,
                "relation_id": relation_id,
                "relation_type": str(candidate.get("relation_type", candidate.get("type", ""))).lower(),
                "subject_id": str(candidate["subject_id"]).strip(),
                "subject_type": str(candidate["subject_type"]).upper(),
                "target_id": str(candidate["target_id"]).strip(),
                "target_type": str(candidate["target_type"]).upper(),
                "evidence_refs": refs,
                "affected_domains": affected,
                "reason": str(candidate.get("reason", "")),
                "status": str(candidate.get("status", "PROPOSED")).upper(),
            }

        resolved = self._reconcile_relations(registry)
        write_jsonl(registry_path, [registry[key] for key in sorted(registry)])
        self._write_relation_sections(resolved)
        return []

    def reconcile_relations(self) -> None:
        """Retry unresolved relations after a new note becomes available."""

        self.publish_relations({})

    def _reconcile_relations(self, registry: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
        targets = self._target_index()
        unresolved = {
            str(row.get("relation_id")): row
            for row in read_jsonl(self.paths.state / "unresolved.jsonl")
            if row.get("relation_id")
        }
        resolved: list[dict[str, Any]] = []
        for relation_id in sorted(registry):
            row = registry[relation_id]
            if row.get("status") in {"REJECTED", "SUPERSEDED"}:
                row.pop("subject_path", None)
                row.pop("target_path", None)
                row.pop("resolution_error", None)
                unresolved.pop(relation_id, None)
                continue
            subject = targets.get(str(row.get("subject_id")))
            target = targets.get(str(row.get("target_id")))
            if subject and target:
                row["status"] = "PUBLISHED"
                row["subject_path"] = subject["path"]
                row["target_path"] = target["path"]
                row.pop("resolution_error", None)
                unresolved.pop(relation_id, None)
                resolved.append(row)
                continue
            missing: list[str] = []
            if not subject:
                missing.append(f"{row.get('subject_type')}:{row.get('subject_id')}")
            if not target:
                missing.append(f"{row.get('target_type')}:{row.get('target_id')}")
            row["status"] = "UNRESOLVED"
            row.pop("subject_path", None)
            row.pop("target_path", None)
            row["resolution_error"] = "Missing or ambiguous target: " + ", ".join(missing)
            unresolved[relation_id] = {
                "schema_version": 1,
                "finding_id": "UNRES-" + relation_id.removeprefix("REL-"),
                "kind": "RELATION_TARGET_UNRESOLVED",
                "relation_id": relation_id,
                "status": "UNRESOLVED",
                "subject_id": row.get("subject_id"),
                "target_id": row.get("target_id"),
                "remediation": "Publish or correct the reviewed target before exposing this relation.",
            }
        write_jsonl(self.paths.state / "unresolved.jsonl", [unresolved[key] for key in sorted(unresolved)])
        return resolved

    def _target_index(self) -> dict[str, dict[str, str]]:
        """Return unambiguous stable IDs and their vault-relative note paths."""

        candidates: dict[str, set[Path]] = {}
        labels: dict[Path, str] = {}

        def add(identifier: Any, path: Path, label: str | None = None) -> None:
            value = str(identifier or "").strip()
            if not value:
                return
            candidates.setdefault(value, set()).add(path)
            labels[path] = label or path.stem

        for path in sorted(self.paths.vault.rglob("*.md")):
            metadata = self._note_frontmatter(path)
            if not metadata:
                continue
            for key in ("stable_id", "source_id", "question_id", "domain_id", "map_id"):
                if metadata.get(key):
                    add(metadata[key], path, str(metadata.get("title") or path.stem))

        # Registries provide a deterministic fallback for notes whose
        # frontmatter predates the graph fields.
        for row in read_jsonl(self.paths.state / "knowledge_registry.jsonl"):
            stable_id = str(row.get("stable_id", ""))
            folder = "20_Concepts" if row.get("artifact_type") == "CONCEPT" else "40_Rules"
            path = self.paths.vault / folder / f"{safe_filename(stable_id)}.md"
            if stable_id and path.exists():
                add(stable_id, path, str(row.get("title") or path.stem))
        for row in read_jsonl(self.paths.state / "question_registry.jsonl"):
            question_id = str(row.get("question_id", ""))
            domain = str(row.get("domain", ""))
            path = self.paths.vault / "50_Questionnaires" / domain / f"{safe_filename(question_id)}.md"
            if question_id and path.exists():
                add(question_id, path, question_id)

        index: dict[str, dict[str, str]] = {}
        for identifier, paths in candidates.items():
            if len(paths) != 1:
                # Ambiguous IDs are treated exactly like missing IDs.  Picking
                # a winner would make parallel publication non-deterministic.
                continue
            path = next(iter(paths))
            relative = path.relative_to(self.paths.vault).with_suffix("").as_posix()
            index[identifier] = {"path": relative, "label": labels.get(path, path.stem)}
        return index

    @staticmethod
    def _note_frontmatter(path: Path) -> dict[str, Any]:
        try:
            text = path.read_text(encoding="utf-8")
            match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
            if not match:
                return {}
            value = yaml.safe_load(match.group(1))
            return value if isinstance(value, dict) else {}
        except (OSError, UnicodeError, yaml.YAMLError):
            return {}

    def _write_relation_sections(self, relations: list[dict[str, Any]]) -> None:
        outgoing: dict[str, list[dict[str, Any]]] = {}
        incoming: dict[str, list[dict[str, Any]]] = {}
        by_path = {str(item["subject_path"]): item for item in relations if item.get("subject_path")}
        for row in relations:
            subject_path = str(row.get("subject_path", ""))
            target_path = str(row.get("target_path", ""))
            if not subject_path or not target_path:
                continue
            outgoing.setdefault(subject_path, []).append(row)
            incoming.setdefault(target_path, []).append(row)
        paths = set(outgoing) | set(incoming)
        for path_text in sorted(paths):
            path = self.paths.vault / (path_text + ".md")
            if not path.exists():
                continue
            rows_out = sorted(outgoing.get(path_text, []), key=lambda row: (str(row.get("relation_type")), str(row.get("target_path")), str(row.get("relation_id"))))
            rows_in = sorted(incoming.get(path_text, []), key=lambda row: (str(row.get("relation_type")), str(row.get("subject_path")), str(row.get("relation_id"))))
            relation_ids = sorted({str(row.get("relation_id")) for row in rows_out + rows_in})
            self._update_note_relations(path, rows_out, rows_in, relation_ids)

        # Remove stale generated sections from notes whose relations were
        # superseded or resolved away.
        for path in sorted(self.paths.vault.rglob("*.md")):
            if path in {self.paths.vault / (item + ".md") for item in paths}:
                continue
            text = path.read_text(encoding="utf-8")
            if "<!-- gov360:relations:start -->" in text:
                self._update_note_relations(path, [], [], [])

    def _update_note_relations(
        self,
        path: Path,
        outgoing: list[dict[str, Any]],
        incoming: list[dict[str, Any]],
        relation_ids: list[str],
    ) -> None:
        text = path.read_text(encoding="utf-8")
        metadata, body = self._split_note_frontmatter(text)
        if metadata is not None:
            metadata.pop("relation_ids", None)
            metadata["relations"] = [
                {
                    "relation_id": str(row.get("relation_id")),
                    "relation_type": str(row.get("relation_type")),
                    "target_id": str(row.get("target_id")),
                    "target_type": str(row.get("target_type")),
                    "status": "PUBLISHED",
                    "reason": str(row.get("reason", "")),
                    "evidence_refs": list(row.get("evidence_refs", [])),
                }
                for row in outgoing
            ]
            # The relation pass also touches legacy domain/system notes.  They
            # are normalized through the same renderer, while the audit owns
            # the decision whether a legacy note now satisfies the schema.
            text = render_note(metadata, body.lstrip("\n"), validate=False)
        text = re.sub(r"\n?<!-- gov360:relations:start -->.*?<!-- gov360:relations:end -->\n?", "\n", text, flags=re.DOTALL)
        if outgoing or incoming:
            lines = ["<!-- gov360:relations:start -->", "## Relations", ""]
            lines.extend(
                f"- `{row['relation_type']}` → {self._link_for_path(str(row['target_path']))} (`{row['relation_id']}`)"
                for row in outgoing
            )
            if incoming:
                lines.extend(["", "## Backlinks", ""])
                lines.extend(
                    f"- {self._link_for_path(str(row['subject_path']))} — `{row['relation_type']}` (`{row['relation_id']}`)"
                    for row in incoming
                )
            lines.append("<!-- gov360:relations:end -->")
            text = text.rstrip() + "\n\n" + "\n".join(lines) + "\n"
        else:
            text = text.rstrip() + "\n"
        atomic_write_text(path, text)

    @staticmethod
    def _link_for_path(path: str) -> str:
        label = path.rsplit("/", 1)[-1].replace("|", "¦")
        return f"[[{path}|{label}]]"

    @staticmethod
    def _split_note_frontmatter(text: str) -> tuple[dict[str, Any] | None, str]:
        match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
        if not match:
            return None, text
        try:
            value = yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            return None, text
        return (value if isinstance(value, dict) else None), text[match.end() :]

    def rebuild_index(self) -> Path:
        self.ensure_layout()
        sections = {
            "Sources": "10_Sources",
            "Concepts": "20_Concepts",
            "Domains": "30_Domains",
            "Rules": "40_Rules",
            "Questionnaires": "50_Questionnaires",
            "Maps": "60_Maps",
        }
        lines = ["# Governance Brain Index", "", "This index is rebuilt deterministically.", ""]
        for title, folder in sections.items():
            lines.extend([f"## {title}", ""])
            paths = sorted((self.paths.vault / folder).rglob("*.md"), key=lambda item: item.relative_to(self.paths.vault).as_posix().lower())
            if not paths:
                lines.append("_None._")
            else:
                for path in paths:
                    relative = path.relative_to(self.paths.vault).with_suffix("").as_posix()
                    lines.append(f"- [[{relative}|{path.stem}]]")
            lines.append("")
        target = self.paths.vault / "00_System" / "Index.md"
        metadata = {
            "type": "system",
            "schema_version": 1,
            "stable_id": "GOV360_INDEX",
            "revision": 1,
            "title": "Governance Brain Index",
            "aliases": ["Index"],
            "domains": [],
            "affected_domains": [],
            "status": "CURRENT",
            "artifact_type": "SYSTEM",
            "evidence_refs": [],
            "relations": [],
            "provenance": {"generated_by": "vault_indexer"},
        }
        atomic_write_text(target, render_note(metadata, "\n".join(lines), validate=True))
        return target

    def write_audit(self) -> Path:
        self.ensure_layout()
        source_manifest = read_jsonl(self.paths.state / "source_manifest.jsonl")
        evidence = read_jsonl(self.paths.state / "evidence_registry.jsonl")
        questions = read_jsonl(self.paths.state / "question_registry.jsonl")
        statuses: dict[str, int] = {}
        for row in source_manifest:
            status = str(row.get("status", "UNKNOWN"))
            statuses[status] = statuses.get(status, 0) + 1
        broken: list[str] = []
        for page in self.paths.vault.rglob("*.md"):
            text = page.read_text(encoding="utf-8")
            for token in re.findall(r"\[\[([^\]|#]+)", text):
                normalized = token.replace("\\", "/").strip()
                candidates = (
                    self.paths.vault / f"{normalized}.md",
                    self.paths.vault / normalized,
                    page.parent / f"{normalized}.md",
                    page.parent / normalized,
                )
                if not any(candidate.exists() for candidate in candidates):
                    broken.append(f"{page.relative_to(self.paths.vault).as_posix()} -> {token}")
        lines = [
            "# Vault Audit",
            "",
            "Generated deterministically from state and vault files.",
            "",
            "## Counts",
            "",
            f"- Sources: {len(source_manifest)}",
            f"- Verified evidence items: {sum(1 for row in evidence if row.get('status') == 'VERIFIED')}",
            f"- Published questions: {sum(1 for row in questions if row.get('status') == 'PUBLISHED')}",
            f"- Broken wiki links: {len(set(broken))}",
            "",
            "## Source states",
            "",
            *(f"- {key}: {statuses[key]}" for key in sorted(statuses)),
            "",
            "## Broken links",
            "",
            *(sorted(set(broken)) or ["None."]),
        ]
        path = self.paths.vault / "90_Audit" / "Vault_Audit.md"
        audit_status = "READY_FOR_HUMAN_APPROVAL"
        audit_state = self.paths.state / "audit_report.json"
        if audit_state.exists():
            try:
                candidate_status = str(json.loads(audit_state.read_text(encoding="utf-8")).get("status", ""))
                if candidate_status in {"READY_FOR_HUMAN_APPROVAL", "BLOCKED"}:
                    audit_status = candidate_status
            except (OSError, json.JSONDecodeError):
                pass
        metadata = {
            "type": "audit",
            "schema_version": 1,
            "stable_id": "VAULT_AUDIT",
            "revision": 1,
            "title": "Vault Audit",
            "aliases": [],
            "domains": [],
            "affected_domains": [],
            "status": audit_status,
            "artifact_type": "AUDIT",
            "evidence_refs": [],
            "relations": [],
            "provenance": {"generated_by": "vault_auditor"},
        }
        atomic_write_text(path, render_note(metadata, "\n".join(lines), validate=True))
        return path

    def publish_questionnaires(self, pack: DomainPack, proposal: dict[str, Any]) -> list[Path]:
        if proposal.get("domain_id") != pack.domain_id:
            raise ValueError("Questionnaire proposal domain mismatch")
        verified_refs = {
            (
                str(row.get("source_id")),
                str(row.get("source_sha256")),
                str(row.get("locator")),
            )
            for row in read_jsonl(self.paths.state / "evidence_registry.jsonl")
            if row.get("status") == "VERIFIED"
        }
        registry = read_jsonl(self.paths.state / "question_registry.jsonl")
        by_id = {str(row.get("question_id")): row for row in registry}
        output: list[Path] = []
        proposed_ids: set[str] = set()
        for question in proposal.get("questions", []):
            if question.get("change_type") == "NOOP":
                continue
            question_id = str(question.get("question_id", ""))
            if not question_id.startswith(pack.question_prefix + "_"):
                raise ValueError(f"Question ID does not use domain prefix: {question_id}")
            if question_id in proposed_ids:
                raise ValueError(f"Duplicate question ID in proposal: {question_id}")
            proposed_ids.add(question_id)
            refs = list(question.get("evidence_refs", []))
            ref_keys = {
                (str(item.get("source_id")), str(item.get("source_sha256")), str(item.get("locator")))
                for item in refs if isinstance(item, dict)
            }
            if not refs or len(ref_keys) != len(refs) or any(item not in verified_refs for item in ref_keys):
                raise ValueError(f"Question lacks verified evidence: {question_id}")
            self._validate_condition_tree(question.get("applies_if", {}))
            self._validate_condition_tree(question.get("depends_on", {}))
            previous = by_id.get(question_id)
            revision = int(question.get("revision", 1))
            if previous and question.get("change_type") == "UPDATE" and revision <= int(previous.get("revision", 1)):
                raise ValueError(f"Question update must increase revision: {question_id}")
            value = {
                "schema_version": 1,
                "change_type": str(question.get("change_type", "ADD")),
                "question_id": question_id,
                "revision": revision,
                "domain": pack.domain_id,
                "topic": str(question.get("topic", "")),
                "response_type": str(question.get("response_type", "BOOLEAN")),
                "applies_if": question.get("applies_if", {}),
                "depends_on": question.get("depends_on", {}),
                "question_en": str(question.get("question_en", "")),
                "question_fr": str(question.get("question_fr", "")),
                "evidence_refs": refs,
                "status": "PUBLISHED",
            }
            for optional in ("options", "supersedes", "affected_domains"):
                if optional in question:
                    value[optional] = question[optional]
            if value.get("change_type") == "SUPERSEDE" and value.get("supersedes") in by_id:
                by_id[str(value["supersedes"])]["status"] = "SUPERSEDED"
            by_id[question_id] = value
            output.append(self._write_question(pack, value))
        self._assert_acyclic(by_id)
        write_jsonl(self.paths.state / "question_registry.jsonl", [by_id[key] for key in sorted(by_id)])
        self.reconcile_relations()
        return output

    def _write_question(self, pack: DomainPack, question: dict[str, Any]) -> Path:
        folder = self.paths.vault / "50_Questionnaires" / pack.domain_id
        folder.mkdir(parents=True, exist_ok=True)
        refs = list(question["evidence_refs"])
        metadata: dict[str, Any] = {
            "type": "questionnaire_question",
            "schema_version": 1,
            "stable_id": question["question_id"],
            "question_id": question["question_id"],
            "revision": int(question["revision"]),
            "title": question["question_id"],
            "aliases": [str(question.get("topic", ""))] if question.get("topic") else [],
            "domain": pack.domain_id,
            "domains": [pack.domain_id],
            "affected_domains": list(question.get("affected_domains", [pack.domain_id])),
            "status": "PUBLISHED",
            "artifact_type": "QUESTIONNAIRE",
            "topic": str(question.get("topic", "")),
            "response_type": question["response_type"],
            "applies_if": question["applies_if"],
            "depends_on": question["depends_on"],
            "question_en": question["question_en"],
            "question_fr": question["question_fr"],
            "evidence_refs": refs,
            "relations": [],
            "provenance": {
                "source_ids": sorted({str(item.get("source_id")) for item in refs}),
                "source_sha256s": sorted({str(item.get("source_sha256")) for item in refs}),
                "locators": sorted({str(item.get("locator")) for item in refs}),
                "evidence_refs": refs,
                "generated_by": "questionnaire_curator",
            },
        }
        for optional in ("options", "supersedes", "change_type"):
            if optional in question:
                metadata[optional] = question[optional]
        lines = [
            f"# {question['question_id']}",
            "",
            "## English",
            "",
            question["question_en"],
            "",
            "## Français",
            "",
            question["question_fr"],
            "",
            "## Evidence",
            "",
            *(f"- `{item['source_id']}` — {item['locator']}" for item in question["evidence_refs"]),
        ]
        path = folder / f"{question['question_id']}.md"
        atomic_write_text(path, render_note(metadata, "\n".join(lines), validate=True))
        return path

    @staticmethod
    def _validate_condition_tree(value: Any) -> None:
        if value in ({}, None):
            return
        if not isinstance(value, dict):
            raise ValueError("Question condition must be an object")
        if "all" in value or "any" in value:
            key = "all" if "all" in value else "any"
            if not isinstance(value[key], list):
                raise ValueError("Condition group must contain a list")
            for child in value[key]:
                VaultPublisher._validate_condition_tree(child)
            return
        if value.get("operator") not in {"eq", "neq", "in", "contains", "exists"}:
            raise ValueError("Unsupported questionnaire condition operator")
        if not (value.get("field") or value.get("question_id")):
            raise ValueError("Condition requires field or question_id")

    @staticmethod
    def _assert_acyclic(questions: dict[str, dict[str, Any]]) -> None:
        graph: dict[str, set[str]] = {key: set() for key in questions}

        def collect(value: Any) -> set[str]:
            if not isinstance(value, dict):
                return set()
            refs = {str(value["question_id"])} if value.get("question_id") else set()
            for key in ("all", "any"):
                for child in value.get(key, []) if isinstance(value.get(key, []), list) else []:
                    refs.update(collect(child))
            return refs

        for key, item in questions.items():
            graph[key] = {ref for ref in collect(item.get("depends_on", {})) if ref in graph}
        visiting: set[str] = set()
        visited: set[str] = set()

        def visit(node: str) -> None:
            if node in visiting:
                raise ValueError("Question dependency graph contains a cycle")
            if node in visited:
                return
            visiting.add(node)
            for child in graph[node]:
                visit(child)
            visiting.remove(node)
            visited.add(node)

        for node in graph:
            visit(node)
