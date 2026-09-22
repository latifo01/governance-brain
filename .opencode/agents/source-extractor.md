---
description: Extracts evidence candidates from assigned validated Markdown units.
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

Read `AGENTS.md` and `prompts/roles/source_extractor.md` before starting. The
role prompt is canonical; this file only adapts it to OpenCode. Use only the
assigned validated Markdown units under `ingest/`. Return the requested typed
result without editing receipts, shared state, or vault files.
