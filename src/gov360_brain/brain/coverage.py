"""Fail-closed projection of reviewed criterion decisions.

This is an overlay candidate for U01.  It deliberately has no writer and does
not read source or ingest bodies.  A decision changes a matrix cell only when
its envelope, own payload hash, current input hashes, independent review,
approval (when required), and evidence relationship all validate.
"""
from __future__ import annotations

from datetime import date, datetime, timezone
import hashlib
import json
from pathlib import Path
from typing import Any

import jsonschema


DECISION_SCHEMA_VERSION = 1
DECISIONS = frozenset({"EVIDENCE_APPROVED", "NAVIGATION_ONLY", "REVIEW_REQUIRED", "SOURCE_GAP"})
UNASSESSED = "UNASSESSED"
RECORDS_RELATIVE_PATH = "state/workshop/coverage/criterion-reviews.json"
COMPLETION_POLICY = (
    "Only a current, independently reviewed decision record projects a status; "
    "missing or invalid records remain UNASSESSED."
)


def _canonical(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _digest(value: bytes | str) -> str:
    return hashlib.sha256(value.encode("utf-8") if isinstance(value, str) else value).hexdigest()


def _safe_path(root: Path, relative: str, *, area: str | None = None) -> Path:
    """Resolve a repository-relative path while rejecting symlinks."""
    root = root.resolve()
    raw = Path(relative)
    if raw.is_absolute() or ".." in raw.parts or "\\" in relative:
        raise ValueError("unsafe repository-relative path")
    path = root / raw
    for index in range(1, len(raw.parts) + 1):
        if (root / Path(*raw.parts[:index])).is_symlink():
            raise ValueError("symbolic links are not accepted for Brain inputs")
    if not path.resolve().is_relative_to(root):
        raise ValueError("path escapes repository")
    if area and not path.resolve().is_relative_to((root / area).resolve()):
        raise ValueError("path outside expected input area")
    return path


def _diagnostic(code: str, *, cell_id: str | None = None, path: str | None = None,
                detail: str | None = None) -> dict[str, str]:
    result: dict[str, str] = {"code": code}
    if cell_id:
        result["cell_id"] = cell_id
    if path:
        result["path"] = path
    if detail:
        result["detail"] = detail
    return result


def decision_payload(record: dict[str, Any]) -> dict[str, Any]:
    """Return the author's payload, excluding attestations and its own hash."""
    return {
        key: value for key, value in record.items()
        if key not in {"payload_sha256", "review", "approval"}
    }


def decision_payload_sha256(record: dict[str, Any]) -> str:
    """Hash the decision payload, never an upstream candidate or matrix hash."""
    return _digest(_canonical(decision_payload(record)))


def matrix_sha256(matrix: dict[str, Any]) -> str:
    """Hash the complete matrix object, including review-count fields."""
    return _digest(_canonical(matrix))


def _parse_date(value: Any, *, date_time_only: bool = False) -> date | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        if "T" in value:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            return parsed.astimezone(timezone.utc).date() if parsed.tzinfo else parsed.date()
        if date_time_only:
            return None
        return date.fromisoformat(value)
    except (TypeError, ValueError, OverflowError):
        return None


def _as_of(value: Any) -> date | None:
    if value is None:
        return datetime.now(timezone.utc).date()
    if isinstance(value, datetime):
        return value.astimezone(timezone.utc).date() if value.tzinfo else value.date()
    if isinstance(value, date):
        return value
    return _parse_date(value)


def _load_schema(root: Path) -> dict[str, Any] | None:
    # Prefer the contract shipped beside this overlay when it is imported in
    # isolation; an integrated copy is also available at the active config path.
    module_path = Path(__file__).resolve()
    candidates = [module_path.with_name("brain-coverage-review.schema.json"),
                  root / "config/schemas/brain-coverage-review.schema.json"]
    # After integration the module lives under src/... while tests may use a
    # synthetic root with no config directory. Walk the module repository for
    # the public schema before declaring the contract unavailable.
    candidates.extend(parent / "config/schemas/brain-coverage-review.schema.json"
                     for parent in module_path.parents)
    for path in candidates:
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError):
            continue
    return None


