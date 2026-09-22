from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import yaml

from ..project import ProjectPaths
from ..utils import append_jsonl, atomic_write_text, canonical_json, read_jsonl, sha256_text, slugify, write_jsonl, yaml_scalar


DOMAIN_STATES = {"DRAFT", "INGESTING", "REVIEW_REQUIRED", "ACTIVE", "DEPRECATED"}
REVIEW_POLICIES = {"HUMAN_APPROVAL"}
_IDENTIFIER = re.compile(r"^[A-Z][A-Z0-9_]{1,63}$")
_PREFIX = re.compile(r"^[A-Z][A-Z0-9]{1,11}$")


class DomainPackError(ValueError):
    """Raised when a Domain Pack violates the public contract."""


@dataclass(frozen=True, slots=True)
class DomainPack:
    schema_version: int
    domain_id: str
    slug: str
    status: str
    name_en: str
    name_fr: str
    description: str
    question_prefix: str
    languages: tuple[str, ...]
    source_roots: tuple[str, ...]
    review_policy: str

    @classmethod
    def from_mapping(cls, value: dict[str, Any]) -> "DomainPack":
        labels = value.get("labels") or {}
        pack = cls(
            schema_version=int(value.get("schema_version", 0)),
            domain_id=str(value.get("domain_id", "")),
            slug=str(value.get("slug", "")),
            status=str(value.get("status", "")),
            name_en=str(labels.get("en", "")),
            name_fr=str(labels.get("fr", "")),
            description=str(value.get("description", "")),
            question_prefix=str(value.get("question_prefix", "")),
            languages=tuple(str(item) for item in value.get("languages", ())),
            source_roots=tuple(str(item).replace("\\", "/") for item in value.get("source_roots", ())),
            review_policy=str(value.get("review_policy", "")),
        )
        pack.validate()
        return pack

    def validate(self) -> None:
        if self.schema_version != 1:
            raise DomainPackError("Only Domain Pack schema_version 1 is supported")
        if not _IDENTIFIER.fullmatch(self.domain_id):
            raise DomainPackError("domain_id must be an uppercase stable identifier")
        if not _PREFIX.fullmatch(self.question_prefix):
            raise DomainPackError("question_prefix must be 2-12 uppercase alphanumeric characters")
        if self.slug != slugify(self.slug):
            raise DomainPackError("slug must be normalized lowercase kebab-case")
        if self.status not in DOMAIN_STATES:
            raise DomainPackError(f"Unsupported domain status: {self.status}")
        if not self.name_en or not self.name_fr:
            raise DomainPackError("Both English and French labels are required")
        if not {"en", "fr"}.issubset(self.languages):
            raise DomainPackError("Domain Pack languages must include en and fr")
        if not self.source_roots:
            raise DomainPackError("At least one source_root is required")
        for root in self.source_roots:
            if Path(root).is_absolute() or ".." in Path(root).parts or not root.startswith("sources/"):
                raise DomainPackError(f"source_root must stay below sources/: {root}")
        if self.review_policy not in REVIEW_POLICIES:
            raise DomainPackError("Only HUMAN_APPROVAL publication is supported")

    def to_mapping(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "domain_id": self.domain_id,
            "slug": self.slug,
            "status": self.status,
            "labels": {"en": self.name_en, "fr": self.name_fr},
            "description": self.description,
            "question_prefix": self.question_prefix,
            "languages": list(self.languages),
            "source_roots": list(self.source_roots),
            "review_policy": self.review_policy,
        }


def _render_yaml(pack: DomainPack) -> str:
    fields = pack.to_mapping()
    lines = [
        f"schema_version: {fields['schema_version']}",
        f"domain_id: {pack.domain_id}",
        f"slug: {pack.slug}",
        f"status: {pack.status}",
        "labels:",
        f"  en: {yaml_scalar(pack.name_en)}",
        f"  fr: {yaml_scalar(pack.name_fr)}",
        f"description: {yaml_scalar(pack.description)}",
        f"question_prefix: {pack.question_prefix}",
        "languages: [en, fr]",
        "source_roots:",
        *(f"  - {yaml_scalar(root)}" for root in pack.source_roots),
        f"review_policy: {pack.review_policy}",
    ]
    return "\n".join(lines) + "\n"


