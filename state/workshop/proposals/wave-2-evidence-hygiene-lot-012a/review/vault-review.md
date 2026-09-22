# Vault review — wave-2 evidence-hygiene lot 012a

Status: PASS

Reviewer: Codex vault-reviewer role  
Review date: 2026-09-15  
Candidate SHA-256: `f5a3bba6b417a098f9e8d5cf2bc483d5b4d94c31714d88c66965115f49d0abf3`

This is an independent readiness review, not human approval. No active vault
note, source file, ingest unit, manifest, or approval record was modified by
this review. The lot remains unpublished.

## Findings

Counts: CRITICAL 0, ERROR 0, WARNING 1, INFO 2. No blocking defect found.

- **WARNING — V-1 — legacy manifest classification.** The lot manifest does
  not carry the v2 `risk_tier` or `evidence_locks` fields and the deterministic
  preview reports `risk_tiers: ["legacy"]`. This is compatible with the
  pre-existing lot-012 follow-up workflow, but it must not be treated as a new
  fast-lane release. Any successor lot must use `release-init` and a v2
  manifest.
- **INFO — V-2 — source status.** `git status --short -- sources/` reports the
  pre-existing untracked `sources/` directory. No file under it was changed by
  this review; retain and report that baseline state.
- **INFO — V-3 — human gate pending.** `review/approval.md` remains
  `NOT_REQUESTED`, as required. Publication is blocked until an authorised
  human approves this exact candidate hash.

## Verified checks

1. The active vault validator passes: 86 notes, zero errors.
2. Overlay validation passes for all seven update files and the candidate hash
   recomputes to the questionnaire-review hash above.
3. Deterministic integration preview reports `valid: true`, `reviewed: true`,
   `approved: false`, seven files, and seven would-be writes; no files were
   applied.
4. The questionnaire review is PASS and covers schema, provenance, links,
   bilingual equivalence, duplicate intent, and dependencies.
5. The evidence audit is `AUDITED`, with binding authority regeneration and
   explicit supersession handling; no unsupported normative claim was found in
   the overlay.
6. The overlay contains only the seven files declared by `manifest.json`; no
   source or ingest path is present.
7. No human approval was inferred from validation or agent review.

## Verdict

READY_FOR_HUMAN_APPROVAL

The next permitted step is for an authorised human to review the exact
candidate hash and complete `review/approval.md`. Do not run `--apply` before
that record is present and matches the candidate.
