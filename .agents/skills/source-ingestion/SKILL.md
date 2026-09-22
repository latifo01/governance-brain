---
name: source-ingestion
description: Inventory, normalize, and validate immutable governance source files into provenance-preserving Markdown. Use when adding or operating source adapters or diagnosing ingest output; stop before evidence synthesis.
---

# Source ingestion

Read the repository `AGENTS.md` first. Operate through the adapter registry and keep the transformation deterministic.

1. Probe file signature and MIME before trusting the extension.
2. Inventory native units and capabilities without interpreting business meaning.
3. Normalize to `ingest/<source_id>/` with stable locators, hashes, and sanitized warnings.
4. Validate coverage and `document.json` before setting `READY_FOR_LLM`.
5. Quarantine unsupported, corrupt, encrypted, executable, or ambiguous input instead of approximating.

When implementing or diagnosing a specific format, read [format routing](references/format-routing.md) and only its applicable section. Validate unit metadata against [the public schema](../../../config/schemas/ingested-unit.schema.json).

For a supplied sharing-kit manifest, preview `gov360 brain bootstrap` before its
authorized `--apply` reconstruction. Match originals by hash and retain source
IDs; report missing or changed material. A differing output hash requires a
new review. For structured ATLAS evidence, derive addressable fragments from
validated Markdown while preserving the parent hash and object locator.
