# Independent technical review: U02 / U04 / U05

Review date: 2026-09-22. This is a read-only technical review; it does not grant human approval or publication status.

The reviewed implementation has explicit fail-closed gates for evidence status, source access, lineage hashes, dates, applicability, review expiry, jurisdiction, modality and authority. Assistance mode excludes unresolved evidence and requires BINDING authority for obligations and prohibitions. The validated-ingest reader confines reads to the manifest, validated ingest document and normalized unit files. Research is an explicit unreviewed mode, and the ATLAS derivation consumes the validated `/objects` Markdown unit rather than opening an immutable original. Context and research packets use separate schemas, expose their budget estimate and data policy, and have bounded outputs.

The focused suite passed 52 tests. The reference evaluation passed 45/45 cases (30/30 positive hits and 15/15 negative cases); the extension passed 8/8. A read-only synthetic probe confirmed that a guidance-only obligation is excluded, a reviewed BINDING obligation is retained, expired review is excluded, and fully dated reviewed evidence can satisfy `require_known_validity`.

Two findings remain open.

1. **U04 benchmark extension is narrow (`WARNING`).** The eight-case extension has four positive queries for one operational-resilience monitoring concept, with repeated expected notes, while its vocabulary contains the matching French and English terms. Its 1.0 result is useful as a phrase and access probe, but it cannot support a broad retrieval generalisation claim. Add held-out cases across pillars, independent paraphrases, distractors and near misses, and keep the extension labelled as a probe.

2. **U05 derived outputs are stale (`WARNING`).** `gov360 brain build --check` exited 1 with `current=false`, `written=0`, no LLM calls, and five changed derived paths: `state/derived/brain/catalogue.json`, `coverage-matrix.json`, `reconciliation.json`, `baseline.json` and `report.md`. The command still reported `valid=true`, zero evidence findings, and unchanged source baseline. The owning controlled build lane must regenerate those outputs and rerun the check to obtain `current=true`; this review did not write them.

One non-blocking follow-up is recorded: `evidence.resolve_library` indexes classification events by `source_id` without an explicit duplicate or event-order policy. Current classification IDs are unique, so no current failure was observed. Define a fail-closed policy before multiple events per source are allowed.

The JSON companion contains the complete command receipts and SHA-256 inventory for every file actually read. No source or ingest body text is reproduced here.
