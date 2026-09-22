---
id: risk-003-model-monitoring-response
title: Monitoring and response
type: question
domains: [AI, RISK, PROCESS]
status: active
aliases:
  - Model monitoring response
tags:
  - questionnaire
  - monitoring
evidence_sources: [AI_REGULATION_INTERNAL, AI_NICE_TO_KNOW]
topic: monitoring-response
priority: high
applies_to: AI
answer_type: boolean
depends_on: null
question_fr: "Le dispositif de monitoring définit-il les signaux suivis, les seuils, les responsables et les actions à déclencher en cas de détérioration, d’usage hors périmètre ou d’incident ?"
question_en: "Does the monitoring arrangement define tracked signals, thresholds, owners and actions to trigger for deterioration, out-of-scope use or incidents?"
---

# Monitoring and response

## Purpose

This question tests whether production monitoring leads to accountable action.

## Guidance

Answer "yes" only when monitoring is tied to named owners, review cadence, thresholds or tolerances, escalation paths, and documented response options such as additional analysis, overlay, recalibration, restricted use, redevelopment or decommissioning.

## Related Knowledge

- [[ai-model-monitoring]]
- [[ai-model-validation]]

## Source References

- SRC-0038 is excluded from this release because the selected units remain pending visual-fidelity review; no evidence binding in this release relies on it.

- SRC-0036, pages 9-11 and 14, for model deterioration, overlays, adjustment, redevelopment and vendor monitoring.
- SRC-0039, pages 35-38, for risk tracking, monitoring plans, appeals, incidents, recovery and change management.
