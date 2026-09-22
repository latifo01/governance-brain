---
aliases:
- AI Act prohibited-use screening
answer_type: choice
applies_to: AI
brain_id: core-011-prohibited-practice-screening
brain_sha256: 4108b617fde7b3e61b48d7c98352a1322d3af703626ea806d8fee7e14a989653
depends_on:
  equals: true
  question_id: core-010-eu-ai-act-scope
domains:
- AI
- LEGAL
- LEGAL_REGULATORY
- RISK
evidence_sources:
- AI_ACT
- AI_LEGAL_GUIDANCE
id: core-011-prohibited-practice-screening
options:
- label_en: No prohibited practice identified
  label_fr: Aucune pratique interdite identifiée
  value: no-prohibited-practice-identified
- label_en: Potential or confirmed prohibited practice
  label_fr: Pratique interdite potentielle ou confirmée
  value: potential-or-confirmed-prohibited-practice
- label_en: Uncertain
  label_fr: Incertain
  value: uncertain
- label_en: Not assessed
  label_fr: Non évalué
  value: not-assessed
priority: high
question_en: What documented conclusion results from assessing the system and its
  intended use against potentially applicable prohibited AI practices?
question_fr: Quelle conclusion documentée résulte de l’analyse du système et de son
  usage prévu au regard des pratiques d’IA interdites potentiellement applicables
  ?
status: stable
tags:
- questionnaire
- common-core
- ai-act
- prohibited-practice
title: Prohibited AI practice outcome
topic: prohibited-practice-outcome
type: question
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

- [ai-act-prohibited-practices](/concepts/ai-act-prohibited-practices.md)
- [eu-ai-act](/concepts/eu-ai-act.md)
- [legal-001-ai-act-classification-record](/concepts/legal-001-ai-act-classification-record.md)

## Source references

- SRC-0011, pages 172-178, for Article 5 prohibited practices and conditions.
- SRC-0043, pages 18 and 35, for the 2026-amended Article 5 prohibited-content practices applying from 2 December 2026.
- SRC-0022, pages 95-97, for interpretive training on prohibited and high-risk routing.
