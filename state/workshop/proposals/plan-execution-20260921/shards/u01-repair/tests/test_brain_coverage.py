"""Synthetic contract tests for the U01 coverage projector overlay."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

import pytest


OVERLAY = Path(__file__).parents[1]
SPEC = importlib.util.spec_from_file_location("u01_repair_coverage", OVERLAY / "coverage.py")
coverage = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(coverage)


def _base() -> dict:
    return {"schema_version": 1, "catalogue_sha256": "c" * 64,
            "unapplied_review_records": 1,
            "cells": [{"cell_id": "P::criterion", "pillar_id": "P",
                        "criterion": "criterion", "status": "UNASSESSED"}]}


def _catalogue() -> dict:
    return {"catalogue_sha256": "c" * 64,
            "notes": [{"id": "published-note", "sha256": "b" * 64,
                        "publication_verified": True, "type": "knowledge"}],
            "sections": [{"section_id": "published-note:scope", "note_id": "published-note",
                          "note_sha256": "b" * 64, "sha256": "c" * 64,
                          "evidence_status": "REVIEWED", "derived_from": ["reviewed-evidence"]}],
            "evidence": {"records": [{"evidence_ref": "reviewed-evidence",
                                        "evidence_sha256": "d" * 64,
                                        "evidence_status": "REVIEWED"}]}}


def _record(cat: dict, matrix: dict, **overrides) -> dict:
    record = {"record_id": "decision-1", "cell_id": "P::criterion", "pillar_id": "P",
              "criterion": "criterion", "decision": "EVIDENCE_APPROVED",
              "justification": "Reviewed basis", "note_refs": [{"note_id": "published-note", "note_sha256": "b" * 64}],
              "section_refs": [{"section_id": "published-note:scope", "note_id": "published-note",
                                "note_sha256": "b" * 64, "section_sha256": "c" * 64}],
              "question_refs": [], "evidence_refs": [{"evidence_ref": "reviewed-evidence", "evidence_sha256": "d" * 64}],
              "input_hashes": {"catalogue_sha256": cat["catalogue_sha256"],
                               "base_matrix_sha256": coverage.matrix_sha256(matrix)},
              "author_identity": "author", "review": {"reviewer_identity": "reviewer",
              "reviewed_at": "2026-09-01T00:00:00Z", "verdict": "APPROVED"},
              "approval": {"status": "APPROVED", "approver_identity": "human-approver",
                            "approved_at": "2026-09-02T00:00:00Z"}, "requires_human_approval": True,
              "expires_at": None, "payload_sha256": "0" * 64}
    record.update(overrides)
    record["payload_sha256"] = coverage.decision_payload_sha256(record)
    record["review"]["payload_sha256"] = record["payload_sha256"]
    if "approval" not in overrides and isinstance(record.get("approval"), dict):
        record["approval"]["payload_sha256"] = record["payload_sha256"]
    return record


def _write(root: Path, records, *, envelope_extra=None):
    target = root / "state/workshop/coverage/criterion-reviews.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    envelope = {"schema_version": 1, "records": records}
    if envelope_extra:
        envelope.update(envelope_extra)
    target.write_text(json.dumps(envelope), encoding="utf-8")


def _run(tmp_path: Path, records, *, as_of="2026-09-22", envelope_extra=None):
    cat, matrix = _catalogue(), _base()
    _write(tmp_path, records, envelope_extra=envelope_extra)
    return coverage.project_coverage(tmp_path, cat, matrix, as_of=as_of)


def test_current_reviewed_approved_decision_applies(tmp_path):
    cat, matrix = _catalogue(), _base()
    result = _run(tmp_path, [_record(cat, matrix)])
    cell = result["cells"][0]
    assert cell["status"] == "EVIDENCE_APPROVED"
    assert cell["decision_valid"] is True
    assert not result["diagnostics"]


@pytest.mark.parametrize("field", ["catalogue_sha256", "base_matrix_sha256"])
def test_stale_input_hash_fails_closed(tmp_path, field):
    cat, matrix = _catalogue(), _base()
    record = _record(cat, matrix)
    record["input_hashes"][field] = "a" * 64
    result = _run(tmp_path, [record])
    assert result["cells"][0]["status"] == "UNASSESSED"
    assert any(item["code"] == "CATALOGUE_HASH_MISMATCH" if field == "catalogue_sha256"
               else item["code"] == "BASE_MATRIX_HASH_MISMATCH" for item in result["diagnostics"])


def test_self_review_fails_closed(tmp_path):
    cat, matrix = _catalogue(), _base()
    record = _record(cat, matrix)
    record["review"]["reviewer_identity"] = record["author_identity"]
    result = _run(tmp_path, [record])
    assert result["cells"][0]["decision_valid"] is False
    assert any(item["code"] == "INDEPENDENT_REVIEW_REQUIRED" for item in result["diagnostics"])


def test_duplicate_good_and_bad_records_fail_closed(tmp_path):
    cat, matrix = _catalogue(), _base()
    good = _record(cat, matrix)
    bad = copy.deepcopy(good)
    bad["record_id"] = "decision-2"
    bad["payload_sha256"] = "f" * 64
    result = _run(tmp_path, [good, bad])
    assert result["cells"][0]["status"] == "UNASSESSED"
    assert any(item["code"] == "DUPLICATE_DECISION_CELL" for item in result["diagnostics"])


def test_expired_record_review_and_approval_fail_closed(tmp_path):
    cat, matrix = _catalogue(), _base()
    record = _record(cat, matrix, expires_at="2026-09-01")
    record["review"]["review_expires_at"] = "2026-09-01"
    record["approval"]["expires_at"] = "2026-09-01"
    # Expiry metadata belongs to the payload, so recompute attestations.
    record["payload_sha256"] = coverage.decision_payload_sha256(record)
    record["review"]["payload_sha256"] = record["payload_sha256"]
    if isinstance(record.get("approval"), dict):
        record["approval"]["payload_sha256"] = record["payload_sha256"]
    result = _run(tmp_path, [record])
    assert result["cells"][0]["status"] == "UNASSESSED"
    codes = {item["code"] for item in result["diagnostics"]}
    assert {"DECISION_EXPIRED", "REVIEW_EXPIRED", "APPROVAL_EXPIRED"} <= codes


def test_envelope_timestamp_cannot_choose_verifier_clock(tmp_path):
    cat, matrix = _catalogue(), _base()
    record = _record(cat, matrix, expires_at="2026-09-01")
    _write(tmp_path, [record], envelope_extra={"evaluated_at": "2026-01-01T00:00:00Z"})
    result = coverage.project_coverage(tmp_path, cat, matrix, as_of="2026-09-22")
    assert result["cells"][0]["status"] == "UNASSESSED"
    assert any(item["code"] == "DECISION_EXPIRED" for item in result["diagnostics"])


def test_review_count_is_part_of_base_matrix_hash(tmp_path):
    cat, matrix = _catalogue(), _base()
    record = _record(cat, matrix)
    matrix["unapplied_review_records"] = 2
    _write(tmp_path, [record])
    result = coverage.project_coverage(tmp_path, cat, matrix, as_of="2026-09-22")
    assert result["cells"][0]["status"] == "UNASSESSED"
    assert any(item["code"] == "BASE_MATRIX_HASH_MISMATCH" for item in result["diagnostics"])


def test_unpublished_note_cannot_use_published_alias(tmp_path):
    cat, matrix = _catalogue(), _base()
    cat["notes"][0]["publication_verified"] = False
    cat["notes"][0]["published"] = True
    _write(tmp_path, [_record(cat, matrix)])
    result = coverage.project_coverage(tmp_path, cat, matrix, as_of="2026-09-22")
    assert result["cells"][0]["status"] == "UNASSESSED"
    assert any(item["code"] == "NOTE_NOT_CURRENTLY_PUBLISHED" for item in result["diagnostics"])


def test_duplicate_base_cells_never_project(tmp_path):
    cat, matrix = _catalogue(), _base()
    matrix["cells"].append(copy.deepcopy(matrix["cells"][0]))
    record = _record(cat, matrix)
    # Bind against the duplicated matrix supplied to the projector.
    matrix["cells"].pop()
    record["input_hashes"]["base_matrix_sha256"] = coverage.matrix_sha256(matrix)
    matrix["cells"].append(copy.deepcopy(matrix["cells"][0]))
    _write(tmp_path, [record])
    result = coverage.project_coverage(tmp_path, cat, matrix, as_of="2026-09-22")
    assert all(cell["status"] == "UNASSESSED" for cell in result["cells"])
    assert any(item["code"] == "BASE_MATRIX_DUPLICATE_CELL" for item in result["diagnostics"])


def test_future_review_and_approval_dates_fail_closed(tmp_path):
    cat, matrix = _catalogue(), _base()
    record = _record(cat, matrix)
    record["review"]["reviewed_at"] = "2026-10-01T00:00:00Z"
    record["approval"]["approved_at"] = "2026-10-02T00:00:00Z"
    result = _run(tmp_path, [record])
    assert result["cells"][0]["status"] == "UNASSESSED"
    codes = {item["code"] for item in result["diagnostics"]}
    assert {"REVIEW_DATE_IN_FUTURE", "APPROVAL_DATE_IN_FUTURE"} <= codes


@pytest.mark.parametrize("approval", [None, {"status": "PENDING"}, {"status": "APPROVED", "payload_sha256": "a" * 64}])
def test_missing_or_wrong_approval_fails_closed(tmp_path, approval):
    cat, matrix = _catalogue(), _base()
    record = _record(cat, matrix, approval=approval)
    record["payload_sha256"] = coverage.decision_payload_sha256(record)
    if isinstance(approval, dict) and approval.get("status") == "APPROVED" and approval.get("payload_sha256") != record["payload_sha256"]:
        pass
    record["review"]["payload_sha256"] = record["payload_sha256"]
    result = _run(tmp_path, [record])
    assert result["cells"][0]["status"] == "UNASSESSED"
    assert any(item["code"].startswith("HUMAN_APPROVAL") or item["code"] == "APPROVAL_PAYLOAD_HASH_MISMATCH"
               for item in result["diagnostics"])


def test_unrelated_evidence_relationship_fails_closed(tmp_path):
    cat, matrix = _catalogue(), _base()
    record = _record(cat, matrix)
    record["evidence_refs"] = [{"evidence_ref": "unrelated", "evidence_sha256": "e" * 64}]
    record["payload_sha256"] = coverage.decision_payload_sha256(record)
    record["review"]["payload_sha256"] = record["payload_sha256"]
    record["approval"]["payload_sha256"] = record["payload_sha256"]
    result = _run(tmp_path, [record])
    assert result["cells"][0]["status"] == "UNASSESSED"
    assert any(item["code"] in {"EVIDENCE_REF_UNKNOWN", "EVIDENCE_RELATIONSHIP_MISMATCH"}
               for item in result["diagnostics"])


def test_malformed_envelope_and_date_fail_closed(tmp_path):
    cat, matrix = _catalogue(), _base()
    _write(tmp_path, [_record(cat, matrix)], envelope_extra={"evaluated_at": "not-a-date"})
    result = coverage.project_coverage(tmp_path, cat, matrix, as_of="2026-09-22")
    assert result["cells"][0]["status"] == "UNASSESSED"
    assert any(item["code"] == "DECISION_RECORD_ENVELOPE_INVALID" for item in result["diagnostics"])
    result = _run(tmp_path, [_record(cat, matrix)], as_of="not-a-date")
    assert result["cells"][0]["status"] == "UNASSESSED"
    assert any(item["code"] == "VERIFIER_AS_OF_INVALID" for item in result["diagnostics"])


def test_symlinked_decision_file_fails_closed(tmp_path):
    cat, matrix = _catalogue(), _base()
    outside = tmp_path / "outside.json"
    outside.write_text(json.dumps({"schema_version": 1, "records": []}), encoding="utf-8")
    target = tmp_path / "state/workshop/coverage/criterion-reviews.json"
    target.parent.mkdir(parents=True)
    try:
        target.symlink_to(outside)
    except OSError:
        pytest.skip("symlinks unavailable")
    result = coverage.project_coverage(tmp_path, cat, matrix, as_of="2026-09-22")
    assert result["cells"][0]["status"] == "UNASSESSED"
    assert any(item["code"] == "DECISION_RECORD_PATH_UNSAFE" for item in result["diagnostics"])


def test_never_invents_complete(tmp_path):
    cat, matrix = _catalogue(), _base()
    matrix["cells"][0]["status"] = "COMPLETE"
    result = _run(tmp_path, [])
    assert result["cells"][0]["status"] == "UNASSESSED"
    assert "COMPLETE" not in result["decision_summary"]
