---
aliases:
- Fundamental rights impact assessment trigger question
answer_type: boolean
applies_to: AI
brain_id: legal-002-fria-trigger
brain_sha256: c1f936b9a8cfefc65ab27788999391ead5fddcf6b27578b3b3fb5884a835ded3
depends_on:
  equals: high-risk
  question_id: core-013-high-risk-ai-classification
domains:
- AI
- LEGAL
- RISK
- PROCESS
evidence_sources:
- AI_ACT
- AI_LEGAL_GUIDANCE
id: legal-002-fria-trigger
priority: high
question_en: Before first use, has the project determined, for the high-risk AI system
  covered by Article 6(2), whether the Article 27 fundamental-rights impact assessment
  obligation applies to its deployer role, taking into account the deployer categories,
  the Annex III point 2 exclusion and the relevant Article 113 application date?
question_fr: Avant la première utilisation, le projet a-t-il déterminé, pour le système
  d’IA à haut risque visé à l’article 6, paragraphe 2, si l’obligation d’analyse d’impact
  sur les droits fondamentaux de l’article 27 s’applique à son rôle de déployeur,
  en tenant compte des catégories de déployeurs, de l’exclusion de l’annexe III, point
  2, et de la date d’application pertinente de l’article 113 ?
sources:
- authority: BINDING
  brain_source_id: SRC-0011
  evidence_ref: fria-question-src-0011-p0222-ec-001
  id: brain-0bf137bfa342debc
  locator: Page 222
  resource: /references/src-0011-bd7134beb56eaca3b859e272563e464dc234f2daee8f305b942b64eb16fc700c.md
  unit_file_sha256: a036e415dec47d0a1832124f69f8df6dded0b2b64415cbfb1f064580884c7607
  unit_path: ingest/SRC-0011/units/p0222.md
  unit_sha256: 6337dca60a7d782f77e632a7b4b48480569df93258e8c496d4f3aa6d2f246b8d
- authority: BINDING
  brain_source_id: SRC-0011
  evidence_ref: fria-question-src-0011-p0223-ec-008
  id: brain-74bd179d8d01291d
  locator: Page 223
  resource: /references/src-0011-bd7134beb56eaca3b859e272563e464dc234f2daee8f305b942b64eb16fc700c.md
  unit_file_sha256: 8a5c0ba929b0b9d096d7cb38f7236be1af2a420635c58545f643e3b8022b6fec
  unit_path: ingest/SRC-0011/units/p0223.md
  unit_sha256: 4df5ff267fbe5dbcafc4ac2c7281da40ca9605edfd68d89cdfa08d584ea961ab
- authority: BINDING
  brain_source_id: SRC-0043
  evidence_ref: fria-question-src-0043-p0035-ec-001
  id: brain-e76eea6626adbf20
  locator: Page 35
  resource: /references/src-0043-0bea4d808256b08275777949ba9cb3c70b7d02e4ebb3ac9b205671b1f552d386.md
  unit_file_sha256: 39653650ddd6df4d8b30002799440556d67ffd56899f4600bafb5f9306d9f88b
  unit_path: ingest/SRC-0043/units/p0035.md
  unit_sha256: bb8788e4b98857fd2f44b21395e51a8aaac96801951382e173b159978fb90d8e
status: stable
tags:
- questionnaire
- fria
title: FRIA applicability decision
topic: fria-applicability-decision
type: question
---


# FRIA applicability decision

## Purpose

This question checks whether the project has made and documented the Article 27 applicability determination before first use, after high-risk classification, rather than treating a fundamental-rights impact assessment as universally required or as a late compliance appendix.

Section evidence: [^brain-0bf137bfa342debc] [^brain-74bd179d8d01291d]

## Guidance

Answer "yes" only when the determination records the Article 27(1) actor and system gates: the deployer category, the Article 6(2) and Annex III route, and the Annex III point 2 exclusion. It must also account for the Article 113 route-dependent application date. This question assesses applicability and timing; it does not replace the separate assessment of the FRIA contents.

Section evidence: [^brain-0bf137bfa342debc] [^brain-74bd179d8d01291d] [^brain-e76eea6626adbf20]

## Related knowledge

- [fundamental-right-impact-assessment-fria](/concepts/fundamental-right-impact-assessment-fria.md)
- [eu-ai-act](/concepts/eu-ai-act.md)

## Source references

- SRC-0011, pages 222–223, Article 27(1)–(3), for the actor and system gates, first-use timing and notification framework.
- SRC-0043, page 35, Article 113, for the route-dependent application dates for Article 6(2)/Annex III and Article 6(1)/Annex I systems.


[^brain-0bf137bfa342debc]: [SRC-0011](/references/src-0011-bd7134beb56eaca3b859e272563e464dc234f2daee8f305b942b64eb16fc700c.md); locator: Page 222.
[^brain-74bd179d8d01291d]: [SRC-0011](/references/src-0011-bd7134beb56eaca3b859e272563e464dc234f2daee8f305b942b64eb16fc700c.md); locator: Page 223.
[^brain-e76eea6626adbf20]: [SRC-0043](/references/src-0043-0bea4d808256b08275777949ba9cb3c70b7d02e4ebb3ac9b205671b1f552d386.md); locator: Page 35.
