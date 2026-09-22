from __future__ import annotations

from pathlib import Path

import pytest

from gov360_brain.domains import DomainPack
from gov360_brain.project import ProjectPaths
from gov360_brain.utils import read_jsonl, write_jsonl
from gov360_brain.vault import VaultAuditor, VaultPublisher


def _paths(tmp_path: Path) -> tuple[ProjectPaths, DomainPack]:
    paths = ProjectPaths(tmp_path)
    paths.ensure_layout()
    schema_dir = tmp_path / "config" / "schemas"
    schema_dir.mkdir(parents=True)
    source_schema_dir = Path(__file__).resolve().parents[1] / "config" / "schemas"
    for path in source_schema_dir.glob("*.json"):
        (schema_dir / path.name).write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    pack = DomainPack.from_mapping(
        {
            "schema_version": 1,
            "domain_id": "FINANCE",
            "slug": "finance",
            "status": "ACTIVE",
            "labels": {"en": "Finance", "fr": "Finance"},
            "description": "Finance",
            "question_prefix": "FIN",
            "languages": ["en", "fr"],
            "source_roots": ["sources/finance"],
            "review_policy": "HUMAN_APPROVAL",
        }
    )
    return paths, pack


def _verified_state(paths: ProjectPaths) -> None:
    source_hash = "a" * 64
    write_jsonl(
        paths.state / "evidence_registry.jsonl",
        [
            {
                "schema_version": 1,
                "evidence_ref": "EV-0001",
                "source_id": "SRC-0001",
                "source_sha256": source_hash,
                "locator": "Page 1",
                "unit_content_sha256": "b" * 64,
                "claim": "A documented control is maintained.",
                "evidence_kind": "control",
                "normativity": "control",
                "status": "VERIFIED",
                "reason_code": "SUPPORTED",
                "visual_dependency": False,
                "domains": ["FINANCE"],
            }
        ],
    )


def test_relations_resolve_in_two_passes_and_render_backlinks(tmp_path: Path) -> None:
    paths, pack = _paths(tmp_path)
    _verified_state(paths)
    publisher = VaultPublisher(paths)
    proposal = {
        "changes": [
            {
                "change_type": "ADD",
                "artifact_type": "CONCEPT",
                "stable_id": "CON-0001",
                "title": "Control",
                "statement": "A documented control is maintained.",
                "modality": "control",
                "evidence_refs": ["EV-0001"],
                "affected_domains": ["FINANCE"],
            },
            {
                "change_type": "ADD",
                "artifact_type": "RULE",
                "stable_id": "RULE-0001",
                "title": "Control rule",
                "statement": "The control rule requires documentation.",
                "modality": "control",
                "evidence_refs": ["EV-0001"],
                "affected_domains": ["FINANCE"],
            },
        ],
        "relations": [
            {
                "relation_type": "requires",
                "subject_id": "CON-0001",
                "subject_type": "CONCEPT",
                "target_id": "RULE-0001",
                "target_type": "RULE",
                "evidence_refs": ["EV-0001"],
                "affected_domains": ["FINANCE"],
            }
        ],
    }
    publisher.publish_knowledge(pack, proposal)

    relations = read_jsonl(paths.state / "relations.jsonl")
    assert len(relations) == 1
    relation = relations[0]
    assert relation["status"] == "PUBLISHED"
    assert relation["subject_path"] == "20_Concepts/CON-0001"
    assert relation["target_path"] == "40_Rules/RULE-0001"
    concept = (paths.vault / "20_Concepts" / "CON-0001.md").read_text(encoding="utf-8")
    rule = (paths.vault / "40_Rules" / "RULE-0001.md").read_text(encoding="utf-8")
    assert "[[40_Rules/RULE-0001|RULE-0001]]" in concept
    assert "## Backlinks" in rule
    assert "[[20_Concepts/CON-0001|CON-0001]]" in rule
    metadata = publisher._note_frontmatter(paths.vault / "20_Concepts" / "CON-0001.md")
    assert relation["relation_id"] in {
        str(item.get("relation_id")) for item in metadata.get("relations", [])
    }


def test_missing_relation_target_is_explicit_and_blocks_audit(tmp_path: Path) -> None:
    paths, pack = _paths(tmp_path)
    _verified_state(paths)
    publisher = VaultPublisher(paths)
    publisher.publish_knowledge(
        pack,
        {
            "changes": [
                {
                    "change_type": "ADD",
                    "artifact_type": "CONCEPT",
                    "stable_id": "CON-0002",
                    "title": "Control",
                    "statement": "A documented control is maintained.",
                    "modality": "control",
                    "evidence_refs": ["EV-0001"],
                    "affected_domains": ["FINANCE"],
                }
            ],
            "relations": [
                {
                    "relation_type": "related_to",
                    "subject_id": "CON-0002",
                    "subject_type": "CONCEPT",
                    "target_id": "CON-DOES-NOT-EXIST",
                    "target_type": "CONCEPT",
                    "evidence_refs": ["EV-0001"],
                    "affected_domains": ["FINANCE"],
                }
            ],
        },
    )
    relation = read_jsonl(paths.state / "relations.jsonl")[0]
    assert relation["status"] == "UNRESOLVED"
    assert read_jsonl(paths.state / "unresolved.jsonl")[0]["kind"] == "RELATION_TARGET_UNRESOLVED"
    assert not any("CON-DOES-NOT-EXIST" in path.name for path in paths.vault.rglob("*.md"))
    report = VaultAuditor(paths).run("FINANCE")
    assert report["status"] == "BLOCKED"
    assert any(item["code"] == "UNRESOLVED_RELATION" for item in report["findings"])


def test_relation_vocabulary_and_endpoint_matrix_are_enforced(tmp_path: Path) -> None:
    paths, pack = _paths(tmp_path)
    _verified_state(paths)
    with pytest.raises(ValueError, match="Unsupported relation type"):
        VaultPublisher(paths).publish_relations(
            {
                "relations": [
                    {
                        "relation_type": "equivalent_to",
                        "subject_id": "CON-1",
                        "subject_type": "CONCEPT",
                        "target_id": "RULE-1",
                        "target_type": "RULE",
                        "evidence_refs": ["EV-0001"],
                    }
                ]
            }
        )
    with pytest.raises(ValueError, match="endpoint is not allowed"):
        VaultPublisher(paths).publish_relations(
            {
                "relations": [
                    {
                        "relation_type": "applies_to",
                        "subject_id": "SOURCE-1",
                        "subject_type": "SOURCE",
                        "target_id": "CON-1",
                        "target_type": "CONCEPT",
                        "evidence_refs": ["EV-0001"],
                    }
                ]
            }
        )
