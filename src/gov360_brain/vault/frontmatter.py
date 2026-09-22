"""Unified, deterministic frontmatter contract for Governance Brain notes.

The vault is an Obsidian projection of the governed registries.  This module
keeps that projection deliberately small and predictable: every note has the
same graph fields (identity, aliases, domains, evidence, relations and
provenance), while type-specific fields remain available for existing notes.

The API is intentionally pure until :func:`write_note` is called.  Parsing,
normalisation, validation and rendering therefore work in a staging directory
and can be composed with the publisher's atomic commit protocol.
"""

from __future__ import annotations

import copy
import json
from collections import OrderedDict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

import jsonschema
import yaml

from ..utils import atomic_write_text, canonical_json


SCHEMA_VERSION = 1
SCHEMA_FILENAME = "vault-frontmatter.schema.json"

NOTE_TYPES = frozenset(
    {
        "source",
        "concept",
        "domain",
        "rule",
        "questionnaire",
        # Existing publisher output uses this more precise subtype.
        "questionnaire_question",
        "map",
        "audit",
        "system",
        "system_log",
    }
)

GRAPH_NOTE_TYPES = frozenset({"source", "concept", "domain", "rule", "questionnaire", "questionnaire_question", "map"})
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

# The identity fields were present before this module was introduced.  They
# are retained in rendered output so old consumers and existing notes keep
# working while stable_id becomes the common graph key.
LEGACY_ID_FIELDS = {
    "source": "source_id",
    "domain": "domain_id",
    "questionnaire": "question_id",
    "questionnaire_question": "question_id",
    "map": "map_id",
}

_COMMON_ORDER = (
    "type",
    "schema_version",
    "stable_id",
    "source_id",
    "question_id",
    "domain_id",
    "revision",
    "title",
    "aliases",
    "domain",
    "domains",
    "affected_domains",
    "status",
    "source_sha256",
    "source_format",
    "normativity",
    "evidence_refs",
    "relations",
    "provenance",
)


class FrontmatterError(ValueError):
    """Base class for malformed or invalid note frontmatter."""


class FrontmatterParseError(FrontmatterError):
    """Raised when a Markdown document has no valid YAML frontmatter."""


class FrontmatterValidationError(FrontmatterError):
    """Raised when frontmatter does not satisfy the public JSON Schema."""

    def __init__(self, errors: list[str]):
        self.errors = tuple(errors)
        super().__init__("Invalid vault frontmatter: " + "; ".join(errors))


def _schema_path(path: Path | None = None) -> Path:
    if path is not None:
        return Path(path)
    # frontmatter.py -> vault -> gov360_brain -> src -> repository root
    return Path(__file__).resolve().parents[3] / "config" / "schemas" / SCHEMA_FILENAME


def _as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return list(value)
    return [value]


def _unique_sorted_scalars(value: Any) -> list[Any]:
    values = _as_list(value)
    seen: set[str] = set()
    result: list[Any] = []
    for item in values:
        # Alias/domain/tag values are strings in the public schema.  Keep the
        # original value for validation to report an actionable type error.
        key = canonical_json(item)
        if key not in seen:
            seen.add(key)
            result.append(item)
    return sorted(result, key=lambda item: str(item).casefold())


def _sorted_objects(value: Any) -> list[Any]:
    values = _as_list(value)
    # Keep scalar legacy evidence refs intact and order structured references
    # by their canonical representation.  This prevents worker arrival order
    # from changing generated notes.
    return sorted(copy.deepcopy(values), key=canonical_json)


def _identity_for(value: Mapping[str, Any], note_type: str) -> str | None:
    stable_id = value.get("stable_id")
    if stable_id not in (None, ""):
        return str(stable_id)
    legacy = LEGACY_ID_FIELDS.get(note_type)
    if legacy and value.get(legacy) not in (None, ""):
        return str(value[legacy])
    for key in ("note_id", "id"):
        if value.get(key) not in (None, ""):
            return str(value[key])
    return None


