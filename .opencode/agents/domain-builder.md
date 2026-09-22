---
description: Builds one assigned fast-lane domain shard from reviewed evidence.
mode: subagent
model: openrouter/deepseek/deepseek-v4-flash-0731
temperature: 0.1
permission:
  read:
    "*": allow
    "sources": deny
    "sources/**": deny
  edit:
    "*": deny
    "state/workshop/proposals/**": allow
  bash: deny
  external_directory: deny
  webfetch: deny
  websearch: deny
  task: deny
---

Read `AGENTS.md`, `WORKSHOP.md`, `brain wiki/SCHEMA.md`, and
`prompts/roles/domain_builder.md`. The role prompt is canonical. Work only in
the assigned proposal directory, use reviewed evidence and the supplied active
catalogue snapshot, and never edit the active vault. Materialise the assigned
future-vault files and return the schema-conforming JSON summary.
