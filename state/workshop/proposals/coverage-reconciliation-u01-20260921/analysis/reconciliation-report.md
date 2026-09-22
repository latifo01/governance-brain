# U01 - Reconciliation report

- Generated: 2026-09-21
- Input matrix: f653e9e6c16fb9bf86e39635f42b7106d96bf700209fbf356db539c036c37a33
- P0 candidate: 62efa5e600896f498e0316f434d0ea544c8bafb8c4e77f67b7471ce9e9b48f7d
- P0 coverage map: a1a5e99079d175da927f80914cc8710151a9ef627b6d2b11cb3d162268d14d01
- Cells examined: 150
- Prior generated status: 150 UNASSESSED

## Proposed dispositions

| Disposition | Count | Meaning |
| --- | ---: | --- |
| EVIDENCE_APPROVED | 18 | P0 cells covered by the exact approved candidate and reviewed evidence |
| NAVIGATION_ONLY | 2 | P0 index cells with no independent governance claim |
| REVIEW_REQUIRED | 100 | Candidate material exists, but criterion-level evidence/decision is absent |
| SOURCE_GAP | 30 | Pillar is recorded as a source gap; domain overlap is not evidence |

The recommendation is not a publication decision. The active register remains unchanged, and no cell is promoted to COMPLETE by this dossier.

## Integrity gates

- Workshop validation is required before review.
- Brain validation is required alongside schema and provenance checks.
- Exact P0 candidate approval is inherited only for the 18 evidence-backed cells.
- Independent criterion review is pending.
- Human approval is required for any future vault candidate.
- Sources and ingest are unchanged by this lot.

## Findings

- A01-PROJECTION: the generator emits UNASSESSED for every cell and reports unapplied review records; it needs a versioned review input before projection.
- A02-CANDIDATE-OVERLAP: note, question and source overlap is routing evidence only; it cannot establish criterion completion.
- A03-P0-NAVIGATION: the two domain index cells provide navigation and remain non-substantive.
- A04-SOURCE-GAP-STATUS: three pillars remain SOURCE_GAP even where broad candidate material is present.

## Next gate

Review this dossier independently. If accepted, implement the projector as a separate strict contract change, add synthetic tests for stale, ambiguous and hash-mismatched decisions, and regenerate the derived matrix. Do not edit the active register manually.

