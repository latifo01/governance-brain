---
id: adversarial-machine-learning
title: Adversarial machine learning
type: knowledge
domains: [AI_SECURITY, RISK, AI, MODEL_RISK]
status: active
aliases:
  - Adversarial AI
  - Apprentissage automatique adversarial
tags:
  - ai-concepts
  - adversarial-ai
  - security
  - threat-modeling
evidence_sources: [AI_NICE_TO_KNOW, AI_REGULATION_INTERNAL]
---

# Adversarial machine learning

## Summary

Adversarial machine learning concerns attacks and misuse that deliberately manipulate data, inputs, model behaviour, system context or interfaces to cause an AI system to evade safeguards, reveal information, degrade performance or produce an attacker-chosen outcome. NIST identifies adversarial examples and adversarial use as security and resilience concerns; the risk is broader than a model-only defect because the attack can target data pipelines, prompts, retrieval, tools or deployment context.

## Applicability

Use this concept in threat modelling and assurance for models, classifiers, generative systems, retrieval systems and agents. The relevant attack surface includes training and fine-tuning data, test data, inputs, model interfaces, external content, tools, memory, outputs and downstream actions. The existing [[mitre-atlas]] and [[prompt-injection]] notes provide attack vocabulary for specific AI threat paths.

## Governance Considerations

An adversarial-ML assessment can identify assets, attacker capabilities, trust boundaries, attack paths, likely impact, preventive controls, detection signals, response actions and residual uncertainty. Evaluation should include representative and adversarial conditions, test the system's safeguards and connected privileges, and feed findings into remediation, monitoring and incident response. Controls should be assessed across the system boundary, since model robustness alone cannot protect an over-privileged application or poisoned data source.

## Limits

No finite test set establishes that all adversarial behaviour is prevented. Attack techniques and system configurations evolve, and an attack demonstrated in one context may not transfer to another. The referenced NIST material provides a framework and risk context; it does not define a complete attack catalogue, guarantee a defense or create a universal legal obligation.

## Related Concepts

- [[mitre-atlas]]
- [[prompt-injection]]
- [[red-teaming]]
- [[ai-robustness-and-reliability]]
- [[ai-incident-response-resilience]]

## Source References

- SRC-0039, NIST AI RMF 1.0, pages 19-20 (adversarial examples, security, robustness and resilience), pages 34-35 (security, resilience and robustness evaluation).
- SRC-0026 and SRC-0027 provide related reviewed security guidance for prompt injection and agentic attack paths; they are not part of this lot's evidence lock.
