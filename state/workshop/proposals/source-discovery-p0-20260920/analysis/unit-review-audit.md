# P0 candidate unit review audit — 2026-09-20

Status: **AUDITED_WITH_BLOCKERS**. Candidate units: **216**.

This audit checks hashes, locators, source routing, visual-fidelity state and review gates without copying source text. It does not resolve evidence or authorize synthesis.

## Findings

- Candidate rows audited: 216.
- Blocked pending criterion review: 216.
- Source normativity distribution: {'normativity:UNCLASSIFIED': 131, 'normativity:BINDING': 41, 'normativity:RESEARCH': 44}.
- Visual-review distribution: {'visual:NONE': 174, 'visual:REVIEW_REQUIRED': 20, 'visual:DECORATIVE': 22}.
- Currentness, applicability and independent evidence review remain required for every candidate row.
- Units flagged `REVIEW_REQUIRED` or `UNREADABLE` remain blocked until selective visual review.

## Required next gates

1. Review each candidate against the criterion scope and exclude keyword-only false positives.
2. Confirm authority, jurisdiction, effective date and supersession status from the source and validated unit.
3. Perform visual review for any unit whose metadata requires it.
4. Build a strict evidence-lock only from rows that pass all checks and receive independent review.

No source, ingest or active-vault file was modified.
