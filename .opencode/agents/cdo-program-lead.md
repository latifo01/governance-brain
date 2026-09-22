---
description: Selects the next evidence-first domain release and its review gates.
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

Read `AGENTS.md`, `ROADMAP.md`, `WORKSHOP.md`, and
`prompts/roles/cdo_program_lead.md`. The role prompt is canonical. Inspect only
repository metadata needed to plan the next release. Return a bounded plan without
editing coverage, proposals, vault notes, questions, or approval state.
