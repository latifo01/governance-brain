# U01 - Coverage reconciliation

Status: PROPOSAL_READY. This dossier is a deterministic reconciliation aid; it does not alter the active coverage register or publish vault content.

## Scope

This lot compares the generated 15-pillar by 10-criterion matrix with the approved P0 release and current candidate routing. The existing derived matrix contains 150 UNASSESSED cells because its generator does not project criterion decisions. The result proposes a disposition for every cell while preserving that diagnostic state.

The 18 evidence-backed P0 cells inherit the exact human approval of candidate 62efa5e600896f498e0316f434d0ea544c8bafb8c4e77f67b7471ce9e9b48f7d; the two P0 index cells remain NAVIGATION_ONLY. This inheritance is a traceability proposal and does not by itself change a pillar to COMPLETE. All other cells remain REVIEW_REQUIRED or SOURCE_GAP pending independent criterion review and any required strict release.

## Files

- analysis/criterion-reconciliation.json: 150-cell deterministic triage output.
- analysis/criterion-review.schema.json: proposal-only contract for a cell review.
- analysis/reconciliation-report.md: counts, gates and next actions.
- evidence-lock.json: no new source evidence; references the approved P0 evidence lock for traceability.

## Gates

- Sources and ingest unchanged.
- Active vault unchanged.
- No COMPLETE status is written.
- Existing approval is reused only by exact candidate hash.
- New evidence, legal interpretation, contract change or supersession requires the strict lane.

## Next action

An independent reviewer should verify the 18 inherited cells against the approval chain, then review the remaining 132 cells by criterion. Only after that review may a deterministic assembler update the shared coverage register and derived matrix.

