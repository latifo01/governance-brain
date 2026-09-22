---
aliases:
- Is it an AI system
answer_type: choice
applies_to: ALL
brain_id: core-003-ai-system-determination
brain_sha256: 8b38f8e0176f243ed0f24838decc021281f046a0a6aecc28ac013cd8b1c8fd35
depends_on: null
domains:
- AI
- LEGAL
- LEGAL_REGULATORY
evidence_sources:
- AI_ACT
id: core-003-ai-system-determination
options:
- label_en: 'Yes'
  label_fr: Oui
  value: 'yes'
- label_en: 'No'
  label_fr: Non
  value: 'no'
- label_en: Uncertain
  label_fr: Incertain
  value: uncertain
- label_en: Not assessed
  label_fr: Non évalué
  value: not-assessed
priority: high
question_en: Does the documented assessment conclude that the solution meets the definition
  of an AI system applicable to the project?
question_fr: L’évaluation documentée conclut-elle que la solution répond à la définition
  d’un système d’IA applicable au projet ?
status: stable
tags:
- questionnaire
- common-core
- classification
title: AI system determination
topic: ai-system-determination
type: question
---


# AI system determination

## Purpose

Route the use case into or out of the AI-specific governance catalogue while
preserving uncertainty for legal or technical review.

## Guidance

Record the applicable definition and assess machine basis, autonomy,
adaptiveness, inference, objectives, outputs and influence. A product label is
not a determination. Select `not-assessed` when no documented assessment exists;
never use `no` merely because the assessment is missing.

## Related knowledge

- [ai-system](/concepts/ai-system.md)
- [eu-ai-act](/concepts/eu-ai-act.md)

## Source references

- SRC-0011, page 159, for the binding Article 3(1) AI-system definition in the official regulation.
- SRC-0011, pages 162-163, for the surrounding Article 3 definitions.
- SRC-0017, pages 2-3 and 11-12, for the non-binding Commission interpretation of the definition elements and output categories.
