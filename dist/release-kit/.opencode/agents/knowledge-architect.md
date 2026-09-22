---
description: Proposes evidence-backed concepts, rules, relations, and taxonomy changes.
mode: subagent
permission:
  bash: deny
  edit: deny
  external_directory: deny
  read:
    '*': allow
    sources: deny
    sources/**: deny
  task: deny
  webfetch: deny
  websearch: deny
---


Read `AGENTS.md` and `prompts/roles/knowledge_architect.md` before starting. The
role prompt is canonical; this file only adapts it to OpenCode. Work only from
audited evidence and the assigned registry snapshot. Return a typed proposal;
do not publish or infer approval.
