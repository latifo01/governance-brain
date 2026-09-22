---
id: gov-002-lifecycle-change-reassessment
title: Lifecycle change and risk reassessment
type: question
domains: [GOVERNANCE_ACCOUNTABILITY, PROCESS, MODEL_RISK]
status: active
aliases: [AI change impact review]
tags: [questionnaire, lifecycle, change-management, risk]
evidence_sources: [AI_LEGAL_GUIDANCE, AI_NICE_TO_KNOW]
topic: lifecycle-change-reassessment
priority: high
applies_to: AI
answer_type: boolean
depends_on:
  question_id: core-003-ai-system-determination
  equals: yes
question_fr: "Le processus de changement exige-t-il une réévaluation documentée du risque, de la finalité, du périmètre, des contrôles et des preuves avant une modification importante du système d'IA ?"
question_en: "Does the change process require a documented reassessment of risk, purpose, scope, controls and evidence before a material change to the AI system?"
---

# Lifecycle change and risk reassessment

## Purpose

Check that material changes do not bypass the governance, testing and evidence
decisions that applied to the approved system.

## Guidance

Answer "yes" only when the change process identifies material changes to data,
code, models, libraries, configuration, suppliers, interfaces or operating
context, and records the resulting risk reassessment, approval, restrictions or
additional validation before release.

## Related knowledge

- [[ai-governance-accountability]]
- [[ai-model-monitoring]]
- [[ai-model-validation]]
- [[traceability]]

## Source references

- SRC-0001, page 17, for version control, reassessment and monitoring after implementation changes.
- SRC-0002, pages 8 and 10, for update triggers and lifecycle documentation.
- SRC-0009, page 6, for linking policy, engineering, launch and monitoring activities.
