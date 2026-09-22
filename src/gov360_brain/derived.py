"""Deterministic question registry and Obsidian Canvas generation."""
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

import yaml

from .utils import atomic_write_text, canonical_json, sha256_file, sha256_text


REGISTRY_PATH = Path("state/derived/question-registry.jsonl")
CANVAS_PATH = Path("brain wiki/Risk analysis questionnaire.canvas")
ATLAS_CATALOG_PATH = Path("state/derived/atlas-catalog.jsonl")
ATLAS_MANIFEST_PATH = Path("state/derived/atlas-catalog-manifest.json")
_PALETTE = ("4", "5", "2", "3", "6", "1")


def atlas_catalog(root: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Build a stable, provenance-preserving catalogue from an ingested STIX source.

    Only the validated /objects Markdown unit is read. Original source paths
    remain provenance metadata and are never opened by this transformation.
    """
    root = root.resolve()
    from .brain.ingest_reader import source_document, structured_json, validated_unit
    source, document = source_document(root, "SRC-0046")
    source_id = document.get("source_id")
    source_hash = document.get("source_sha256")
    if source_id != "SRC-0046" or not isinstance(source_hash, str):
        raise ValueError("SRC-0046 document has invalid identity or source hash")
    source_rel = document.get("relative_source_paths", [None])[0]
    units = [item for item in document['units'] if item.get('locator') == '/objects']
    if len(units) != 1:
        raise ValueError("SRC-0046 object unit is missing or ambiguous")
    unit = units[0]
    normalized = validated_unit(root, source, document, unit['filename'])
    if normalized['metadata'].get('non_exhaustive'):
        raise ValueError("SRC-0046 object unit is non-exhaustive")
    objects = structured_json(normalized)
    if not isinstance(objects, list) or any(not isinstance(obj, dict) for obj in objects):
        raise ValueError("SRC-0046 objects must be an array of records")
    selected_types = {"attack-pattern", "course-of-action", "campaign"}
    object_rows: list[dict[str, Any]] = []
    by_stix: dict[str, str] = {}
    for obj in objects:
        if obj.get("type") not in selected_types:
            continue
        ext = next((ref for ref in obj.get("external_references", [])
                    if ref.get("source_name") == "mitre-atlas" and ref.get("external_id")), None)
        if not ext:
            continue
        external_id = str(ext["external_id"])
        kind = {"attack-pattern": "technique", "course-of-action": "mitigation", "campaign": "case-study"}[obj["type"]]
        row = {"record_type": "object", "kind": kind, "external_id": external_id,
               "stix_id": obj.get("id"), "name": obj.get("name", ""),
               "description": obj.get("description", ""), "url": ext.get("url"),
               "created": obj.get("created"), "modified": obj.get("modified"),
               "platforms": obj.get("x_mitre_platforms", []),
               "source_id": source_id, "source_sha256": source_hash,
               "locator": unit.get("locator"), "unit_sha256": unit.get("content_sha256")}
        object_rows.append(row)
        by_stix[str(obj.get("id"))] = external_id
    for obj in objects:
        if obj.get("type") != "relationship" or obj.get("source_ref") not in by_stix or obj.get("target_ref") not in by_stix:
            continue
        object_rows.append({"record_type": "relation", "kind": obj.get("relationship_type", "related-to"),
                            "source": by_stix[obj["source_ref"]], "target": by_stix[obj["target_ref"]],
                            "stix_id": obj.get("id"), "source_id": source_id, "source_sha256": source_hash,
                            "locator": unit.get("locator"), "unit_sha256": unit.get("content_sha256")})
    object_rows.sort(key=lambda row: (row["record_type"], row.get("external_id", ""), row.get("source", ""), row.get("target", ""), row.get("stix_id", "")))
    return object_rows, {"schema_version": 2, "source_id": source_id, "source_sha256": source_hash,
                         "input_kind": "validated_markdown",
                         "unit_path": normalized['path'],
                         "unit_file_sha256": unit['file_sha256'],
                         "text_encoding": "decoded_normalized_json_quotes",
                         "limitations": ["Legacy normalized HTML angle-bracket entities are not distinguishable from original literal entities."],
                         "source_path": source_rel, "unit_locator": unit.get("locator"),
                         "unit_sha256": unit.get("content_sha256"), "record_count": len(object_rows),
                         "object_count": sum(r["record_type"] == "object" for r in object_rows),
                         "relation_count": sum(r["record_type"] == "relation" for r in object_rows)}


def build_atlas_catalog(root: Path, *, write: bool = True) -> dict[str, Any]:
    rows, manifest = atlas_catalog(root)
    catalog_text = "".join(canonical_json(row) + "\n" for row in rows)
    manifest = {**manifest, "catalog_sha256": sha256_text(catalog_text)}
    outputs = {root.resolve() / ATLAS_CATALOG_PATH: catalog_text,
               root.resolve() / ATLAS_MANIFEST_PATH: json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"}
    changed = [p for p, content in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != content]
    if write:
        for path in changed:
            atomic_write_text(path, outputs[path])
    return {"valid": True, "current": not changed, "written": len(changed) if write else 0, **manifest,
            "changed_paths": [p.relative_to(root.resolve()).as_posix() for p in changed]}


def _frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"Missing frontmatter: {path}")
    try:
        raw = text.split("---\n", 2)[1]
        value = yaml.safe_load(raw) or {}
    except (IndexError, yaml.YAMLError) as exc:
        raise ValueError(f"Invalid frontmatter: {path}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"Frontmatter object expected: {path}")
    return value


def question_records(root: Path) -> list[dict[str, Any]]:
    """Read active canonical questions and return a stable derived registry."""
    root = root.resolve()
    vault = root / "brain wiki"
    question_root = vault / "questions"
    records: list[dict[str, Any]] = []
    seen: set[str] = set()
    for path in sorted(question_root.rglob("*.md")):
        meta = _frontmatter(path)
        if meta.get("type") != "question" or meta.get("status") != "active":
            continue
        question_id = str(meta.get("id", ""))
        if not question_id or question_id in seen:
            raise ValueError(f"Duplicate or empty question ID: {question_id or path.name}")
        seen.add(question_id)
        relative = path.relative_to(vault).as_posix()
        parts = path.relative_to(question_root).parts
        module = parts[0] if len(parts) > 1 else "questions"
        record = {
            "schema_version": 2,
            "question_id": question_id,
            "note_path": relative,
            "module": module,
            "title": meta["title"],
            "status": meta["status"],
            "domains": meta["domains"],
            "topic": meta["topic"],
            "priority": meta["priority"],
            "applies_to": meta["applies_to"],
            "answer_type": meta["answer_type"],
            "depends_on": meta["depends_on"],
            "question_fr": meta["question_fr"],
            "question_en": meta["question_en"],
            "options": meta.get("options", []),
            "tags": meta["tags"],
            "evidence_sources": meta["evidence_sources"],
            "content_sha256": sha256_file(path),
        }
        records.append(record)
    records.sort(key=lambda item: item["question_id"])
    return records


def registry_text(records: list[dict[str, Any]]) -> str:
    return "".join(canonical_json(record) + "\n" for record in records)


def _stable_id(kind: str, value: str) -> str:
    return sha256_text(f"{kind}:{value}")[:16]


def _edge_label(value: Any) -> str:
    if value is True:
        return "yes"
    if value is False:
        return "no"
    if value is None:
        return "null"
    return str(value)


def canvas_document(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Create a deterministic Canvas with file nodes grouped by module."""
    by_id = {record["question_id"]: record for record in records}
    for record in records:
        dependency = record["depends_on"]
        if dependency is not None and dependency["question_id"] not in by_id:
            raise ValueError(
                f"Missing dependency {dependency['question_id']} for {record['question_id']}"
            )
    dependencies = {
        record["question_id"]: record["depends_on"]["question_id"]
        for record in records if record["depends_on"] is not None
    }
    for question_id in dependencies:
        seen = {question_id}
        target = dependencies[question_id]
        while target in dependencies:
            if target in seen:
                raise ValueError(f"Dependency cycle involving {question_id}")
            seen.add(target)
            target = dependencies[target]

    modules = sorted({record["module"] for record in records}, key=lambda value: (value != "core", value))
    nodes: list[dict[str, Any]] = [{
        "id": _stable_id("legend", "questionnaire"),
        "type": "text",
        "text": "# Governance questionnaire\n\nGenerated from canonical Markdown questions. Answers are not stored in this Canvas.",
        "x": 0,
        "y": -260,
        "width": 520,
        "height": 150,
        "color": "1",
    }]
    positions: dict[str, tuple[int, int]] = {}
    cursor_x = 0
    for module_index, module in enumerate(modules):
        items = [record for record in records if record["module"] == module]
        columns = min(3, max(1, len(items)))
        rows = (len(items) + columns - 1) // columns
        width = columns * 300 + 80
        height = rows * 160 + 100
        color = _PALETTE[module_index % len(_PALETTE)]
        nodes.append({
            "id": _stable_id("group", module),
            "type": "group",
            "x": cursor_x,
            "y": 0,
            "width": width,
            "height": height,
            "color": color,
            "label": module.replace("-", " ").title(),
        })
        for index, record in enumerate(items):
            x = cursor_x + 40 + (index % columns) * 300
            y = 70 + (index // columns) * 160
            positions[record["question_id"]] = (x, y)
            nodes.append({
                "id": _stable_id("question", record["question_id"]),
                "type": "file",
                "file": record["note_path"],
                "x": x,
                "y": y,
                "width": 260,
                "height": 120,
                "color": color,
            })
        cursor_x += width + 120

    edges: list[dict[str, Any]] = []
    for record in records:
        dependency = record["depends_on"]
        if dependency is None:
            continue
        parent = dependency["question_id"]
        parent_x, _ = positions[parent]
        child_x, _ = positions[record["question_id"]]
        edges.append({
            "id": _stable_id("dependency", f"{parent}:{record['question_id']}:{canonical_json(dependency['equals'])}"),
            "fromNode": _stable_id("question", parent),
            "fromSide": "right" if parent_x <= child_x else "left",
            "toNode": _stable_id("question", record["question_id"]),
            "toSide": "left" if parent_x <= child_x else "right",
            "label": _edge_label(dependency["equals"]),
        })
    edges.sort(key=lambda item: item["id"])
    return {"nodes": nodes, "edges": edges}


def canvas_text(records: list[dict[str, Any]]) -> str:
    return json.dumps(canvas_document(records), ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def build_derived(root: Path, *, write: bool = True) -> dict[str, Any]:
    """Build or check both derived artifacts without invoking an LLM."""
    root = root.resolve()
    registry_path = root / "config" / "brain-domains.json"
    domains = json.loads(registry_path.read_text(encoding="utf-8")) if registry_path.exists() else ["GENERAL"]
    from .workshop import validate
    validation = validate(root / "brain wiki", domains)
    if not validation["valid"]:
        first = validation["errors"][0] if validation["errors"] else {"error": "unknown"}
        raise ValueError(f"Active vault validation failed: {first}")
    records = question_records(root)
    outputs = {
        root / REGISTRY_PATH: registry_text(records),
        root / CANVAS_PATH: canvas_text(records),
    }
    changed = [
        path for path, content in outputs.items()
        if not path.exists() or path.read_text(encoding="utf-8") != content
    ]
    if write and changed:
        previous = {path: path.read_text(encoding="utf-8") if path.exists() else None for path in changed}
        try:
            for path in changed:
                atomic_write_text(path, outputs[path])
        except BaseException:
            for path, content in previous.items():
                if content is None:
                    path.unlink(missing_ok=True)
                else:
                    atomic_write_text(path, content)
            raise
    dependencies = sum(record["depends_on"] is not None for record in records)
    return {
        "valid": True,
        "current": not changed,
        "written": len(changed) if write else 0,
        "questions": len(records),
        "dependencies": dependencies,
        "registry_sha256": sha256_text(outputs[root / REGISTRY_PATH]),
        "canvas_sha256": sha256_text(outputs[root / CANVAS_PATH]),
        "changed_paths": [path.relative_to(root).as_posix() for path in changed],
    }


def _question_fingerprint(root: Path) -> tuple[tuple[str, int, int], ...]:
    question_root = root / "brain wiki" / "questions"
    return tuple(
        (path.relative_to(root).as_posix(), path.stat().st_mtime_ns, path.stat().st_size)
        for path in sorted(question_root.rglob("*.md"))
    )


def watch_derived(root: Path, *, interval: float = 1.0) -> None:
    """Watch canonical question files and rebuild derived artifacts on change."""
    if interval <= 0:
        raise ValueError("Watch interval must be positive")
    root = root.resolve()
    initial = build_derived(root)
    print(json.dumps({"watching": True, **initial}, ensure_ascii=False), flush=True)
    previous = _question_fingerprint(root)
    while True:
        time.sleep(interval)
        current = _question_fingerprint(root)
        if current != previous:
            try:
                result = build_derived(root)
                message = {"watching": True, **result}
            except ValueError as exc:
                message = {"watching": True, "valid": False, "error": str(exc)}
            print(json.dumps(message, ensure_ascii=False), flush=True)
            previous = current
