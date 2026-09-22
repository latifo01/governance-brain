# GDPR currentness source plan

## Purpose

Resolve the remaining `GDPR_CURRENTNESS_UNRESOLVED` blocker for Articles 35,
36 and 39 in the strict Article 35 release. This plan does not grant legal
currentness and does not change the active vault.

## Candidate official sources

- EUR-Lex consolidated Regulation (EU) 2016/679, CELEX `32016R0679`:
  `https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex:32016R0679`
- Regulation (EU) 2025/2518 on additional procedural rules for GDPR
  enforcement, CELEX `32025R2518`:
  `https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32025R2518`

## Required controlled acquisition

1. Download the official documents into `sources/` without modifying the
   existing `SRC-0010` original.
2. Register new immutable source IDs and SHA-256 values in the source manifest.
3. Normalize only the assigned pages containing Articles 35, 36 and 39 and
   the relevant amendment or applicability provisions into `ingest/`.
4. Run extraction quality and local fidelity checks.
5. Produce a currentness resolution that distinguishes amendments to Articles
   35/36/39 from supplementary procedural rules that do not replace their text.
6. Rerun the independent Article 35 review before creating an evidence-lock.

## Current status

The URLs were identified through an official EUR-Lex lookup. No remote source
has been downloaded, added to `sources/`, or used as binding evidence in the
release. The release remains blocked until the controlled acquisition and
hash-bound ingest review are complete.
