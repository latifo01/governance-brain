---
agent: release-reviewer
description: Review a strict legal or evidence-changing domain release
subtask: true
---


Review the strict release at: $ARGUMENTS.

Require its evidence audit, evidence lock, manifest, complete future-vault
overlay and deterministic validation report. Apply the canonical release-review
contract, record the exact candidate hash, and write only
`review/release-review.json` with reviewer identity, review date and findings.
Return `BLOCKED` or
`READY_FOR_HUMAN_APPROVAL`. Never approve or integrate the release.
