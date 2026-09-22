---
aliases:
- DPIA for AI processing question
answer_type: boolean
applies_to: AI
brain_id: legal-003-dpia-ai-processing
brain_sha256: 321ba0bf97c5a947eb5c2ee973d79038c955514bd24ae1ac6384e5c83454ebf9
depends_on:
  equals: true
  question_id: core-009-personal-data-involvement
domains:
- DATA_PROTECTION
- LEGAL
- AI
- RISK
- PROCESS
evidence_sources:
- AI_LEGAL_GUIDANCE
- DATA_AI_CLASSIFICATION
id: legal-003-dpia-ai-processing
priority: high
question_en: Has the project assessed whether the personal-data processing linked
  to the AI system requires a DPIA, independently of the system’s technical or AI
  Act classification alone?
question_fr: Le projet a-t-il évalué si le traitement de données personnelles lié
  à l’IA exige une DPIA, indépendamment de la seule classification technique ou AI
  Act du système ?
status: stable
tags:
- questionnaire
- dpia
title: DPIA decision for AI processing
topic: dpia-ai-processing
type: question
---


# DPIA decision for AI processing

## Purpose

This question checks whether the project has assessed DPIA need based on processing risk rather than assuming that only AI Act high-risk systems require privacy impact assessment.

## Guidance

Answer "yes" only when the assessment considers automated evaluation, special-category or criminal-offence data, large-scale public monitoring, new technologies and contextual risk to natural persons.

## Related knowledge

- [data-protection-impact-assessments-dpia](/concepts/data-protection-impact-assessments-dpia.md)
- [automatic-decision-making-assessment-adma](/concepts/automatic-decision-making-assessment-adma.md)
- [eu-ai-act](/concepts/eu-ai-act.md)

## Source references

- SRC-0010, pages 53-54, for GDPR Article 35 DPIA triggers and minimum content.
- SRC-0022, pages 180-183, for training-based explanation of DPIA use in AI projects.
