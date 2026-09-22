---
id: legal-004-automated-decision-safeguards
title: Automated decision-making safeguards
type: question
domains: [DATA_PROTECTION, LEGAL, AI, RISK, PROCESS]
status: active
aliases:
  - Article 22 safeguards question
tags:
  - questionnaire
  - automated-decision-making
evidence_sources: [AI_LEGAL_GUIDANCE, DATA_AI_CLASSIFICATION]
topic: automated-decision-making-safeguards
priority: high
applies_to: AI
answer_type: boolean
depends_on:
  question_id: core-012-automated-decision-trigger
  equals: true
question_fr: "Lorsque le système peut produire ou orienter une décision significative concernant une personne, le projet documente-t-il la base applicable et les garanties permettant l’intervention humaine, l’expression du point de vue et la contestation de la décision ?"
question_en: "Where the system may produce or drive a significant decision about a person, does the project document the applicable basis and safeguards enabling human intervention, expression of the person’s view and contestation of the decision?"
---

# Automated decision-making safeguards

## Purpose

This question checks whether Article 22-style safeguards are operationalised when system outputs can materially affect individuals.

## Guidance

Answer "yes" only when the project identifies the controller, decision process, safeguard owners, human intervention channel and contestation process.

## Related knowledge

- [[automatic-decision-making-assessment-adma]]
- [[human-oversight]]
- [[data-protection-impact-assessments-dpia]]

## Source references

- SRC-0010, page 46, for GDPR Article 22 conditions and safeguards.
- SRC-0022, pages 150-152, for training-based explanation of Article 22 assessment and AI oversight implications.