def _render_domain_note(pack: DomainPack) -> str:
    """Render a graph-compatible domain note without reading source files."""

    # Keep this local (rather than importing the vault package) to avoid a
    # domains -> vault -> publisher -> domains import cycle during CLI start.
    fields = {
        "type": "domain",
        "schema_version": 1,
        "stable_id": pack.domain_id,
        "domain_id": pack.domain_id,
        "slug": pack.slug,
        "revision": 1,
        "title": pack.name_en,
        "aliases": [pack.name_fr] if pack.name_fr and pack.name_fr != pack.name_en else [],
        "domains": [pack.domain_id],
        "affected_domains": [pack.domain_id],
        "status": pack.status,
        "artifact_type": "DOMAIN",
        "description": pack.description,
        "question_prefix": pack.question_prefix,
        "languages": list(pack.languages),
        "source_roots": list(pack.source_roots),
        "review_policy": pack.review_policy,
        "evidence_refs": [],
        "relations": [],
        "provenance": {"generated_by": "domain_manager"},
    }
    from ..utils import frontmatter

    body = (
        f"# {pack.name_en}\n\n"
        f"**French label:** {pack.name_fr}\n\n"
        f"{pack.description or 'Description pending human review.'}\n\n"
        "## Sources\n\n"
        "_Rebuilt by the deterministic vault indexer after ingestion._\n"
    )
    return frontmatter(fields) + "\n" + body


