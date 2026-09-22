"""Fail-closed projection of reviewed criterion coverage decisions.

Coverage is a derived diagnostic.  A domain match, a pillar status, or an old
release receipt can identify useful routing context, but none of those facts
is a criterion decision.  This module only projects a cell when a current,
independently reviewed decision record is bound to the current catalogue and
matrix.

The module intentionally has no writer.  The catalogue builder may call
``project_coverage(root, catalogue, base_matrix)`` and decide how to persist
the returned deterministic value.
"""
from __future__ import annotations

from datetime import date, datetime, timezone
import json
from pathlib import Path
from typing import Any

import jsonschema

from .common import canonical, digest, read_json, safe_path


DECISION_SCHEMA_VERSION = 1
DECISIONS = frozenset({"EVIDENCE_APPROVED", "NAVIGATION_ONLY", "REVIEW_REQUIRED", "SOURCE_GAP"})
UNASSESSED = "UNASSESSED"
RECORDS_RELATIVE_PATH = "state/workshop/coverage/criterion-reviews.json"


def decision_payload(record: dict[str, Any]) -> dict[str, Any]:
    """Return the hash-bound portion of a decision record.

    Review and approval are deliberately excluded: both are attestations over
    the author's payload and are allowed to be added after the payload is
    authored.  The function is public so producers and validators calculate
    exactly the same hash.
    """
    return {
        key: value for key, value in record.items()
        if key not in {"payload_sha256", "review", "approval"}
    }


def decision_payload_sha256(record: dict[str, Any]) -> str:
    """Compute the decision's own canonical payload hash."""
    return digest(canonical(decision_payload(record)))


def _diagnostic(code: str, *, cell_id: str | None = None, path: str | None = None,
                detail: str | None = None) -> dict[str, str]:
    row: dict[str, str] = {"code": code}
    if cell_id:
        row["cell_id"] = cell_id
    if path:
        row["path"] = path
    if detail:
        row["detail"] = detail
    return row


def _matrix_sha256(matrix: dict[str, Any]) -> str:
    """Hash the complete input matrix, including its current cell ordering."""
    return digest(canonical(matrix))


def _as_date(value: Any) -> date | None:
    if value is None:
        return None
    if not isinstance(value, str):
        return None
    try:
        # Date-only expiry is convenient for records; date-time is accepted as
        # required by JSON Schema and compared in UTC.
        if "T" in value:
            return datetime.fromisoformat(value.replace("Z", "+00:00")).date()
        return date.fromisoformat(value)
    except ValueError:
        return None


def _evaluation_date(envelope: Any) -> date:
    """Use an envelope timestamp when supplied, otherwise today's UTC date."""
    if isinstance(envelope, dict):
        evaluated_at = envelope.get("evaluated_at")
        parsed = _as_date(evaluated_at)
        if parsed:
            return parsed
    return datetime.now(timezone.utc).date()


def _load_decision_envelope(root: Path) -> tuple[Any, list[dict[str, str]]]:
    """Read the sole canonical decision file without accepting path escapes."""
    diagnostics: list[dict[str, str]] = []
    try:
        path = safe_path(root, RECORDS_RELATIVE_PATH, area="state/workshop/coverage")
    except (OSError, ValueError):
        return None, [_diagnostic("DECISION_RECORD_PATH_UNSAFE", path=RECORDS_RELATIVE_PATH)]
    if not path.exists():
        return {"schema_version": DECISION_SCHEMA_VERSION, "records": []}, diagnostics
    if not path.is_file():
        return None, [_diagnostic("DECISION_RECORD_FILE_INVALID", path=RECORDS_RELATIVE_PATH)]
    try:
        envelope = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return None, [_diagnostic("DECISION_RECORD_JSON_INVALID", path=RECORDS_RELATIVE_PATH)]
    return envelope, diagnostics


