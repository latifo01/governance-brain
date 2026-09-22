---
aliases:
- Adversarial AI
- Apprentissage automatique adversarial
brain_id: adversarial-machine-learning
brain_sha256: 8226c9291fbdb6431373b8a05c19a97ab10d2360ae67747d2d6da7955d80a273
domains:
- AI_SECURITY
- RISK
- AI
- MODEL_RISK
evidence_sources:
- AI_NICE_TO_KNOW
- AI_REGULATION_INTERNAL
id: adversarial-machine-learning
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
- adversarial-ai
- security
- threat-modeling
title: Adversarial machine learning
type: knowledge
---


# Adversarial machine learning

## Summary

Adversarial machine learning concerns attacks and misuse that deliberately manipulate data, inputs, model behaviour, system context or interfaces to cause an AI system to evade safeguards, reveal information, degrade performance or produce an attacker-chosen outcome. NIST identifies adversarial examples and adversarial use as security and resilience concerns; the risk is broader than a model-only defect because the attack can target data pipelines, prompts, retrieval, tools or deployment context.

Section evidence: [^brain-85c804137bf66818] [^brain-91fa4dab8afef825]

## Applicability

Use this concept in threat modelling and assurance for models, classifiers, generative systems, retrieval systems and agents. The relevant attack surface includes training and fine-tuning data, test data, inputs, model interfaces, external content, tools, memory, outputs and downstream actions. The existing [mitre-atlas](/concepts/mitre-atlas.md) and [prompt-injection](/concepts/prompt-injection.md) notes provide attack vocabulary for specific AI threat paths.

Section evidence: [^brain-85c804137bf66818] [^brain-91fa4dab8afef825]

## Governance Considerations

An adversarial-ML assessment can identify assets, attacker capabilities, trust boundaries, attack paths, likely impact, preventive controls, detection signals, response actions and residual uncertainty. Evaluation should include representative and adversarial conditions, test the system's safeguards and connected privileges, and feed findings into remediation, monitoring and incident response. Controls should be assessed across the system boundary, since model robustness alone cannot protect an over-privileged application or poisoned data source.

Section evidence: [^brain-1baad50e7c71f499] [^brain-67f5acf65c5bac1a]

## Limits

No finite test set establishes that all adversarial behaviour is prevented. Attack techniques and system configurations evolve, and an attack demonstrated in one context may not transfer to another. The referenced NIST material provides a framework and risk context; it does not define a complete attack catalogue, guarantee a defense or create a universal legal obligation.

Section evidence: [^brain-85c804137bf66818] [^brain-91fa4dab8afef825]

## Related Concepts

- [mitre-atlas](/concepts/mitre-atlas.md)
- [prompt-injection](/concepts/prompt-injection.md)
- [red-teaming](/concepts/red-teaming.md)
- [ai-robustness-and-reliability](/concepts/ai-robustness-and-reliability.md)
- [ai-incident-response-resilience](/concepts/ai-incident-response-resilience.md)

## Source References

- SRC-0039, NIST AI RMF 1.0, pages 19-20 (adversarial examples, security, robustness and resilience), pages 34-35 (security, resilience and robustness evaluation).
- SRC-0026 and SRC-0027 provide related reviewed security guidance for prompt injection and agentic attack paths; they are not part of this lot's evidence lock.


[^brain-1baad50e7c71f499]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 35.
[^brain-67f5acf65c5bac1a]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 34.
[^brain-85c804137bf66818]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 20.
[^brain-91fa4dab8afef825]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 19.