def _load_envelope(root: Path) -> tuple[Any, list[dict[str, str]]]:
    try:
        path = _safe_path(root, RECORDS_RELATIVE_PATH, area="state/workshop/coverage")
    except (OSError, ValueError):
        return None, [_diagnostic("DECISION_RECORD_PATH_UNSAFE", path=RECORDS_RELATIVE_PATH)]
    if not path.exists():
        return {"schema_version": DECISION_SCHEMA_VERSION, "records": []}, []
    if not path.is_file():
        return None, [_diagnostic("DECISION_RECORD_FILE_INVALID", path=RECORDS_RELATIVE_PATH)]
    try:
        return json.loads(path.read_text(encoding="utf-8")), []
    except (OSError, UnicodeError, json.JSONDecodeError):
        return None, [_diagnostic("DECISION_RECORD_JSON_INVALID", path=RECORDS_RELATIVE_PATH)]


def _envelope_records(envelope: Any, schema: dict[str, Any]) -> tuple[list[Any], list[dict[str, str]]]:
    if not isinstance(envelope, dict):
        return [], [_diagnostic("DECISION_RECORD_ENVELOPE_INVALID")]
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    errors = sorted(validator.iter_errors(envelope), key=lambda error: list(error.absolute_path))
    if errors:
        path = ".".join(str(part) for part in errors[0].absolute_path) or "envelope"
        diagnostics = [_diagnostic("DECISION_RECORD_ENVELOPE_INVALID", detail=path)]
        for item in envelope.get("records", []) if isinstance(envelope.get("records"), list) else []:
            if not isinstance(item, dict):
                continue
            cell_id = item.get("cell_id") if isinstance(item.get("cell_id"), str) else None
            if item.get("approval") is None and item.get("decision") == "EVIDENCE_APPROVED":
                diagnostics.append(_diagnostic("HUMAN_APPROVAL_MISSING", cell_id=cell_id))
            elif isinstance(item.get("approval"), dict):
                status = item["approval"].get("status")
                if status == "PENDING":
                    diagnostics.append(_diagnostic("HUMAN_APPROVAL_PENDING", cell_id=cell_id))
                elif status not in {"APPROVED", "NOT_REQUIRED", None}:
                    diagnostics.append(_diagnostic("HUMAN_APPROVAL_UNKNOWN", cell_id=cell_id))
            if item.get("review") is None:
                diagnostics.append(_diagnostic("INDEPENDENT_REVIEW_MISSING", cell_id=cell_id))
            elif isinstance(item.get("review"), dict) and item["review"].get("verdict") != "APPROVED":
                diagnostics.append(_diagnostic("INDEPENDENT_REVIEW_NOT_APPROVED", cell_id=cell_id))
        return [], diagnostics
    evaluated_at = envelope.get("evaluated_at")
    if evaluated_at is not None and _parse_date(evaluated_at, date_time_only=True) is None:
        return [], [_diagnostic("DECISION_RECORD_ENVELOPE_INVALID", detail="evaluated_at")]
    return envelope["records"], []


def _record_shape(record: Any, schema: dict[str, Any]) -> list[dict[str, str]]:
    if not isinstance(record, dict):
        return [_diagnostic("DECISION_RECORD_NOT_OBJECT")]
    record_schema = schema.get("$defs", {}).get("record")
    if not isinstance(record_schema, dict):
        return [_diagnostic("DECISION_SCHEMA_INVALID")]
    # The record definition's references are rooted at the envelope schema.
    validator_schema = dict(record_schema)
    validator_schema["$defs"] = schema.get("$defs", {})
    validator = jsonschema.Draft202012Validator(validator_schema, format_checker=jsonschema.FormatChecker())
    errors = sorted(validator.iter_errors(record), key=lambda error: list(error.absolute_path))
    if not errors:
        review = record.get("review")
        if isinstance(review, dict) and _parse_date(review.get("reviewed_at"), date_time_only=True) is None:
            return [_diagnostic("REVIEW_DATE_INVALID", cell_id=record.get("cell_id")
                               if isinstance(record.get("cell_id"), str) else None)]
        return []
    path = ".".join(str(part) for part in errors[0].absolute_path) or "record"
    diagnostics = [_diagnostic("DECISION_RECORD_SCHEMA_INVALID", cell_id=record.get("cell_id")
                               if isinstance(record.get("cell_id"), str) else None, detail=path)]
    if path.startswith("review"):
        diagnostics.append(_diagnostic("INDEPENDENT_REVIEW_INVALID", cell_id=record.get("cell_id")
                                       if isinstance(record.get("cell_id"), str) else None))
    if path.startswith("approval"):
        diagnostics.append(_diagnostic("HUMAN_APPROVAL_INVALID", cell_id=record.get("cell_id")
                                       if isinstance(record.get("cell_id"), str) else None))
    return diagnostics


