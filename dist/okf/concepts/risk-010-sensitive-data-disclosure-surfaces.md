---
aliases:
- Inventory of AI disclosure surfaces for sensitive data
answer_type: boolean
applies_to: AI
brain_id: risk-010-sensitive-data-disclosure-surfaces
brain_sha256: afd954feb26b93fa32304eabcfa6cbac00a4fae1e5dc482a632906fa6813ef54
depends_on: null
domains:
- AI
- RISK
- DATA_PROTECTION
- PROCESS
evidence_sources:
- AI_NICE_TO_KNOW
- DATA_AI_CLASSIFICATION
id: risk-010-sensitive-data-disclosure-surfaces
priority: high
question_en: Does the inventory of sensitive-data disclosure surfaces cover tool-call
  arguments, reasoning traces, retrieved chunks, logs, telemetry and embeddings, with
  common classification and redaction rules?
question_fr: L’inventaire des surfaces de divulgation de données sensibles couvre-t-il
  les arguments d’appels d’outils, les traces de raisonnement, les fragments récupérés,
  les journaux, la télémétrie et les embeddings, avec des règles communes de classification
  et de censure ?
sources:
- authority: UNCLASSIFIED
  brain_source_id: SRC-0026
  evidence_ref: provenance-repair-20260920-src-0026-p0047
  id: brain-2534e3aed5fd2daf
  locator: Page 47
  resource: /references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md
  unit_file_sha256: f120ff6cc1c0d559669b31adf6b15ec192f24a4dfd1e8b9c1baa6ffe89710cc9
  unit_path: ingest/SRC-0026/units/p0047.md
  unit_sha256: 413fb969928128c9cbb625df0ac8bffa0a8eaa8a06da3e89a5c236bbe6fd0360
- authority: UNCLASSIFIED
  brain_source_id: SRC-0026
  evidence_ref: provenance-repair-20260920-src-0026-p0018
  id: brain-5682599f10bc542c
  locator: Page 18
  resource: /references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md
  unit_file_sha256: c8f1ca0c308045986310f16fcc62ba36a867852fd4c751ae26783177d3b5da3d
  unit_path: ingest/SRC-0026/units/p0018.md
  unit_sha256: 278cfc30cd0110dfebc7eb3920d62a5073356e41d86a690624f4a98fe5de68f2
status: stable
tags:
- questionnaire
- data-leakage
- privacy
title: Sensitive data disclosure surfaces
topic: sensitive-data-disclosure-surfaces
type: question
---


# Sensitive data disclosure surfaces

## Purpose

This question checks whether disclosure controls cover every AI output channel and not only the visible final answer.

Section evidence: [^brain-2534e3aed5fd2daf] [^brain-5682599f10bc542c]

## Guidance

Answer "yes" only when tool-call arguments, reasoning traces, retrieved chunks, logs, telemetry and embeddings are inventoried as disclosure surfaces and subject to the same data-classification and redaction rules as user-visible output.

Section evidence: [^brain-2534e3aed5fd2daf] [^brain-5682599f10bc542c]

## Related Knowledge

- [data-leakage](/concepts/data-leakage.md)

## Source References

- SRC-0026, OWASP Top 10 for LLM Applications 2026, page 18, for the definition of disclosure surfaces beyond the final answer.
- SRC-0026, page 47, for keeping credentials out of hidden context and treating disclosure of permissions as a probe vector.


[^brain-2534e3aed5fd2daf]: [SRC-0026](/references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md); locator: Page 47.
[^brain-5682599f10bc542c]: [SRC-0026](/references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md); locator: Page 18.
