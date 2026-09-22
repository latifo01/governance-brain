---
id: core-013-high-risk-ai-classification
title: High-risk AI classification outcome
type: question
domains: [AI, LEGAL, LEGAL_REGULATORY, RISK]
status: active
aliases: [EU AI Act high-risk outcome]
tags: [questionnaire, common-core, ai-act, classification]
evidence_sources: [AI_ACT, AI_LEGAL_GUIDANCE]
topic: high-risk-ai-classification
priority: high
applies_to: AI
answer_type: choice
depends_on:
  question_id: core-011-prohibited-practice-screening
  equals: no-prohibited-practice-identified
question_fr: "Quelle est la conclusion documentée de la classification du système au regard des catégories de systèmes d’IA à haut risque de l’AI Act ?"
question_en: "What is the documented conclusion of classifying the system against the AI Act high-risk AI system categories?"
options:
  - value: high-risk
    label_fr: Système d’IA à haut risque
    label_en: High-risk AI system
  - value: not-high-risk
    label_fr: Système d’IA non classé à haut risque
    label_en: AI system not classified as high-risk
  - value: uncertain
    label_fr: Incertain
    label_en: Uncertain
  - value: not-assessed
    label_fr: Non évalué
    label_en: Not assessed
---

# High-risk AI classification outcome

## Purpose

Route an in-scope AI system to high-risk obligations and impact-assessment
checks without inferring the result from the existence of a classification
record.

## Guidance

Record the applicable organisational role, intended purpose, Annex I or Annex
III route, any profiling, exclusion or derogation, legal reviewer, evidence,
version and effective date. Use `uncertain` or `not-assessed` when the project
does not yet have a defensible conclusion.

## Related knowledge

- [[eu-ai-act]]
- [[legal-001-ai-act-classification-record]]
- [[fundamental-right-impact-assessment-fria]]

## Source references

- SRC-0011, pages 179-181, for Article 6 high-risk classification and derogation documentation.
- SRC-0022, pages 95-97, for training-based explanation of product safety and Annex III high-risk routing.
