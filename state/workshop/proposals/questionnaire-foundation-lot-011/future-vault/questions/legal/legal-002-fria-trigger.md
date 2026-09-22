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
question_fr: "Le projet a-t-il déterminé, avant le déploiement, si une analyse d’impact sur les droits fondamentaux est requise pour le système d’IA à haut risque et le rôle réel du déployeur ?"
question_en: "Has the project determined, before deployment, whether a fundamental rights impact assessment is required for the high-risk AI system and the deployer’s actual role?"
---

# FRIA applicability decision

## Purpose

This question checks that FRIA applicability is assessed before deployment and after AI Act high-risk classification, rather than added late as a compliance appendix.

## Guidance

Answer "yes" only when the assessment considers the deployer category, Annex III route, excluded categories and the specific use context.

## Related knowledge

- [[fundamental-right-impact-assessment-fria]]
- [[eu-ai-act]]

## Source references

- SRC-0011, pages 222-224, for Article 27 FRIA trigger, required assessment content and DPIA relationship.
- SRC-0022, page 183, for training-based explanation of FRIA applicability before initial deployment.
