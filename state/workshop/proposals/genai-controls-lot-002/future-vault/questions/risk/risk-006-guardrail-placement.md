---
id: risk-006-guardrail-placement
title: Guardrail placement
type: question
domains: [AI, RISK, PROCESS]
status: active
aliases:
  - Guardrail architecture
tags:
  - questionnaire
  - guardrails
evidence_sources: [AI_NICE_TO_KNOW, AI_REGULATION_INTERNAL]
topic: guardrail-placement
priority: high
applies_to: AI
answer_type: boolean
depends_on: null
question_fr: "Les garde-fous sont-ils placés aux points de contrôle pertinents, notamment avant le modèle, après la récupération, avant les appels d’outils, après la sortie du modèle et avant toute propagation aval ?"
question_en: "Are guardrails placed at the relevant control points, including before the model, after retrieval, before tool calls, after model output and before downstream propagation?"
---

# Guardrail placement

## Purpose

This question assesses whether guardrails are embedded in the system architecture rather than treated as a single model-level instruction.

## Guidance

Answer "yes" only when the architecture shows where controls operate, which risks each control addresses, who owns exceptions, and how failures are monitored and remediated.

## Related Knowledge

- [[genai-guardrails]]
- [[prompt-injection]]

## Source References

- SRC-0027, pages 11, 33 and 38, for input safeguards, human approval, policy gates, output validation, blast-radius controls and monitoring.
- SRC-0039, pages 32 and 35-38, for documented controls, measurement and risk treatment.

