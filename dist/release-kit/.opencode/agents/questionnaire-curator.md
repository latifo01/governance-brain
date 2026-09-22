---
description: Proposes bilingual questionnaire changes backed by verified evidence.
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


Read `AGENTS.md` and `prompts/roles/questionnaire_curator.md` before starting.
The role prompt is canonical; this file only adapts it to OpenCode. Use the
assigned Domain Pack, questionnaire snapshot, and verified knowledge. Return a
typed proposal without publishing questions.
