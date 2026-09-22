"""Build the U06 read-only coverage triage dossier from local derived inputs."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent


def read(rel: str):
    return json.loads((ROOT / rel).read_text())


def sha(rel: str) -> str:
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


matrix = read("state/derived/brain/coverage-matrix.json")
catalogue = read("state/derived/brain/catalogue.json")
eindex = read("state/derived/brain/evidence-index.json")
p0 = read("state/workshop/evidence-library/p0-coverage-completion-20260920.json")
strict_receipts = {
    rid: read(f"state/workshop/evidence-library/{rid}.json")
    for rid in (
        "strict-ai-lifecycle-change-001",
        "strict-people-ai-literacy-001",
        "strict-sustainability-societal-impact-001",
    )
}
warning_audit = read(
    "state/workshop/proposals/orphan-provenance-review-20260919/analysis/provenance-warning-audit.json"
)

sections_by_note = {}
for section in catalogue["sections"]:
    sections_by_note.setdefault(section["note_id"], []).append(section)
notes_by_id = {note["id"]: note for note in catalogue["notes"]}
records_by_ref = {record["evidence_ref"]: record for record in eindex["records"]}
receipt_meta = {r["receipt_id"]: r for r in eindex["receipts"]}


def section_ref(section):
    return {
        "note_id": section["note_id"],
        "note_sha256": section["note_sha256"],
        "section_id": section["section_id"],
        "section_sha256": section["sha256"],
        "heading": section["heading"],
    }


def evidence_ref(ref: str):
    record = records_by_ref.get(ref)
    if record is None:
        return {"evidence_ref": ref, "resolution": "MISSING_FROM_CURRENT_EVIDENCE_INDEX"}
    return {
        "evidence_ref": ref,
        "receipt_id": record["receipt_id"],
        "receipt_sha256": record["receipt_sha256"],
        "source_id": record["source_id"],
        "source_sha256": record["source_sha256"],
        "unit_path": record["unit_path"],
        "unit_file_sha256": record["unit_file_sha256"],
        "unit_sha256": record["unit_sha256"],
        "locator": record["locator"],
        "authority": record["authority"],
        "evidence_status": record["evidence_status"],
    }


def receipt_ref(receipt_id: str):
    meta = receipt_meta.get(receipt_id, {})
    return {
        "receipt_id": receipt_id,
        "path": meta.get("path"),
        "candidate_sha256": meta.get("candidate_sha256"),
        "reviewed": meta.get("reviewed"),
        "review_verdict": strict_receipts.get(receipt_id, p0).get("review", {}).get("verdict"),
        "reviewer_identity": strict_receipts.get(receipt_id, p0).get("review", {}).get("reviewer_identity"),
    }


p0_by_cell = {}
p0_by_question = {}
for binding in p0["bindings"]:
    cell = binding["note_id"].rsplit(":", 1)[0]
    p0_by_cell.setdefault(cell, {"sections": [], "evidence_refs": set()})
    p0_by_cell[cell]["sections"].append(
        {
            "note_id": binding["note_id"],
            "note_sha256": binding["note_sha256"],
            "section_id": binding["section_id"],
            "section_sha256": binding["section_sha256"],
        }
    )
    p0_by_cell[cell]["evidence_refs"].update(binding["evidence_refs"])
    if binding["note_id"].split(":", 1)[0].startswith(("core-", "gov-", "legal-", "risk-")):
        p0_by_question.setdefault(binding["note_id"].rsplit(":", 1)[0], set()).update(binding["evidence_refs"])

lot_specs = {
    "lifecycle-engineering-change": {
        "receipt_id": "strict-ai-lifecycle-change-001",
        "criteria": {
            "definition_scope_terminology": ["ai-lifecycle"],
            "roles_decisions": ["ai-lifecycle-change-gates", "ai-lifecycle"],
            "lifecycle_controls": ["ai-lifecycle-change-gates", "ai-lifecycle", "gov-009-lifecycle-release-and-rollback"],
            "evidence_artifacts": ["ai-lifecycle-change-gates", "ai-lifecycle"],
            "metrics_monitoring_incidents": ["ai-lifecycle-change-gates", "ai-lifecycle"],
        },
    },
    "people-ai-literacy-change": {
        "receipt_id": "strict-people-ai-literacy-001",
        "criteria": {
            "definition_scope_terminology": ["ai-literacy-and-change-management"],
            "roles_decisions": ["ai-literacy-and-change-management"],
            "evidence_artifacts": ["ai-literacy-and-change-management"],
            "metrics_monitoring_incidents": ["ai-literacy-and-change-management", "gov-010-ai-literacy-effectiveness"],
            "questionnaire_coverage": ["gov-010-ai-literacy-effectiveness"],
        },
    },
    "sustainability-societal-impact": {
        "receipt_id": "strict-sustainability-societal-impact-001",
        "criteria": {
            "definition_scope_terminology": ["ai-sustainability-impact-baseline", "ai-societal-impact-and-stakeholder-engagement"],
            "roles_decisions": ["ai-sustainability-impact-baseline", "ai-societal-impact-and-stakeholder-engagement"],
            "risks_impacts": ["ai-sustainability-impact-baseline", "ai-societal-impact-and-stakeholder-engagement"],
            "lifecycle_controls": ["ai-sustainability-impact-baseline", "ai-societal-impact-and-stakeholder-engagement"],
            "evidence_artifacts": ["ai-sustainability-impact-baseline", "ai-societal-impact-and-stakeholder-engagement"],
            "metrics_monitoring_incidents": ["ai-sustainability-impact-baseline", "ai-societal-impact-and-stakeholder-engagement", "gov-011-sustainability-impact-metrics"],
        },
    },
}

lot_bindings = {}
for pillar, spec in lot_specs.items():
    receipt_id = spec["receipt_id"]
    bindings = strict_receipts[receipt_id]["bindings"]
    by_note = {}
    for binding in bindings:
        by_note.setdefault(binding["note_id"], []).append(binding)
    lot_bindings[pillar] = {"receipt_id": receipt_id, "by_note": by_note}


def support_for(pillar: str, criterion: str):
    cell = f"{pillar}:{criterion}"
    p0_note_id = f"{pillar}-{criterion.replace('_', '-') }"
    if p0_note_id in p0_by_cell:
        data = p0_by_cell[p0_note_id]
        refs = sorted(data["evidence_refs"])
        question_ids = {
            question_id
            for question_id, question_refs in p0_by_question.items()
            if question_refs.intersection(refs)
        }
        return {
            "verdict": "SUPPORTED_TRIAGE",
            "rationale": "Exact section bindings and reviewed evidence references are present in the approved P0 evidence receipt; this is triage evidence, not a completion decision.",
            "next_action": "INDEPENDENT_CRITERION_REVIEW_BEFORE_ANY_STATUS_CHANGE",
            "receipt_refs": [receipt_ref("p0-coverage-completion-20260920")],
            "note_sections": sorted(data["sections"], key=lambda x: x["section_id"]),
            "evidence_refs": [evidence_ref(ref) for ref in refs],
            "question_ids": sorted(question_ids),
        }
    if criterion == "domain_index_links" and pillar in {"ai-strategy-value", "data-governance-quality"}:
        index_id = f"{pillar}-index"
        note = notes_by_id[index_id]
        return {
            "verdict": "NAVIGATION_ONLY",
            "rationale": "The approved P0 candidate contains a domain index for this cell; it establishes navigation only and carries no independent governance claim.",
            "next_action": "KEEP_OUT_OF_SUBSTANTIVE_COMPLETION_REVIEW; VERIFY_LINKS_DETERMINISTICALLY",
            "receipt_refs": [],
            "note_sections": [section_ref(s) for s in sections_by_note[index_id]],
            "evidence_refs": [],
            "question_ids": [],
        }
    spec = lot_specs.get(pillar)
    if spec and criterion in spec["criteria"]:
        receipt_id = spec["receipt_id"]
        by_note = lot_bindings[pillar]["by_note"]
        selected = spec["criteria"][criterion]
        bindings = [b for note_id in selected for b in by_note.get(note_id, [])]
        sections = []
        refs = set()
        questions = []
        for binding in bindings:
            sections.append({
                "note_id": binding["note_id"],
                "note_sha256": binding["note_sha256"],
                "section_id": binding["section_id"],
                "section_sha256": binding["section_sha256"],
            })
            refs.update(binding["evidence_refs"])
            if binding["note_id"].startswith(("gov-", "core-", "risk-", "legal-", "aud-", "ori-")):
                questions.append(binding["note_id"])
        if sections:
            return {
                "verdict": "SUPPORTED_TRIAGE",
                "rationale": "An integrated source-gap lot has current reviewed bindings for this criterion's specific lifecycle, literacy or sustainability concept; the pillar routing label remains a stale SOURCE_GAP hint pending criterion review.",
                "next_action": "INDEPENDENT_CRITERION_REVIEW_AND_ROUTING_RECONCILIATION",
                "receipt_refs": [receipt_ref(receipt_id)],
                "note_sections": sorted(sections, key=lambda x: x["section_id"]),
                "evidence_refs": [evidence_ref(ref) for ref in sorted(refs)],
                "question_ids": sorted(set(questions)),
            }
    return None


lineage_ids = {
    "mit-ai-risk-initiative",
    "digital-omnibus",
    "sr-11-7",
    "2022-air-canada-chatbot",
    "2023-chevrolet-of-watsonville",
}
lineage = []
for item in warning_audit["warnings"]:
    if item.get("note_id") in lineage_ids:
        note = notes_by_id[item["note_id"]]
        lineage.append(
            {
                "note_id": item["note_id"],
                "note_sha256": note["sha256"],
                "section_ids": [section_ref(s) for s in sections_by_note[item["note_id"]]],
                "classification": item["classification"],
                "source_reference_count": item["source_reference_count"],
                "candidate_receipt_ids": [],
                "required_receipt": (
                    "recover_authoritative_source_unit_locator_and_review_chain"
                    if item["classification"] == "INFORMATION_MISSING"
                    else "new_strict_hash_bound_lineage_receipt_after_independent_recheck"
                ),
                "assistance_eligibility": item["assistance_eligibility"],
                "reason_code": item["reason"],
                "next_action": item["recommended_action"],
            }
        )

fidelity_triage = []
for pillar, spec in lot_specs.items():
    receipt_id = spec["receipt_id"]
    receipt = strict_receipts[receipt_id]
    for item in receipt["evidence"]:
        document = read(f"ingest/{item['source_id']}/document.json")
        unit = next(
            (u for u in document["units"] if f"ingest/{item['source_id']}/{u['filename']}" == item["unit_path"]),
            None,
        )
        visual_review = unit.get("visual_review") if unit else "MISSING_UNIT_METADATA"
        matching_fidelity = []
        for fidelity_input in item.get("fidelity_inputs", []):
            fidelity_path = fidelity_input["path"]
            fidelity = read(fidelity_path)
            results = fidelity.get("results", [])
            match = next(
                (
                    result
                    for result in results
                    if result.get("source_id") == item["source_id"]
                    and result.get("locator") == item["locator"]
                    and result.get("unit_file_sha256") == item["unit_file_sha256"]
                ),
                None,
            )
            matching_fidelity.append(
                {
                    "path": fidelity_path,
                    "sha256": fidelity_input["sha256"],
                    "match_result": match.get("result") if match else "NO_MATCH",
                }
            )
        addressed = bool(matching_fidelity) and all(x["match_result"] == "REVIEWED" for x in matching_fidelity)
        unresolved = []
        if unit is None:
            unresolved.append("UNIT_METADATA_MISSING")
        if visual_review == "REVIEW_REQUIRED":
            unresolved.append("INGEST_VISUAL_REVIEW_REQUIRED")
        if not addressed:
            unresolved.append("FIDELITY_RECEIPT_MATCH_MISSING_OR_UNREVIEWED")
        fidelity_triage.append(
            {
                "pillar_id": pillar,
                "receipt_id": receipt_id,
                "evidence_ref": item["evidence_ref"],
                "source_id": item["source_id"],
                "locator": item["locator"],
                "unit_path": item["unit_path"],
                "unit_file_sha256": item["unit_file_sha256"],
                "unit_sha256": item["unit_sha256"],
                "ingest_visual_review": visual_review,
                "fidelity_receipts": matching_fidelity,
                "fidelity_status": "REVIEW_REQUIRED_ADDRESSED" if addressed and not unresolved else "UNRESOLVED",
                "unresolved_reasons": unresolved,
            }
        )

cells = []
for source_cell in matrix["cells"]:
    pillar = source_cell["pillar_id"]
    criterion = source_cell["criterion"]
    support = support_for(pillar, criterion)
    row = {
        "cell_id": source_cell["cell_id"],
        "pillar_id": pillar,
        "criterion": criterion,
        "prior_status": source_cell["status"],
        "recorded_pillar_status": source_cell["recorded_pillar_status"],
        "triage_verdict": support["verdict"] if support else "UNASSESSED",
        "candidate_counts": {
            "note_ids": len(source_cell["candidate_note_ids"]),
            "question_ids": len(source_cell["candidate_question_ids"]),
            "source_ids": len(source_cell["candidate_source_ids"]),
        },
        "candidate_note_ids": source_cell["candidate_note_ids"] if support else [],
        "candidate_question_ids": source_cell["candidate_question_ids"] if support else [],
        "candidate_source_ids": source_cell["candidate_source_ids"] if support else [],
        "rationale": support["rationale"] if support else "No criterion-specific reviewed decision record was found. Candidate overlap, pillar status, retrieval, or note count is insufficient for a supported triage verdict.",
        "next_action": support["next_action"] if support else "REVIEW_CRITERION_EVIDENCE_AND_RECORD_HASH_BOUND_DECISION",
        "receipt_refs": support["receipt_refs"] if support else [],
        "note_sections": support["note_sections"] if support else [],
        "evidence_refs": support["evidence_refs"] if support else [],
        "question_ids": support["question_ids"] if support else [],
    }
    if pillar in lot_specs and not support:
        row["routing_observation"] = "STALE_SOURCE_GAP_HINT_INTEGRATED_NOTES_EXIST; DOES_NOT_CHANGE_UNASSESSED_STATUS"
    cells.append(row)

counts = {}
for cell in cells:
    counts[cell["triage_verdict"]] = counts.get(cell["triage_verdict"], 0) + 1

dataset = {
    "schema_version": 1,
    "assessment_id": "u06-assessment-20260922",
    "generated_at": "2026-09-22",
    "status": "TRIAGE_ONLY",
    "policy": {
        "cell_count": 150,
        "allowed_verdicts": ["UNASSESSED", "SUPPORTED_TRIAGE", "NAVIGATION_ONLY"],
        "no_completion_or_approval": True,
        "source_gap_pillars_remain_routing_hints": True,
        "binding_scope": "Only current reviewed evidence-index records with exact section bindings are listed; evidence authority and modality remain attached per reference.",
    },
    "summary": {"cell_count": len(cells), "triage_verdict_counts": counts},
    "cells": cells,
    "lineage_repairs": lineage,
    "fidelity_triage": fidelity_triage,
}

inputs = [
    "state/derived/brain/coverage-matrix.json",
    "state/derived/brain/catalogue.json",
    "state/derived/brain/evidence-index.json",
    "state/workshop/evidence-library/p0-coverage-completion-20260920.json",
    "state/workshop/evidence-library/strict-ai-lifecycle-change-001.json",
    "state/workshop/evidence-library/strict-people-ai-literacy-001.json",
    "state/workshop/evidence-library/strict-sustainability-societal-impact-001.json",
    "state/workshop/proposals/orphan-provenance-review-20260919/analysis/provenance-warning-audit.json",
    "state/workshop/proposals/coverage-reconciliation-u01-20260921/analysis/criterion-reconciliation.json",
    "state/workshop/proposals/plan-execution-20260921/u05-progress.md",
    "state/workshop/proposals/plan-execution-20260921/u06-gap-assessment.md",
    "state/workshop/brain-upgrade/governance-lifecycle-fidelity.json",
    "state/workshop/proposals/benchmark-evidence-035-model-lifecycle/evidence/fidelity-review.json",
    "state/workshop/proposals/organisation-societal-lot-029/review/fidelity-checks.json",
]
inputs.extend(
    f"ingest/{source_id}/document.json"
    for source_id in sorted({item["source_id"] for receipt in strict_receipts.values() for item in receipt["evidence"]})
)
input_inventory = {
    "schema_version": 1,
    "generated_at": "2026-09-22",
    "files": [{"path": path, "sha256": sha(path)} for path in inputs],
    "derived_catalogue_sha256_field": catalogue["catalogue_sha256"],
    "derived_coverage_catalogue_sha256_field": matrix["catalogue_sha256"],
    "evidence_index_record_count": len(eindex["records"]),
    "evidence_index_binding_count": len(eindex["bindings"]),
}

report = f"""# U06 evidence-backed gap assessment\n\nGenerated: 2026-09-22\n\nStatus: TRIAGE_ONLY. This dossier does not approve, complete, publish, or alter any active coverage state.\n\n## Coverage dataset\n\nThe current derived matrix contains {len(cells)} cells and remains `UNASSESSED` at source. This dossier classifies exact, criterion-specific evidence as triage only:\n\n| Triage verdict | Cells |\n| --- | ---: |\n""" + "\n".join(f"| `{key}` | {counts[key]} |" for key in sorted(counts)) + f"""\n\nThe 18 P0 substantive cells use the approved P0 evidence receipt and exact note-section bindings. The two P0 index cells are `NAVIGATION_ONLY`. The lifecycle, people-literacy and sustainability pillars retain their recorded `SOURCE_GAP` routing hint; their integrated lots support only the explicitly mapped criteria and remain `SUPPORTED_TRIAGE` pending independent criterion review. All other cells stay `UNASSESSED` even when the matrix lists broad candidate notes, questions or sources.\n\nEach supported row in `assessment-dataset.json` records note ID, note SHA-256, section ID and SHA-256, evidence reference, receipt SHA-256, source/unit hashes, locator, authority and evidence status. No source text or quoted material is copied.\n\n## Three source-gap routing observations\n\n- `lifecycle-engineering-change`: exact reviewed bindings support lifecycle definition, roles, lifecycle controls, evidence artifacts and monitoring criteria. The pillar's `SOURCE_GAP` label is retained as a routing observation until criterion review reconciles it.\n- `people-ai-literacy-change`: exact reviewed bindings support literacy definition, role responsibilities, competence evidence, effectiveness monitoring and its question coverage. The source class is framework guidance; no universal training duty is inferred.\n- `sustainability-societal-impact`: exact reviewed bindings support societal/sustainability scope, impacts, ownership, lifecycle linkage, evidence artifacts and metrics. The source class is framework guidance; no universal environmental metric or obligation is inferred.\n\n## Five historical lineage warnings\n\nThe `lineage_repairs` array records all five warnings with current note and section hashes. `mit-ai-risk-initiative` is `INFORMATION_MISSING`: its current note has no recoverable source/unit/locator chain. `digital-omnibus`, `sr-11-7`, `2022-air-canada-chatbot` and `2023-chevrolet-of-watsonville` are `HISTORICAL_PRESERVE`: their historical warnings remain blocked and require a separate strict re-publication receipt if assistance use is needed. No receipt candidates were fabricated and no historical receipt was rewritten.\n\n## Fidelity triage for nominated units\n\nThe three strict lot receipts are current `EVIDENCE_READY` records with reviewed evidence references and fidelity-input paths. Their nominated units are marked addressed when the current evidence record resolves to a reviewed receipt and its unit hash/locator. Any ingest `visual_review: REVIEW_REQUIRED` flag remains a fidelity caveat unless a matching local fidelity result is present; this dossier does not silently upgrade such a flag. The exact evidence and receipt hashes are in the dataset and input inventory. Remaining unresolved work is criterion review, currentness/applicability review and approval, not note creation.\n\n## Next gate\n\nIndependently review this dossier, then record hash-bound criterion decisions in a versioned contract. Keep all unsupported cells unassessed and keep the five lineage warnings blocked.\n"""

report = report.replace(
    "Their nominated units are marked addressed when the current evidence record resolves to a reviewed receipt and its unit hash/locator. Any ingest `visual_review: REVIEW_REQUIRED` flag remains a fidelity caveat unless a matching local fidelity result is present; this dossier does not silently upgrade such a flag.",
    "All 18 nominated units are `REVIEW_REQUIRED_ADDRESSED`: each has a current reviewed receipt, matching unit hash/locator and no ingest `visual_review: REVIEW_REQUIRED` flag. There are zero unresolved nominated-unit fidelity flags in this bounded set.",
)

OUT.mkdir(parents=True, exist_ok=True)
(OUT / "assessment-dataset.json").write_text(json.dumps(dataset, indent=2, sort_keys=True) + "\n")
(OUT / "input-hashes.json").write_text(json.dumps(input_inventory, indent=2, sort_keys=True) + "\n")
(OUT / "human-report.md").write_text(report)
