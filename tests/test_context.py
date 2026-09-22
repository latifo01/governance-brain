from __future__ import annotations

import json
from pathlib import Path

from gov360_brain.context import ContextBuilder
from gov360_brain.project import ProjectPaths
from gov360_brain.utils import frontmatter, sha256_file, sha256_text, write_jsonl


def _write_ingest_unit(paths: ProjectPaths, *, source_id: str = "SRC-0001", body: str = "Retention controls apply to personal data.") -> dict[str, str]:
    source_sha256 = "a" * 64
    content_sha256 = sha256_text(body.rstrip() + "\n")
    metadata = {
        "type": "ingested_unit",
        "schema_version": 1,
        "source_id": source_id,
        "source_sha256": source_sha256,
        "source_format": "md",
        "adapter_id": "text",
        "adapter_version": "1.0.0",
        "locator_kind": "section",
        "locator": "Section 1",
        "content_sha256": content_sha256,
        "extraction_mode": "native",
        "visual_review": "NONE",
        "warnings": [],
    }
    unit_text = frontmatter(metadata) + body.rstrip() + "\n"
    source_dir = paths.ingest / source_id / "units"
    source_dir.mkdir(parents=True, exist_ok=True)
    unit_path = source_dir / "section-0001.md"
    unit_path.write_text(unit_text, encoding="utf-8")
    document = {
        "schema_version": 1,
        "source_id": source_id,
        "source_sha256": source_sha256,
        "relative_source_paths": [f"sources/data/{source_id}.md"],
        "domains": ["DATA_PRIVACY"],
        "source_format": "md",
        "source_kind": "document",
        "adapter_id": "text",
        "adapter_version": "1.0.0",
        "inventory": {"unit_count": 1, "native_unit_count": 1, "normalized_unit_count": 1, "metadata": {}, "warnings": []},
        "units": [{
            "index": 1,
            "filename": "units/section-0001.md",
            "locator_kind": "section",
            "locator": "Section 1",
            "content_sha256": content_sha256,
            "file_sha256": sha256_file(unit_path),
            "visual_review": "NONE",
            "warnings": [],
        }],
        "validation": {"valid": True, "warnings": [], "metrics": {}},
        "warnings": [],
    }
    (paths.ingest / source_id / "document.json").write_text(json.dumps(document), encoding="utf-8")
    return {"source_id": source_id, "source_sha256": source_sha256, "locator": "Section 1", "content_sha256": content_sha256}


def _write_manifest(paths: ProjectPaths, unit: dict[str, str], **extra: object) -> None:
    row = {
        "schema_version": 1,
        "source_id": unit["source_id"],
        "source_sha256": unit["source_sha256"],
        "relative_paths": [f"sources/data/{unit['source_id']}.md"],
        "source_format": "md",
        "source_kind": "document",
        "primary_domain": "DATA_PRIVACY",
        "domains": ["DATA_PRIVACY"],
        "status": "READY_FOR_LLM",
        "adapter_id": "text",
        "adapter_version": "1.0.0",
        "unit_count": 1,
        **extra,
    }
    write_jsonl(paths.state / "source_manifest.jsonl", [row])


def test_context_builder_links_verified_knowledge_and_is_deterministic(tmp_path: Path) -> None:
    paths = ProjectPaths(tmp_path)
    paths.ensure_layout()
    unit = _write_ingest_unit(paths)
    _write_manifest(paths, unit, normativity="BINDING")
    write_jsonl(paths.state / "evidence_registry.jsonl", [{
        "schema_version": 1,
        "evidence_ref": "EVID-1",
        "source_id": unit["source_id"],
        "source_sha256": unit["source_sha256"],
        "locator": unit["locator"],
        "unit_content_sha256": unit["content_sha256"],
        "claim": "Retention must be limited to the documented purpose.",
        "evidence_kind": "requirement",
        "normativity": "BINDING",
        "status": "VERIFIED",
        "domains": ["DATA_PRIVACY"],
    }])
    write_jsonl(paths.state / "knowledge_registry.jsonl", [{
        "schema_version": 1,
        "stable_id": "KNOW-RETENTION",
        "artifact_type": "RULE",
        "title": "Data retention",
        "statement": "Retention must be limited to the documented purpose.",
        "modality": "obligation",
        "evidence_refs": ["EVID-1"],
        "affected_domains": ["DATA_PRIVACY"],
        "status": "PUBLISHED",
        "valid_from": "2024-01-01",
        "valid_to": "2026-12-31",
        "release_id": "REL-1",
    }])

    builder = ContextBuilder(paths)
    request = {
        "query": "data retention",
        "project_context": {"domain": "DATA_PRIVACY", "reference_date": "2025-06-01"},
        "access_scope": {"allowed_domains": ["DATA_PRIVACY"]},
        "release_id": "REL-1",
        "token_budget": 256,
    }
    first = builder.build_context(**request)
    second = builder.build_context(**request)

    assert first == second
    assert first["items"][0]["item_id"] == "KNOW-RETENTION"
    assert first["items"][0]["evidence_level"] == "REVIEWED_WITH_VERIFIED_EVIDENCE"
    assert first["items"][0]["authority"] == "BINDING"
    assert first["citations"][0]["ingest_path"].startswith("ingest/")
    assert first["selection"]["estimated_tokens"] <= first["selection"]["token_budget"]
    assert not any(item["reason"] == "AUTHORITY_INVALID" for item in first["exclusions"])


