## Purpose

Describe the bounded problem and the resulting behavior.

## Governance checks

- [ ] Existing files under `sources/` were not modified, renamed or deleted.
- [ ] Agents consumed only assigned validated Markdown under `ingest/`.
- [ ] Claims and questions are linked to reviewed evidence and exact locators.
- [ ] Binding language is supported only by reviewed `BINDING` evidence.
- [ ] Author and reviewer are independent.
- [ ] Any vault integration has a human approval for the exact candidate hash.
- [ ] No secret, project answer, personal data or raw source text was added to logs.

## Validation

- [ ] `uv run pytest -q`
- [ ] `uv run gov360 brain validate`
- [ ] `uv run gov360 brain build --check`
- [ ] derived, retrieval and source-integrity checks pass
