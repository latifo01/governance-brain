---
id: legal-002-fria-trigger
title: FRIA applicability decision
type: question
domains: [AI, LEGAL, RISK, PROCESS]
status: active
aliases:
  - Fundamental rights impact assessment trigger question
tags:
  - questionnaire
  - fria
evidence_sources: [AI_ACT, AI_LEGAL_GUIDANCE]
topic: fria-applicability-decision
priority: high
applies_to: AI
answer_type: boolean
depends_on:
  question_id: core-013-high-risk-ai-classification
  equals: high-risk
question_fr: "Avant la première utilisation, le projet a-t-il déterminé, pour le système d’IA à haut risque visé à l’article 6, paragraphe 2, si l’obligation d’analyse d’impact sur les droits fondamentaux de l’article 27 s’applique à son rôle de déployeur, en tenant compte des catégories de déployeurs, de l’exclusion de l’annexe III, point 2, et de la date d’application pertinente de l’article 113 ?"
question_en: "Before first use, has the project determined, for the high-risk AI system covered by Article 6(2), whether the Article 27 fundamental-rights impact assessment obligation applies to its deployer role, taking into account the deployer categories, the Annex III point 2 exclusion and the relevant Article 113 application date?"
---

# FRIA applicability decision

## Purpose

This question checks whether the project has made and documented the Article 27 applicability determination before first use, after high-risk classification, rather than treating a fundamental-rights impact assessment as universally required or as a late compliance appendix.

## Guidance

Answer "yes" only when the determination records the Article 27(1) actor and system gates: the deployer category, the Article 6(2) and Annex III route, and the Annex III point 2 exclusion. It must also account for the Article 113 route-dependent application date. This question assesses applicability and timing; it does not replace the separate assessment of the FRIA contents.

## Related knowledge

- [[fundamental-right-impact-assessment-fria]]
- [[eu-ai-act]]

## Source references

- SRC-0011, pages 222–223, Article 27(1)–(3), for the actor and system gates, first-use timing and notification framework.
- SRC-0043, page 35, Article 113, for the route-dependent application dates for Article 6(2)/Annex III and Article 6(1)/Annex I systems.
