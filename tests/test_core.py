from pathlib import Path
from types import SimpleNamespace
from gov360_brain.orchestration.state import SourceCatalog

import pytest

from gov360_brain.project import ProjectPaths
from gov360_brain.utils import (
    atomic_write_json,
    ensure_within,
    escape_markdown_cell,
    read_jsonl,
    sha256_file,
    write_jsonl,
)


def test_atomic_json_and_jsonl_are_deterministic(tmp_path: Path) -> None:
    json_path = tmp_path / "nested" / "item.json"
    atomic_write_json(json_path, {"b": 2, "a": 1})
    assert json_path.read_text(encoding="utf-8") == '{\n  "a": 1,\n  "b": 2\n}\n'

    jsonl_path = tmp_path / "state.jsonl"
    write_jsonl(jsonl_path, [{"b": 2, "a": 1}, {"id": "two"}])
    first = jsonl_path.read_bytes()
    write_jsonl(jsonl_path, [{"b": 2, "a": 1}, {"id": "two"}])
    assert jsonl_path.read_bytes() == first
    assert read_jsonl(jsonl_path)[0] == {"a": 1, "b": 2}


def test_markdown_cells_neutralize_active_prefixes() -> None:
    assert escape_markdown_cell("=cmd|value\nnext") == "`=cmd\\|value<br>next`"
    assert escape_markdown_cell("plain") == "plain"


def test_ensure_within_rejects_path_escape(tmp_path: Path) -> None:
    root = tmp_path / "project"
    root.mkdir()
    assert ensure_within(root, root / "state") == (root / "state").resolve()
    with pytest.raises(ValueError):
        ensure_within(root, tmp_path / "outside")


def test_source_hash_changes_only_when_source_changes(tmp_path: Path) -> None:
    source = tmp_path / "source.txt"
    source.write_text("immutable", encoding="utf-8")
    before = sha256_file(source)
    source.read_text(encoding="utf-8")
    assert sha256_file(source) == before


def test_source_inventory_ignores_windows_zone_identifier_sidecars(tmp_path: Path) -> None:
    paths = ProjectPaths(tmp_path)
    paths.ensure_layout()
    source_root = paths.sources / "legal"
    source_root.mkdir()
    (source_root / "regulation.pdf:Zone.Identifier").write_text(
        "[ZoneTransfer]\nZoneId=3\n", encoding="utf-8"
    )
    pack = SimpleNamespace(source_roots=("sources/legal",), domain_id="LEGAL_REGULATORY")

    assert SourceCatalog(paths).discover(pack, object()) == []
    assert read_jsonl(paths.state / "source_manifest.jsonl") == []


def test_project_discovery(tmp_path: Path) -> None:
    (tmp_path / "pyproject.toml").write_text("[project]\nname='x'\n", encoding="utf-8")
    nested = tmp_path / "a" / "b"
    nested.mkdir(parents=True)
    assert ProjectPaths.discover(nested).root == tmp_path.resolve()


def test_source_classification_is_explicit_and_does_not_touch_original(tmp_path: Path) -> None:
    paths = ProjectPaths(tmp_path)
    paths.ensure_layout()
    source = paths.sources / "policy.txt"
    source.write_text("local source", encoding="utf-8")
    digest = sha256_file(source)
    write_jsonl(paths.state / "source_manifest.jsonl", [{
        "schema_version": 1,
        "source_id": "SRC-0001",
        "source_sha256": digest,
        "relative_paths": ["sources/policy.txt"],
        "source_format": "txt",
        "source_kind": "document",
        "primary_domain": "FINANCE",
        "domains": ["FINANCE"],
        "status": "READY_FOR_LLM",
    }])
    result = SourceCatalog(paths).classify("SRC-0001", normativity="GUIDANCE", reviewer="cdo-1")
    assert result["normativity"] == "GUIDANCE"
    assert sha256_file(source) == digest
    assert read_jsonl(paths.state / "source_classification_events.jsonl")[0]["reviewer"] == "cdo-1"