def canonicalize_frontmatter(value: Mapping[str, Any], *, validate: bool = False) -> dict[str, Any]:
    """Return a normalized copy of a note's frontmatter.

    Legacy ``source_id``, ``question_id`` and ``domain_id`` fields are kept and
    mirrored to ``stable_id``.  Singular ``domain`` is kept for questionnaire
    compatibility and also represented in the common ``domains`` list.
    Lists whose order has no semantic meaning are sorted and de-duplicated.
    No timestamps or generated identifiers are introduced.
    """

    if not isinstance(value, Mapping):
        raise FrontmatterError("frontmatter must be a mapping")
    result: dict[str, Any] = copy.deepcopy(dict(value))
    note_type = str(result.get("type", "")).strip().lower()
    if note_type:
        result["type"] = note_type
    result.setdefault("schema_version", SCHEMA_VERSION)
    try:
        result["schema_version"] = int(result["schema_version"])
    except (TypeError, ValueError) as exc:
        raise FrontmatterError("schema_version must be an integer") from exc

    identity = _identity_for(result, note_type)
    if identity is not None:
        result["stable_id"] = identity
        legacy = LEGACY_ID_FIELDS.get(note_type)
        if legacy and result.get(legacy) in (None, ""):
            result[legacy] = identity

    if "revision" not in result:
        result["revision"] = 1
    try:
        result["revision"] = int(result["revision"])
    except (TypeError, ValueError) as exc:
        raise FrontmatterError("revision must be an integer") from exc

    if "alias" in result and "aliases" not in result:
        result["aliases"] = result.pop("alias")
    result["aliases"] = _unique_sorted_scalars(result.get("aliases", []))

    domains = _as_list(result.get("domains", []))
    if not domains and result.get("domain") not in (None, ""):
        domains = [result["domain"]]
    if result.get("domain_id") not in (None, "") and note_type != "domain":
        domains.append(result["domain_id"])
    result["domains"] = _unique_sorted_scalars(domains)
    result["affected_domains"] = _unique_sorted_scalars(result.get("affected_domains", []))
    result["evidence_refs"] = _sorted_objects(result.get("evidence_refs", []))
    result["relations"] = _sorted_objects(result.get("relations", []))
    result["tags"] = _unique_sorted_scalars(result.get("tags", []))

    provenance = result.get("provenance", {})
    if provenance is None:
        provenance = {}
    if not isinstance(provenance, Mapping):
        raise FrontmatterError("provenance must be a mapping")
    provenance = copy.deepcopy(dict(provenance))
    # Carry direct legacy provenance into the common nested object.  The
    # direct fields remain because source notes and old scripts use them.
    if result.get("source_id") not in (None, ""):
        provenance.setdefault("source_id", result["source_id"])
    if result.get("source_sha256") not in (None, ""):
        provenance.setdefault("source_sha256", result["source_sha256"])
    result["provenance"] = provenance

    if validate:
        validate_frontmatter(result)
    return result


def _split_document(text: str) -> tuple[dict[str, Any], str]:
    normalized = str(text).replace("\r\n", "\n").replace("\r", "\n")
    if not normalized.startswith("---\n"):
        raise FrontmatterParseError("Markdown document must start with YAML frontmatter")
    end = normalized.find("\n---\n", 4)
    if end < 0:
        if normalized.endswith("\n---"):
            end = len(normalized) - 4
            body = ""
        else:
            raise FrontmatterParseError("unterminated YAML frontmatter")
    else:
        body = normalized[end + len("\n---\n") :]
    try:
        parsed = yaml.safe_load(normalized[4:end])
    except yaml.YAMLError as exc:
        raise FrontmatterParseError(f"invalid YAML frontmatter: {exc}") from exc
    if not isinstance(parsed, Mapping):
        raise FrontmatterParseError("frontmatter must be a YAML mapping")
    return dict(parsed), body


def _ordered(value: Mapping[str, Any]) -> OrderedDict[str, Any]:
    keys = [key for key in _COMMON_ORDER if key in value]
    keys.extend(sorted((key for key in value if key not in keys), key=str))
    return OrderedDict((key, value[key]) for key in keys)


def render_frontmatter(value: Mapping[str, Any], *, validate: bool = True, canonical: bool = True) -> str:
    """Render deterministic YAML frontmatter, including opening/closing fences."""

    normalized = canonicalize_frontmatter(value) if canonical else copy.deepcopy(dict(value))
    if validate:
        validate_frontmatter(normalized)
    # safe_dump cannot represent OrderedDict without a Python tag.  A regular
    # insertion-ordered dict gives the same deterministic output on Python 3.12.
    dumped = yaml.safe_dump(
        dict(_ordered(normalized)),
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=120,
    ).rstrip()
    return f"---\n{dumped}\n---\n"


