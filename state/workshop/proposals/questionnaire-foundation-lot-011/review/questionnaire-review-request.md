# Questionnaire review assignment

Review `questionnaire-foundation-lot-011` independently. Read only:

- `AGENTS.md`, `brain wiki/SCHEMA.md`, and the canonical role prompt;
- `config/schemas/brain-note.schema.json` and `config/brain-domains.json`;
- the current question notes under `brain wiki/questions/`;
- this proposal's `manifest.json`, `future-vault/`, and `review/` files;
- `state/workshop/questionnaire-canvas/` inventories and reconciliation records.

Do not read `sources/` or `ingest/`. The local fidelity report is the assigned
evidence-status input for this review. Do not edit or publish any file.

Assess every `ADD` and `UPDATE` for one intent, FR/EN equivalence, duplication,
answer semantics, routing, dependencies, links, evidence/authority boundary,
Canvas reconciliation, and usability for mandatory AI-project intake. Treat a
successful validation as evidence of structure only.

Return one JSON object with exactly these top-level keys:

```json
{
  "reviewer": "questionnaire-reviewer",
  "model": "string",
  "proposal_id": "questionnaire-foundation-lot-011",
  "checks": [{"name": "string", "result": "PASS|FAIL", "detail": "string"}],
  "question_findings": [{"question_id": "string", "severity": "CRITICAL|ERROR|WARNING|INFO", "finding": "string", "remediation": "string"}],
  "duplicate_candidates": [{"question_id": "string", "candidate_id": "string", "disposition": "DUPLICATE|DISTINCT|REVIEW", "reason": "string"}],
  "dependency_findings": [{"question_id": "string", "severity": "CRITICAL|ERROR|WARNING|INFO", "finding": "string", "remediation": "string"}],
  "canvas_coverage": {"result": "PASS|FAIL", "detail": "string"},
  "counts": {"critical": 0, "error": 0, "warning": 0, "info": 0},
  "result": "BLOCKED|READY_FOR_VAULT_REVIEW"
}
```

Use empty arrays when there are no findings. `READY_FOR_VAULT_REVIEW` requires
zero `CRITICAL` and zero `ERROR` findings. Output JSON only.
