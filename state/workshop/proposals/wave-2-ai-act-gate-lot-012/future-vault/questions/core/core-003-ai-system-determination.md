---
id: core-003-ai-system-determination
title: AI system determination
type: question
domains: [AI, LEGAL, LEGAL_REGULATORY]
status: active
aliases: [Is it an AI system]
tags: [questionnaire, common-core, classification]
evidence_sources: [AI_ACT]
topic: ai-system-determination
priority: high
applies_to: ALL
answer_type: choice
depends_on: null
question_fr: "L’évaluation documentée conclut-elle que la solution répond à la définition d’un système d’IA applicable au projet ?"
question_en: "Does the documented assessment conclude that the solution meets the definition of an AI system applicable to the project?"
options:
  - value: "yes"
    label_fr: Oui
    label_en: "Yes"
  - value: "no"
    label_fr: Non
    label_en: "No"
  - value: "uncertain"
    label_fr: Incertain
    label_en: Uncertain
  - value: "not-assessed"
    label_fr: Non évalué
    label_en: Not assessed
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

- [[ai-system]]
- [[eu-ai-act]]

## Source references

- SRC-0011, page 159, for the binding Article 3(1) AI-system definition in the official regulation.
- SRC-0011, pages 162-163, for the surrounding Article 3 actor and system definitions.
- SRC-0017, pages 2-3 and 11-12, for the non-binding Commission interpretation of the definition elements and output categories.
