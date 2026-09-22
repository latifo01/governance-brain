---
description: Proposes bilingual questionnaire changes backed by verified evidence.
mode: subagent
model: openrouter/deepseek/deepseek-v4-flash-0731
permission:
  read:
    "*": allow
    "sources": deny
    "sources/**": deny
  edit: deny
  bash: deny
  external_directory: deny
  webfetch: deny
  websearch: deny
  task: deny
---

Read `AGENTS.md` and `prompts/roles/questionnaire_curator.md` before starting.
The role prompt is canonical; this file only adapts it to OpenCode. Use the
assigned Domain Pack, questionnaire snapshot, and verified knowledge. Return a
typed proposal without publishing questions.
