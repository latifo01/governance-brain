---
aliases:
- EU AI Act high-risk outcome
answer_type: choice
applies_to: AI
brain_id: core-013-high-risk-ai-classification
brain_sha256: 1f46564c3aae238c2ddef68551ebcb22c6637f94d6720a0bc58010cf228f2380
depends_on:
  equals: no-prohibited-practice-identified
  question_id: core-011-prohibited-practice-screening
domains:
- AI
- LEGAL
- LEGAL_REGULATORY
- RISK
evidence_sources:
- AI_ACT
- AI_LEGAL_GUIDANCE
id: core-013-high-risk-ai-classification
options:
- label_en: High-risk AI system
  label_fr: Système d’IA à haut risque
  value: high-risk
- label_en: AI system not classified as high-risk
  label_fr: Système d’IA non classé à haut risque
  value: not-high-risk
- label_en: Uncertain
  label_fr: Incertain
  value: uncertain
- label_en: Not assessed
  label_fr: Non évalué
  value: not-assessed
priority: high
question_en: What is the documented conclusion of classifying the system against the
  AI Act high-risk AI system categories?
question_fr: Quelle est la conclusion documentée de la classification du système au
  regard des catégories de systèmes d’IA à haut risque de l’AI Act ?
status: stable
tags:
- questionnaire
- common-core
- ai-act
- classification
title: High-risk AI classification outcome
topic: high-risk-ai-classification
type: question
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

- [high-risk-ai-system-classification](/concepts/high-risk-ai-system-classification.md)
- [eu-ai-act](/concepts/eu-ai-act.md)
- [legal-001-ai-act-classification-record](/concepts/legal-001-ai-act-classification-record.md)
- [fundamental-right-impact-assessment-fria](/concepts/fundamental-right-impact-assessment-fria.md)

## Source references

- SRC-0011, pages 179-181, for Article 6 high-risk classification and derogation documentation.
- SRC-0043, pages 18 and 35, for the 2026-amended Article 6 clarifications and the route-specific application dates (2 December 2027 for Annex III, 2 August 2028 for Annex I).
- SRC-0022, pages 95-97, for training-based explanation of product safety and Annex III high-risk routing.
