---
id: model-validation-lot-001-fidelity-checks
title: Model validation lot 001 fidelity checks
type: index
domains: [GENERAL]
status: active
aliases: []
tags:
  - workshop
  - fidelity
evidence_sources: []
---

# Model validation lot 001 fidelity checks

## Method

The lot uses CDO drafts as editorial input and verified `ingest/` Markdown as working source text. For documentary fidelity, the relevant PDFs in `sources/` were independently extracted locally with `pdftotext -layout` into `state/workshop/proposals/model-validation-lot-001/pdf-text/`. The selected Markdown units were then compared against the direct PDF text extraction by page-level normalized text matching and targeted phrase lookup.

This is a local documentary check, not a legal validation and not human approval. It verifies that the passages used for drafting are faithfully represented in `ingest/` at the page level.

## Checked Sources

| Source | PDF path | Pages used | Result |
|---|---|---:|---|
| SRC-0036 | `sources/07_Model_Risk_Management/SR2602.pdf` | 2, 5, 9, 10, 11, 13, 14 | Pass. Direct extraction matched the ingested page text or confirmed targeted passages by phrase lookup. Pages 13-14 showed form-feed/page-offset effects in automated chunk comparison but targeted passages were present in direct PDF text. |
| SRC-0038 | `sources/07_Model_Risk_Management/sr1107a1.pdf` | 9, 12, 13, 14, 15, 17, 18, 21 | Pass with limitation. Direct extraction matched or targeted phrase lookup confirmed the selected passages. The ingest metadata records image-inspection warnings on all pages of this PDF; the used content is native text and no claim relies on visual content. |
| SRC-0039 | `sources/08_NIST_AI_Risk/NIST AI RMF 1.0.pdf` | 19, 24, 26, 33, 34, 35, 36, 38 | Pass. Direct extraction matched the ingested page text. Some tables have line wrapping differences, but the referenced subcategory content is present and readable. |

## Automated Similarity Snapshot

High similarity was observed for SRC-0036 pages 2, 5, 9, 10, 11; SRC-0038 page 9; and SRC-0039 pages 19, 24, 26, 33-36, 38. Low ratios for SRC-0036 pages 13-14 and SRC-0038 pages 12-15, 17-18, 21 were caused by PDF text chunk/page-boundary differences, not by missing content; targeted phrase searches confirmed the relevant passages.

## Limitations

- Visual content was not used as evidence in this lot.
- The SR 11-7 appendix has image-inspection warnings in ingest metadata; because this lot relies only on native text, the warning is recorded but does not block the draft.
- The notes avoid treating SR 11-7 as current standalone guidance where SR 26-2 supersession is relevant.
- This report validates only the pages and passages used in this first lot.

