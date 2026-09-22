---
id: explainability-and-interpretability
title: Explainability and interpretability
type: knowledge
domains: [AI, TRANSPARENCY_DISCLOSURE, HUMAN_OVERSIGHT_RESPONSIBLE_AI, RISK]
status: active
aliases:
  - Explainable AI
  - Interpretable AI
  - Explicabilité et interprétabilité
tags:
  - ai-concepts
  - explainability
  - interpretability
  - transparency
evidence_sources: [AI_NICE_TO_KNOW, AI_REGULATION_INTERNAL]
---

# Explainability and interpretability

## Summary

Explainability and interpretability are related but distinct properties of an AI system. In the NIST framing, transparency addresses what happened, explainability addresses how a result was produced, and interpretability addresses why the result has meaning in context for a user. They help people understand, evaluate and appropriately use system outputs, while transparency also covers the surrounding system information and operation.

## Applicability

Use this distinction when designing documentation, user communications, human oversight, contestability, evaluation and incident investigation. The useful explanation depends on the audience, decision context, model, interface, stakes and available evidence. A technical feature-importance output may not explain a composite system decision to an affected person or operator.

## Governance Considerations

An explainability record can state the decision or output context, intended audience, explanation method, relevant inputs or factors, known uncertainty, limitations and the route for human challenge. Interpretability work should be evaluated in the context in which outputs are used, alongside accuracy, robustness, fairness, privacy and human factors. The distinction should remain visible in [[ai-model-transparency]], [[human-oversight]] and [[ai-model-documentation]].

## Limits

An explanation can be incomplete, misleading or detached from the actual model behaviour. Post-hoc explanations do not automatically establish causal validity, fairness, lawful processing or a right result. Some models and sociotechnical interactions remain difficult to interpret; uncertainty and explanation limits should therefore be disclosed rather than hidden behind a confidence claim.

## Related Concepts

- [[ai-model-transparency]]
- [[human-oversight]]
- [[ai-model-validation]]
- [[ai-model-documentation]]
- [[ai-system]]

## Source References

- SRC-0039, NIST AI RMF 1.0, pages 11 (measurement and inscrutability), 19 (validity, robustness and reliability), 35 (explanation, validation, documentation and contextual interpretation).
