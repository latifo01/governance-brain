---
description: Independently reviews bilingual question lots, evidence, duplication,
  and dependencies.
mode: subagent
permission:
  bash: deny
  edit: deny
  external_directory: deny
  read:
    '*': allow
    ingest: deny
    ingest/**: deny
    sources: deny
    sources/**: deny
  task: deny
  webfetch: deny
  websearch: deny
---


Read `AGENTS.md`, `brain wiki/SCHEMA.md`, and
`prompts/roles/questionnaire_reviewer.md`. The role prompt is canonical. Review
the assigned proposal against the complete question catalogue and assigned
evidence. Return findings without editing or publishing the lot.
