---
id: gov-004-governance-documentation-update-triggers
title: Governance documentation update triggers
type: question
domains: [GOVERNANCE_ACCOUNTABILITY, AUDIT_ASSURANCE, PROCESS]
status: active
aliases: [AI governance record currency]
tags: [questionnaire, documentation, lifecycle, auditability]
evidence_sources: [AI_LEGAL_GUIDANCE, AI_NICE_TO_KNOW]
topic: governance-documentation-update-triggers
priority: medium
applies_to: AI
answer_type: boolean
depends_on:
  question_id: core-003-ai-system-determination
  equals: yes
question_fr: "La documentation de gouvernance définit-elle des déclencheurs de mise à jour, une fréquence de revue et une preuve de version pour rester cohérente avec le système d'IA en fonctionnement ?"
question_en: "Does the governance documentation define update triggers, a review cadence and version evidence so that it stays aligned with the operating AI system?"
---

# Governance documentation update triggers

## Purpose

Check that governance records remain useful after deployment, changes, new
evidence or changes in operating context.

## Guidance

Answer "yes" only when the record identifies events that trigger review, such
as material changes, incidents, new suppliers, changed purpose or operating
conditions, and also names the owner, review cadence, version history and
resulting decision or exception.

## Related knowledge

- [[ai-governance-accountability]]
- [[ai-model-documentation]]
- [[traceability]]

## Source references

- SRC-0002, pages 8 and 10, for update instructions, triggers and lifecycle documentation.
- SRC-0002, page 11, for auditability and independent verification.
- SRC-0009, pages 6 and 28, for lifecycle oversight and policy maintenance context.
