# Audit checks

## Contracts and provenance

Validate Domain Packs, manifest records, unit metadata, receipts, and active
notes against their versioned schemas. Use `brain-note.schema.json` for the
active vault. Verify stable source IDs, source hashes, locators, unit hashes,
receipt coverage, fidelity status, and evidence verdicts.

## Knowledge and graph

Reject claims without reviewed evidence, obligations from non-binding sources,
duplicate stable IDs, unresolved merge markers, and missing link targets. Check
that index links are useful, deterministic, and do not introduce unsupported
claims.

## Questionnaires and approval

Require English and French text, one intent, stable topics, compatible response
options, an acyclic `depends_on` graph, and reviewed evidence for normative
premises. Check semantic duplicates across all questions and reconcile relevant
Canvas nodes. Confirm recorded approval for every affected domain and stage. A
successful agent review is not approval.

## Operational hygiene

Check that logs contain no source excerpts, values, prompts, secrets, or credentials; sources remain unchanged; generated writes were atomic; quarantined inputs were not processed; and an unchanged rerun produces no material diff.
