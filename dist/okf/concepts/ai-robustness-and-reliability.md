---
aliases:
- Robust and reliable AI
- Robustesse et fiabilité de l'IA
brain_id: ai-robustness-and-reliability
brain_sha256: c92c340f2161ef852821d1e19836ebf9d5af05e53214659bbd08632221c3f144
domains:
- AI
- RISK
- MODEL_RISK
- AI_SECURITY
evidence_sources:
- AI_NICE_TO_KNOW
- AI_REGULATION_INTERNAL
id: ai-robustness-and-reliability
sources:
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: aicp0-src-0039-p0035
  id: brain-1baad50e7c71f499
  locator: Page 35
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 9c378153e475afecb6438fda22c12e7a4d0af0fafe7055b4619a1934f41f2add
  unit_path: ingest/SRC-0039/units/p0035.md
  unit_sha256: 7c2df886cf5671889f4e54cfd1e5097145ed938a3c5ac78ed1e4c151c06ebcef
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: aicp0-src-0039-p0034
  id: brain-67f5acf65c5bac1a
  locator: Page 34
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 4a993b22fe7d513c3a4bd0a29af77058c4692f0fdd401aa37d5f8e4cf0acccd4
  unit_path: ingest/SRC-0039/units/p0034.md
  unit_sha256: c721e01ce436180b63165e69fb45c7a2994b59916bbbaf6676777b9efd11701d
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: aicp0-src-0039-p0020
  id: brain-85c804137bf66818
  locator: Page 20
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: a0861e7e22132a30cd5695e2c633451231bd0c3f3d83fbfeb1c1b6945bb8de69
  unit_path: ingest/SRC-0039/units/p0020.md
  unit_sha256: a3ef9d9a9127cc2e8dee3e4d25807177b139dec76e0b4e21c05c622de76263ed
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: aicp0-src-0039-p0019
  id: brain-91fa4dab8afef825
  locator: Page 19
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 4ae38bae64b04241a9a3e3a2009e18379aa9d0f6056878a9ceed639d9f6788c0
  unit_path: ingest/SRC-0039/units/p0019.md
  unit_sha256: cd40c4c5370072e0513212997a18907787d6850e4aec8be6956c902460fda651
status: stable
tags:
- ai-concepts
- robustness
- reliability
- resilience
title: AI robustness and reliability
type: knowledge
---


# AI robustness and reliability

## Summary

AI robustness is the ability of a system to maintain an acceptable level of behaviour under expected variation, changed conditions, reasonable misuse and circumstances beyond the training conditions. Reliability concerns whether the system performs consistently as intended over time and in its operating context. NIST treats validity, accuracy, robustness and reliability as related but distinct contributions to trustworthy AI, and distinguishes resilience from security while recognising their relationship.

Section evidence: [^brain-85c804137bf66818] [^brain-91fa4dab8afef825]

## Applicability

Assess these properties across the model, application, data, interfaces, human-AI configuration and operating environment. Relevant conditions can include distribution changes, missing or noisy inputs, integration faults, unusual users, adversarial use, component failures and recovery from adverse events. The acceptable level depends on intended use, impact, risk tolerance and the system's failure consequences.

Section evidence: [^brain-85c804137bf66818] [^brain-91fa4dab8afef825]

## Governance Considerations

A robustness and reliability record can define operating assumptions, failure modes, stress and boundary tests, performance ranges, safe-failure behaviour, monitoring signals, fallback or recovery paths, ownership and escalation. TEVV should examine deployment-relevant conditions and document residual limitations. Security testing, red teaming, monitoring and incident learning complement performance evaluation. [ai-evaluation-and-tevv](/concepts/ai-evaluation-and-tevv.md), [ai-model-monitoring](/concepts/ai-model-monitoring.md) and [ai-incident-response-resilience](/concepts/ai-incident-response-resilience.md) provide related controls.

Section evidence: [^brain-1baad50e7c71f499] [^brain-67f5acf65c5bac1a]

## Limits

Robustness and reliability are context-dependent; a result under one distribution, threat model or operating configuration cannot establish universal performance. Resilience after an incident does not remove the underlying vulnerability, and security controls do not guarantee reliable outputs. Unknown failure modes and sparse feedback should remain explicit uncertainties.

Section evidence: [^brain-85c804137bf66818] [^brain-91fa4dab8afef825]

## Related Concepts

- [ai-evaluation-and-tevv](/concepts/ai-evaluation-and-tevv.md)
- [ai-model-monitoring](/concepts/ai-model-monitoring.md)
- [red-teaming](/concepts/red-teaming.md)
- [ai-incident-response-resilience](/concepts/ai-incident-response-resilience.md)
- [adversarial-machine-learning](/concepts/adversarial-machine-learning.md)

## Source References

- SRC-0039, NIST AI RMF 1.0, pages 19-20 (robustness, reliability, security and resilience), pages 34-35 (validity, reliability, safety, robustness and resilience measures).
- SRC-0036, SR 26-2, pages 6-11 and 14 (model performance, monitoring, deterioration, adjustment and limitations within supervisory scope).


[^brain-1baad50e7c71f499]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 35.
[^brain-67f5acf65c5bac1a]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 34.
[^brain-85c804137bf66818]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 20.
[^brain-91fa4dab8afef825]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 19.
