---
id: ai-robustness-and-reliability
title: AI robustness and reliability
type: knowledge
domains: [AI, RISK, MODEL_RISK, AI_SECURITY]
status: active
aliases:
  - Robust and reliable AI
  - Robustesse et fiabilité de l'IA
tags:
  - ai-concepts
  - robustness
  - reliability
  - resilience
evidence_sources: [AI_NICE_TO_KNOW, AI_REGULATION_INTERNAL]
---

# AI robustness and reliability

## Summary

AI robustness is the ability of a system to maintain an acceptable level of behaviour under expected variation, changed conditions, reasonable misuse and circumstances beyond the training conditions. Reliability concerns whether the system performs consistently as intended over time and in its operating context. NIST treats validity, accuracy, robustness and reliability as related but distinct contributions to trustworthy AI, and distinguishes resilience from security while recognising their relationship.

## Applicability

Assess these properties across the model, application, data, interfaces, human-AI configuration and operating environment. Relevant conditions can include distribution changes, missing or noisy inputs, integration faults, unusual users, adversarial use, component failures and recovery from adverse events. The acceptable level depends on intended use, impact, risk tolerance and the system's failure consequences.

## Governance Considerations

A robustness and reliability record can define operating assumptions, failure modes, stress and boundary tests, performance ranges, safe-failure behaviour, monitoring signals, fallback or recovery paths, ownership and escalation. TEVV should examine deployment-relevant conditions and document residual limitations. Security testing, red teaming, monitoring and incident learning complement performance evaluation. [[ai-evaluation-and-tevv]], [[ai-model-monitoring]] and [[ai-incident-response-resilience]] provide related controls.

## Limits

Robustness and reliability are context-dependent; a result under one distribution, threat model or operating configuration cannot establish universal performance. Resilience after an incident does not remove the underlying vulnerability, and security controls do not guarantee reliable outputs. Unknown failure modes and sparse feedback should remain explicit uncertainties.

## Related Concepts

- [[ai-evaluation-and-tevv]]
- [[ai-model-monitoring]]
- [[red-teaming]]
- [[ai-incident-response-resilience]]
- [[adversarial-machine-learning]]

## Source References

- SRC-0039, NIST AI RMF 1.0, pages 19-20 (robustness, reliability, security and resilience), pages 34-35 (validity, reliability, safety, robustness and resilience measures).
- SRC-0036, SR 26-2, pages 6-11 and 14 (model performance, monitoring, deterioration, adjustment and limitations within supervisory scope).
