from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import pytest

_HARNESS_PATH = Path(__file__).resolve().parents[1] / "src/gov360_brain/brain/harness.py"
_SPEC = importlib.util.spec_from_file_location("gov360_brain.brain.harness_repair", _HARNESS_PATH)
assert _SPEC and _SPEC.loader
_HARNESS = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = _HARNESS
_SPEC.loader.exec_module(_HARNESS)

HarnessError = _HARNESS.HarnessError
TaskBrief = _HARNESS.TaskBrief
Telemetry = _HARNESS.Telemetry
assert_output_allowed = _HARNESS.assert_output_allowed
make_reviewer_handoff = _HARNESS.make_reviewer_handoff
preflight_capability = _HARNESS.preflight_capability
run_local_sandbox = _HARNESS.run_local_sandbox
verify_inputs = _HARNESS.verify_inputs


FORBIDDEN = [
    "sources/**",
    "brain wiki/**",
    "state/workshop/evidence-library/**",
    "state/workshop/proposals/*/review/approval.md",
]


def brief(tmp_path: Path, *, output_files: list[str] | None = None) -> tuple[dict, Path]:
    input_path = tmp_path / "ingest" / "SRC-9001" / "units" / "unit.md"
    input_path.parent.mkdir(parents=True)
    source_sha = "a" * 64
    body = "Synthetic validated unit\n"
    content_sha = hashlib.sha256(body.rstrip().encode() + b"\n").hexdigest()
    metadata = (
        "---\n"
        "type: ingested_unit\n"
        "schema_version: 1\n"
        "source_id: SRC-9001\n"
        f"source_sha256: {source_sha}\n"
        "source_format: txt\n"
        "adapter_id: synthetic\n"
        "adapter_version: '1'\n"
        "locator_kind: section\n"
        "locator: Synthetic\n"
        f"content_sha256: {content_sha}\n"
        "extraction_mode: native\n"
        "visual_review: NONE\n"
        "warnings: []\n"
        "---\n"
    )
    input_path.write_text(metadata + body, encoding="utf-8")
    digest = hashlib.sha256(input_path.read_bytes()).hexdigest()
    document = {
        "source_id": "SRC-9001", "source_sha256": source_sha, "validation": {"valid": True},
        "units": [{"filename": "units/unit.md", "locator": "Synthetic", "file_sha256": digest, "content_sha256": content_sha}],
    }
    (input_path.parent.parent / "document.json").write_text(json.dumps(document), encoding="utf-8")
    (tmp_path / "state").mkdir(parents=True)
    (tmp_path / "state/source_manifest.jsonl").write_text(json.dumps({"source_id": "SRC-9001", "source_sha256": source_sha, "status": "READY_FOR_LLM"}) + "\n", encoding="utf-8")
    output_files = output_files or ["state/workshop/proposals/lot-a/future-vault/note.md"]
    return (
        {
            "schema_version": 1,
            "task_id": "u03-fixture",
            "objective": "Exercise bounded task preflight with synthetic evidence.",
            "role": "domain_builder",
            "author_id": "builder-01",
            "reviewer_id": "reviewer-01",
            "input_files": [{"path": "ingest/SRC-9001/units/unit.md", "sha256": digest, "kind": "ingest-unit", "material_id": "src-fixture-01"}],
            "evidence_allowlist": ["src-fixture-01"],
            "output_root": "state/workshop/proposals/lot-a",
            "output_files": output_files,
            "forbidden_paths": FORBIDDEN,
            "exit_criteria": ["Produce only the assigned overlay."],
            "processing": {"profile": "strict-local", "authorized": False, "material_ids": []},
        },
        input_path,
    )


def test_schema_and_direct_dataclass_boundaries_are_enforced(tmp_path: Path) -> None:
    raw, _ = brief(tmp_path)
    task = TaskBrief.from_mapping(raw)
    assert task.sha256 == TaskBrief.from_mapping(json.loads(json.dumps(raw))).sha256
    with pytest.raises(HarnessError, match="SCHEMA_INVALID"):
        bad = dict(raw)
        bad["unexpected"] = "must be rejected"
        TaskBrief.from_mapping(bad)
    with pytest.raises(HarnessError, match=r"SCHEMA_INVALID:\$|SCHEMA_INVALID:objective") as error:
        malformed = dict(raw)
        malformed["objective"] = {"secret": "must not appear"}
        TaskBrief.from_mapping(malformed)
    assert "must not appear" not in str(error.value)
    with pytest.raises(HarnessError, match="relative"):
        TaskBrief("task", "objective", "domain_builder", "author", "reviewer", (), (), "C:/escape", ("C:/escape/x",), ("sources/**",), ("done",))


