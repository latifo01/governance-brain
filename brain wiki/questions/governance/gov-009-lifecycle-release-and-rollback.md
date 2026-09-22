---
id: gov-009-lifecycle-release-and-rollback
title: Lifecycle release, rollback and retirement gate
type: question
domains: [GOVERNANCE_ACCOUNTABILITY, PROCESS, MODEL_RISK]
status: active
aliases: [AI lifecycle release gate]
tags: [questionnaire, lifecycle, change-management, release-control]
evidence_sources: [AI_NICE_TO_KNOW, AI_LEGAL_GUIDANCE]
topic: lifecycle-release-rollback
priority: high
applies_to: AI
answer_type: boolean
depends_on:
  question_id: core-003-ai-system-determination
  equals: yes
question_fr: "Le projet exige-t-il, avant toute mise en production ou modification importante, une décision documentée couvrant l'impact du changement, la réévaluation des risques, la validation, les conditions de retour arrière et le suivi ou retrait du système ?"
question_en: "Before production or a material change, does the project require a documented decision covering change impact, risk reassessment, validation, rollback conditions and continued monitoring or retirement?"
---

# Lifecycle release, rollback and retirement gate

## Purpose

Check that material changes do not bypass reassessment, validation, approval, rollback planning or lifecycle closure.

## Guidance

Answer "yes" only when the project identifies material changes, records the responsible decision-maker, performs the required risk and validation review, defines release restrictions or rollback conditions and retains post-release monitoring or retirement evidence.

## Related knowledge

- [[ai-lifecycle]]
- [[ai-lifecycle-change-gates]]
- [[ai-model-validation]]
- [[ai-model-monitoring]]
- [[traceability]]

## Source references

- SRC-0001, page 17; SRC-0002, pages 8 and 10; SRC-0039, page 19.