def _normalise_envelope(envelope: Any) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    """Normalise only the two harmless envelope spellings used by early drafts."""
    if isinstance(envelope, list):
        return envelope, []
    if not isinstance(envelope, dict):
        return [], [_diagnostic("DECISION_RECORD_ENVELOPE_INVALID")]
    if envelope.get("schema_version") != DECISION_SCHEMA_VERSION:
        return [], [_diagnostic("DECISION_RECORD_SCHEMA_VERSION_UNSUPPORTED")]
    records = envelope.get("records")
    if not isinstance(records, list):
        return [], [_diagnostic("DECISION_RECORDS_MISSING")]
    return records, []


def _refs_by_key(values: Any, key: str) -> dict[str, dict[str, Any]]:
    if not isinstance(values, list):
        return {}
    result: dict[str, dict[str, Any]] = {}
    for value in values:
        if isinstance(value, dict) and isinstance(value.get(key), str):
            result[value[key]] = value
    return result


def _actual_ref_hash(value: dict[str, Any], hash_keys: tuple[str, ...], *, fallback: Any = None) -> str | None:
    for key in hash_keys:
        item = value.get(key)
        if isinstance(item, str):
            return item
    if fallback is not None:
        return digest(canonical(fallback))
    return None


def _validate_record_shape(record: Any, schema: dict[str, Any]) -> list[dict[str, str]]:
    if not isinstance(record, dict):
        return [_diagnostic("DECISION_RECORD_NOT_OBJECT")]
    try:
        jsonschema.validate(record, schema)
    except jsonschema.ValidationError as exc:
        # Do not include source or project content from a malformed record.
        path = ".".join(str(item) for item in exc.absolute_path)
        return [_diagnostic("DECISION_RECORD_SCHEMA_INVALID", detail=path or "record")]
    return []


def _catalogue_indexes(catalogue: dict[str, Any]) -> tuple[dict[str, dict], dict[str, dict], dict[str, dict]]:
    notes = {item.get("id"): item for item in catalogue.get("notes", [])
             if isinstance(item, dict) and isinstance(item.get("id"), str)}
    sections = {item.get("section_id"): item for item in catalogue.get("sections", [])
                if isinstance(item, dict) and isinstance(item.get("section_id"), str)}
    records = {item.get("evidence_ref"): item for item in catalogue.get("evidence", {}).get("records", [])
               if isinstance(item, dict) and isinstance(item.get("evidence_ref"), str)}
    return notes, sections, records


