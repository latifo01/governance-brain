---
id: genai-controls-lot-002-fidelity-checks
title: GenAI controls lot 002 fidelity checks
type: index
domains: [GENERAL]
status: active
aliases: []
tags:
  - workshop
  - fidelity
evidence_sources: []
---

# GenAI controls lot 002 fidelity checks

## Method

The lot uses CDO drafts as editorial input and `ingest/` Markdown as the working documentary layer. The relevant PDFs were independently extracted locally with `pdftotext -layout` into `state/workshop/proposals/genai-controls-lot-002/pdf-text/`. Selected Markdown units were compared against direct PDF text extraction by normalized page-level matching. Where a page is layout-heavy, the lot either uses it only as secondary support or records the limitation.

## Checked Sources

| Source | PDF path | Pages used | Result |
|---|---|---:|---|
| SRC-0026 | `sources/02_AI_Security_Frameworks/OWASP Top 10 for LLM Applications 2026.pdf` | 10, 11, 12, 30 | Pass. Page-level text matched direct PDF extraction with high similarity. |
| SRC-0027 | `sources/02_AI_Security_Frameworks/OWASP-Top-10-for-Agentic-Applications-2026-12.6-1.pdf` | 10, 11, 33, 38 | Pass. Page-level text matched direct PDF extraction with high similarity. |
| SRC-0016 | `sources/05_EU_AI_Legislation/Guidelines on prohibited AI practices under AI Act.pdf` | 117, 125 | Pass. Page-level text matched direct PDF extraction with high similarity. |
| SRC-0039 | `sources/08_NIST_AI_Risk/NIST AI RMF 1.0.pdf` | 32, 45 | Pass with table-layout limitation on page 32. The relevant human oversight and documented-control text is readable in `ingest` and direct PDF extraction. |
| SRC-0009 | `sources/10_Responsible_AI/Microsoft Responsible AI Transparency Report.pdf` | 9, 16, 22, 28 | Secondary support only. Pages are layout-heavy and page-level similarity is low, although relevant text is readable in `ingest`; no primary claim depends solely on these pages. |

## Limitations

- No visual claim is used as evidence in this lot.
- Microsoft transparency report pages are retained only for supporting examples of practice and tooling, not as authoritative requirements.
- OWASP sources are security frameworks and do not create legal obligations by themselves.
- AI Act guidance is used narrowly for human oversight and should not be generalized beyond the legal contexts it describes.

