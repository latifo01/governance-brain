---
description: Reviews proposed vault changes for evidence, schema, link, and governance defects.
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

Read `AGENTS.md` and `prompts/roles/vault_reviewer.md` before starting. The role
prompt is canonical; this file only adapts it to OpenCode. Review the assigned
proposal and immutable snapshots without changing them. A passing review is
never human approval.