def _validate_current_inputs(record: dict[str, Any], catalogue: dict[str, Any],
                             base_matrix: dict[str, Any], *, cell_id: str,
                             notes: dict[str, dict], sections: dict[str, dict],
                             evidence: dict[str, dict], today: date, root: Path) -> list[dict[str, str]]:
    diagnostics: list[dict[str, str]] = []
    inputs = record.get("input_hashes", {})
    expected_catalogue = catalogue.get("catalogue_sha256")
    expected_matrix = _matrix_sha256(base_matrix)
    if inputs.get("catalogue_sha256") != expected_catalogue:
        diagnostics.append(_diagnostic("CATALOGUE_HASH_MISMATCH", cell_id=cell_id))
    if inputs.get("base_matrix_sha256") != expected_matrix:
        diagnostics.append(_diagnostic("BASE_MATRIX_HASH_MISMATCH", cell_id=cell_id))

    # Optional file hashes give a stable binding for externally produced
    # diagnostic inputs while keeping path access repository-confined.
    file_hashes = inputs.get("files", {})
    if not isinstance(file_hashes, dict):
        diagnostics.append(_diagnostic("INPUT_FILE_HASHES_INVALID", cell_id=cell_id))
    else:
        for relative, expected in sorted(file_hashes.items()):
            if not isinstance(relative, str) or not isinstance(expected, str):
                diagnostics.append(_diagnostic("INPUT_FILE_HASH_INVALID", cell_id=cell_id))
                continue
            try:
                path = safe_path(root, relative)
            except (OSError, ValueError):
                diagnostics.append(_diagnostic("INPUT_PATH_UNSAFE", cell_id=cell_id))
                continue
            try:
                actual = digest(path.read_bytes())
            except (OSError, ValueError):
                actual = None
            if actual != expected:
                diagnostics.append(_diagnostic("INPUT_FILE_HASH_MISMATCH", cell_id=cell_id))

    expiry = _as_date(record.get("expires_at"))
    if record.get("expires_at") is not None and expiry is None:
        diagnostics.append(_diagnostic("DECISION_EXPIRY_INVALID", cell_id=cell_id))
    elif expiry is not None and expiry < today:
        diagnostics.append(_diagnostic("DECISION_EXPIRED", cell_id=cell_id))

    note_refs = _refs_by_key(record.get("note_refs"), "note_id")
    for identity, ref in sorted(note_refs.items()):
        current = notes.get(identity)
        if current is None or current.get("note_sha256") != ref.get("note_sha256"):
            diagnostics.append(_diagnostic("NOTE_HASH_MISMATCH", cell_id=cell_id))
    for ref in record.get("section_refs", []):
        if not isinstance(ref, dict):
            diagnostics.append(_diagnostic("SECTION_REF_INVALID", cell_id=cell_id))
            continue
        identity = ref.get("section_id")
        current = sections.get(identity)
        if (current is None or current.get("note_id") != ref.get("note_id")
                or current.get("sha256") != ref.get("section_sha256")):
            diagnostics.append(_diagnostic("SECTION_HASH_MISMATCH", cell_id=cell_id))
    for ref in record.get("question_refs", []):
        if not isinstance(ref, dict):
            diagnostics.append(_diagnostic("QUESTION_REF_INVALID", cell_id=cell_id))
            continue
        current = notes.get(ref.get("question_id"))
        if (current is None or current.get("type") != "question"
                or current.get("note_sha256") != ref.get("question_sha256")):
            diagnostics.append(_diagnostic("QUESTION_HASH_MISMATCH", cell_id=cell_id))
    for ref in record.get("evidence_refs", []):
        if not isinstance(ref, dict):
            diagnostics.append(_diagnostic("EVIDENCE_REF_INVALID", cell_id=cell_id))
            continue
        identity = ref.get("evidence_ref")
        current = evidence.get(identity)
        actual = _actual_ref_hash(current or {}, ("evidence_sha256", "record_sha256"), fallback=current) if current else None
        if current is None or current.get("evidence_status") != "REVIEWED" or actual != ref.get("evidence_sha256"):
            diagnostics.append(_diagnostic("EVIDENCE_HASH_MISMATCH", cell_id=cell_id))
    return diagnostics


