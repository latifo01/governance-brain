from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

import yaml
import pytest

from gov360_brain.adapters import get_default_registry
from gov360_brain.cli import _rebuild_vault_index
from gov360_brain.domains import DomainManager
from gov360_brain.orchestration.ingestion import IngestionOrchestrator
from gov360_brain.orchestration.pipeline import KnowledgePipeline
from gov360_brain.orchestration.approval import ApprovalManager
from gov360_brain.orchestration.state import RunJournal
from gov360_brain.project import ProjectPaths
from gov360_brain.utils import read_jsonl, sha256_file
from gov360_brain.vault import VaultAuditor


class FakeLLM:
    def __init__(self) -> None:
        self.calls = 0

    def generate(self, messages, response_schema, images=None, idempotency_key=None):
        self.calls += 1
        props = response_schema["properties"]
        if "coverage" in props:
            return {"coverage": ["Lines 1-2"], "evidence_candidates": [{"candidate_id": "C1", "claim": "An organization documents its control.", "evidence_kind": "control", "normativity_candidate": "control", "visual_dependency": False}], "warnings": []}
        if "verdicts" in props:
            return {"verdicts": [{"candidate_id": "C1", "status": "VERIFIED", "reason_code": "SUPPORTED"}], "warnings": []}
        if "changes" in props:
            user = json.loads(messages[-1]["content"])
            ref = user["verified_evidence"][0]["evidence_ref"]
            return {"changes": [{"change_type": "ADD", "artifact_type": "CONCEPT", "title": "Control documentation", "statement": "Control documentation records how a control operates.", "modality": "control", "evidence_refs": [ref], "affected_domains": ["FINANCE"]}], "taxonomy_proposals": [], "conflicts": [], "warnings": []}
        user = json.loads(messages[-1]["content"])
        ref = user["verified_evidence"][0]["evidence_ref"]
        return {"questions": [{"intent_key": "document-control", "topic": "Controls", "response_type": "BOOLEAN", "applies_if": {}, "depends_on": {}, "question_en": "Is the control documented?", "question_fr": "Le contrôle est-il documenté ?", "evidence_ref_ids": [ref]}], "warnings": []}


def project(tmp_path: Path) -> tuple[ProjectPaths, Any]:
    paths = ProjectPaths(tmp_path)
    (tmp_path / "pyproject.toml").write_text("[project]\nname='test'\nversion='0'\n", encoding="utf-8")
    paths.ensure_layout()
    schema_source_dir = Path(__file__).resolve().parents[1] / "config" / "schemas"
    schema_target_dir = tmp_path / "config" / "schemas"
    schema_target_dir.mkdir(parents=True)
    for schema_source in schema_source_dir.glob("*.json"):
        shutil.copy2(schema_source, schema_target_dir / schema_source.name)
    template = {
        "schema_version": 1,
        "domain_id": "FINANCE",
        "slug": "finance",
        "status": "ACTIVE",
        "labels": {"en": "Finance", "fr": "Finance"},
        "description": "Finance controls.",
        "question_prefix": "FIN",
        "languages": ["en", "fr"],
        "source_roots": ["sources/finance"],
        "review_policy": "HUMAN_APPROVAL",
    }
    domain_file = tmp_path / "domain_packs" / "finance" / "domain.yaml"
    domain_file.parent.mkdir(parents=True)
    domain_file.write_text(yaml.safe_dump(template, sort_keys=False), encoding="utf-8")
    source = tmp_path / "sources" / "finance" / "policy.txt"
    source.parent.mkdir(parents=True)
    source.write_text("The organization documents its control.\n", encoding="utf-8")
    pack = DomainManager(paths).load("finance")
    return paths, pack


def test_parallel_ingest_is_idempotent_and_llm_cache_skips_unchanged_input(tmp_path: Path) -> None:
    paths, pack = project(tmp_path)
    source = tmp_path / "sources" / "finance" / "policy.txt"
    original_hash = sha256_file(source)
    ingestion = IngestionOrchestrator(paths, get_default_registry(), light_workers=2)
    rows = ingestion.inventory(pack)
    first = ingestion.ingest(pack, rows, profile="no-llm")
    assert first[0]["status"] == "NORMALIZED"
    rows = [row for row in read_jsonl(paths.state / "source_manifest.jsonl") if pack.domain_id in row["domains"]]
    second = ingestion.ingest(pack, rows, profile="no-llm")
    assert second[0]["status"] == "NOOP"
    assert sha256_file(source) == original_hash

    fake = FakeLLM()
    journal = RunJournal.create(paths, domain_id=pack.domain_id, profile="strict-local")
    summary = KnowledgePipeline(paths, fake, workers=2).run(pack, rows, journal)
    journal.finish("REVIEW_REQUIRED", **summary)
    assert fake.calls == 4
    assert summary["question_count"] == 1

    approved_knowledge = ApprovalManager(paths).approve("finance", "knowledge", run_id=journal.run_id)
    assert approved_knowledge["published_count"] >= 1
    approved_questions = ApprovalManager(paths).approve("finance", "questionnaires", run_id=journal.run_id)
    assert approved_questions["published_count"] == 1
    assert VaultAuditor(paths).run("FINANCE")["status"] == "READY_FOR_HUMAN_APPROVAL"

    refreshed = [row for row in read_jsonl(paths.state / "source_manifest.jsonl") if pack.domain_id in row["domains"]]
    cached_client = FakeLLM()
    journal2 = RunJournal.create(paths, domain_id=pack.domain_id, profile="strict-local")
    cached = KnowledgePipeline(paths, cached_client, workers=2).run(pack, refreshed, journal2)
    assert cached["no_op"] is True
    assert cached_client.calls == 0


def test_llm_worker_rechecks_validated_unit_hash_before_reading(tmp_path: Path) -> None:
    paths, pack = project(tmp_path)
    ingestion = IngestionOrchestrator(paths, get_default_registry(), light_workers=1)
    discovered = ingestion.inventory(pack)
    ingestion.ingest(pack, discovered, profile="no-llm")
    rows = [row for row in read_jsonl(paths.state / "source_manifest.jsonl") if pack.domain_id in row["domains"]]
    document = json.loads((paths.ingest / rows[0]["source_id"] / "document.json").read_text(encoding="utf-8"))
    unit = document["units"][0]
    unit_path = paths.ingest / rows[0]["source_id"] / unit["filename"]
    unit_path.write_text(unit_path.read_text(encoding="utf-8") + "\nTampered after validation.\n", encoding="utf-8")
    fake = FakeLLM()
    journal = RunJournal.create(paths, domain_id=pack.domain_id, profile="strict-local")
    with pytest.raises(ValueError, match="hash changed"):
        KnowledgePipeline(paths, fake)._one_unit(pack, rows[0], document, unit, journal)
    assert fake.calls == 0


def test_registry_rebuild_does_not_project_legacy_notes_into_current_vault(tmp_path: Path) -> None:
    paths, _ = project(tmp_path)
    (paths.vault / "SCHEMA.md").write_text("current Markdown contract\n", encoding="utf-8")

    rows = DomainManager(paths).rebuild_registry()

    assert [row["domain_id"] for row in rows] == ["FINANCE"]
    assert not (paths.vault / "30_Domains").exists()


def test_ingestion_does_not_run_legacy_indexer_on_current_vault(tmp_path: Path) -> None:
    paths, _ = project(tmp_path)
    (paths.vault / "SCHEMA.md").write_text("current Markdown contract\n", encoding="utf-8")

    assert _rebuild_vault_index(paths) is False
    assert not (paths.vault / "00_System").exists()
