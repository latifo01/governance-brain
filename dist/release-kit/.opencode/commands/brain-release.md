---
description: Validate and integrate an explicitly approved domain release
subtask: false
---

Process the release at: $ARGUMENTS.

Read `AGENTS.md` and `WORKSHOP.md`. First run the deterministic integration
preview with the proposal path. If and only if the manifest, independent review
and complete human approval record are already approved for the same candidate
hash, run the identical integration command with `--apply`. Then run
`check-derived`, the relevant tests, and report the exact files and hashes.
Never create or infer the human approval record.