def _validate_record(record: Any, *, schema: dict[str, Any], catalogue: dict[str, Any],
                     base_matrix: dict[str, Any], cells: dict[str, dict],
                     notes: dict[str, dict], sections: dict[str, dict],
                     evidence: dict[str, dict], today: date, root: Path) -> tuple[str | None, list[dict[str, str]]]:
    diagnostics = _validate_record_shape(record, schema)
    if diagnostics:
        return None, diagnostics
    cell_id = record["cell_id"]
    diagnostics.extend(_validate_current_inputs(record, catalogue, base_matrix, cell_id=cell_id,
                                                notes=notes, sections=sections, evidence=evidence,
                                                today=today, root=root))
    cell = cells.get(cell_id)
    if cell is None:
        diagnostics.append(_diagnostic("DECISION_CELL_UNKNOWN", cell_id=cell_id))
    elif (record["pillar_id"], record["criterion"]) != (cell.get("pillar_id"), cell.get("criterion")):
        diagnostics.append(_diagnostic("DECISION_CELL_AMBIGUOUS", cell_id=cell_id))

    payload_hash = decision_payload_sha256(record)
    if record.get("payload_sha256") != payload_hash:
        diagnostics.append(_diagnostic("DECISION_PAYLOAD_HASH_MISMATCH", cell_id=cell_id))
    # An upstream candidate hash is not a decision dossier hash.  Reject
    # accidental reuse of any declared input hash as the decision hash.
    input_hashes = record.get("input_hashes", {})
    if record.get("payload_sha256") in {v for k, v in input_hashes.items() if k != "files" and isinstance(v, str)}:
        diagnostics.append(_diagnostic("DECISION_PAYLOAD_HASH_REUSED", cell_id=cell_id))
    review = record.get("review", {})
    if review.get("reviewer_identity") == record.get("author_identity"):
        diagnostics.append(_diagnostic("INDEPENDENT_REVIEW_REQUIRED", cell_id=cell_id))
    if review.get("payload_sha256") != payload_hash:
        diagnostics.append(_diagnostic("REVIEW_PAYLOAD_HASH_MISMATCH", cell_id=cell_id))
    if review.get("verdict") != "APPROVED":
        diagnostics.append(_diagnostic("INDEPENDENT_REVIEW_NOT_APPROVED", cell_id=cell_id))

    approval = record.get("approval", {})
    requires_approval = record["decision"] == "EVIDENCE_APPROVED" or record.get("requires_human_approval", False)
    if requires_approval:
        if approval.get("status") != "APPROVED":
            diagnostics.append(_diagnostic("HUMAN_APPROVAL_REQUIRED", cell_id=cell_id))
        if approval.get("payload_sha256") != payload_hash:
            diagnostics.append(_diagnostic("APPROVAL_PAYLOAD_HASH_MISMATCH", cell_id=cell_id))
    elif approval.get("status") not in {"NOT_REQUIRED", "APPROVED"}:
        diagnostics.append(_diagnostic("APPROVAL_STATE_INVALID", cell_id=cell_id))

    # EVIDENCE_APPROVED must have a concrete, current basis.  Other decisions
    # may intentionally record an empty evidence set (e.g. SOURCE_GAP).
    if record["decision"] == "EVIDENCE_APPROVED" and not (record.get("note_refs") or record.get("section_refs") or record.get("evidence_refs")):
        diagnostics.append(_diagnostic("APPROVED_DECISION_HAS_NO_BASIS", cell_id=cell_id))
    return cell_id, diagnostics


def _fail_closed_cells(base_matrix: dict[str, Any], diagnostics: list[dict[str, str]]) -> dict[str, Any]:
    cells = []
    for original in base_matrix.get("cells", []) if isinstance(base_matrix, dict) else []:
        if not isinstance(original, dict):
            continue
        cell = dict(original)
        hint = cell.get("status", cell.get("recorded_pillar_status"))
        cell["status"] = UNASSESSED
        cell["decision"] = None
        cell["decision_valid"] = False
        if hint is not None:
            cell["routing_hint"] = hint
        cells.append(cell)
    return {"schema_version": 2, "catalogue_sha256": None, "base_matrix_sha256": _matrix_sha256(base_matrix) if isinstance(base_matrix, dict) else None,
            "cells": cells, "diagnostics": sorted(diagnostics, key=canonical),
            "completion_policy": "Only a current, independently reviewed decision record projects a status; missing or invalid records remain UNASSESSED."}


