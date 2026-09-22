# Vault review assignment

Review these two bounded, unpublished proposals as one human-gate candidate:

1. `state/workshop/proposals/questionnaire-foundation-lot-011/`
2. `state/workshop/proposals/domain-navigation-proposal/`

Read the active vault, `brain wiki/SCHEMA.md`,
`config/schemas/brain-note.schema.json`, `config/brain-domains.json`, active
Domain Packs, proposal manifests, proposed files, validation reports, fidelity
and reviewer records. Do not read `sources/` or `ingest/`; the questionnaire
fidelity record is the assigned evidence-status input.

Verify schema, stable IDs and paths, link targets, domain and bank vocabulary,
question intent and dependencies, index accuracy, provenance/authority
boundaries, unchanged active-vault state, and the pending human gate. Treat
`READY_FOR_VAULT_REVIEW` as an input review result, not as approval.

Return JSON with `reviewer`, `model`, `proposal_ids`, `checks`, `findings`,
`counts`, and `result`. Each finding must contain `severity`, `artifact`,
`finding`, and `remediation`. Use `READY_FOR_HUMAN_APPROVAL` only with zero
`CRITICAL` and zero `ERROR` findings. Do not edit or publish anything.
