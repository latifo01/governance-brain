# CDO plan — ATLAS incident enrichment lot 016

## Objective

Use the 18 prioritised MITRE ATLAS case studies to improve incident and risk
context in the Brain without importing the complete ATLAS incident catalogue.

## Evidence boundary

- Source: `SRC-0046`, MITRE ATLAS v2026.08 STIX export.
- Inputs: validated `ingest/SRC-0046/` and `state/derived/atlas-catalog.jsonl`.
- Incidents are contextual security knowledge, not legal obligations.

## Decision rule

- Enrich an existing incident note when the intent remains unchanged.
- Create a note only for a distinct reusable incident absent from the vault.
- Use `NOOP` when the active vault already covers the scenario adequately.

## Gate

All changes remain in `future-vault/` until evidence review, independent release
review and hash-bound human approval.
