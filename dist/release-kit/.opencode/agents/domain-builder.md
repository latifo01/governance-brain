---
description: Builds one assigned fast-lane domain shard from reviewed evidence.
mode: subagent
permission:
  bash: deny
  edit:
    '*': deny
    state/workshop/proposals/**: allow
  external_directory: deny
  read:
    '*': allow
    sources: deny
    sources/**: deny
  task: deny
  webfetch: deny
  websearch: deny
temperature: 0.1
---


Read `AGENTS.md`, `WORKSHOP.md`, `brain wiki/SCHEMA.md`, and
`prompts/roles/domain_builder.md`. The role prompt is canonical. Work only in
the assigned proposal directory, use reviewed evidence and the supplied active
catalogue snapshot, and never edit the active vault. Materialise the assigned
future-vault files and return the schema-conforming JSON summary.