def test_inputs_are_validated_ingest_only_and_parent_symlinks_are_rejected(tmp_path: Path) -> None:
    raw, _ = brief(tmp_path)
    task = TaskBrief.from_mapping(raw)
    assert verify_inputs(task, tmp_path) == {"ingest/SRC-9001/units/unit.md": raw["input_files"][0]["sha256"]}
    raw["input_files"][0] = {"path": "sources/raw.pdf", "sha256": raw["input_files"][0]["sha256"]}
    with pytest.raises(HarnessError, match="ingest"):
        TaskBrief.from_mapping(raw)
    raw, _ = brief(tmp_path / "symlink")
    task = TaskBrief.from_mapping(raw)
    outside = tmp_path / "outside"
    outside.mkdir()
    (tmp_path / "symlink" / "ingest").rename(tmp_path / "symlink" / "ingest-real")
    (tmp_path / "symlink" / "ingest").symlink_to(outside, target_is_directory=True)
    with pytest.raises(HarnessError, match="INPUT_NOT_VALIDATED_UNIT"):
        verify_inputs(task, tmp_path / "symlink")
    raw, _ = brief(tmp_path / "pdf")
    raw["input_files"][0]["path"] = "ingest/SRC-9001/units/unit.pdf"
    task = TaskBrief.from_mapping(raw)
    with pytest.raises(HarnessError, match="INPUT_NOT_VALIDATED_UNIT"):
        verify_inputs(task, tmp_path / "pdf")


@pytest.mark.parametrize("path", ["state/workshop/proposals/lot-b/future-vault/note.md", "sources/leak.txt", "brain wiki/accidental.md", "state/workshop/evidence-library/raw.md", "state/workshop/proposals/lot-a/review/approval.md", "../escape", "C:/escape", "state//workshop/proposals/lot-a/x.md"])
def test_output_scope_and_mandatory_protected_boundaries(tmp_path: Path, path: str) -> None:
    task = TaskBrief.from_mapping(brief(tmp_path)[0])
    with pytest.raises(HarnessError):
        assert_output_allowed(task, path, tmp_path)


def test_output_parent_symlink_is_rejected(tmp_path: Path) -> None:
    raw, _ = brief(tmp_path)
    task = TaskBrief.from_mapping(raw)
    outside = tmp_path / "outside"
    outside.mkdir()
    proposal = tmp_path / "state/workshop/proposals"
    proposal.mkdir(parents=True)
    (proposal / "lot-a").symlink_to(outside, target_is_directory=True)
    with pytest.raises(HarnessError, match="symlink"):
        assert_output_allowed(task, raw["output_files"][0], tmp_path)


def test_remote_materials_bind_to_inputs_and_evidence(tmp_path: Path) -> None:
    raw, _ = brief(tmp_path)
    raw["processing"] = {"profile": "approved-remote", "authorized": True, "endpoint": "https://example.invalid/api", "material_ids": ["src-fixture-01"], "authorization_ref": "approval-01"}
    assert TaskBrief.from_mapping(raw).processing.profile == "approved-remote"
    raw["input_files"][0].pop("material_id")
    with pytest.raises(HarnessError, match="material_id"):
        TaskBrief.from_mapping(raw)
    raw, _ = brief(tmp_path / "bad-material")
    raw["processing"] = {"profile": "approved-remote", "authorized": True, "endpoint": "https://example.invalid/api", "material_ids": ["other-material"], "authorization_ref": "approval-01"}
    with pytest.raises(HarnessError, match="evidence"):
        TaskBrief.from_mapping(raw)
    raw, _ = brief(tmp_path / "missing-material")
    raw["processing"] = {"profile": "approved-remote", "authorized": True, "endpoint": "https://example.invalid/api", "material_ids": [], "authorization_ref": "approval-01"}
    with pytest.raises(HarnessError, match="material"):
        TaskBrief.from_mapping(raw)


@pytest.mark.parametrize("value", [{"calls": -1}, {"tokens": float("nan")}, {"duration_ms": float("inf")}, {"cost": "api-key-secret"}, {"calls": True}])
def test_telemetry_rejects_negative_nonfinite_and_arbitrary_strings(value: dict) -> None:
    with pytest.raises(HarnessError):
        Telemetry.from_mapping(value)
    assert Telemetry.from_mapping({"calls": 0}).calls == 0
    assert Telemetry.from_mapping({}).to_mapping() == {"calls": "unknown", "tokens": "unknown", "duration_ms": "unknown", "cost": "unknown"}
    with pytest.raises(HarnessError):
        Telemetry(calls="secret")


def test_handoff_computes_candidate_hash_from_outputs(tmp_path: Path) -> None:
    raw, _ = brief(tmp_path)
    task = TaskBrief.from_mapping(raw)
    output = tmp_path / raw["output_files"][0]
    output.parent.mkdir(parents=True)
    output.write_text("candidate\n", encoding="utf-8")
    handoff = make_reviewer_handoff(task, None, "reviewer-01", raw["output_files"], tmp_path)
    assert len(handoff.candidate_sha256) == 64
    with pytest.raises(HarnessError, match="does not match"):
        make_reviewer_handoff(task, "a" * 64, "reviewer-01", raw["output_files"], tmp_path)
    assert "synthetic validated unit" not in json.dumps(handoff.to_mapping())


