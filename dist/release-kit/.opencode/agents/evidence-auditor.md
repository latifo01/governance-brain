---
description: Verifies evidence, locators, coverage, and normativity before synthesis.
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


Read `AGENTS.md` and `prompts/roles/evidence_auditor.md` before starting. The
role prompt is canonical; this file only adapts it to OpenCode. Use only the
assigned validated Markdown units and extractor result. Return the requested
typed review without editing receipts, shared state, or vault files.
