---
description: Independently review a consolidated domain release
agent: release-reviewer
subtask: true
---

Review the complete release at: $ARGUMENTS.

Use its manifest, evidence lock, future-vault overlay, deterministic validation
report and the active catalogues. Write `review/release-review.json` with either
`BLOCKED` or `READY_FOR_HUMAN_APPROVAL`, concrete findings and the exact
candidate hash, reviewer identity and review date. Do not approve, integrate or
edit candidate notes.