def _index(catalogue: dict[str, Any], field: str) -> dict[str, dict[str, Any]]:
    values = catalogue.get(field, [])
    return {item[field[:-1] if field.endswith("s") else field]: item for item in values
            if isinstance(item, dict) and isinstance(item.get(field[:-1] if field.endswith("s") else field), str)}


def _catalogue_indexes(catalogue: dict[str, Any]) -> tuple[dict[str, dict], dict[str, dict], dict[str, dict]]:
    note_rows = catalogue.get("notes", []) if isinstance(catalogue.get("notes", []), list) else []
    section_rows = catalogue.get("sections", []) if isinstance(catalogue.get("sections", []), list) else []
    evidence_container = catalogue.get("evidence")
    evidence_rows = evidence_container.get("records", []) if isinstance(evidence_container, dict) else []
    notes = {item["id"]: item for item in note_rows
             if isinstance(item, dict) and isinstance(item.get("id"), str)}
    sections = {item["section_id"]: item for item in section_rows
                if isinstance(item, dict) and isinstance(item.get("section_id"), str)}
    evidence = {item["evidence_ref"]: item for item in evidence_rows
                if isinstance(item, dict) and isinstance(item.get("evidence_ref"), str)}
    return notes, sections, evidence


def _note_hash(note: dict[str, Any]) -> str | None:
    # Active catalogue notes expose ``sha256``; synthetic/review overlays may
    # expose the explicit ``note_sha256`` spelling.  Accept either value.
    value = note.get("note_sha256") or note.get("sha256")
    return value if isinstance(value, str) else None


def _section_hash(section: dict[str, Any]) -> str | None:
    value = section.get("section_sha256") or section.get("sha256")
    return value if isinstance(value, str) else None


def _evidence_hash(evidence: dict[str, Any]) -> str:
    for key in ("evidence_sha256", "record_sha256", "sha256"):
        value = evidence.get(key)
        if isinstance(value, str):
            return value
    return _digest(_canonical(evidence))


def _ref_map(value: Any, key: str) -> dict[str, dict[str, Any]]:
    if not isinstance(value, list):
        return {}
    return {item[key]: item for item in value
            if isinstance(item, dict) and isinstance(item.get(key), str)}


def _file_hashes(record: dict[str, Any], root: Path, cell_id: str) -> list[dict[str, str]]:
    diagnostics: list[dict[str, str]] = []
    files = record.get("input_hashes", {}).get("files", {})
    if not isinstance(files, dict):
        return [_diagnostic("INPUT_FILE_HASHES_INVALID", cell_id=cell_id)]
    for relative, expected in sorted(files.items()):
        if not isinstance(relative, str) or not isinstance(expected, str):
            diagnostics.append(_diagnostic("INPUT_FILE_HASH_INVALID", cell_id=cell_id))
            continue
        try:
            path = _safe_path(root, relative)
            actual = _digest(path.read_bytes()) if path.is_file() else None
        except (OSError, ValueError):
            actual = None
            diagnostics.append(_diagnostic("INPUT_PATH_UNSAFE", cell_id=cell_id))
            continue
        if actual != expected:
            diagnostics.append(_diagnostic("INPUT_FILE_HASH_MISMATCH", cell_id=cell_id))
    return diagnostics