def project_coverage(root: Path, catalogue: dict[str, Any], base_matrix: dict[str, Any]) -> dict[str, Any]:
    """Project valid criterion decisions over ``base_matrix``.

    The function is deterministic for a fixed repository and input objects;
    records without current hashes, independent review, or required approval
    are ignored.  Invalid records never affect other cells.
    """
    root = Path(root).resolve()
    diagnostics: list[dict[str, str]] = []
    if not isinstance(catalogue, dict) or not isinstance(base_matrix, dict):
        return _fail_closed_cells(base_matrix if isinstance(base_matrix, dict) else {},
                                  [_diagnostic("COVERAGE_INPUT_INVALID")])
    if not isinstance(base_matrix.get("cells"), list):
        return _fail_closed_cells(base_matrix, [_diagnostic("BASE_MATRIX_CELLS_INVALID")])
    cells: dict[str, dict] = {}
    for cell in base_matrix["cells"]:
        if not isinstance(cell, dict) or not isinstance(cell.get("cell_id"), str):
            diagnostics.append(_diagnostic("BASE_MATRIX_CELL_INVALID"))
            continue
        if cell["cell_id"] in cells:
            diagnostics.append(_diagnostic("BASE_MATRIX_DUPLICATE_CELL", cell_id=cell["cell_id"]))
        else:
            cells[cell["cell_id"]] = cell
    envelope, load_diagnostics = _load_decision_envelope(root)
    diagnostics.extend(load_diagnostics)
    records, envelope_diagnostics = _normalise_envelope(envelope)
    diagnostics.extend(envelope_diagnostics)
    schema_paths = [root / "config/schemas/brain-coverage-review.schema.json",
                    Path(__file__).resolve().parents[3] / "config/schemas/brain-coverage-review.schema.json"]
    schema = None
    for schema_path in schema_paths:
        try:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            break
        except (OSError, UnicodeError, json.JSONDecodeError):
            continue
    if schema is None:
        # The overlay can be staged independently; the schema is also shipped
        # beside it.  Missing contract means no decisions are safe to apply.
        return _fail_closed_cells(base_matrix, diagnostics + [_diagnostic("DECISION_SCHEMA_UNAVAILABLE")])
    notes, sections, evidence = _catalogue_indexes(catalogue)
    today = _evaluation_date(envelope)
    accepted: dict[str, dict[str, Any]] = {}
    seen: set[str] = set()
    for record in records:
        identity = record.get("cell_id") if isinstance(record, dict) else None
        if identity in seen:
            diagnostics.append(_diagnostic("DUPLICATE_DECISION_CELL", cell_id=identity))
            continue
        if identity:
            seen.add(identity)
        cell_id, record_diagnostics = _validate_record(record, schema=schema, catalogue=catalogue,
                                                       base_matrix=base_matrix, cells=cells,
                                                       notes=notes, sections=sections, evidence=evidence,
                                                       today=today, root=root)
        if record_diagnostics:
            diagnostics.extend(record_diagnostics)
        elif cell_id:
            accepted[cell_id] = record
    if not records:
        diagnostics.append(_diagnostic("NO_DECISION_RECORDS"))

    projected = []
    for original in base_matrix["cells"]:
        if not isinstance(original, dict):
            continue
        cell = dict(original)
        cell_id = cell.get("cell_id")
        hint = cell.get("status", cell.get("recorded_pillar_status"))
        record = accepted.get(cell_id)
        if record:
            cell["status"] = record["decision"]
            cell["decision"] = record["decision"]
            cell["decision_valid"] = True
            cell["decision_record_id"] = record["record_id"]
            cell["decision_payload_sha256"] = record["payload_sha256"]
        else:
            # Historical status values are observable routing hints only.
            cell["status"] = UNASSESSED
            cell["decision"] = None
            cell["decision_valid"] = False
            if hint is not None:
                cell["routing_hint"] = hint
        projected.append(cell)
    summary: dict[str, int] = {}
    for cell in projected:
        status = cell.get("status", UNASSESSED)
        summary[status] = summary.get(status, 0) + 1
    return {"schema_version": 2, "catalogue_sha256": catalogue.get("catalogue_sha256"),
            "base_matrix_sha256": _matrix_sha256(base_matrix), "cells": projected,
            "decision_summary": dict(sorted(summary.items())),
            "diagnostics": sorted(diagnostics, key=canonical),
            "completion_policy": "Only a current, independently reviewed decision record projects a status; missing or invalid records remain UNASSESSED."}


__all__ = ["project_coverage", "decision_payload", "decision_payload_sha256"]
