---
id: core-011-prohibited-practice-screening
title: Prohibited AI practice outcome
type: question
domains: [AI, LEGAL, LEGAL_REGULATORY, RISK]
status: active
aliases: [AI Act prohibited-use screening]
tags: [questionnaire, common-core, ai-act, prohibited-practice]
evidence_sources: [AI_ACT, AI_LEGAL_GUIDANCE]
topic: prohibited-practice-outcome
priority: high
applies_to: AI
answer_type: choice
depends_on:
  question_id: core-010-eu-ai-act-scope
  equals: true
question_fr: "Quelle conclusion documentée résulte de l’analyse du système et de son usage prévu au regard des pratiques d’IA interdites potentiellement applicables ?"
question_en: "What documented conclusion results from assessing the system and its intended use against potentially applicable prohibited AI practices?"
options:
  - value: no-prohibited-practice-identified
    label_fr: Aucune pratique interdite identifiée
    label_en: No prohibited practice identified
  - value: potential-or-confirmed-prohibited-practice
    label_fr: Pratique interdite potentielle ou confirmée
    label_en: Potential or confirmed prohibited practice
  - value: uncertain
    label_fr: Incertain
    label_en: Uncertain
  - value: not-assessed
    label_fr: Non évalué
    label_en: Not assessed
---

# Prohibited AI practice outcome

## Purpose

Record the prohibited-practice decision before high-risk classification and
downstream control selection.

## Guidance

Select the documented outcome only when the analysis records the use context,
potentially relevant Article 5 category, evidence, legal reviewer, conclusion
and redesign or stop decision where needed. Use `uncertain` or `not-assessed`
rather than treating missing analysis as a safe outcome.

## Related knowledge

- [[ai-act-prohibited-practices]]
- [[eu-ai-act]]
- [[legal-001-ai-act-classification-record]]

## Source references

- SRC-0011, pages 172-178, for Article 5 prohibited practices and conditions.
- SRC-0043, pages 18 and 35, for the 2026-amended Article 5 prohibited-content practices applying from 2 December 2026.
- SRC-0022, pages 95-97, for interpretive training on prohibited and high-risk routing.