def render_note(
    value: Mapping[str, Any] | "VaultNote",
    body: str | None = None,
    *,
    validate: bool = True,
    canonical: bool = True,
) -> str:
    """Render a complete Markdown note without touching the filesystem."""

    if isinstance(value, VaultNote):
        metadata = value.metadata
        note_body = value.body if body is None else body
    else:
        metadata = value
        note_body = "" if body is None else body
    clean_body = str(note_body).replace("\r\n", "\n").replace("\r", "\n").lstrip("\n")
    rendered = render_frontmatter(metadata, validate=validate, canonical=canonical)
    if not clean_body:
        return rendered
    # Keep a blank separator line between YAML and Markdown body.  This is the
    # canonical form used by the existing vault notes and avoids ambiguity in
    # Obsidian renderers that treat the closing fence as a block boundary.
    return rendered + "\n" + clean_body.rstrip("\n") + "\n"


def normalize_note(
    text: str,
    *,
    note_type: str | None = None,
    validate: bool = True,
) -> str:
    """Migrate a note's frontmatter while preserving its Markdown body.

    Unlike :func:`render_note`, this migration helper does not trim or add
    blank lines to the body.  It is therefore suitable for upgrading legacy
    system/audit notes and for rewriting a frontmatter block in place.
    Line endings are normalized to LF by the parser, matching the repository's
    generated-file convention.
    """

    note = parse_note(text, validate=False, canonical=True, note_type=note_type)
    if validate:
        validate_frontmatter(note.metadata)
    return render_frontmatter(note.metadata, validate=False) + note.body


def _infer_legacy_note_type(path: Path) -> str | None:
    parts = {part.casefold() for part in Path(path).parts}
    if "90_audit" in parts:
        return "audit"
    if "00_system" in parts:
        return "system"
    return None


def normalize_note_file(path: Path, *, note_type: str | None = None, validate: bool = True) -> Path:
    """Atomically migrate one existing Markdown note in place."""

    target = Path(path)
    _assert_not_immutable_source(target)
    original = target.read_text(encoding="utf-8")
    atomic_write_text(target, normalize_note(original, note_type=note_type or _infer_legacy_note_type(target), validate=validate))
    return target


def parse_note(
    text: str,
    *,
    validate: bool = True,
    canonical: bool = True,
    note_type: str | None = None,
) -> "VaultNote":
    """Parse a complete Markdown note and optionally validate its contract."""

    try:
        raw, body = _split_document(text)
    except FrontmatterParseError as exc:
        # A small number of pre-contract system/audit notes were plain
        # Markdown.  They can be read safely when the caller supplies the
        # note family; malformed YAML is still rejected.
        normalized = str(text).replace("\r\n", "\n").replace("\r", "\n")
        if note_type not in {"audit", "system", "system_log"} or normalized.startswith("---\n"):
            raise
        raw, body = {"type": note_type}, normalized
    metadata = canonicalize_frontmatter(raw) if canonical else raw
    if validate:
        validate_frontmatter(metadata)
    return VaultNote(metadata=metadata, body=body)


def parse_frontmatter(
    text: str,
    *,
    validate: bool = True,
    canonical: bool = True,
    note_type: str | None = None,
) -> dict[str, Any]:
    """Parse and return only the frontmatter mapping from a Markdown note."""

    return parse_note(text, validate=validate, canonical=canonical, note_type=note_type).metadata


def validation_errors(value: Mapping[str, Any], *, schema_path: Path | None = None) -> list[str]:
    """Collect stable, human-readable JSON Schema errors without raising."""

    try:
        metadata = canonicalize_frontmatter(value)
    except (FrontmatterError, TypeError, ValueError) as exc:
        return [str(exc)]
    path = _schema_path(schema_path)
    try:
        schema = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        return [f"cannot read vault frontmatter schema: {exc}"]
    validator = jsonschema.Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(metadata), key=lambda error: (tuple(str(item) for item in error.path), error.message))
    messages = [f"{'.'.join(str(item) for item in error.path) or '<frontmatter>'}: {error.message}" for error in errors]
    messages.extend(_semantic_errors(metadata))
    return sorted(set(messages))


