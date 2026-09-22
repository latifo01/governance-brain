---
description: Extracts evidence candidates from assigned validated Markdown units.
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


Read `AGENTS.md` and `prompts/roles/source_extractor.md` before starting. The
role prompt is canonical; this file only adapts it to OpenCode. Use only the
assigned validated Markdown units under `ingest/`. Return the requested typed
result without editing receipts, shared state, or vault files.
