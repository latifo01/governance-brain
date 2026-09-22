---
id: gov-003-incident-and-abnormal-behaviour-records
title: Incident and abnormal behaviour records
type: question
domains: [GOVERNANCE_ACCOUNTABILITY, OPERATIONAL_RESILIENCE_INCIDENTS, RISK]
status: active
aliases: [AI incident governance records]
tags: [questionnaire, incidents, monitoring, accountability]
evidence_sources: [AI_LEGAL_GUIDANCE, AI_NICE_TO_KNOW]
topic: incident-and-abnormal-behaviour-records
priority: high
applies_to: AI
answer_type: boolean
depends_on:
  question_id: core-003-ai-system-determination
  equals: yes
question_fr: "Le dispositif conserve-t-il des enregistrements traçables des comportements anormaux, incidents, décisions d'escalade, mesures correctives et enseignements du système d'IA ?"
question_en: "Does the control arrangement retain traceable records of abnormal behaviour, incidents, escalation decisions, remediation and lessons learned for the AI system?"
---

# Incident and abnormal behaviour records

## Purpose

Verify that monitoring and incident handling create governance memory that can
support escalation, remediation and later assurance.

## Guidance

Answer "yes" only when the records identify the system and version, event or
signal, impact and scope, owner, escalation decision, containment or remediation,
status and lessons learned. Include the route for connecting incidents to
monitoring results and future risk or change reviews.

## Related knowledge

- [[ai-governance-accountability]]
- [[ai-model-monitoring]]
- [[atlas-incidents-index]]

## Source references

- SRC-0001, page 17, for monitoring records, abnormal behaviour and incidents.
- SRC-0002, pages 9-10, for accountability and auditability across the AI chain.
- SRC-0009, page 6, for monitoring and incident response in a policy-to-implementation process.
