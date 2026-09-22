---
id: core-009-personal-data-involvement
title: Personal data involvement
type: question
domains: [AI, DATA_PROTECTION, DATA_PRIVACY, LEGAL]
status: active
aliases: [AI personal-data trigger]
tags: [questionnaire, common-core, privacy]
evidence_sources: [AI_LEGAL_GUIDANCE, DATA_AI_CLASSIFICATION]
topic: personal-data-involvement
priority: high
applies_to: AI
answer_type: boolean
depends_on:
  question_id: core-003-ai-system-determination
  equals: "yes"
question_fr: "Des données personnelles sont-elles traitées à une étape quelconque du cycle de vie du système, notamment entraînement, test, entrée, récupération, mémoire, sortie, journalisation ou monitoring ?"
question_en: "Is personal data processed at any stage of the system lifecycle, including training, testing, input, retrieval, memory, output, logging or monitoring?"
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

- [[gdpr]]
- [[data-protection-impact-assessments-dpia]]
- [[data-leakage]]

## Source references

- SRC-0010, pages 34-36, for personal-data definitions, processing principles and lawful bases.
- SRC-0010, pages 51-54, for security and DPIA obligations across processing.
