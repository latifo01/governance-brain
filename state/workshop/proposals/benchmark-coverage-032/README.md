# Benchmark and coverage proposal 032

This proposal records the deterministic diagnosis of the 45-case retrieval benchmark and a bounded expected-ID correction. It updated only `config/brain-evaluation.json` after hash-bound human approval; it did not edit the active vault, the coverage register, or `sources/`.

## Current state

- Catalogue SHA-256: `307a8c2c42640e49be6006ec24d7cd3a0a7722b4fc2e87073bb497b2f9ad0212`
- Evaluation: 4/30 positive cases assistance-ready, recall-at-5 `1.0` over ready cases, 15/15 negative cases passing, accepted `false`.
- Root causes: 8 positive cases use stale/missing expected IDs; 18 reference active targets without reviewed eligible evidence; 4 are currently ready.
- Coverage: 150/150 cells remain `UNASSESSED` by design.

## Proposed bounded correction

The proposal maps four stale IDs to active IDs already present in the catalogue. The scenario queries and bilingual wording remain unchanged. Lifecycle change accepts both the operational question and the related knowledge note because the query spans both concepts.

Applying the proposal in memory predicts 12/30 positive cases ready and 12/12 recall-at-5, while 18 positive cases remain unavailable until their evidence is reviewed. It therefore improves benchmark correctness without falsely declaring the Brain complete.

## Applied result

The approved candidate `6ca0138a638dd9ddbe120ee3d171b3cf90ae841e96407b697269d29aed4711f2` is integrated. The rerun reports 12/30 positive cases ready, 18 evidence-gated cases remaining, 15/15 negative cases passing and `accepted: false`. Coverage triage remains an overlay; it cannot mark a criterion complete.
