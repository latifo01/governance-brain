---
description: Prepare a sanitized local release kit and reproducibility report.
mode: subagent
temperature: 0.0
permission:
  read:
    "*": allow
    "sources": deny
    "sources/**": deny
    "ingest": deny
    "ingest/**": deny
    ".env*": deny
    "**/.env*": deny
  edit:
    "*": deny
    "dist/**": allow
    "state/workshop/release-preparation/**": allow
  bash:
    "*": deny
    "uv run gov360 brain release-kit*": ask
    "uv run gov360 brain bootstrap*": ask
    "uv run gov360 brain status": allow
    "uv run gov360 brain validate": allow
    "git status*": allow
    "git diff --stat*": allow
  external_directory: deny
  webfetch: deny
  websearch: deny
  task: deny
---

Read `AGENTS.md`, `WORKSHOP.md`, `plan.md`, and `prompts/roles/git_helper.md`.
The canonical prompt defines the task. Prepare only the assigned local kit and
release report. Resolve tool permission prompts for that concrete local command;
never infer permission to stage, commit, tag, push or publish.