def _current_refs(record: dict[str, Any], catalogue: dict[str, Any], base_matrix: dict[str, Any], root: Path,
                  *, cell_id: str, today: date) -> list[dict[str, str]]:
    notes, sections, evidence = _catalogue_indexes(catalogue)
    diagnostics: list[dict[str, str]] = []
    inputs = record.get("input_hashes", {})
    if inputs.get("catalogue_sha256") != catalogue.get("catalogue_sha256"):
        diagnostics.append(_diagnostic("CATALOGUE_HASH_MISMATCH", cell_id=cell_id))
    if inputs.get("base_matrix_sha256") != matrix_sha256(base_matrix):
        diagnostics.append(_diagnostic("BASE_MATRIX_HASH_MISMATCH", cell_id=cell_id))
    diagnostics.extend(_file_hashes(record, root, cell_id))

    expires = _parse_date(record.get("expires_at"))
    if record.get("expires_at") is not None and expires is None:
        diagnostics.append(_diagnostic("DECISION_EXPIRY_INVALID", cell_id=cell_id))
    elif expires is not None and expires < today:
        diagnostics.append(_diagnostic("DECISION_EXPIRED", cell_id=cell_id))

    for ref in record.get("note_refs", []):
        current = notes.get(ref.get("note_id")) if isinstance(ref, dict) else None
        if current is None or _note_hash(current) != ref.get("note_sha256"):
            diagnostics.append(_diagnostic("NOTE_HASH_MISMATCH", cell_id=cell_id))
    for ref in record.get("section_refs", []):
        current = sections.get(ref.get("section_id")) if isinstance(ref, dict) else None
        if (current is None or current.get("note_id") != ref.get("note_id")
                or _section_hash(current) != ref.get("section_sha256")
                or ("note_sha256" in ref and current.get("note_sha256") != ref.get("note_sha256"))):
            diagnostics.append(_diagnostic("SECTION_HASH_MISMATCH", cell_id=cell_id))
    for ref in record.get("question_refs", []):
        current = notes.get(ref.get("question_id")) if isinstance(ref, dict) else None
        if (current is None or current.get("type") != "question"
                or _note_hash(current) != ref.get("question_sha256")):
            diagnostics.append(_diagnostic("QUESTION_HASH_MISMATCH", cell_id=cell_id))
    for ref in record.get("evidence_refs", []):
        current = evidence.get(ref.get("evidence_ref")) if isinstance(ref, dict) else None
        if current is None:
            diagnostics.append(_diagnostic("EVIDENCE_REF_UNKNOWN", cell_id=cell_id))
        elif current.get("evidence_status") != "REVIEWED":
            diagnostics.append(_diagnostic("EVIDENCE_NOT_REVIEWED", cell_id=cell_id))
        elif _evidence_hash(current) != ref.get("evidence_sha256"):
            diagnostics.append(_diagnostic("EVIDENCE_HASH_MISMATCH", cell_id=cell_id))
        else:
            review_expiry = _parse_date(current.get("review_expires_at"))
            validity_expiry = _parse_date(current.get("valid_until") or current.get("applicable_until"))
            if review_expiry is not None and review_expiry < today:
                diagnostics.append(_diagnostic("EVIDENCE_REVIEW_EXPIRED", cell_id=cell_id))
            if validity_expiry is not None and validity_expiry < today:
                diagnostics.append(_diagnostic("EVIDENCE_EXPIRED", cell_id=cell_id))
            for field, code in (("valid_from", "EVIDENCE_NOT_YET_VALID"),
                                ("applicable_from", "EVIDENCE_NOT_YET_APPLICABLE"),
                                ("valid_until", "EVIDENCE_EXPIRED"),
                                ("applicable_until", "EVIDENCE_NOT_APPLICABLE"),
                                ("review_expires_at", "EVIDENCE_REVIEW_EXPIRED")):
                value = current.get(field)
                if value is None:
                    continue
                parsed = _parse_date(value)
                if parsed is None:
                    diagnostics.append(_diagnostic("EVIDENCE_DATE_INVALID", cell_id=cell_id))
                elif field.endswith("_from") and parsed > today:
                    diagnostics.append(_diagnostic(code, cell_id=cell_id))
                elif field.endswith("_until") and parsed < today:
                    diagnostics.append(_diagnostic(code, cell_id=cell_id))
                elif field == "review_expires_at" and parsed < today:
                    diagnostics.append(_diagnostic(code, cell_id=cell_id))
            if current.get("revoked") is True:
                diagnostics.append(_diagnostic("EVIDENCE_REVOKED", cell_id=cell_id))
            if current.get("superseded_by"):
                diagnostics.append(_diagnostic("EVIDENCE_SUPERSEDED", cell_id=cell_id))
    return diagnostics


