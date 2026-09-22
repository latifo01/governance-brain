---
id: ai-model-monitoring
title: AI model monitoring
type: knowledge
domains: [AI, RISK, PROCESS]
status: active
aliases:
  - Ongoing model monitoring
  - Model monitoring
  - Monitoring des modèles IA
tags:
  - model-risk
  - monitoring
  - lifecycle
evidence_sources: [AI_REGULATION_INTERNAL, AI_NICE_TO_KNOW]
---

# AI model monitoring

## Summary

AI model monitoring is the ongoing evaluation of whether a model remains appropriately implemented, used within its intended scope and performing as expected as products, exposures, activities, users, data relevance and operating conditions change. Monitoring starts when a model is implemented for business use and continues throughout the model lifecycle.

Monitoring is the operational continuation of [[ai-model-validation]]. It turns validation assumptions into observable controls: performance metrics, data quality checks, process verification, override analysis, benchmark comparisons, incidents, user feedback, and evidence of emergent risks. Without monitoring, approval is frozen at a point in time while the model and its environment keep moving.

## Applicability

Monitoring applies to deployed models and AI systems whose performance, impact or risk profile can change over time. It is especially relevant where model use is material, model outputs inform decisions, the environment is volatile, model updates occur frequently, inputs drift, third-party components are used, or human operators can override outputs.

The banking guidance supporting this note is specific to model risk management in its supervisory scope. NIST AI RMF provides a broader voluntary framework for AI systems, including regular evaluation of trustworthiness, post-deployment monitoring plans, incident response, appeals, change management and input from relevant AI actors.

## Governance Considerations

A monitoring plan should define what is monitored, why it matters, which thresholds or tolerances apply, who reviews the signals, how often review occurs, and what decisions are triggered by issues. The plan should be proportionate to model materiality and should include a clear route from signal detection to accountable action.

Core monitoring activities include:

- checking that data inputs remain accurate, complete, relevant and aligned with the model purpose;
- verifying that code, configuration, data feeds and reports continue to function as designed;
- tracking performance against agreed thresholds and expected ranges;
- monitoring known limitations and conditions where the model may be outside its valid use;
- analyzing overrides, appeals, incidents and user feedback;
- comparing model outputs with suitable internal or external benchmarks where available;
- reviewing whether model changes, context changes or new evidence require additional validation.

Monitoring should be connected to management decisions. A persistent deviation, high override rate, failed benchmark, change in data relevance or field incident should lead to a recorded decision: no action with rationale, temporary limit, additional analysis, overlay, recalibration, redevelopment, decommissioning, or escalation.

For CDO review, the most important test is whether monitoring produces governance memory. The organization should be able to show not only dashboards, but also decisions, owners, thresholds, exceptions, remediation status and lessons learned.

## Limits

Monitoring can miss harms that are not measured, communities that are not represented in feedback channels, or risks that appear outside technical performance metrics. NIST AI RMF therefore points to consultation with domain experts, users, affected communities and other relevant AI actors where appropriate.

Monitoring also does not cure a model that is outside its approved purpose. If the model is extended beyond its original scope, the extension itself should be assessed, documented and, where material, validated.

## Related Concepts

- [[ai-model-validation]] defines the validation baseline that monitoring keeps current.
- [[ai-model-backtesting]] is one outcomes-analysis technique that may be used during monitoring.
- [[ai-model-documentation]] records monitoring design, results, exceptions and decisions.

## Source References

- SRC-0038 is excluded from this release because the selected units remain pending visual-fidelity review; no evidence binding in this release relies on it.

- SRC-0036, SR 26-2, pages 9-11 and 14. Used for current supervisory framing of model use, monitoring performance, model deterioration, overlays, adjustment, redevelopment and vendor model monitoring.
- SRC-0039, NIST AI RMF 1.0, pages 33-38. Used for lifecycle measurement, risk tracking, user/community feedback, regular monitoring, post-deployment monitoring plans, appeals, incident response, recovery and change management.