def test_context_builder_filters_access_and_date_without_opening_sources(tmp_path: Path) -> None:
    paths = ProjectPaths(tmp_path)
    paths.ensure_layout()
    unit = _write_ingest_unit(paths, body="The control applies to model validation.")
    _write_manifest(paths, unit, classification="CONFIDENTIAL", valid_to="2023-12-31")
    write_jsonl(paths.state / "evidence_registry.jsonl", [{
        "schema_version": 1,
        "evidence_ref": "EVID-OLD",
        "source_id": unit["source_id"],
        "source_sha256": unit["source_sha256"],
        "locator": unit["locator"],
        "unit_content_sha256": unit["content_sha256"],
        "claim": "The control applies to model validation.",
        "normativity": "GUIDANCE",
        "status": "VERIFIED",
        "domains": ["DATA_PRIVACY"],
    }])

    packet = ContextBuilder(paths).build_context(
        "model validation",
        {"domain": "DATA_PRIVACY", "reference_date": "2025-01-01"},
        {"allowed_classifications": ["PUBLIC"]},
        "CURRENT",
        128,
    )
    assert packet["items"] == []
    reasons = {item["reason"] for item in packet["exclusions"]}
    assert "ACCESS_SCOPE" in reasons
    assert "OUT_OF_DATE" in reasons or "ACCESS_SCOPE" in reasons
    assert any(gap["code"] == "NO_MATCH" for gap in packet["gaps"])
    assert not (paths.root / "sources" / "data").exists()


def test_context_builder_can_expose_validated_unit_as_unverified_fallback(tmp_path: Path) -> None:
    paths = ProjectPaths(tmp_path)
    paths.ensure_layout()
    unit = _write_ingest_unit(paths, body="A local retention procedure is documented here.")
    _write_manifest(paths, unit)
    packet = ContextBuilder(paths).build_context("retention procedure", {"domain": "DATA_PRIVACY"}, {}, "CURRENT", 128)

    assert len(packet["items"]) == 1
    assert packet["items"][0]["kind"] == "UNIT"
    assert packet["items"][0]["evidence_level"] == "UNVERIFIED_SOURCE_TEXT"
    assert any(gap["code"] == "NO_REVIEWED_KNOWLEDGE" for gap in packet["gaps"])
    assert len(packet["citations"]) == 1


def test_context_builder_rejects_metadata_tampering_even_when_body_hash_matches(tmp_path: Path) -> None:
    paths = ProjectPaths(tmp_path)
    paths.ensure_layout()
    unit = _write_ingest_unit(paths)
    _write_manifest(paths, unit)
    unit_path = paths.ingest / unit["source_id"] / "units" / "section-0001.md"
    unit_path.write_text(unit_path.read_text(encoding="utf-8").replace('visual_review: "NONE"', 'visual_review: "REVIEWED"'), encoding="utf-8")
    packet = ContextBuilder(paths).build_context("retention procedure", {"domain": "DATA_PRIVACY"}, {}, "CURRENT", 128)
    assert packet["items"] == []
    assert any(item["reason"] == "INVALID_INGEST" for item in packet["exclusions"])


def test_context_builder_prefers_active_derived_question_registry(tmp_path: Path) -> None:
    paths = ProjectPaths(tmp_path)
    paths.ensure_layout()
    write_jsonl(paths.state / "derived/question-registry.jsonl", [{
        "schema_version": 2,
        "question_id": "core-001-business-purpose",
        "title": "Business purpose",
        "status": "active",
        "domains": ["AI", "PROCESS"],
        "topic": "business-purpose",
        "question_en": "What business purpose does the AI system serve?",
        "question_fr": "Quel objectif métier le système d'IA sert-il ?",
        "evidence_sources": [],
    }])
    write_jsonl(paths.state / "question_registry.jsonl", [{
        "question_id": "LEGACY_001", "status": "PUBLISHED",
        "domain": "AI", "topic": "legacy",
        "question_en": "Legacy question?", "question_fr": "Question historique ?",
    }])

    ids = {item.item_id for item in ContextBuilder(paths)._load_questions()}
    assert "core-001-business-purpose" in ids
    assert "LEGACY_001" not in ids