def _evidence_relationship(record: dict[str, Any], catalogue: dict[str, Any], *, cell_id: str,
                           today: date) -> list[dict[str, str]]:
    notes, sections, evidence = _catalogue_indexes(catalogue)
    diagnostics: list[dict[str, str]] = []
    note_refs = _ref_map(record.get("note_refs"), "note_id")
    section_refs = _ref_map(record.get("section_refs"), "section_id")
    wanted = {ref["evidence_ref"] for ref in record.get("evidence_refs", [])}
    if not note_refs or not section_refs or not wanted:
        return [_diagnostic("APPROVED_DECISION_HAS_NO_BASIS", cell_id=cell_id)]
    for identity, ref in note_refs.items():
        current = notes.get(identity)
        published = bool(current and current.get("publication_verified") is True)
        if current is None:
            diagnostics.append(_diagnostic("NOTE_REF_UNKNOWN", cell_id=cell_id))
        elif not published:
            diagnostics.append(_diagnostic("NOTE_NOT_CURRENTLY_PUBLISHED", cell_id=cell_id))
    related: set[str] = set()
    for identity, ref in section_refs.items():
        current = sections.get(identity)
        if current is None:
            diagnostics.append(_diagnostic("SECTION_REF_UNKNOWN", cell_id=cell_id))
            continue
        if current.get("note_id") not in note_refs:
            diagnostics.append(_diagnostic("SECTION_NOTE_RELATIONSHIP_MISMATCH", cell_id=cell_id))
        if current.get("evidence_status") != "REVIEWED":
            diagnostics.append(_diagnostic("SECTION_NOT_REVIEWED", cell_id=cell_id))
        section_refs_from_catalogue = current.get("derived_from")
        if not isinstance(section_refs_from_catalogue, list):
            section_refs_from_catalogue = [citation.get("evidence_ref") for citation in current.get("citations", [])
                                          if isinstance(citation, dict) and isinstance(citation.get("evidence_ref"), str)]
        section_set = {item for item in section_refs_from_catalogue if isinstance(item, str)}
        related.update(section_set)
        if not section_set:
            diagnostics.append(_diagnostic("SECTION_EVIDENCE_RELATIONSHIP_MISSING", cell_id=cell_id))
        for evidence_ref in section_set:
            current_evidence = evidence.get(evidence_ref)
            if current_evidence is None:
                diagnostics.append(_diagnostic("EVIDENCE_REF_UNKNOWN", cell_id=cell_id))
                continue
            for field, code in (("valid_from", "EVIDENCE_NOT_YET_VALID"),
                                ("applicable_from", "EVIDENCE_NOT_YET_APPLICABLE"),
                                ("valid_until", "EVIDENCE_EXPIRED"),
                                ("applicable_until", "EVIDENCE_NOT_APPLICABLE"),
                                ("review_expires_at", "EVIDENCE_REVIEW_EXPIRED")):
                value = current_evidence.get(field)
                if value is None:
                    continue
                parsed = _parse_date(value)
                if parsed is None:
                    diagnostics.append(_diagnostic("EVIDENCE_DATE_INVALID", cell_id=cell_id))
                elif field.endswith("_from") and parsed > today:
                    diagnostics.append(_diagnostic(code, cell_id=cell_id))
                elif field.endswith("_until") and parsed < today:
                    diagnostics.append(_diagnostic(code, cell_id=cell_id))
                elif field == "review_expires_at" and parsed < today:
                    diagnostics.append(_diagnostic(code, cell_id=cell_id))
    if related != wanted:
        diagnostics.append(_diagnostic("EVIDENCE_RELATIONSHIP_MISMATCH", cell_id=cell_id))
    return diagnostics


