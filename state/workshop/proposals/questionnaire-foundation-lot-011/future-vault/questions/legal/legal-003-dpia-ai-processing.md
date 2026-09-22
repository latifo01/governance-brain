---
id: legal-003-dpia-ai-processing
title: DPIA decision for AI processing
type: question
domains: [DATA_PROTECTION, LEGAL, AI, RISK, PROCESS]
status: active
aliases:
  - DPIA for AI processing question
tags:
  - questionnaire
  - dpia
evidence_sources: [AI_LEGAL_GUIDANCE, DATA_AI_CLASSIFICATION]
topic: dpia-ai-processing
priority: high
applies_to: AI
answer_type: boolean
depends_on:
  question_id: core-009-personal-data-involvement
  equals: true
question_fr: "Le projet a-t-il évalué si le traitement de données personnelles lié à l’IA exige une DPIA, indépendamment de la seule classification technique ou AI Act du système ?"
question_en: "Has the project assessed whether the personal-data processing linked to the AI system requires a DPIA, independently of the system’s technical or AI Act classification alone?"
---

# DPIA decision for AI processing

## Purpose

This question checks whether the project has assessed DPIA need based on processing risk rather than assuming that only AI Act high-risk systems require privacy impact assessment.

## Guidance

Answer "yes" only when the assessment considers automated evaluation, special-category or criminal-offence data, large-scale public monitoring, new technologies and contextual risk to natural persons.

## Related knowledge

- [[data-protection-impact-assessments-dpia]]
- [[automatic-decision-making-assessment-adma]]
- [[eu-ai-act]]

## Source references

- SRC-0010, pages 53-54, for GDPR Article 35 DPIA triggers and minimum content.
- SRC-0022, pages 180-183, for training-based explanation of DPIA use in AI projects.
