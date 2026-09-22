# Deterministic validation report

## Result

Status: PASS_FOR_INDEPENDENT_REVIEW

- Active vault: 65 notes, 0 errors.
- Proposed overlay: 78 notes, 0 errors.
- Proposed additions: 13 questions.
- Proposed replacements: 4 questions.
- Source locator unit checks: 98 question-to-page references covering 68
  unique pages, 0 missing units.
- Exact topic collisions after overlay: 0.
- Dependency cycles: 0.
- Original Canvas: 21 nodes, 20 edges, hash matches import manifest.

## Commands

    uv run --offline --no-sync python -m gov360_brain.workshop validate
    uv run --offline --no-sync python -m gov360_brain.workshop validate --proposal state/workshop/proposals/questionnaire-foundation-lot-011

## Limits

These checks establish schema, path, link, dependency and locator presence. They
do not establish extraction fidelity, semantic non-duplication, legal accuracy,
independent review or human approval. Those gates remain pending.
