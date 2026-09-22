---
id: legal-005-data-subject-rights-readiness
title: Data subject rights readiness
type: question
domains: [DATA_PROTECTION, LEGAL, AI, PROCESS]
status: active
aliases:
  - AI data subject rights question
  - Data subject rights routing question
tags:
  - questionnaire
  - data-subject-rights
  - ai-governance
evidence_sources: [AI_LEGAL_GUIDANCE, DATA_AI_CLASSIFICATION]
topic: data-subject-rights-readiness
priority: high
applies_to: AI
answer_type: boolean
depends_on:
  question_id: core-009-personal-data-involvement
  equals: true
question_fr: "Le projet a-t-il documenté les droits des personnes applicables au traitement IA, leurs responsables, les voies d'escalade et les garanties liées aux décisions automatisées lorsqu'elles sont pertinentes ?"
question_en: "Has the project documented the data subject rights applicable to the AI processing, their owners, escalation routes and safeguards for automated decisions where relevant?"
---

# Data subject rights readiness

## Purpose

This question checks whether the project has converted the applicable GDPR
rights into a traceable governance route for the AI processing in scope.

## Guidance

Answer "yes" only when the project has identified the relevant rights and
conditions, named the response owner, mapped the systems and recipients needed
to handle requests, and documented the route for automated decision-making
safeguards when Article 22 may apply. Do not treat the presence of a privacy
notice alone as evidence of operational readiness.

## Related knowledge

- [[data-subject-rights-ai]]
- [[data-subject-access-requests]]
- [[gdpr-article-22-automated-decision-making]]
- [[data-protection-impact-assessments-dpia]]

## Source references

- SRC-0010, pages 43-46, for the GDPR rights map and Article 22 safeguards.
