---
id: prompt-injection
title: Prompt injection
type: knowledge
domains: [AI, RISK]
status: active
aliases:
  - Prompt injection
  - Injection de prompt
  - Jailbreak
tags:
  - genai-security
  - prompt-injection
  - adversarial-ai
evidence_sources: [AI_NICE_TO_KNOW, AI_REGULATION_INTERNAL]
---

# Prompt injection

## Summary

Prompt injection is a GenAI security weakness in which input processed by a language model changes the model's behavior in a way the application developer did not intend. The input may be supplied directly or carried indirectly through retrieved documents, email, tool output, images, database content or other context.

The governance concern increases when the model can retrieve content, retain memory, call tools, access data or influence downstream actions. A prompt injection can then affect the full chain from context to plan, tool call, output and propagation.

## Applicability

This note applies to LLM applications, retrieval-augmented systems, copilots, AI agents and multi-agent systems that process untrusted or semi-trusted content. OWASP distinguishes direct prompt injection from indirect prompt injection and identifies persistence, context pooling, memory and agentic execution as factors that can increase impact.

Threat modelling should identify delivery surfaces, propagation paths, encoding methods, connected privileges and the systems or data reachable after an injected instruction is followed. Examples describe possible attack paths; they do not establish that every system is vulnerable.

## Governance Considerations

A defensible control design should:

- classify user inputs, retrieved content, tool outputs, memory and external data according to trust and influence;
- validate inputs, connected data, model outputs, tool calls and agent intent outside the model where feasible;
- apply least privilege, scoped access, isolation and policy enforcement to tools and connected systems;
- place human approval gates before high-impact or goal-changing actions and monitor agent activity for anomalies;
- feed detected prompt-injection events into testing, red-team exercises, incident response and control improvement.

These are security guidance and control-design practices. They are not universal legal requirements.

## Limits

OWASP material supports definitions, threat modelling and control design, while the Microsoft report provides research context on indirect prompt injection and possible defenses. The sources do not by themselves establish a binding obligation, a complete defense or a universal legal rule. Applicability, risk acceptance and required controls remain dependent on the system, organization and governing framework.

## Related Concepts

- [[genai-guardrails]]
- [[red-teaming]]
- [[human-oversight]]
- [[ai-model-monitoring]]

## Source References

- SRC-0026, pages 10-12, for the definition of prompt injection, direct and indirect attack surfaces, threat-model dimensions and possible impact paths.
- SRC-0027, pages 10-11 and 33, for agent goal hijack, untrusted input, validation, least privilege, monitoring and human gates.
- SRC-0009, page 28, for research context on indirect prompt injection and possible defenses. This is not treated as primary normative authority.