def _semantic_errors(metadata: Mapping[str, Any]) -> list[str]:
    """Checks that JSON Schema cannot express across related fields."""

    errors: list[str] = []
    note_type = str(metadata.get("type", ""))
    stable_id = metadata.get("stable_id")
    legacy_key = LEGACY_ID_FIELDS.get(note_type)
    legacy_id = metadata.get(legacy_key) if legacy_key else None
    if stable_id not in (None, "") and legacy_id not in (None, "") and str(stable_id) != str(legacy_id):
        errors.append(f"stable_id: must match {legacy_key}")
    provenance = metadata.get("provenance")
    if isinstance(provenance, Mapping):
        if metadata.get("source_id") not in (None, "") and provenance.get("source_id") not in (None, "") and str(metadata["source_id"]) != str(provenance["source_id"]):
            errors.append("provenance.source_id: must match source_id")
        if metadata.get("source_sha256") not in (None, "") and provenance.get("source_sha256") not in (None, "") and str(metadata["source_sha256"]) != str(provenance["source_sha256"]):
            errors.append("provenance.source_sha256: must match source_sha256")
    return errors


def validate_frontmatter(value: Mapping[str, Any], *, schema_path: Path | None = None) -> None:
    """Validate frontmatter against the public schema or raise one error."""

    errors = validation_errors(value, schema_path=schema_path)
    if errors:
        raise FrontmatterValidationError(errors)


def write_note(
    path: Path,
    value: Mapping[str, Any] | "VaultNote",
    body: str | None = None,
    *,
    validate: bool = True,
    canonical: bool = True,
) -> Path:
    """Atomically write a validated note and return its target path."""

    target = Path(path)
    _assert_not_immutable_source(target)
    atomic_write_text(target, render_note(value, body, validate=validate, canonical=canonical))
    return target


def _assert_not_immutable_source(path: Path) -> None:
    """Keep note helpers from violating the repository source immutability rule."""

    target = Path(path).resolve()
    source_root = (Path(__file__).resolve().parents[3] / "sources").resolve()
    if target == source_root or source_root in target.parents:
        raise FrontmatterError("Files under sources/ are immutable and cannot be rewritten")


def read_note(path: Path, *, validate: bool = True, canonical: bool = True) -> "VaultNote":
    """Read a Markdown note through the same parser used by validators."""

    target = Path(path)
    text = target.read_text(encoding="utf-8")
    # Infer only the two legacy folders whose files historically had no
    # frontmatter.  Other folders fail closed so a missing contract cannot be
    # mistaken for a valid source or knowledge note.
    return parse_note(text, validate=validate, canonical=canonical, note_type=_infer_legacy_note_type(target))


@dataclass(frozen=True, slots=True)
class VaultNote:
    """Parsed note with a graph-friendly metadata mapping and Markdown body."""

    metadata: dict[str, Any]
    body: str = ""

    @property
    def frontmatter(self) -> dict[str, Any]:
        return self.metadata

    @property
    def note_type(self) -> str:
        return str(self.metadata.get("type", ""))

    @property
    def stable_id(self) -> str | None:
        value = self.metadata.get("stable_id")
        return None if value in (None, "") else str(value)

    @property
    def aliases(self) -> tuple[str, ...]:
        return tuple(str(value) for value in self.metadata.get("aliases", []))

    @property
    def domains(self) -> tuple[str, ...]:
        return tuple(str(value) for value in self.metadata.get("domains", []))

    def validate(self, *, schema_path: Path | None = None) -> None:
        validate_frontmatter(self.metadata, schema_path=schema_path)

    def render(self, *, validate: bool = True, canonical: bool = True) -> str:
        return render_note(self, validate=validate, canonical=canonical)


# A short alias is useful to callers that treat a parsed document as a note.
parse = parse_note
render = render_note
validate = validate_frontmatter


__all__ = [
    "FrontmatterError",
    "FrontmatterParseError",
    "FrontmatterValidationError",
    "GRAPH_NOTE_TYPES",
    "NOTE_TYPES",
    "RELATION_TYPES",
    "SCHEMA_VERSION",
    "VaultNote",
    "canonicalize_frontmatter",
    "parse",
    "parse_frontmatter",
    "parse_note",
    "read_note",
    "render",
    "render_frontmatter",
    "render_note",
    "normalize_note",
    "normalize_note_file",
    "validate",
    "validate_frontmatter",
    "validation_errors",
    "write_note",
]
