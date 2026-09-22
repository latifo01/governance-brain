---
id: risk-007-red-team-remediation
title: Red-team remediation
type: question
domains: [AI, RISK, PROCESS]
status: active
aliases:
  - Red-team findings remediation
tags:
  - questionnaire
  - red-teaming
evidence_sources: [AI_NICE_TO_KNOW]
topic: red-team-remediation
priority: medium
applies_to: AI
answer_type: boolean
depends_on: null
question_fr: "Les résultats de red teaming sont-ils reliés à des décisions de lancement, de limitation d’usage, de correction, de retest ou de monitoring ?"
question_en: "Are red-team results linked to release decisions, use restrictions, remediation, retesting or monitoring?"
---

# Red-team remediation

## Purpose

This question checks whether red teaming produces governance action and not only a test report.

## Guidance

Answer "yes" only when findings are tracked to accountable remediation decisions, residual-risk acceptance, retesting or monitoring changes.

## Related Knowledge

- [[red-teaming]]
- [[genai-guardrails]]
- [[ai-model-monitoring]]

## Source References

- SRC-0009, pages 9, 16, 22 and 28, for red-team operations, release-readiness support, tooling and measurement research.
- SRC-0026, page 30, for red teaming and evaluations in model selection and production robustness testing.
- SRC-0039, pages 33-36, for TEVV, measurement, documentation and risk tracking.

