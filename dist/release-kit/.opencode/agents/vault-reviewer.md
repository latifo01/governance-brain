---
description: Reviews proposed vault changes for evidence, schema, link, and governance
  defects.
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


Read `AGENTS.md` and `prompts/roles/vault_reviewer.md` before starting. The role
prompt is canonical; this file only adapts it to OpenCode. Review the assigned
proposal and immutable snapshots without changing them. A passing review is
never human approval.