def _validate_record(record: Any, *, schema: dict[str, Any], catalogue: dict[str, Any],
                     base_matrix: dict[str, Any], cells: dict[str, dict[str, Any]], root: Path,
                     today: date) -> tuple[str | None, list[dict[str, str]]]:
    diagnostics = _record_shape(record, schema)
    if diagnostics:
        return (record.get("cell_id") if isinstance(record, dict) and isinstance(record.get("cell_id"), str) else None,
                diagnostics)
    cell_id = record["cell_id"]
    diagnostics = _current_refs(record, catalogue, base_matrix, root, cell_id=cell_id, today=today)
    cell = cells.get(cell_id)
    if cell is None:
        diagnostics.append(_diagnostic("DECISION_CELL_UNKNOWN", cell_id=cell_id))
    elif (record["pillar_id"], record["criterion"]) != (cell.get("pillar_id"), cell.get("criterion")):
        diagnostics.append(_diagnostic("DECISION_CELL_AMBIGUOUS", cell_id=cell_id))

    payload_hash = decision_payload_sha256(record)
    if record.get("payload_sha256") != payload_hash:
        diagnostics.append(_diagnostic("DECISION_PAYLOAD_HASH_MISMATCH", cell_id=cell_id))
    input_hashes = record.get("input_hashes", {})
    if record.get("payload_sha256") in {value for key, value in input_hashes.items()
                                        if key != "files" and isinstance(value, str)}:
        diagnostics.append(_diagnostic("DECISION_PAYLOAD_HASH_REUSED", cell_id=cell_id))

    review = record.get("review")
    if not isinstance(review, dict):
        diagnostics.append(_diagnostic("INDEPENDENT_REVIEW_MISSING", cell_id=cell_id))
    else:
        if review.get("reviewer_identity") == record.get("author_identity"):
            diagnostics.append(_diagnostic("INDEPENDENT_REVIEW_REQUIRED", cell_id=cell_id))
        if review.get("payload_sha256") != payload_hash:
            diagnostics.append(_diagnostic("REVIEW_PAYLOAD_HASH_MISMATCH", cell_id=cell_id))
        if review.get("verdict") != "APPROVED":
            diagnostics.append(_diagnostic("INDEPENDENT_REVIEW_NOT_APPROVED", cell_id=cell_id))
        expiry = _parse_date(review.get("review_expires_at"))
        if review.get("review_expires_at") is not None and expiry is None:
            diagnostics.append(_diagnostic("REVIEW_EXPIRY_INVALID", cell_id=cell_id))
        elif expiry is not None and expiry < today:
            diagnostics.append(_diagnostic("REVIEW_EXPIRED", cell_id=cell_id))
        reviewed_at = _parse_date(review.get("reviewed_at"), date_time_only=True)
        if reviewed_at is not None and reviewed_at > today:
            diagnostics.append(_diagnostic("REVIEW_DATE_IN_FUTURE", cell_id=cell_id))

    approval = record.get("approval")
    requires_approval = record["decision"] == "EVIDENCE_APPROVED" or record.get("requires_human_approval", False)
    if not isinstance(approval, dict):
        if requires_approval:
            diagnostics.append(_diagnostic("HUMAN_APPROVAL_MISSING", cell_id=cell_id))
    elif requires_approval:
        if approval.get("status") == "PENDING":
            diagnostics.append(_diagnostic("HUMAN_APPROVAL_PENDING", cell_id=cell_id))
        elif approval.get("status") != "APPROVED":
            diagnostics.append(_diagnostic("HUMAN_APPROVAL_UNKNOWN", cell_id=cell_id))
        if approval.get("payload_sha256") != payload_hash:
            diagnostics.append(_diagnostic("APPROVAL_PAYLOAD_HASH_MISMATCH", cell_id=cell_id))
        expiry = _parse_date(approval.get("expires_at"))
        if approval.get("expires_at") is not None and expiry is None:
            diagnostics.append(_diagnostic("APPROVAL_EXPIRY_INVALID", cell_id=cell_id))
        elif expiry is not None and expiry < today:
            diagnostics.append(_diagnostic("APPROVAL_EXPIRED", cell_id=cell_id))
        approved_at = approval.get("approved_at")
        if not isinstance(approval.get("approver_identity"), str) or not approval.get("approver_identity"):
            diagnostics.append(_diagnostic("HUMAN_APPROVAL_IDENTITY_MISSING", cell_id=cell_id))
        if approved_at is None:
            diagnostics.append(_diagnostic("HUMAN_APPROVAL_DATE_MISSING", cell_id=cell_id))
        elif _parse_date(approved_at, date_time_only=True) is None:
            diagnostics.append(_diagnostic("APPROVAL_DATE_INVALID", cell_id=cell_id))
        elif _parse_date(approved_at, date_time_only=True) > today:
            diagnostics.append(_diagnostic("APPROVAL_DATE_IN_FUTURE", cell_id=cell_id))
    elif approval.get("status") not in {"NOT_REQUIRED", "APPROVED"}:
        diagnostics.append(_diagnostic("APPROVAL_STATE_INVALID", cell_id=cell_id))
    elif approval.get("status") == "APPROVED" and not requires_approval:
        # An optional approval is still a human attestation when present; do
        # not manufacture its identity or date merely because it is optional.
        if not isinstance(approval.get("approver_identity"), str) or not approval.get("approver_identity"):
            diagnostics.append(_diagnostic("HUMAN_APPROVAL_IDENTITY_MISSING", cell_id=cell_id))
        approved_at = approval.get("approved_at")
        if approved_at is None:
            diagnostics.append(_diagnostic("HUMAN_APPROVAL_DATE_MISSING", cell_id=cell_id))
        else:
            approved_date = _parse_date(approved_at, date_time_only=True)
            if approved_date is None:
                diagnostics.append(_diagnostic("APPROVAL_DATE_INVALID", cell_id=cell_id))
            elif approved_date > today:
                diagnostics.append(_diagnostic("APPROVAL_DATE_IN_FUTURE", cell_id=cell_id))

    if record["decision"] == "EVIDENCE_APPROVED":
        diagnostics.extend(_evidence_relationship(record, catalogue, cell_id=cell_id, today=today))
    return cell_id, diagnostics