class DomainManager:
    def __init__(self, paths: ProjectPaths):
        self.paths = paths

    @property
    def registry_path(self) -> Path:
        return self.paths.state / "domain_registry.jsonl"

    def list(self) -> list[DomainPack]:
        if not self.paths.domain_packs.exists():
            return []
        packs: list[DomainPack] = []
        for path in sorted(self.paths.domain_packs.glob("*/domain.yaml")):
            if path.parent.name.startswith("_"):
                continue
            packs.append(self.load(path.parent.name))
        self._validate_uniqueness(packs)
        return packs

    def load(self, slug_or_id: str) -> DomainPack:
        normalized = slugify(slug_or_id)
        direct = self.paths.domain_packs / normalized / "domain.yaml"
        candidates = [direct] if direct.exists() else sorted(self.paths.domain_packs.glob("*/domain.yaml"))
        for path in candidates:
            raw = yaml.safe_load(path.read_text(encoding="utf-8"))
            if not isinstance(raw, dict):
                raise DomainPackError(f"Invalid Domain Pack mapping: {path}")
            pack = DomainPack.from_mapping(raw)
            if pack.slug == normalized or pack.domain_id == slug_or_id.upper():
                return pack
        raise DomainPackError(f"Unknown domain: {slug_or_id}")

    def init(
        self,
        slug: str,
        *,
        name_en: str,
        name_fr: str,
        question_prefix: str,
        description: str = "",
        domain_id: str | None = None,
    ) -> DomainPack:
        clean_slug = slugify(slug)
        identifier = domain_id or re.sub(r"[^A-Z0-9]+", "_", clean_slug.upper()).strip("_")
        pack = DomainPack(
            schema_version=1,
            domain_id=identifier,
            slug=clean_slug,
            status="DRAFT",
            name_en=name_en.strip(),
            name_fr=name_fr.strip(),
            description=description.strip(),
            question_prefix=question_prefix.strip().upper(),
            languages=("en", "fr"),
            source_roots=(f"sources/{clean_slug}",),
            review_policy="HUMAN_APPROVAL",
        )
        pack.validate()
        existing = self.list()
        collisions = [
            item for item in existing
            if item.slug == pack.slug
            or item.domain_id == pack.domain_id
            or item.question_prefix == pack.question_prefix
        ]
        if collisions:
            self._record_collision(pack, collisions)
            raise DomainPackError("Domain collision recorded as a taxonomy proposal")
        pack_path = self.paths.domain_packs / clean_slug / "domain.yaml"
        if pack_path.exists():
            raise DomainPackError(f"Domain Pack already exists: {clean_slug}")
        atomic_write_text(pack_path, _render_yaml(pack))
        (self.paths.sources / clean_slug).mkdir(parents=True, exist_ok=True)
        (self.paths.vault / "50_Questionnaires" / pack.domain_id).mkdir(parents=True, exist_ok=True)
        domain_note = self.paths.vault / "30_Domains" / f"{pack.name_en}.md"
        atomic_write_text(domain_note, _render_domain_note(pack))
        self.rebuild_registry()
        return pack

    def set_status(self, slug_or_id: str, status: str) -> DomainPack:
        if status not in DOMAIN_STATES:
            raise DomainPackError(f"Unsupported domain status: {status}")
        pack = self.load(slug_or_id)
        path = self.paths.domain_packs / pack.slug / "domain.yaml"
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
        raw["status"] = status
        updated = DomainPack.from_mapping(raw)
        atomic_write_text(path, _render_yaml(updated))
        self.rebuild_registry()
        domain_note = self.paths.vault / "30_Domains" / f"{updated.name_en}.md"
        atomic_write_text(domain_note, _render_domain_note(updated))
        return updated

    def _record_collision(self, candidate: DomainPack, collisions: list[DomainPack]) -> None:
        payload = {
            "schema_version": 1,
            "proposal_type": "ALIAS",
            "status": "PROPOSED",
            "candidate": candidate.to_mapping(),
            "collides_with": sorted(item.domain_id for item in collisions),
            "options": ["NEW_DOMAIN", "ALIAS", "MERGE", "SUBDOMAIN"],
        }
        payload["proposal_id"] = "TAX-" + sha256_text(canonical_json(payload))[:16].upper()
        target = self.paths.state / "taxonomy_proposals.jsonl"
        if not any(item.get("proposal_id") == payload["proposal_id"] for item in read_jsonl(target)):
            append_jsonl(target, payload)

    def rebuild_registry(self) -> list[dict[str, Any]]:
        previous = {row.get("domain_id"): row for row in read_jsonl(self.registry_path)}
        current_markdown_contract = (self.paths.vault / "SCHEMA.md").is_file()
        rows: list[dict[str, Any]] = []
        for pack in sorted(self.list(), key=lambda item: item.domain_id):
            old = previous.get(pack.domain_id)
            if old and old.get("status") == "ACTIVE":
                if old.get("question_prefix") != pack.question_prefix:
                    raise DomainPackError(f"question_prefix is immutable for active domain {pack.domain_id}")
                if old.get("slug") != pack.slug:
                    raise DomainPackError(f"slug is immutable for active domain {pack.domain_id}")
            rows.append({
                "schema_version": 1,
                "domain_id": pack.domain_id,
                "slug": pack.slug,
                "status": pack.status,
                "question_prefix": pack.question_prefix,
                "pack_path": f"domain_packs/{pack.slug}/domain.yaml",
            })
            # Initial Domain Packs may predate the vault projection.  Create a
            # missing domain note deterministically, while leaving an existing
            # reviewed note untouched; status changes continue to rewrite it
            # through ``set_status``.
            domain_note = self.paths.vault / "30_Domains" / f"{pack.name_en}.md"
            if not current_markdown_contract and not domain_note.exists():
                domain_note.parent.mkdir(parents=True, exist_ok=True)
                atomic_write_text(domain_note, _render_domain_note(pack))
        write_jsonl(self.registry_path, rows)
        return rows

    @staticmethod
    def _validate_uniqueness(packs: list[DomainPack]) -> None:
        fields = ("slug", "domain_id", "question_prefix")
        for field in fields:
            values = [getattr(pack, field) for pack in packs]
            if len(values) != len(set(values)):
                raise DomainPackError(f"Duplicate Domain Pack {field}")

    # Kept as a compatibility hook for callers that used the old private
    # method; all writes above use the unified renderer.
    _render_domain_note = staticmethod(_render_domain_note)
