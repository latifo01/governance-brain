---
aliases:
- Explainable AI
- Interpretable AI
- Explicabilité et interprétabilité
brain_id: explainability-and-interpretability
brain_sha256: 67754e03a23d3567125972c47cf65e6ab36de280c94eba17252078ffd8fefe84
domains:
- AI
- TRANSPARENCY_DISCLOSURE
- HUMAN_OVERSIGHT_RESPONSIBLE_AI
- RISK
evidence_sources:
- AI_NICE_TO_KNOW
- AI_REGULATION_INTERNAL
id: explainability-and-interpretability
sources:
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: aicp0-src-0039-p0011
  id: brain-1357afe523720eb1
  locator: Page 11
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 52e81952f5463689e68ee6ae4d3aade3422ab9509511ffe19f08aee7a5c7cc14
  unit_path: ingest/SRC-0039/units/p0011.md
  unit_sha256: 2367ab80f6e243ca3b15de05416e05e5e8a5653472c8bc505d40adaca2a29770
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
- explainability
- interpretability
- transparency
title: Explainability and interpretability
type: knowledge
---


# Explainability and interpretability

## Summary

Explainability and interpretability are related but distinct properties of an AI system. In the NIST framing, transparency addresses what happened, explainability addresses how a result was produced, and interpretability addresses why the result has meaning in context for a user. They help people understand, evaluate and appropriately use system outputs, while transparency also covers the surrounding system information and operation.

Section evidence: [^brain-1357afe523720eb1] [^brain-1baad50e7c71f499]

## Applicability

Use this distinction when designing documentation, user communications, human oversight, contestability, evaluation and incident investigation. The useful explanation depends on the audience, decision context, model, interface, stakes and available evidence. A technical feature-importance output may not explain a composite system decision to an affected person or operator.

Section evidence: [^brain-1baad50e7c71f499]

## Governance Considerations

An explainability record can state the decision or output context, intended audience, explanation method, relevant inputs or factors, known uncertainty, limitations and the route for human challenge. Interpretability work should be evaluated in the context in which outputs are used, alongside accuracy, robustness, fairness, privacy and human factors. The distinction should remain visible in [ai-model-transparency](/concepts/ai-model-transparency.md), [human-oversight](/concepts/human-oversight.md) and [ai-model-documentation](/concepts/ai-model-documentation.md).

Section evidence: [^brain-1baad50e7c71f499]

## Limits

An explanation can be incomplete, misleading or detached from the actual model behaviour. Post-hoc explanations do not automatically establish causal validity, fairness, lawful processing or a right result. Some models and sociotechnical interactions remain difficult to interpret; uncertainty and explanation limits should therefore be disclosed rather than hidden behind a confidence claim.

Section evidence: [^brain-1357afe523720eb1] [^brain-91fa4dab8afef825]

## Related Concepts

- [ai-model-transparency](/concepts/ai-model-transparency.md)
- [human-oversight](/concepts/human-oversight.md)
- [ai-model-validation](/concepts/ai-model-validation.md)
- [ai-model-documentation](/concepts/ai-model-documentation.md)
- [ai-system](/concepts/ai-system.md)

## Source References

- SRC-0039, NIST AI RMF 1.0, pages 11 (measurement and inscrutability), 19 (validity, robustness and reliability), 35 (explanation, validation, documentation and contextual interpretation).


[^brain-1357afe523720eb1]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 11.
[^brain-1baad50e7c71f499]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 35.
[^brain-91fa4dab8afef825]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 19.
