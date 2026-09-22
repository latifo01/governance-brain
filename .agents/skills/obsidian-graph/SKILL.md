---
name: obsidian-graph
description: Assemble deterministic Obsidian notes, links, indexes, and maps from approved governance change sets. Use for vault graph construction or link repair; do not use to create unsupported knowledge.
---

# Obsidian graph

Read the repository `AGENTS.md`, `WORKSHOP.md`, and `brain wiki/SCHEMA.md`.
Consume approved change sets and immutable registry snapshots; never use vault
prose as a substitute for evidence.

- Keep stable IDs and aliases in frontmatter and preserve source locators in visible citations.
- Use meaningful Obsidian links to stable note IDs.
- Preserve the current folder layout and add domain navigation with `index`
  notes unless an approved migration explicitly changes paths.
- Serialize shared index updates after source-specific work completes.
- Validate all generated links before atomic replacement.

Read [vault contract](references/vault-contract.md) when creating a note type, graph map, or index entry.

Use `gov360 brain build` for derived section catalogues and graph outputs, and
`build --check` to detect staleness. OKF export is a derived view, not canonical
content. Preserve evidence associations through link conversion. Do not create
new semantic relations or approval metadata during deterministic assembly.
