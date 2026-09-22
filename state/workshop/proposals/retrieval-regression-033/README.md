# Retrieval regression audit 033

This is a diagnostic report only. It does not modify the active vault,
`config/brain-evaluation.json`, retrieval code, receipts, or publication state.

The audit was run against the current built catalogue with the default
`brain evaluate` budget of 6000 tokens.

## Result

- 45 scenarios: 30 positive and 15 negative.
- 12/30 positive scenarios have an assistance eligible expected note.
- Top-5 recall among those 12 ready scenarios is 12/12 (`1.0`).
- All 15 negative scenarios pass.
- The benchmark remains `accepted: false` because 18 positive scenarios have no
  expected note with resolved, reviewed evidence eligible for assistance.
- 29/30 positive packets report `sections_omitted_for_budget`; this is mostly
  bounded graph or additional-section omission. It does not reduce top-5
  recall at 4096 tokens or above on the currently ready cases.

Detailed machine-readable metrics are in
`analysis/retrieval-audit.json`.

## Cause and next action

The primary blocker is evidence eligibility, not lexical ranking. The 15 unique
expected IDs listed in the JSON need reviewed evidence/provenance releases. The
45 publication-lineage warnings should be repaired through provenance work.
Budget enforcement must remain fail-closed. A future approved benchmark
proposal may test 4096 tokens as the minimum observed budget preserving 12/12
ready-case recall; this report does not change that contract.

Validation executed:

- `uv run gov360 brain evaluate` — completed, accepted false as expected.
- `uv run gov360 brain build --check` — valid, current, no changed paths.
- `uv run gov360 brain validate` — valid, zero errors, zero evidence findings.
- `uv run pytest -q` — passed.
