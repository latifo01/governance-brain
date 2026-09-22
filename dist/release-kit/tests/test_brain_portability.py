"""Portable exports and reconstruction tests using synthetic source material only."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

import pytest
import yaml

from gov360_brain.brain import portability as mod
from gov360_brain.adapters.registry import get_default_registry
from gov360_brain.contracts import NormalizationContext
from gov360_brain.orchestration.ingestion import IngestionOrchestrator
from gov360_brain.project import ProjectPaths

ROOT = Path(__file__).resolve().parents[1]


def put(root, path, text):
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    return target


def json_put(root, path, value):
    return put(root, path, json.dumps(value))


def synthetic_seed(root):
    source = put(root, "sources/synthetic original.txt", "Synthetic fixture control.\n")
    digest = mod.sha256_file(source)
    adapter = get_default_registry().select(source)
    row = {"schema_version": 1, "source_id": "SRC-0042", "source_sha256": digest,
           "relative_paths": ["sources/synthetic original.txt"], "source_format": "txt",
           "source_kind": "document", "domains": ["RISK"], "primary_domain": "RISK",
           "status": "READY_FOR_LLM", "adapter_id": adapter.adapter_id, "adapter_version": adapter.adapter_version}
    output = root / "scratch"
    output.mkdir()
    ctx = NormalizationContext(project_root=root, source_id=row["source_id"], source_sha256=digest,
        relative_source_path=row["relative_paths"][0], domain_slugs=("risk",), output_dir=output, profile="strict-local")
    result = adapter.normalize(source, ctx)
    report = adapter.validate(result, ctx)
    doc = IngestionOrchestrator(ProjectPaths(root), get_default_registry())._write_result(output, row, ctx, result, report)
    expected = [{k: u[k] for k in ("filename", "file_sha256", "locator", "locator_kind")} for u in doc["units"]]
    seed_row = {**row, "expected_units": expected, "reconstruction": "expected"}
    seed_row.pop("status")
    seed_row.pop("schema_version")
    seed = {"schema_version": 1, "sources": [seed_row]}
    json_put(root, "config/source-seed.json", seed)
    shutil.rmtree(output)
    return seed


def read_manifest(root):
    return [json.loads(line) for line in (root / "state/source_manifest.jsonl").read_text().splitlines()]


def test_bootstrap_clean_identity_manifest_and_noop(tmp_path):
    seed = synthetic_seed(tmp_path)
    original = (tmp_path / "sources/synthetic original.txt").read_bytes()
    preview = mod.bootstrap(tmp_path)
    assert preview["valid"] and preview["sources"][0]["status"] == "READY"
    assert not (tmp_path / "state").exists()
    result = mod.bootstrap(tmp_path, apply=True)
    assert result["valid"] and result["reconstructed"] == 1
    row = read_manifest(tmp_path)[0]
    assert row["source_id"] == "SRC-0042" and row["status"] == "READY_FOR_LLM"
    assert row["normativity"] == "UNCLASSIFIED" and "discovered_at" not in row
    assert row["source_sha256"] == seed["sources"][0]["source_sha256"]
    assert (tmp_path / "sources/synthetic original.txt").read_bytes() == original
    before = (tmp_path / "state/source_manifest.jsonl").stat().st_mtime_ns
    again = mod.bootstrap(tmp_path, apply=True)
    assert again["sources"][0]["status"] == "NOOP"
    assert (tmp_path / "state/source_manifest.jsonl").stat().st_mtime_ns == before


def test_missing_source_reserves_id_without_ready(tmp_path):
    seed = synthetic_seed(tmp_path)
    # Remove only the synthetic fixture, not a repository original.
    (tmp_path / "sources/synthetic original.txt").unlink()
    result = mod.bootstrap(tmp_path, apply=True)
    assert not result["valid"] and result["sources"][0]["status"] == "MISSING_SOURCE"
    row = read_manifest(tmp_path)[0]
    assert row["source_id"] == seed["sources"][0]["source_id"]
    assert row["status"] == "DISCOVERED" and row["unit_count"] == 0
    assert not (tmp_path / "ingest/SRC-0042").exists()


@pytest.mark.parametrize("change,status", [("adapter", "ADAPTER_VERSION_MISMATCH"), ("hash", "RECONSTRUCTION_HASH_MISMATCH"), ("baseline", "NO_RECONSTRUCTION_BASELINE")])
def test_bootstrap_mismatch_quarantined_without_install(tmp_path, change, status):
    seed = synthetic_seed(tmp_path)
    if change == "adapter": seed["sources"][0]["adapter_version"] = "unavailable"
    elif change == "hash": seed["sources"][0]["expected_units"][0]["file_sha256"] = "0" * 64
    else: seed["sources"][0]["expected_units"] = []
    json_put(tmp_path, "config/source-seed.json", seed)
    result = mod.bootstrap(tmp_path, apply=True)
    assert not result["valid"] and result["sources"][0]["status"] == status
    assert read_manifest(tmp_path)[0]["status"] == "QUARANTINED"
    assert not (tmp_path / "ingest/SRC-0042").exists()


def test_bootstrap_preserves_existing_valid_metadata_and_rejects_id_conflict(tmp_path):
    synthetic_seed(tmp_path)
    mod.bootstrap(tmp_path, apply=True)
    row = read_manifest(tmp_path)[0]
    row.update(normativity="GUIDANCE", discovered_at="2026-01-01T00:00:00Z")
    put(tmp_path, "state/source_manifest.jsonl", json.dumps(row) + "\n")
    mod.bootstrap(tmp_path, apply=True)
    assert read_manifest(tmp_path)[0] == row
    row["source_sha256"] = "b" * 64
    put(tmp_path, "state/source_manifest.jsonl", json.dumps(row) + "\n")
    with pytest.raises(ValueError, match="MANIFEST_CONFLICT"):
        mod.bootstrap(tmp_path, apply=True)


def test_bootstrap_rolls_back_ingest_on_manifest_failure(tmp_path, monkeypatch):
    synthetic_seed(tmp_path)
    replace = mod.os.replace
    def fail_manifest(src, dst):
        if Path(dst).name == "source_manifest.jsonl":
            raise OSError("synthetic write failure")
        return replace(src, dst)
    monkeypatch.setattr(mod.os, "replace", fail_manifest)
    with pytest.raises(OSError): mod.bootstrap(tmp_path, apply=True)
    assert not (tmp_path / "ingest/SRC-0042").exists()
    assert not (tmp_path / "state/source_manifest.jsonl").exists()
    assert not list((tmp_path / "ingest").glob(".bootstrap-*"))


def test_bootstrap_rejects_symlink_and_source_root_escape(tmp_path):
    synthetic_seed(tmp_path)
    with pytest.raises(ValueError): mod.bootstrap(tmp_path, "../sources")
    with pytest.raises(ValueError): mod.bootstrap(tmp_path, "ingest")
    (tmp_path / "sources/link.txt").symlink_to(tmp_path / "sources/synthetic original.txt")
    with pytest.raises(ValueError, match="SYMLINK_SOURCE"): mod.bootstrap(tmp_path)


def fixture_catalogue():
    body = "# Synthetic note\n\n## Scope\n\nSynthetic supported statement.\n\n## Unreviewed\n\nSynthetic unreviewed statement.\n\n[[second note|Alias]] and [[synthetic#Scope]].\n`[[literal]]`\n"
    note = {"id": "synthetic", "title": "Synthetic", "type": "knowledge", "status": "active", "aliases": [],
        "path": "brain wiki/Synthetic/synthetic.md", "sha256": "a" * 64, "metadata": {"verified": {"by": "fake", "at": "fake"}}, "body": body}
    other = {**note, "id": "second-note", "title": "Second", "aliases": ["second note"], "path": "brain wiki/Synthetic/second-note.md", "body": "# Second\n"}
    citation = {"evidence_ref": "synthetic-reference", "source_id": "SRC-0042", "source_sha256": "b" * 64,
        "unit_path": "ingest/SRC-0042/units/synthetic.md", "unit_sha256": "c" * 64,
        "unit_file_sha256": "d" * 64, "locator": "Section 1", "authority": "GUIDANCE", "evidence_status": "REVIEWED"}
    return {"notes": [note, other], "sections": [{"note_id": "synthetic", "section_id": "synthetic:scope", "text": "Synthetic supported statement.", "evidence_status": "REVIEWED", "citations": [citation]},
        {"note_id": "synthetic", "text": "Synthetic unreviewed statement.", "evidence_status": "UNRESOLVED", "citations": [citation]}]}


def test_okf_section_attribution_links_spec_and_noop(tmp_path, monkeypatch):
    from gov360_brain.brain import catalogue
    monkeypatch.setattr(catalogue, "compile_brain", lambda root: fixture_catalogue())
    result = mod.export_okf(tmp_path)
    assert result["manifest"]["specification"]["version"] == "0.2"
    target = tmp_path / "dist/okf/concepts/synthetic.md"
    content = target.read_text()
    metadata = yaml.safe_load(content.split("---")[1])
    assert "verified" not in metadata and "generated" not in metadata
    ref = metadata["sources"][0]
    assert (tmp_path / "dist/okf" / ref["resource"].lstrip("/")).exists()
    assert f"Section evidence: [^{ref['id']}]" in content
    assert content.index("Section evidence:") < content.index("## Unreviewed")
    assert content.count("Section evidence:") == 1
    assert "[Alias](/concepts/second-note.md)" in content
    assert "(/concepts/synthetic.md#scope)" in content
    assert "`[[literal]]`" in content
    assert mod.export_okf(tmp_path)["current"]
    target.write_text(content + "human edit\n")
    with pytest.raises(ValueError, match="UNMANAGED_OR_MODIFIED"):
        mod.export_okf(tmp_path)


def test_public_export_deny_and_exact_hash_grant(tmp_path, monkeypatch):
    from gov360_brain.brain import catalogue
    monkeypatch.setattr(catalogue, "compile_brain", lambda root: fixture_catalogue())
    policy = {"schema_version": 1, "default": "deny", "content_grants": []}
    json_put(tmp_path, "config/redistribution-policy.json", policy)
    assert mod.export_okf(tmp_path, public=True, write=False)["manifest"]["mapping"] == {}
    policy["content_grants"] = [{"path": "brain wiki/Synthetic/synthetic.md", "sha256": "a" * 64,
        "permission": "redistribute", "license": "operator-test", "review_record": "synthetic-review"}]
    json_put(tmp_path, "config/redistribution-policy.json", policy)
    result = mod.export_okf(tmp_path, public=True)
    assert list(result["manifest"]["mapping"]) == ["synthetic"]
    assert any(g["code"] == "UNRESOLVED_OR_EXCLUDED_LINK" for g in result["manifest"]["gaps"])


@pytest.mark.parametrize("path", ["sources/original.txt", "ingest/SRC-0042/document.json", ".codex/config.toml", ".opencode/config.json", ".git/config", "opencode.json", "state/source_manifest.jsonl", "brain wiki/knowledge.md", "../escape.py"])
def test_kit_boundary_cannot_be_overridden_by_allowlist(tmp_path, path):
    json_put(tmp_path, "config/redistribution-policy.json", {"schema_version": 1, "default": "deny", "original_files": [path]})
    with pytest.raises(ValueError): mod.release_kit(tmp_path)


def test_kit_inherits_seed_without_original_manifest(tmp_path):
    seed = synthetic_seed(tmp_path)
    json_put(tmp_path, "config/redistribution-policy.json", {"schema_version": 1, "default": "deny", "original_files": ["config/redistribution-policy.json"]})
    result = mod.release_kit(tmp_path)
    assert result["manifest"]["source_count"] == 1
    kit = tmp_path / "dist/release-kit"
    assert json.loads((kit / "config/source-seed.json").read_text())["sources"] == seed["sources"]
    assert not (kit / "sources").exists() and not (kit / ".git").exists()
    again = mod.release_kit(kit)
    assert again["manifest"]["source_count"] == 1


def test_allowlisted_kit_imports_in_clean_directory(tmp_path):
    # Copy reviewed original-code files only. No repository sources or ingest.
    policy = json.loads((ROOT / "config/redistribution-policy.json").read_text())
    missing = []
    for path in policy["original_files"]:
        src = ROOT / path
        if src.exists():
            dst = tmp_path / path
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dst)
        else:
            missing.append(path)
    assert missing == [], f"Missing explicitly allowlisted original files: {missing}"
    synthetic_seed(tmp_path)
    result = mod.release_kit(tmp_path)
    assert result["manifest"]["gaps"] == []
    kit = tmp_path / "dist/release-kit"
    code = "import sys; sys.path.insert(0, 'src'); from gov360_brain.cli import main; from gov360_brain.brain.portability import bootstrap; from pathlib import Path; r=bootstrap(Path.cwd()); assert r['sources'][0]['source_id']=='SRC-0042'"
    proc = subprocess.run([sys.executable, "-I", "-c", code], cwd=kit, text=True, capture_output=True)
    assert proc.returncode == 0, proc.stderr
    source = kit / "sources/synthetic original.txt"
    source.parent.mkdir()
    source.write_text("Synthetic fixture control.\n")
    code = "import sys; sys.path.insert(0, 'src'); from gov360_brain.brain.portability import bootstrap; from pathlib import Path; r=bootstrap(Path.cwd(), apply=True); assert r['valid'] and r['reconstructed']==1"
    proc = subprocess.run([sys.executable, "-I", "-c", code], cwd=kit, text=True, capture_output=True)
    assert proc.returncode == 0, proc.stderr
    assert read_manifest(kit)[0]["source_id"] == "SRC-0042"


def test_kit_opencode_templates_are_portable_and_seed_is_sanitized(tmp_path):
    seed = synthetic_seed(tmp_path)
    seed["sources"][0]["quote"] = "synthetic private seed annotation"
    json_put(tmp_path, "config/source-seed.json", seed)
    put(tmp_path, ".opencode/agents/synthetic.md", "---\nmode: subagent\nmodel: synthetic/model\n---\nRead AGENTS.md.\n")
    put(tmp_path, ".opencode/commands/synthetic.md", "---\nagent: synthetic\n---\nRun the assigned task.\n")
    json_put(tmp_path, "config/redistribution-policy.json", {"schema_version": 1, "default": "deny", "original_files": [".opencode/agents/synthetic.md", ".opencode/commands/synthetic.md"]})
    mod.release_kit(tmp_path)
    kit = tmp_path / "dist/release-kit"
    config = json.loads((kit / "opencode.json").read_text())
    assert "model" not in config and "provider" not in config and config["share"] == "disabled"
    agent = (kit / ".opencode/agents/synthetic.md").read_text()
    assert "model:" not in agent and "Read AGENTS.md." in agent
    assert "quote" not in json.loads((kit / "config/source-seed.json").read_text())["sources"][0]
    assert "model: synthetic/model" in (tmp_path / ".opencode/agents/synthetic.md").read_text()


def private_policy(root: Path):
    schema = ROOT / "config/schemas/private-handoff.schema.json"
    target = root / "config/schemas/private-handoff.schema.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(schema, target)
    policy = {
        "schema_version": 1,
        "handoff_id": "synthetic-private-handoff",
        "target": {"host": "github.com", "repository": "latifo01/governance-brain", "visibility": "private"},
        "authorization": {"status": "APPROVED", "recorded_at": "2026-09-22",
                          "scope": ["sources/**", "ingest/**", "brain wiki/**", "state/**", "dist/**"],
                          "public_redistribution": "NOT_AUTHORIZED"},
        "include_roots": ["config", "ingest", "sources", "state"],
        "include_files": ["pyproject.toml"],
        "exclude_paths": ["dist/cdo-handoff"],
    }
    json_put(root, "config/private-handoff-policy.json", policy)
    put(root, "pyproject.toml", "[project]\nname='synthetic'\n")
    return policy


def test_private_handoff_contains_complete_authorized_corpus_and_is_idempotent(tmp_path):
    synthetic_seed(tmp_path)
    assert mod.bootstrap(tmp_path, apply=True)["reconstructed"] == 1
    private_policy(tmp_path)
    result = mod.private_handoff(tmp_path)
    assert result["valid"] and result["manifest"]["public"] is False
    assert result["manifest"]["corpus"] == {
        "logical_sources": 1, "source_files": 1, "ready_sources": 1, "validated_units": 1}
    handoff = tmp_path / "dist/cdo-handoff"
    assert (handoff / "sources/synthetic original.txt").is_file()
    assert (handoff / "ingest/SRC-0042/document.json").is_file()
    assert (handoff / "HANDOFF.md").is_file()
    assert not (handoff / ".git").exists()
    assert not list(handoff.rglob("__pycache__"))
    assert mod.private_handoff(tmp_path)["current"] is True


def test_private_handoff_excludes_nested_runtime_caches(tmp_path):
    synthetic_seed(tmp_path)
    assert mod.bootstrap(tmp_path, apply=True)["reconstructed"] == 1
    private_policy(tmp_path)
    put(tmp_path, "state/workshop/proposals/lot/__pycache__/worker.pyc", "cache")
    put(tmp_path, "state/workshop/proposals/lot/.pytest_cache/state", "cache")
    put(tmp_path, "state/workshop/proposals/lot/workspace.json", "local UI state")
    mod.private_handoff(tmp_path)
    handoff = tmp_path / "dist/cdo-handoff"
    assert not (handoff / "state/workshop/proposals/lot/__pycache__/worker.pyc").exists()
    assert not (handoff / "state/workshop/proposals/lot/.pytest_cache/state").exists()
    assert not (handoff / "state/workshop/proposals/lot/workspace.json").exists()


def test_private_handoff_rejects_unexcluded_windows_incompatible_path(tmp_path):
    synthetic_seed(tmp_path)
    assert mod.bootstrap(tmp_path, apply=True)["reconstructed"] == 1
    private_policy(tmp_path)
    put(tmp_path, "state/workshop/proposals/lot/file.txt:Zone.Identifier", "sidecar")
    with pytest.raises(ValueError, match="WINDOWS_INCOMPATIBLE_HANDOFF_PATH"):
        mod.private_handoff(tmp_path, write=False)


def test_private_handoff_rejects_changed_source_and_public_target(tmp_path):
    synthetic_seed(tmp_path)
    mod.bootstrap(tmp_path, apply=True)
    policy = private_policy(tmp_path)
    (tmp_path / "sources/synthetic original.txt").write_text("changed\n")
    with pytest.raises(ValueError, match="SOURCE_FILE_HASH_MISMATCH"):
        mod.private_handoff(tmp_path, write=False)
    (tmp_path / "sources/synthetic original.txt").write_text("Synthetic fixture control.\n")
    policy["target"]["visibility"] = "public"
    json_put(tmp_path, "config/private-handoff-policy.json", policy)
    with pytest.raises(ValueError, match="INVALID_PRIVATE_HANDOFF_POLICY"):
        mod.private_handoff(tmp_path, write=False)
