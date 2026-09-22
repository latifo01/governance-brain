---
aliases:
- AI personal-data trigger
answer_type: boolean
applies_to: AI
brain_id: core-009-personal-data-involvement
brain_sha256: 98acb783c5793d8088fd8056b54abd0e9aa471a0b322516f24dd78586fcfa9b0
depends_on:
  equals: 'yes'
  question_id: core-003-ai-system-determination
domains:
- AI
- DATA_PROTECTION
- DATA_PRIVACY
- LEGAL
evidence_sources:
- AI_LEGAL_GUIDANCE
- DATA_AI_CLASSIFICATION
id: core-009-personal-data-involvement
priority: high
question_en: Is personal data processed at any stage of the system lifecycle, including
  training, testing, input, retrieval, memory, output, logging or monitoring?
question_fr: Des données personnelles sont-elles traitées à une étape quelconque du
  cycle de vie du système, notamment entraînement, test, entrée, récupération, mémoire,
  sortie, journalisation ou monitoring ?
status: stable
tags:
- questionnaire
- common-core
- privacy
title: Personal data involvement
topic: personal-data-involvement
type: question
---


# Personal data involvement

## Purpose

Trigger the applicable privacy module before DPIA, lawful-basis, rights,
retention, security and automated-decision questions.

## Guidance

Consider direct and indirect identifiers, special-category data, inferred data,
prompts, outputs, logs and third-party processing. Record uncertainty for DPO or
legal review.

## Related knowledge

- [gdpr](/concepts/gdpr.md)
- [data-protection-impact-assessments-dpia](/concepts/data-protection-impact-assessments-dpia.md)
- [data-leakage](/concepts/data-leakage.md)

## Source references

- SRC-0010, pages 34-36, for personal-data definitions, processing principles and lawful bases.
- SRC-0010, pages 51-54, for security and DPIA obligations across processing.
