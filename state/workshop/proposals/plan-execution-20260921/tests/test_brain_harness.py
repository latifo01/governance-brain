from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from gov360_brain.brain.harness import (  # noqa: E402
    HarnessError,
    TaskBrief,
    Telemetry,
    assert_output_allowed,
    make_reviewer_handoff,
    preflight_capability,
    verify_inputs,
)


FORBIDDEN = [
    "sources/**",
    "ingest/**",
    "brain wiki/**",
    "state/workshop/proposals/*/review/approval.md",
    "state/workshop/evidence-library/**",
]


def brief(tmp_path: Path, *, output_root: str = "state/workshop/proposals/lot-a") -> tuple[dict, Path]:
    input_path = tmp_path / "ingest" / "unit.md"
    input_path.parent.mkdir()
    input_path.write_text("synthetic validated unit\n", encoding="utf-8")
    digest = hashlib.sha256(input_path.read_bytes()).hexdigest()
    relative_input = "ingest/unit.md"
    return (
        {
            "task_id": "u03-fixture",
            "objective": "Exercise bounded task preflight with synthetic evidence.",
            "role": "domain_builder",
            "author_id": "builder-01",
            "reviewer_id": "reviewer-01",
            "input_files": [{"path": relative_input, "sha256": digest, "kind": "ingest-unit"}],
            "evidence_allowlist": ["src-fixture-01"],
            "output_root": output_root,
            "output_files": [f"{output_root}/future-vault/note.md"],
            "forbidden_paths": FORBIDDEN,
            "exit_criteria": ["Produce only the assigned overlay."],
            "processing": {"profile": "strict-local", "authorized": False, "material_ids": []},
        },
        input_path,
    )


def test_hash_bound_brief_is_stable_and_inputs_are_verified(tmp_path: Path) -> None:
    raw, _ = brief(tmp_path)
    task = TaskBrief.from_mapping(raw)
    assert task.sha256 == TaskBrief.from_mapping(json.loads(json.dumps(raw))).sha256
    assert verify_inputs(task, tmp_path) == {"ingest/unit.md": raw["input_files"][0]["sha256"]}


def test_sibling_proposal_is_rejected(tmp_path: Path) -> None:
    task = TaskBrief.from_mapping(brief(tmp_path)[0])
    with pytest.raises(HarnessError, match="not assigned"):
        assert_output_allowed(task, "state/workshop/proposals/lot-b/future-vault/note.md", tmp_path)


@pytest.mark.parametrize(
    "path",
    [
        "state/workshop/proposals/lot-a/review/approval.md",
        "sources/leak.txt",
        "state/workshop/evidence-library/raw.md",
        "brain wiki/accidental.md",
    ],
)
def test_approval_sources_and_vault_are_rejected(tmp_path: Path, path: str) -> None:
    task = TaskBrief.from_mapping(brief(tmp_path)[0])
    with pytest.raises(HarnessError):
        assert_output_allowed(task, path, tmp_path)


def test_symlink_traversal_is_rejected(tmp_path: Path) -> None:
    raw, _ = brief(tmp_path)
    task = TaskBrief.from_mapping(raw)
    target = tmp_path / "outside"
    target.mkdir()
    assigned = tmp_path / "state/workshop/proposals/lot-a/future-vault"
    assigned.mkdir(parents=True)
    (assigned / "escape.md").symlink_to(target / "escape.md")
    raw["output_files"] = ["state/workshop/proposals/lot-a/future-vault/escape.md"]
    task = TaskBrief.from_mapping(raw)
    with pytest.raises(HarnessError, match="symlink"):
        assert_output_allowed(task, raw["output_files"][0], tmp_path)


def test_author_cannot_be_reviewer(tmp_path: Path) -> None:
    raw, _ = brief(tmp_path)
    raw["reviewer_id"] = raw["author_id"]
    with pytest.raises(HarnessError, match="independent"):
        TaskBrief.from_mapping(raw)


def test_remote_requires_endpoint_material_and_authorization(tmp_path: Path) -> None:
    raw, _ = brief(tmp_path)
    raw["processing"] = {"profile": "approved-remote", "authorized": True, "material_ids": ["src-fixture-01"]}
    with pytest.raises(HarnessError, match="endpoint"):
        TaskBrief.from_mapping(raw)
    raw["processing"]["endpoint"] = "https://example.invalid/api"
    with pytest.raises(HarnessError, match="authorization reference"):
        TaskBrief.from_mapping(raw)


def test_telemetry_defaults_to_unknown_without_fabricated_zeroes() -> None:
    telemetry = Telemetry.from_mapping({}).to_mapping()
    assert telemetry == {"calls": "unknown", "tokens": "unknown", "duration_ms": "unknown", "cost": "unknown"}
    assert Telemetry.from_mapping({"calls": 0}).calls == 0


def test_handoff_is_hash_bound_and_contains_no_raw_corpus(tmp_path: Path) -> None:
    raw, _ = brief(tmp_path)
    task = TaskBrief.from_mapping(raw)
    handoff = make_reviewer_handoff(
        task,
        "a" * 64,
        "reviewer-01",
        [raw["output_files"][0]],
        tmp_path,
        telemetry={},
    ).to_mapping()
    encoded = json.dumps(handoff)
    assert "synthetic validated unit" not in encoded
    assert handoff["brief_sha256"] == task.sha256
    assert handoff["telemetry"]["cost"] == "unknown"


def test_handoff_rejects_non_assigned_reviewer(tmp_path: Path) -> None:
    raw, _ = brief(tmp_path)
    task = TaskBrief.from_mapping(raw)
    with pytest.raises(HarnessError, match="assigned reviewer"):
        make_reviewer_handoff(task, "a" * 64, "builder-01", [raw["output_files"][0]], tmp_path)


def test_capability_declares_preflight_only() -> None:
    capability = preflight_capability("strict-local")
    assert capability["hash_checks"] is True
    assert capability["provider_sandbox_enforced"] is False
    assert capability["runtime_guarantee"] is False
