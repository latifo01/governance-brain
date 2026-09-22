---
id: ori-001-ai-incident-response-playbook
title: AI incident response playbook
type: question
domains: [OPERATIONAL_RESILIENCE_INCIDENTS, AI_SECURITY, PROCESS]
status: active
aliases: [AI incident response preparedness]
tags: [questionnaire, incidents, resilience, playbooks]
evidence_sources: [AI_NICE_TO_KNOW, AI_REGULATION_INTERNAL]
topic: ai-incident-response-playbook
priority: high
applies_to: AI
answer_type: boolean
depends_on:
  question_id: core-003-ai-system-determination
  equals: yes
question_fr: "Le système d'IA dispose-t-il d'un plan de réponse aux incidents qui définit les rôles, l'escalade, les playbooks de détection, de confinement, de récupération et les communications ?"
question_en: "Does the AI system have an incident response plan defining roles, escalation, detection, containment, recovery and communications playbooks?"
---

# AI incident response playbook

## Purpose

Establish whether the organisation can coordinate an AI-specific incident from
detection through recovery and improvement.

## Guidance

Answer "yes" only when the plan covers AI-specific incident types, named roles,
severity and escalation criteria, evidence preservation, containment,
recovery validation, communications and post-incident learning. It should cover
the model, data, prompts, tools, dependencies and operating environment.

## Related knowledge

- [[ai-incident-response-resilience]]
- [[ai-governance-accountability]]
- [[ai-model-monitoring]]

## Source references

- SRC-0028, pages 6-7 and 21-24, for the AI incident lifecycle, roles, playbooks and communications.
