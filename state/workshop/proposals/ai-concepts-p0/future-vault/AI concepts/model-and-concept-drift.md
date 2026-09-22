---
id: model-and-concept-drift
title: Model and concept drift
type: knowledge
domains: [MODEL_RISK, RISK, AI, PROCESS]
status: active
aliases:
  - Model drift
  - Concept drift
  - Dérive du modèle et dérive conceptuelle
tags:
  - ai-concepts
  - drift
  - monitoring
  - lifecycle
evidence_sources: [AI_NICE_TO_KNOW, AI_REGULATION_INTERNAL]
---

# Model and concept drift

## Summary

Model drift is a change in observed model behaviour or performance relative to its validated baseline. Concept drift is a change in the relationship between inputs, context and the outcome the system is intended to predict or support. Related changes can appear in data distributions, user behaviour, operating conditions, model versions, integrations or the meaning of the target. Drift is therefore a monitoring and reassessment signal, not a single metric.

## Applicability

Use this concept for deployed systems whose data, users, environment, purpose, dependencies or model can change. Monitoring can combine input and data-quality signals, outcome and performance measures, subgroup analysis, override and feedback patterns, incident indicators, configuration changes and evidence about the validity of the original assumptions. Third-party and foundation-model changes also require attention to version and service dependencies.

## Governance Considerations

A drift control defines the baseline, monitored signals, thresholds or review criteria, review cadence, data quality and outcome sources, responsible owner, escalation route and possible actions. A signal may lead to investigation, temporary limits, additional evaluation, recalibration, retraining, redevelopment, rollback, retirement or documented acceptance of residual risk. [[ai-model-monitoring]], [[ai-model-validation]] and [[traceability]] connect drift detection to evidence and decisions.

## Limits

Drift detection can miss unobserved outcomes, delayed harms, subgroup effects and changes that are not represented by available metrics. A stable input distribution does not prove stable performance or unchanged meaning, and a detected change does not by itself identify its cause. Thresholds, baselines and response decisions must remain tied to the system's purpose and context.

## Related Concepts

- [[ai-model-monitoring]]
- [[ai-model-validation]]
- [[traceability]]
- [[ai-lifecycle]]
- [[ai-robustness-and-reliability]]

## Source References

- SRC-0036, SR 26-2, pages 6 and 14 (ongoing monitoring, model deterioration, adjustment, redevelopment and vendor-model monitoring within supervisory scope).
- SRC-0039, NIST AI RMF 1.0, pages 33-36 (risk tracking, regular evaluation, deployment-context measures and emergent risks), pages 40-41 (monitoring and TEVV actor tasks).
