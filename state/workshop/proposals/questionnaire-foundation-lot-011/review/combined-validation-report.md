# Combined deterministic validation report

Status: PASS_FOR_VAULT_REVIEW

Validated the active vault with both human-gate candidates applied as ordered
path overlays:

1. `questionnaire-foundation-lot-011`
2. `domain-navigation-proposal`

Result:

- Combined notes: 84
- Schema, domain, filename, link and dependency errors: 0
- Conflicting paths between proposals: 0
- Question dependency cycles: 0

Command:

    uv run --offline --no-sync python -m gov360_brain.workshop validate --proposal state/workshop/proposals/questionnaire-foundation-lot-011 --proposal state/workshop/proposals/domain-navigation-proposal

The validator accepts repeated `--proposal` arguments and rejects duplicate
relative paths between proposal overlays. This result establishes structural
consistency only. It is not evidence review, legal review or human approval.
