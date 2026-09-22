# U05 — implementation and checks

Status: implementation in progress, not a knowledge publication.

- `brain/ingest_reader.py` checks source availability, document validation,
  file/body hashes, metadata schema, exact lineage and confined unit paths.
- `derived.atlas_catalog` now reads the normalized `/objects` Markdown unit of
  SRC-0046. It does not open the original dataset. Object IDs and relation
  ordering match the existing derived catalogue: 308 objects, 1,088 relations.
- One description, AML.CS0046, differs only in decoded angle-bracket entities
  (1,240 versus 1,228 characters). The historical normalizer did not distinguish
  original literal HTML entities from entities introduced by normalization.
  This limitation is explicit in catalogue manifest version 2. Do not claim
  byte-for-byte source fidelity from this comparison.
- `gov360 brain research` is a separate explicit local command over validated
  ingest, with a dedicated version-1 schema. It cannot feed assistance
  implicitly. Results retain locators and hashes and are labelled unreviewed
  research with unknown authority and redistribution rights.
- Excerpts carry character offsets and their own hashes; parent hashes always
  identify complete normalized units. Unit text is never an instruction.
- Eleven synthetic tests pass for these changes, including absent originals,
  tampering, symlinks, duplicate source IDs, quarantine, non-exhaustive ATLAS,
  access exclusions, lineage and bounded research output.
- Local SRC-0046 smoke: one result, 883 estimated tokens under a 6,000-token
  budget, 46 other logical sources excluded by the explicit allowlist.
  Observed elapsed time: 0.180 seconds (one local run, not a performance SLA).

Pending: independent review, broader regressions, targeted fidelity/coverage
triage, deterministic catalogue rebuild and final input-integrity check.
No original, normalized unit or knowledge note was edited by this work.
