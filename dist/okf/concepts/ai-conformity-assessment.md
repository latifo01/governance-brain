---
aliases:
- Conformity assessment
- AI Act conformity assessment
brain_id: ai-conformity-assessment
brain_sha256: ff772c25f0b68178f8a943ffcb27c2fa7f75368591a778b0ba3c3ac7e270bbfe
domains:
- AI
- LEGAL
- LEGAL_REGULATORY
- AUDIT_ASSURANCE
evidence_sources:
- AI_ACT
- AI_LEGAL_GUIDANCE
id: ai-conformity-assessment
sources:
- authority: BINDING
  brain_source_id: SRC-0043
  evidence_ref: aiconcepts-p1-src-0043-ec-003
  id: brain-89778498700c305d
  locator: Page 13
  resource: /references/src-0043-0bea4d808256b08275777949ba9cb3c70b7d02e4ebb3ac9b205671b1f552d386.md
  unit_file_sha256: e529a174243a38368a5992b6cab34a5f5ecee78acef66d940811ce5b72ba779b
  unit_path: ingest/SRC-0043/units/p0013.md
  unit_sha256: 97bb6ec9fb89cc43568170d953fca2f619dc562ba95d35d9f8c8d2c6ac0bdf19
- authority: BINDING
  brain_source_id: SRC-0043
  evidence_ref: aiconcepts-p1-src-0043-ec-001
  id: brain-e8fd0ed7fd8f4b5e
  locator: Page 7
  resource: /references/src-0043-0bea4d808256b08275777949ba9cb3c70b7d02e4ebb3ac9b205671b1f552d386.md
  unit_file_sha256: 6786de3d46cbb24f26cd07a520c0b8beb5e333ce9210b68393dcf7980f3f0ad6
  unit_path: ingest/SRC-0043/units/p0007.md
  unit_sha256: a7fc3d6255fcf51d20f8e5f4a2cefcfdfe55a5c38f049a5575271421b4460703
- authority: BINDING
  brain_source_id: SRC-0043
  evidence_ref: aiconcepts-p1-src-0043-ec-002
  id: brain-f357d939f839cdd6
  locator: Page 11
  resource: /references/src-0043-0bea4d808256b08275777949ba9cb3c70b7d02e4ebb3ac9b205671b1f552d386.md
  unit_file_sha256: 4e5305317711b2ed82f01464e42c64e00831bcf5c95ff3a18061280e28d271cf
  unit_path: ingest/SRC-0043/units/p0011.md
  unit_sha256: a3cf3e6b04d625bbee045244ff7cb85e1595dc60a22e3d61df5951b66b5fcec6
status: stable
tags:
- ai-concepts
- assurance
- legal-regulatory
title: AI conformity assessment
type: knowledge
---


# AI conformity assessment

## Summary

AI conformity assessment is the documented process used to determine whether a covered AI system meets the requirements applicable to its classification, product context and assessment route. In the EU AI Act context, the route can involve a conformity assessment body. The 2026 amendment clarifies that only bodies designated under the Regulation may assess the categories and types of high-risk AI systems within their designation, and it describes pre-market assessments for systems under the AI Office's exclusive supervision (SRC-0043, pages 7, 11 and 13).

Section evidence: [^brain-89778498700c305d] [^brain-e8fd0ed7fd8f4b5e] [^brain-f357d939f839cdd6]

## Applicability

This concept applies when an AI system falls within a legal or sectoral regime that calls for a conformity assessment, especially a high-risk system linked to Union harmonisation legislation or a designated system category. It does not imply that every AI system requires an external assessment. The classification and product-safety gates remain the responsibility of [high-risk-ai-system-classification](/concepts/high-risk-ai-system-classification.md).

Section evidence: [^brain-89778498700c305d] [^brain-e8fd0ed7fd8f4b5e]

## Governance Considerations

- Record the system category, product or Annex context, applicable requirements and the assessment route as separate fields so that system-level and product-level evidence are not conflated.
- Verify that a proposed conformity assessment body is designated for the relevant category and type of AI system; designation for another category is not evidence for this scope (SRC-0043, page 13).
- Where Union harmonisation legislation also covers the quality-management system, map the overlapping requirements and retain the rationale for the selected route. The amendment describes an approach intended to avoid duplicated assessment work while preserving the applicable level of scrutiny (SRC-0043, page 7).
- Preserve the assessed system version, technical documentation, test results, identified limitations and post-assessment changes so that a later reassessment can be scoped against the original boundary.

Section evidence: [^brain-89778498700c305d] [^brain-e8fd0ed7fd8f4b5e] [^brain-f357d939f839cdd6]

## Limits

The cited amendment changes and clarifies parts of the EU AI Act framework; it is not a complete description of all assessment procedures, harmonised standards or sectoral requirements. This note does not classify an individual system, certify conformity or replace advice from the competent authority or a designated assessment body. The effect of changes in the underlying AI Act and sector legislation requires a current legal review.

Section evidence: [^brain-89778498700c305d] [^brain-e8fd0ed7fd8f4b5e] [^brain-f357d939f839cdd6]

## Related Concepts

- [high-risk-ai-system-classification](/concepts/high-risk-ai-system-classification.md)
- [ai-model-validation](/concepts/ai-model-validation.md)
- [ai-model-documentation](/concepts/ai-model-documentation.md)
- [ai-assurance-and-independent-review](/concepts/ai-assurance-and-independent-review.md)
- [third-party-ai-assurance-and-shared-responsibility](/concepts/third-party-ai-assurance-and-shared-responsibility.md)

## Source References

- SRC-0043, Regulation (EU) 2026/1744, page 7 (high-risk conformity assessment routes, quality-management overlap and designated bodies).
- SRC-0043, Regulation (EU) 2026/1744, page 11 (pre-market assessment under the AI Office's exclusive supervision).
- SRC-0043, Regulation (EU) 2026/1744, page 13 (designation scope by codes, categories and types of AI systems).


[^brain-89778498700c305d]: [SRC-0043](/references/src-0043-0bea4d808256b08275777949ba9cb3c70b7d02e4ebb3ac9b205671b1f552d386.md); locator: Page 13.
[^brain-e8fd0ed7fd8f4b5e]: [SRC-0043](/references/src-0043-0bea4d808256b08275777949ba9cb3c70b7d02e4ebb3ac9b205671b1f552d386.md); locator: Page 7.
[^brain-f357d939f839cdd6]: [SRC-0043](/references/src-0043-0bea4d808256b08275777949ba9cb3c70b7d02e4ebb3ac9b205671b1f552d386.md); locator: Page 11.
