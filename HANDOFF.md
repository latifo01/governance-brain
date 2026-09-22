# CDO private continuation repository

This private snapshot contains the immutable source corpus, validated ingest, active Obsidian vault, workshop state and derived outputs. It does not authorize public redistribution.

1. Read `AGENTS.md`, `README.md`, `WORKSHOP.md`, `ROADMAP.md`, `brain wiki/SCHEMA.md`, and `manuel.md`.
2. Run `uv sync --frozen --extra dev`, then `uv run pytest -q`.
3. Run `uv run gov360 brain validate`, `uv run gov360 brain build --check`, and the derived checks.
4. Open `brain wiki/` in Obsidian and start OpenCode from the repository root.
5. Add new originals; never modify or delete an existing file below `sources/`.

See `docs/windows-setup.md` for the Windows path and `manuel.md` for the complete evidence-first workflow.