def _fail_closed(base_matrix: dict[str, Any], diagnostics: list[dict[str, str]]) -> dict[str, Any]:
    cells = []
    for original in base_matrix.get("cells", []) if isinstance(base_matrix, dict) else []:
        if not isinstance(original, dict):
            continue
        cell = dict(original)
        if cell.get("status") is not None:
            cell["routing_hint"] = cell["status"]
        cell["status"] = UNASSESSED
        cell["decision"] = None
        cell["decision_valid"] = False
        cells.append(cell)
    return {"schema_version": 2, "catalogue_sha256": None,
            "base_matrix_sha256": matrix_sha256(base_matrix) if isinstance(base_matrix, dict) else None,
            "cells": cells, "diagnostics": sorted(diagnostics, key=_canonical),
            "completion_policy": COMPLETION_POLICY}


def project_coverage(root: Path, catalogue: dict[str, Any], base_matrix: dict[str, Any], *,
                     as_of: date | datetime | str | None = None) -> dict[str, Any]:
    """Project only valid decisions; malformed or stale input remains unassessed."""
    root = Path(root).resolve()
    if not isinstance(catalogue, dict) or not isinstance(base_matrix, dict):
        return _fail_closed(base_matrix if isinstance(base_matrix, dict) else {},
                            [_diagnostic("COVERAGE_INPUT_INVALID")])
    if not isinstance(base_matrix.get("cells"), list):
        return _fail_closed(base_matrix, [_diagnostic("BASE_MATRIX_CELLS_INVALID")])
    today = _as_of(as_of)
    if today is None:
        return _fail_closed(base_matrix, [_diagnostic("VERIFIER_AS_OF_INVALID")])
    schema = _load_schema(root)
    if schema is None:
        return _fail_closed(base_matrix, [_diagnostic("DECISION_SCHEMA_UNAVAILABLE")])
    envelope, diagnostics = _load_envelope(root)
    records, envelope_diagnostics = _envelope_records(envelope, schema)
    diagnostics.extend(envelope_diagnostics)
    if envelope_diagnostics:
        return _fail_closed(base_matrix, diagnostics)
    cells: dict[str, dict[str, Any]] = {}
    duplicate_base_ids: set[str] = set()
    for item in base_matrix["cells"]:
        if not isinstance(item, dict) or not isinstance(item.get("cell_id"), str):
            diagnostics.append(_diagnostic("BASE_MATRIX_CELL_INVALID"))
            continue
        if item["cell_id"] in cells:
            duplicate_base_ids.add(item["cell_id"])
            diagnostics.append(_diagnostic("BASE_MATRIX_DUPLICATE_CELL", cell_id=item["cell_id"]))
        else:
            cells[item["cell_id"]] = item
    grouped: dict[str, list[Any]] = {}
    record_ids: dict[str, list[Any]] = {}
    for record in records:
        identity = record.get("cell_id") if isinstance(record, dict) else None
        if isinstance(identity, str):
            grouped.setdefault(identity, []).append(record)
        record_id = record.get("record_id") if isinstance(record, dict) else None
        if isinstance(record_id, str):
            record_ids.setdefault(record_id, []).append(record)
    duplicate_record_ids = {identity for identity, group in record_ids.items() if len(group) > 1}
    for identity in sorted(duplicate_record_ids):
        diagnostics.append(_diagnostic("DUPLICATE_DECISION_RECORD_ID", detail=identity))
    accepted: dict[str, dict[str, Any]] = {}
    for identity, group in sorted(grouped.items()):
        if len(group) > 1:
            diagnostics.append(_diagnostic("DUPLICATE_DECISION_CELL", cell_id=identity))
        for record in group:
            cell_id, record_diagnostics = _validate_record(record, schema=schema, catalogue=catalogue,
                                                           base_matrix=base_matrix, cells=cells, root=root,
                                                           today=today)
            diagnostics.extend(record_diagnostics)
            if (not record_diagnostics and len(group) == 1 and cell_id
                    and record.get("record_id") not in duplicate_record_ids
                    and cell_id not in duplicate_base_ids):
                accepted[cell_id] = record
    for record in records:
        if not isinstance(record, dict) or not isinstance(record.get("cell_id"), str):
            _, record_diagnostics = _validate_record(record, schema=schema, catalogue=catalogue,
                                                     base_matrix=base_matrix, cells=cells, root=root,
                                                     today=today)
            diagnostics.extend(record_diagnostics)
    if not records:
        diagnostics.append(_diagnostic("NO_DECISION_RECORDS"))
    projected = []
    for original in base_matrix["cells"]:
        if not isinstance(original, dict):
            continue
        cell = dict(original)
        identity = cell.get("cell_id")
        decision = accepted.get(identity)
        if decision:
            cell.update({"status": decision["decision"], "decision": decision["decision"],
                         "decision_valid": True, "decision_record_id": decision["record_id"],
                         "decision_payload_sha256": decision["payload_sha256"]})
        else:
            if cell.get("status") is not None:
                cell["routing_hint"] = cell["status"]
            cell.update({"status": UNASSESSED, "decision": None, "decision_valid": False})
        projected.append(cell)
    summary: dict[str, int] = {}
    for cell in projected:
        summary[cell["status"]] = summary.get(cell["status"], 0) + 1
    return {"schema_version": 2, "catalogue_sha256": catalogue.get("catalogue_sha256"),
            "base_matrix_sha256": matrix_sha256(base_matrix), "cells": projected,
            "decision_summary": dict(sorted(summary.items())),
            "diagnostics": sorted(diagnostics, key=_canonical),
            "completion_policy": COMPLETION_POLICY}


__all__ = ["project_coverage", "decision_payload", "decision_payload_sha256", "matrix_sha256"]
