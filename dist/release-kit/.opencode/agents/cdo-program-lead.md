---
description: Selects the next evidence-first domain release and its review gates.
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


Read `AGENTS.md`, `ROADMAP.md`, `WORKSHOP.md`, and
`prompts/roles/cdo_program_lead.md`. The role prompt is canonical. Inspect only
repository metadata needed to plan the next release. Return a bounded plan without
editing coverage, proposals, vault notes, questions, or approval state.
