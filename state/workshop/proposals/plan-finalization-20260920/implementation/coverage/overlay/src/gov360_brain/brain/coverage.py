"""Deterministic criterion coverage reconciliation.

This module is deliberately independent from the catalogue compiler.  A
catalogue supplies candidate notes and reviewed evidence, while criterion
records supply the human decision and its hash-bound release.  Candidate
overlap is exposed for inspection but never changes a criterion status.

The functions accept dictionaries so they can be used by the active catalogue
builder without reading source or ingest bodies.  Only identifiers, hashes,
locators and counts are emitted by the report helpers.
"""
from __future__ import annotations

from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
from typing import Any, Iterable, Mapping, Sequence


SCHEMA_VERSION = 1
HASH_RE = re.compile(r"^[a-f0-9]{64}$")
REVIEW_REQUIRED = "REVIEW_REQUIRED"
STATUS_VALUES = frozenset(
    {
        "SOURCE_GAP",
        "EVIDENCE_READY",
        "PROPOSAL_READY",
        "HUMAN_REVIEW",
        "APPROVED",
        "COMPLETE",
        REVIEW_REQUIRED,
    }
)


def _canonical(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256(value: Any) -> str:
    """Hash bytes, text, or canonical JSON without platform-dependent output."""
    if isinstance(value, bytes):
        raw = value
    elif isinstance(value, str):
        raw = value.encode("utf-8")
    else:
        raw = _canonical(value).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _hash(value: Any) -> str | None:
    value = str(value).lower() if value is not None else ""
    return value if HASH_RE.fullmatch(value) else None


def _as_records(value: Any, *keys: str) -> list[dict[str, Any]]:
    """Normalize a records document while retaining no untrusted free text."""
    if value is None:
        return []
    if isinstance(value, Mapping):
        for key in keys:
            candidate = value.get(key)
            if isinstance(candidate, list):
                return [dict(item) for item in candidate if isinstance(item, Mapping)]
        return [dict(value)] if value.get("cell_id") else []
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return [dict(item) for item in value if isinstance(item, Mapping)]
    return []


def _cell_id(record: Mapping[str, Any]) -> str | None:
    value = record.get("cell_id")
    if value:
        return str(value)
    pillar = record.get("pillar_id")
    criterion = record.get("criterion")
    if pillar and criterion:
        return f"{pillar}:{criterion}"
    return None


def _str_list(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, Sequence) and not isinstance(value, (bytes, str)):
        return sorted({str(item) for item in value if item is not None and str(item)})
    return []


def _merge_record_defaults(record: Mapping[str, Any], parent: Mapping[str, Any]) -> dict[str, Any]:
    merged = dict(parent)
    merged.update(record)
    # criterion_rows in coverage-state-p0 are child records of the approved
    # analysis document and inherit its proposal and candidate hash.
    merged["cell_id"] = _cell_id(merged)
    return merged


def normalize_reviews(value: Any) -> list[dict[str, Any]]:
    """Return cell records with document-level fields inherited deterministically."""
    if not isinstance(value, Mapping):
        return _as_records(value, "cells", "criterion_rows", "records")
    parent = {k: v for k, v in value.items() if k not in {"cells", "criterion_rows", "records"}}
    rows = _as_records(value, "cells", "criterion_rows", "records")
    return [_merge_record_defaults(row, parent) for row in rows if _cell_id(_merge_record_defaults(row, parent))]


def _catalogue_notes(catalogue: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    return {str(item.get("id")): item for item in catalogue.get("notes", []) if item.get("id")}


def _catalogue_evidence(catalogue: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    evidence = catalogue.get("evidence") or catalogue.get("evidence_index") or {}
    rows = evidence.get("records", []) if isinstance(evidence, Mapping) else []
    return {str(item.get("evidence_ref")): item for item in rows if item.get("evidence_ref")}


def _catalogue_sections(catalogue: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    return {str(item.get("section_id")): item for item in catalogue.get("sections", []) if item.get("section_id")}


def _release_rows(value: Any) -> dict[str, dict[str, Any]]:
    """Normalize publication_inventory output or release records.

    A release is eligible only when its exact candidate hash is known and the
    existing publication inventory marks its receipt verified.  An
    ``INTEGRATED`` manifest by itself is intentionally insufficient.
    """
    if isinstance(value, Mapping) and ("releases" in value or "publication_inventory" in value):
        value = value.get("releases", value.get("publication_inventory"))
    if isinstance(value, Mapping):
        value = list(value.values())
    rows: dict[str, dict[str, Any]] = {}
    for raw in value or []:
        if not isinstance(raw, Mapping):
            continue
        row = dict(raw)
        identity = row.get("proposal_id") or row.get("release_id") or row.get("id")
        if not identity:
            continue
        identity = str(identity)
        row["release_id"] = identity
        row["candidate_sha256"] = _hash(
            row.get("candidate_sha256") or row.get("candidate_hash") or row.get("candidate_sha")
        )
        approval = str(row.get("approval_status") or row.get("status") or "").upper()
        row["approved"] = bool(row.get("approved") is True or approval in {"APPROVED", "INTEGRATED"})
        row["publication_verified"] = bool(row.get("publication_verified") is True)
        rows[identity] = row
    return rows


def _explicit_hashes(record: Mapping[str, Any], field: str) -> dict[str, dict[str, str]]:
    """Read note/evidence hash maps in either map or list form."""
    raw = record.get(field)
    result: dict[str, dict[str, str]] = {}
    if isinstance(raw, Mapping):
        for identity, hashes in raw.items():
            if isinstance(hashes, str):
                result[str(identity)] = {"sha256": hashes}
            elif isinstance(hashes, Mapping):
                result[str(identity)] = {str(k): str(v) for k, v in hashes.items() if v is not None}
    elif isinstance(raw, Sequence) and not isinstance(raw, (str, bytes)):
        for item in raw:
            if not isinstance(item, Mapping):
                continue
            identity = item.get("id") or item.get("note_id") or item.get("evidence_ref")
            if identity:
                result[str(identity)] = {str(k): str(v) for k, v in item.items() if k.endswith("sha256") and v is not None}
    return result


def _hash_mismatches(record: Mapping[str, Any], catalogue: Mapping[str, Any]) -> list[str]:
    """Check hashes explicitly bound by a criterion record against the catalogue."""
    mismatches: list[str] = []
    notes = _catalogue_notes(catalogue)
    sections = _catalogue_sections(catalogue)
    evidence = _catalogue_evidence(catalogue)
    for note_id, expected in _explicit_hashes(record, "note_hashes").items():
        actual = notes.get(note_id)
        actual_hash = actual.get("sha256") if actual else None
        wanted = expected.get("sha256") or expected.get("note_sha256")
        if wanted and actual_hash != wanted:
            mismatches.append(f"note:{note_id}")
    for section_id, expected in _explicit_hashes(record, "section_hashes").items():
        actual = sections.get(section_id)
        actual_hash = actual.get("sha256") if actual else None
        wanted = expected.get("sha256") or expected.get("section_sha256")
        if wanted and actual_hash != wanted:
            mismatches.append(f"section:{section_id}")
    for evidence_ref, expected in _explicit_hashes(record, "evidence_hashes").items():
        actual = evidence.get(evidence_ref)
        if not actual:
            mismatches.append(f"evidence:{evidence_ref}:missing")
            continue
        for key in ("source_sha256", "unit_sha256", "unit_file_sha256"):
            wanted = expected.get(key)
            if wanted and actual.get(key) != wanted:
                mismatches.append(f"evidence:{evidence_ref}:{key}")
    expected_catalogue = _hash(record.get("catalogue_sha256"))
    actual_catalogue = _hash(catalogue.get("catalogue_sha256"))
    if expected_catalogue and actual_catalogue and expected_catalogue != actual_catalogue:
        mismatches.append("catalogue")
    return sorted(set(mismatches))


def _record_evidence_refs(record: Mapping[str, Any]) -> list[str]:
    refs = _str_list(record.get("evidence_refs"))
    if not refs and isinstance(record.get("basis"), Mapping):
        refs = _str_list(record["basis"].get("evidence_refs"))
    return refs


def _candidate_ids(record: Mapping[str, Any]) -> tuple[list[str], list[str], list[str], list[str]]:
    basis = record.get("basis") if isinstance(record.get("basis"), Mapping) else {}
    notes = _str_list(record.get("candidate_note_ids") or record.get("note_ids") or basis.get("reviewed_candidate_note_ids"))
    questions = _str_list(record.get("candidate_question_ids") or record.get("question_ids") or basis.get("reviewed_candidate_question_ids"))
    sources = _str_list(record.get("candidate_source_ids") or record.get("source_ids"))
    sections = _str_list(record.get("section_ids"))
    future = record.get("future_note_id")
    if future:
        notes = sorted(set(notes) | {str(future)})
    return notes, questions, sources, sections


def _status_hint(record: Mapping[str, Any]) -> str | None:
    for key in ("projected_status", "status", "proposed_status", "review_status"):
        value = str(record.get(key) or "").upper()
        if value in STATUS_VALUES:
            return value
    return None


def _approved_release(record: Mapping[str, Any], releases: Mapping[str, Mapping[str, Any]]) -> tuple[dict[str, Any] | None, str | None]:
    release_id = record.get("release_id") or record.get("proposal_id") or record.get("approved_release_id")
    candidate = _hash(record.get("candidate_sha256") or record.get("candidate_hash") or record.get("approved_candidate_sha256"))
    if not release_id:
        return None, "approved_release_missing"
    release = releases.get(str(release_id))
    if not release:
        return None, "approved_release_unknown"
    release_candidate = _hash(release.get("candidate_sha256"))
    if candidate and release_candidate and candidate != release_candidate:
        return None, "approved_release_hash_mismatch"
    if not candidate or not release_candidate:
        return None, "approved_release_hash_missing"
    if not release.get("approved"):
        return None, "human_approval_missing"
    if not release.get("publication_verified"):
        return None, "publication_receipt_unverified"
    return release, None


def _is_explicitly_complete(record: Mapping[str, Any]) -> bool:
    """Only a criterion decision can request COMPLETE; no release status does."""
    status = str(record.get("projected_status") or record.get("status") or "").upper()
    complete = record.get("complete_status")
    return bool(
        status == "COMPLETE"
        or record.get("completion_approved") is True
        or str(complete or "").upper() in {"APPROVED", "COMPLETE"}
    )


def _candidate_evidence(record: Mapping[str, Any], catalogue: Mapping[str, Any]) -> list[dict[str, Any]]:
    index = _catalogue_evidence(catalogue)
    result: list[dict[str, Any]] = []
    for ref in _record_evidence_refs(record):
        row = index.get(ref)
        if row:
            result.append(
                {
                    "evidence_ref": ref,
                    "evidence_status": row.get("evidence_status"),
                    "source_id": row.get("source_id"),
                    "locator": row.get("locator"),
                    "source_sha256": row.get("source_sha256"),
                    "unit_sha256": row.get("unit_sha256"),
                    "unit_file_sha256": row.get("unit_file_sha256"),
                }
            )
        else:
            result.append({"evidence_ref": ref, "evidence_status": "MISSING"})
    return sorted(result, key=lambda row: row["evidence_ref"])


def _cell_candidates(cell: Mapping[str, Any], records: Sequence[Mapping[str, Any]], catalogue: Mapping[str, Any]) -> dict[str, Any]:
    """Expose candidates explicitly recorded for this cell only.

    The catalogue's domain overlap remains available under ``domain_candidates``
    for human triage, but is never used in ``candidate_evidence`` or status.
    """
    notes: set[str] = set()
    questions: set[str] = set()
    sources: set[str] = set()
    sections: set[str] = set()
    evidence_refs: set[str] = set()
    for record in records:
        n, q, s, sec = _candidate_ids(record)
        notes.update(n); questions.update(q); sources.update(s); sections.update(sec)
        evidence_refs.update(_record_evidence_refs(record))
    # Keep evidence visible even if the record did not duplicate its refs in a
    # separate candidate field.
    evidence = [_candidate_evidence({"evidence_refs": sorted(evidence_refs)}, catalogue)]
    return {
        "candidate_note_ids": sorted(notes),
        "candidate_question_ids": sorted(questions),
        "candidate_source_ids": sorted(sources),
        "candidate_section_ids": sorted(sections),
        "candidate_evidence": evidence[0],
    }


def _domain_candidates(cell: Mapping[str, Any], catalogue: Mapping[str, Any]) -> dict[str, list[str]]:
    """Diagnostic-only overlap candidates; never feed these into a decision."""
    pillar_domains = set(cell.get("domains") or [])
    notes = [n.get("id") for n in catalogue.get("notes", []) if pillar_domains & set(n.get("domains") or []) and n.get("id")]
    sources = [s.get("source_id") for s in catalogue.get("sources", []) if pillar_domains & set(s.get("domains") or []) and s.get("source_id")]
    return {"note_ids": sorted(set(notes)), "source_ids": sorted(set(sources))}


def _record_reason(record: Mapping[str, Any], release: Mapping[str, Any] | None, mismatch: list[str]) -> list[str]:
    reasons: list[str] = []
    if mismatch:
        reasons.append("hash_changed")
    refs = _record_evidence_refs(record)
    if not refs:
        reasons.append("criterion_evidence_not_bound")
    if refs and any(item.get("evidence_status") != "REVIEWED" for item in _candidate_evidence(record, record.get("_catalogue", {}))):
        reasons.append("reviewed_evidence_missing_or_stale")
    if release is None:
        reasons.append("approved_release_not_verified")
    if not _is_explicitly_complete(record):
        reasons.append("completion_rationale_not_approved")
    return sorted(set(reasons))


def _project_cell(cell: Mapping[str, Any], records: Sequence[Mapping[str, Any]], catalogue: Mapping[str, Any], releases: Mapping[str, Mapping[str, Any]]) -> dict[str, Any]:
    cell_id = str(cell["cell_id"])
    # The first record is not privileged for candidates; the last decision is
    # selected by deterministic source order below.
    records = sorted(records, key=lambda row: (_status_hint(row) or "", str(row.get("proposal_id") or ""), str(row.get("candidate_sha256") or "")))
    selected = records[-1] if records else {}
    selected = dict(selected)
    selected["_catalogue"] = catalogue
    mismatch = _hash_mismatches(selected, catalogue) if records else []
    release, release_problem = _approved_release(selected, releases) if records else (None, "approved_release_missing")
    hint = _status_hint(selected)
    notes, questions, sources, sections = _candidate_ids(selected)
    candidates = _cell_candidates(cell, records, catalogue)
    domain_candidates = _domain_candidates(cell, catalogue)
    gaps: list[str] = []
    if not records:
        if str(cell.get("recorded_pillar_status") or "") == "SOURCE_GAP":
            projected = "SOURCE_GAP"
            gaps.append("criterion_review_missing")
        else:
            projected = REVIEW_REQUIRED
            gaps.append("criterion_review_missing")
    elif mismatch:
        projected = REVIEW_REQUIRED
        gaps.extend(["hash_changed", *mismatch])
    elif release is not None and _is_explicitly_complete(selected):
        # A valid hash-bound approval can complete only the exact criterion
        # record that requests completion.  INTEGRATED is never sufficient.
        projected = "COMPLETE"
    elif release is not None and hint in {"APPROVED", "COMPLETE"}:
        projected = "APPROVED"
        gaps.append("completion_rationale_not_approved")
    elif hint == "SOURCE_GAP" and not candidates["candidate_evidence"]:
        projected = "SOURCE_GAP"
        gaps.append("source_or_taxonomy_gap")
    else:
        projected = REVIEW_REQUIRED
        gaps.append(release_problem or "approved_release_not_verified")
        if hint in {"PROPOSAL_READY", "EVIDENCE_READY", "HUMAN_REVIEW", "APPROVED", "COMPLETE"}:
            gaps.append("criterion_review_not_released")
    if records and not _record_evidence_refs(selected):
        gaps.append("criterion_evidence_not_bound")
    if records and _record_evidence_refs(selected):
        for item in _candidate_evidence(selected, catalogue):
            if item.get("evidence_status") != "REVIEWED":
                gaps.append("reviewed_evidence_missing_or_stale")
    if records and release is None and "approved_release_not_verified" not in gaps:
        gaps.append("approved_release_not_verified")
    approved_links = []
    if release is not None:
        approved_links.append(
            {
                "release_id": release["release_id"],
                "candidate_sha256": release.get("candidate_sha256"),
                "publication_verified": True,
                "approval_status": "APPROVED",
            }
        )
    result = {
        "cell_id": cell_id,
        "pillar_id": cell.get("pillar_id"),
        "criterion": cell.get("criterion"),
        "recorded_pillar_status": cell.get("recorded_pillar_status"),
        "prior_status": cell.get("status") or cell.get("current_status") or "UNASSESSED",
        "status": projected,
        "decision_record_ids": sorted({str(r.get("record_id") or r.get("proposal_id") or "") for r in records if r.get("record_id") or r.get("proposal_id")} ),
        "candidate_note_ids": candidates["candidate_note_ids"],
        "candidate_question_ids": candidates["candidate_question_ids"],
        "candidate_source_ids": candidates["candidate_source_ids"],
        "candidate_section_ids": candidates["candidate_section_ids"],
        "candidate_evidence": candidates["candidate_evidence"],
        "approved_release_links": approved_links,
        "domain_candidates": domain_candidates,
        "remaining_gaps": sorted(set(gaps)),
        "invalidation": {
            "valid": not bool(mismatch),
            "reasons": mismatch,
            "checked_hash_bound_record": bool(records),
        },
        "rationale": "Explicit criterion decision and exact approved release are required; candidate overlap is diagnostic only.",
    }
    return result


def project_coverage(
    coverage_register: Mapping[str, Any],
    catalogue: Mapping[str, Any],
    criterion_reviews: Any = None,
    publication_inventory: Any = None,
    *,
    release_records: Any = None,
) -> dict[str, Any]:
    """Project all registered cells from explicit, hash-bound review records.

    ``criterion_reviews`` may be a document with ``cells`` or
    ``criterion_rows``.  ``publication_inventory`` is the existing catalogue
    inventory tuple's first element or an equivalent release list.  The
    optional ``release_records`` is an alias for callers that already have
    manifest facts; when supplied it is combined with the inventory by release
    ID, with explicit records taking precedence only for non-hash metadata.
    """
    criteria = [str(item) for item in coverage_register.get("definition_of_done", [])]
    cells: list[dict[str, Any]] = []
    records_by_cell: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in normalize_reviews(criterion_reviews):
        identity = _cell_id(record)
        if identity:
            records_by_cell[identity].append(record)
    releases = _release_rows(publication_inventory)
    releases.update(_release_rows(release_records))
    for pillar in coverage_register.get("pillars", []):
        pillar_id = str(pillar.get("id"))
        for criterion in criteria:
            identity = f"{pillar_id}:{criterion}"
            cell = {
                "cell_id": identity,
                "pillar_id": pillar_id,
                "criterion": criterion,
                "domains": list(pillar.get("domains") or []),
                "recorded_pillar_status": pillar.get("status"),
            }
            cells.append(_project_cell(cell, records_by_cell.get(identity, []), catalogue, releases))
    cells.sort(key=lambda row: row["cell_id"])
    counts = Counter(row["status"] for row in cells)
    invalidated = [row["cell_id"] for row in cells if not row["invalidation"]["valid"]]
    return {
        "schema_version": SCHEMA_VERSION,
        "catalogue_sha256": catalogue.get("catalogue_sha256"),
        "coverage_register_sha256": sha256(coverage_register),
        "cells": cells,
        "criteria": criteria,
        "pillars": len(coverage_register.get("pillars", [])),
        "cell_count": len(cells),
        "status_counts": dict(sorted(counts.items())),
        "invalidated_cells": invalidated,
        "review_record_count": sum(len(rows) for rows in records_by_cell.values()),
        "completion_policy": "COMPLETE requires an explicit criterion completion decision, reviewed evidence, matching note/section/evidence hashes and an exact approved, publication-verified release. INTEGRATED alone never completes a cell.",
        "sanitized": True,
    }


def reconcile_coverage(root: Path, catalogue: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Read only deterministic repository metadata and return a report.

    This convenience wrapper reads coverage/review JSON, manifests and review
    receipts.  It intentionally does not open ``sources/`` or ``ingest/``.
    """
    root = Path(root)
    register_path = root / "state/workshop/coverage/coverage-register.json"
    register = json.loads(register_path.read_text(encoding="utf-8"))
    if catalogue is None:
        from .catalogue import compile_brain

        catalogue = compile_brain(root)
    reviews: list[dict[str, Any]] = []
    state_path = root / "state/workshop/proposals/coverage-state-p0-20260920/analysis/coverage-state.json"
    if state_path.is_file():
        reviews.append(json.loads(state_path.read_text(encoding="utf-8")))
    releases: list[dict[str, Any]] = []
    for path in sorted((root / "state/workshop/proposals").glob("*/manifest.json")):
        manifest = json.loads(path.read_text(encoding="utf-8"))
        report_path = path.parent / "review/integration-report.json"
        report = json.loads(report_path.read_text(encoding="utf-8")) if report_path.is_file() else {}
        release = {
            "proposal_id": path.parent.name,
            "status": manifest.get("status"),
            "candidate_sha256": report.get("candidate_sha256") or manifest.get("candidate_sha256"),
            "publication_verified": False,
        }
        # The active inventory is the authority for verification. Importing
        # here avoids duplicating its historical replay rules.
        try:
            from .catalogue import publication_inventory

            inventory, _published = publication_inventory(root)
            fact = next((item for item in inventory if item.get("proposal_id") == path.parent.name), None)
            if fact:
                release.update({k: fact.get(k) for k in ("candidate_sha256", "publication_verified", "findings")})
        except (ImportError, OSError, ValueError, KeyError, TypeError):
            pass
        releases.append(release)
    return project_coverage(register, catalogue, reviews, releases)


coverage_matrix = project_coverage

