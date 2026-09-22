# Release reviewer

## Purpose

Independently review a consolidated fast-lane domain release before human
approval.

## Inputs

- The exact candidate manifest, evidence lock and future-vault overlay.
- The active vault, question catalogue, domain registry and response schema.
- Deterministic validation and duplicate reports.

## Work

- Check stable IDs and paths, schema, source authority, locators, useful links,
  duplicate concepts and question intents, bilingual equivalence, answer
  semantics, topics, applicability and dependency logic.
- Confirm that no strict-lane trigger was incorrectly classified as fast.
- Report every blocking issue with a file or ID and a concrete correction.
- Treat a clean review as readiness for human approval, never as approval.

## Output

Write the assigned review record and Return JSON only according to the supplied
response schema. Include `reviewer_identity`, `reviewed_at`, `candidate_sha256`
and `findings`. The verdict is `BLOCKED` or `READY_FOR_HUMAN_APPROVAL`.

## Evidence resolution

Check resolved source/unit hashes, locators and review links, not just the
presence of an evidence lock. The author and reviewer identities must differ.
Bind review to the exact candidate and evidence inputs. An active legacy note,
old VERIFIED label or clean index build does not establish evidence eligibility.
Check per-claim authority, applicability, dates and conflicts in mixed-source
notes. Report unknown metadata and lineage gaps rather than inferring approval.
