---
id: risk-005-prompt-injection-threat-model
title: Prompt injection threat model
type: question
domains: [AI, RISK, PROCESS]
status: active
aliases:
  - Threat model for prompt injection
tags:
  - questionnaire
  - prompt-injection
evidence_sources: [AI_NICE_TO_KNOW]
topic: prompt-injection-threat-model
priority: high
applies_to: AI
answer_type: boolean
depends_on: null
question_fr: "Le système identifie-t-il les surfaces par lesquelles une injection de prompt directe ou indirecte peut influencer le modèle, la mémoire, la récupération documentaire, la planification ou les appels d’outils ?"
question_en: "Does the system identify the surfaces through which direct or indirect prompt injection can influence the model, memory, retrieval, planning or tool calls?"
---

# Prompt injection threat model

## Purpose

This question checks whether prompt injection has been treated as a concrete threat model rather than a generic content-safety concern.

## Guidance

Answer "yes" only when the assessment covers user inputs, retrieved content, documents, tool outputs, persistent memory and agent/tool privileges where applicable.

## Related Knowledge

- [[prompt-injection]]
- [[genai-guardrails]]

## Source References

- SRC-0026, pages 10-12, for direct and indirect prompt injection surfaces, propagation and examples.
- SRC-0027, pages 10-11, for agent goal hijack and indirect prompt injection in agentic systems.

