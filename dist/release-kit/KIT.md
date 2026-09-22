# Governance Brain reconstruction kit

This directory has no source corpus, extracted text, prior Git history, or publication approvals.

1. Run `uv sync --frozen --extra dev`.
2. Place lawfully held originals below `sources/`; hashes in `config/source-seed.json` identify expected files.
3. Preview `uv run gov360 brain bootstrap`, then run `uv run gov360 brain bootstrap --apply` to reconstruct matching units.
4. Review reconstruction gaps before extracting evidence or drafting knowledge.
5. Run `uv run pytest -q`; the kit carries only synthetic technical tests.
6. Configure OpenCode provider credentials and models locally; the kit keeps agents, commands and skills but removes wrapper model pins. Open `opencode` and use `/brain-next` or `/brain-build <release>`. Select strict-local operation, or explicitly authorise approved-remote endpoint and material before transmitting ingest.

Adapter/version/hash divergence blocks the affected reconstruction. LLM-written notes are not reproducible from source bytes alone. Code licensing does not grant rights to original or derived third-party content.
