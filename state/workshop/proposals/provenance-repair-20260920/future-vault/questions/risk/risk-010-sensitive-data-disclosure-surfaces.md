---
id: risk-010-sensitive-data-disclosure-surfaces
title: Sensitive data disclosure surfaces
type: question
domains: [AI, RISK, DATA_PROTECTION, PROCESS]
status: active
aliases:
  - Inventory of AI disclosure surfaces for sensitive data
tags:
  - questionnaire
  - data-leakage
  - privacy
evidence_sources: [AI_NICE_TO_KNOW, DATA_AI_CLASSIFICATION]
topic: sensitive-data-disclosure-surfaces
priority: high
applies_to: AI
answer_type: boolean
depends_on: null
question_fr: "L’inventaire des surfaces de divulgation de données sensibles couvre-t-il les arguments d’appels d’outils, les traces de raisonnement, les fragments récupérés, les journaux, la télémétrie et les embeddings, avec des règles communes de classification et de censure ?"
question_en: "Does the inventory of sensitive-data disclosure surfaces cover tool-call arguments, reasoning traces, retrieved chunks, logs, telemetry and embeddings, with common classification and redaction rules?"
---

# Sensitive data disclosure surfaces

## Purpose

This question checks whether disclosure controls cover every AI output channel and not only the visible final answer.

## Guidance

Answer "yes" only when tool-call arguments, reasoning traces, retrieved chunks, logs, telemetry and embeddings are inventoried as disclosure surfaces and subject to the same data-classification and redaction rules as user-visible output.

## Related Knowledge

- [[data-leakage]]

## Source References

- SRC-0026, OWASP Top 10 for LLM Applications 2026, page 18, for the definition of disclosure surfaces beyond the final answer.
- SRC-0026, page 47, for keeping credentials out of hidden context and treating disclosure of permissions as a probe vector.
