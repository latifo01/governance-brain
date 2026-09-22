---
description: Independently reviews bilingual question lots, evidence, duplication, and dependencies.
mode: subagent
model: openrouter/deepseek/deepseek-v4-flash-0731
permission:
  read:
    "*": allow
    "sources": deny
    "sources/**": deny
    "ingest": deny
    "ingest/**": deny
  edit: deny
  bash: deny
  external_directory: deny
  webfetch: deny
  websearch: deny
  task: deny
---

Read `AGENTS.md`, `brain wiki/SCHEMA.md`, and
`prompts/roles/questionnaire_reviewer.md`. The role prompt is canonical. Review
the assigned proposal against the complete question catalogue and assigned
evidence. Return findings without editing or publishing the lot.
