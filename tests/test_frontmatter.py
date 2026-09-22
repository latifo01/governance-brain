from __future__ import annotations

from pathlib import Path

import jsonschema
import pytest

from gov360_brain.vault.frontmatter import (
    FrontmatterError,
    FrontmatterParseError,
    FrontmatterValidationError,
    canonicalize_frontmatter,
    normalize_note,
    normalize_note_file,
    parse_note,
    read_note,
    render_frontmatter,
    render_note,
    validate_frontmatter,
    validation_errors,
    write_note,
)


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "config" / "schemas" / "vault-frontmatter.schema.json"
HASH = "a" * 64


def test_public_frontmatter_schema_is_valid() -> None:
    schema = __import__("json").loads(SCHEMA.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)


def test_legacy_source_fields_are_mirrored_to_stable_graph_identity() -> None:
    value = canonicalize_frontmatter(
        {
            "type": "source",
            "schema_version": 1,
            "source_id": "SRC-0001",
            "source_sha256": HASH,
            "status": "VERIFIED",
            "domains": ["MODEL_RISK", "MODEL_RISK"],
            "aliases": ["Risk policy", "Risk policy"],
        }
    )
    assert value["stable_id"] == "SRC-0001"
    assert value["source_id"] == "SRC-0001"
    assert value["domains"] == ["MODEL_RISK"]
    assert value["aliases"] == ["Risk policy"]
    assert value["provenance"] == {"source_id": "SRC-0001", "source_sha256": HASH}
    validate_frontmatter(value)


def test_questionnaire_keeps_singular_domain_and_structured_evidence() -> None:
    value = {
        "type": "questionnaire_question",
        "schema_version": 1,
        "question_id": "FIN_001",
        "revision": 1,
        "domain": "FINANCE",
        "topic": "approval",
        "response_type": "BOOLEAN",
        "applies_if": {},
        "depends_on": {},
        "question_en": "Is the control approved?",
        "question_fr": "Le contrôle est-il approuvé ?",
        "evidence_refs": [
            {"source_id": "SRC-0002", "source_sha256": HASH, "locator": "Page 2", "verification_status": "VERIFIED"}
        ],
        "status": "PROPOSED",
    }
    rendered = render_note(value, "# FIN_001\n")
    parsed = parse_note(rendered)
    assert parsed.stable_id == "FIN_001"
    assert parsed.metadata["question_id"] == "FIN_001"
    assert parsed.domains == ("FINANCE",)
    assert parsed.body.strip() == "# FIN_001"
    assert "evidence_refs:" in rendered
    assert rendered == render_note(parsed)


def test_render_is_deterministic_and_write_is_atomic_friendly(tmp_path: Path) -> None:
    value = {
        "type": "concept",
        "schema_version": 1,
        "stable_id": "CON-ABC123",
        "title": "Control",
        "aliases": ["Z alias", "A alias"],
        "domains": ["Z_DOMAIN", "A_DOMAIN"],
        "status": "PUBLISHED",
        "evidence_refs": ["EVIDENCE-2", "EVIDENCE-1"],
        "relations": [
            {"relation_type": "related_to", "target_id": "CON-Z"},
            {"relation_type": "defines", "target_id": "RULE-1"},
        ],
        "provenance": {"derived_from": ["EVIDENCE-1"]},
    }
    first = render_frontmatter(value)
    second = render_frontmatter(value)
    assert first == second
    assert first.index("stable_id:") < first.index("aliases:") < first.index("domains:")
    path = tmp_path / "brain wiki" / "20_Concepts" / "CON-ABC123.md"
    assert write_note(path, value, "# Control") == path
    assert read_note(path).stable_id == "CON-ABC123"


def test_system_and_legacy_audit_notes_can_be_read_without_business_fields(tmp_path: Path) -> None:
    system_path = tmp_path / "brain wiki" / "00_System" / "Home.md"
    system_path.parent.mkdir(parents=True)
    system_path.write_text("# Home\n", encoding="utf-8")
    audit_path = tmp_path / "brain wiki" / "90_Audit" / "Vault_Audit.md"
    audit_path.parent.mkdir(parents=True)
    audit_path.write_text("# Vault Audit\n", encoding="utf-8")
    assert read_note(system_path).note_type == "system"
    assert read_note(audit_path).note_type == "audit"
    assert read_note(audit_path).stable_id is None
    normalize_note_file(audit_path)
    assert read_note(audit_path).note_type == "audit"
    assert read_note(audit_path).body.strip() == "# Vault Audit"


def test_normalization_migrates_frontmatter_and_preserves_body(tmp_path: Path) -> None:
    body = "# Legacy\n\nA paragraph with [[a-link]].\n"
    legacy = "---\ntype: concept\nschema_version: 1\nstable_id: CON-LEGACY\n---\n" + body
    migrated = normalize_note(legacy)
    assert parse_note(migrated).body == body

    path = tmp_path / "CON-LEGACY.md"
    path.write_text(legacy, encoding="utf-8")
    normalize_note_file(path)
    assert read_note(path).body == body


def test_invalid_graph_note_identity_and_bad_relation_are_reported() -> None:
    missing_identity = {"type": "concept", "schema_version": 1, "title": "No ID"}
    errors = validation_errors(missing_identity)
    assert any("stable_id" in error for error in errors)
    with pytest.raises(FrontmatterValidationError):
        validate_frontmatter(missing_identity)

    bad_relation = canonicalize_frontmatter(
        {
            "type": "map",
            "schema_version": 1,
            "stable_id": "MAP-1",
            "relations": [{"relation_type": "invented", "target_id": "CON-1"}],
        }
    )
    assert any("relation_type" in error for error in validation_errors(bad_relation))

    inconsistent_source = canonicalize_frontmatter(
        {"type": "source", "source_id": "SRC-0001", "stable_id": "SRC-0002", "source_sha256": HASH}
    )
    assert any("must match source_id" in error for error in validation_errors(inconsistent_source))


def test_note_writers_refuse_repository_sources() -> None:
    # The project source root is immutable even when a caller requests a
    # perfectly valid note payload.  Use the real root only when it exists.
    source = ROOT / "sources" / ".frontmatter-test.md"
    with pytest.raises(FrontmatterError):
        write_note(source, {"type": "system"}, "# no")


def test_malformed_yaml_is_not_silently_downgraded() -> None:
    with pytest.raises(FrontmatterParseError):
        parse_note("---\ntype: [broken\n---\n# Note\n", note_type="audit")
