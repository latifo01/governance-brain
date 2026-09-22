---
description: Build one reviewed-evidence domain release shard
agent: domain-builder
subtask: true
---

Build the assigned domain release or shard: $ARGUMENTS.

Read its manifest, evidence lock, active-domain context pack and complete
question snapshot. Confirm that the manifest is eligible for the fast lane.
Materialise only the assigned `future-vault/` paths, update the manifest change
inventory, and return the typed summary. Stop with a strict-lane escalation if
the work introduces binding requirements, new evidence, contract changes or a
supersession. Do not edit the active vault or infer approval.
