---
id: ai-model-validation
title: AI model validation
type: knowledge
domains: [AI, RISK, PROCESS]
status: active
aliases:
  - Model validation
  - Validation des modèles IA
tags:
  - model-risk
  - validation
  - governance
evidence_sources: [AI_REGULATION_INTERNAL, AI_NICE_TO_KNOW]
---

# AI model validation

## Summary

AI model validation is the structured set of activities used to verify whether a model performs as expected for its approved purpose, business use and risk context. In model risk management, validation is not a one-time technical test. It combines review of conceptual soundness, outcomes analysis, ongoing monitoring, documentation quality, model limitations and the governance decisions made when weaknesses are found.

For AI governance, the practical point is simple: a model should not be treated as "validated" merely because it produced acceptable development metrics. The validation record needs to explain what was tested, who challenged it, what limitations remain, what use conditions apply, and what should happen if performance deteriorates. This note is closely related to [[ai-model-backtesting]], [[ai-model-monitoring]] and [[ai-model-documentation]].

## Applicability

This note applies to AI or statistical models that influence material decisions, risk assessments, forecasts, classifications, estimates, controls or reporting. It is directly grounded in banking model risk guidance and in the NIST AI RMF. The banking guidance is sector-specific and should not be generalized into a universal legal duty outside its supervisory scope.

The current local corpus also contains SR 26-2, which supersedes SR 11-7 and narrows the banking guidance scope to specified supervised banking organizations and to traditional statistical and quantitative models plus non-generative, non-agentic AI models. SR 26-2 states that generative AI and agentic AI models are not within its scope, while still indicating that organizations should use their broader risk management and governance practices to determine appropriate controls for tools not covered by that document. For generative or agentic AI, the Brain should therefore use SR 26-2 as a model-risk governance analogue, not as direct binding scope.

## Governance Considerations

Validation should be proportionate to purpose, methodology, materiality, complexity, data availability, frequency of change and the magnitude of potential harm. A validation plan for a low-impact analytical support model does not need the same intensity as a model used in regulated decisioning, capital planning or high-impact automated decisions.

An effective validation file should answer six governance questions:

- What is the model's intended use, and what uses are outside scope?
- Which data, assumptions, methods, implementation components, outputs and reports were tested?
- What evidence supports conceptual soundness, accuracy, robustness, reliability and limitations?
- Who performed the challenge, and were incentives, competence and authority adequate?
- What thresholds or risk tolerances determine acceptable performance?
- What restrictions, compensating controls, remediation actions or escalation routes apply?

The validator should have enough independence to challenge development and business users. Independence is a means to objective review, not a purely organizational box to tick. The review can include work by developers or users, but that work should be critically reviewed by an independent party with sufficient authority, expertise and influence.

Validation decisions should be linked to clear governance outcomes: approve for use, approve with restrictions, require remediation, limit use, require monitoring, recalibrate, redevelop, retire, or escalate to accountable management. A CDO-level review should be alert to a common failure mode: technically detailed validation that never translates into a decision about use, limitations and accountability.

## Limits

Validation cannot eliminate model risk. It can reduce uncertainty, make limitations visible and support better decisions about use. Some models cannot be fully backtested or sensitivity-tested because of limited data, long forecast horizons, limited observability or proprietary third-party constraints. In those cases, the limitation itself becomes a governance issue: use conditions, senior management awareness, compensating controls and monitoring should be explicit.

For AI systems, NIST AI RMF broadens the lens beyond model performance alone. Measurement should include quantitative, qualitative or mixed-method tools, and may need to cover system trustworthiness, human-AI configuration, context of deployment, safety, security, privacy, fairness, explainability, reliability, and stakeholder feedback. This makes validation a lifecycle control, not only a model-development activity.

## Related Concepts

- [[ai-model-backtesting]] defines a specific form of outcomes analysis.
- [[ai-model-monitoring]] covers production monitoring and the treatment of drift, overrides, incidents and emergent risks.
- [[ai-model-documentation]] defines the documentation baseline needed for validation to be repeatable and challengeable.

## Source References

- SRC-0036, SR 26-2, pages 2, 5, 9-11, 13-14. Used for supersession of SR 11-7, scope limits, validation purpose, proportionality, outcomes analysis, ongoing monitoring, documentation and vendor-model limitations.
- SRC-0038, SR 11-7 appendix, pages 9, 12-15, 17-18, 21. Used as historical and detailed model risk management guidance for validation independence, validation components, monitoring, outcomes analysis, governance roles and documentation.
- SRC-0039, NIST AI RMF 1.0, pages 19, 24, 26, 33-36, 38. Used for AI risk measurement, TEVV documentation, trustworthiness characteristics, lifecycle monitoring and risk-response framing.