def test_local_sandbox_mounts_only_declared_files(tmp_path: Path) -> None:
    if not __import__("shutil").which("bwrap"):
        pytest.skip("bubblewrap is unavailable")
    raw, _ = brief(tmp_path)
    task = TaskBrief.from_mapping(raw)
    output = raw["output_files"][0]
    result = run_local_sandbox(task, tmp_path, ["/usr/bin/python3", "-c", "from pathlib import Path; Path('state/workshop/proposals/lot-a/future-vault/note.md').write_text('sandbox\\n')"])
    if result.returncode != 0 and b"Operation not permitted" in (result.stderr or b""):
        pytest.skip("bubblewrap namespace creation is restricted in this runner")
    assert result.returncode == 0
    assert (tmp_path / output).read_text(encoding="utf-8") == "sandbox\n"


def test_local_sandbox_stages_outputs_and_clears_environment(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    raw, _ = brief(tmp_path)
    task = TaskBrief.from_mapping(raw)
    seen: dict[str, object] = {}

    def fake_run(args, **kwargs):
        seen["args"] = args
        seen["env"] = kwargs["env"]
        bind = args.index("--bind")
        staged_root = Path(args[bind + 1])
        staged = staged_root / "future-vault/note.md"
        staged.parent.mkdir(parents=True)
        staged.write_text("staged\n", encoding="utf-8")
        return _HARNESS.subprocess.CompletedProcess(args, 0, b"", b"")

    monkeypatch.setattr(_HARNESS.shutil, "which", lambda _: "/usr/bin/bwrap")
    monkeypatch.setattr(_HARNESS.subprocess, "run", fake_run)
    output = tmp_path / raw["output_files"][0]
    result = run_local_sandbox(task, tmp_path, ["/usr/bin/python3", "-c", "pass"])
    assert result.returncode == 0
    assert output.read_text(encoding="utf-8") == "staged\n"
    args = seen["args"]
    assert "--clearenv" in args and "--remount-ro" in args and "--unshare-all" in args
    assert args.index("--remount-ro") < args.index("--bind")
    assert seen["env"] == {}


def test_local_sandbox_rejects_missing_or_undeclared_outputs(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    raw, _ = brief(tmp_path)
    task = TaskBrief.from_mapping(raw)

    def no_output(args, **kwargs):
        return _HARNESS.subprocess.CompletedProcess(args, 0, b"", b"")

    monkeypatch.setattr(_HARNESS.shutil, "which", lambda _: "/usr/bin/bwrap")
    monkeypatch.setattr(_HARNESS.subprocess, "run", no_output)
    with pytest.raises(HarnessError, match="missing="):
        run_local_sandbox(task, tmp_path, ["/usr/bin/python3", "-c", "pass"])

    def extra_output(args, **kwargs):
        bind = args.index("--bind")
        staged_root = Path(args[bind + 1])
        expected = staged_root / "future-vault/note.md"
        expected.parent.mkdir(parents=True)
        expected.write_text("expected\n", encoding="utf-8")
        (staged_root / "undeclared.md").write_text("extra\n", encoding="utf-8")
        return _HARNESS.subprocess.CompletedProcess(args, 0, b"", b"")

    monkeypatch.setattr(_HARNESS.subprocess, "run", extra_output)
    with pytest.raises(HarnessError, match="undeclared="):
        run_local_sandbox(task, tmp_path, ["/usr/bin/python3", "-c", "pass"])
    assert not (tmp_path / raw["output_files"][0]).exists()


def test_local_sandbox_failure_does_not_create_final_output(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    raw, _ = brief(tmp_path)
    task = TaskBrief.from_mapping(raw)

    def fake_run(args, **kwargs):
        return _HARNESS.subprocess.CompletedProcess(args, 7, b"", b"failed")

    monkeypatch.setattr(_HARNESS.shutil, "which", lambda _: "/usr/bin/bwrap")
    monkeypatch.setattr(_HARNESS.subprocess, "run", fake_run)
    result = run_local_sandbox(task, tmp_path, ["/usr/bin/python3", "-c", "pass"])
    assert result.returncode == 7
    assert not (tmp_path / raw["output_files"][0]).exists()


def test_capability_does_not_claim_provider_enforcement() -> None:
    capability = preflight_capability("strict-local")
    assert capability["provider_sandbox_enforced"] is False
    assert capability["hash_checks"] is True
    assert preflight_capability("strict-local", "local-sandbox")["runtime_guarantee"] is False
