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

Prompt injection is a GenAI security weakness in which input processed by a language model changes the model's behavior in a way the application developer did not intend. The input may come directly from a user, or indirectly from retrieved documents, web pages, emails, tool outputs, images, audio, video, persistent memory or other context sources.

The governance issue is that LLM applications often combine instructions and data into the same model context. When the application also gives the model access to tools, documents, memory, APIs or agent workflows, a prompt injection can move from "bad answer" risk to operational risk: disclosure, unauthorized tool invocation, data exfiltration, corrupted memory, fraudulent output or harmful downstream action.

Prompt injection is closely related to [[genai-guardrails]], [[red-teaming]] and [[human-oversight]].

## Applicability

This note applies to LLM applications, RAG systems, copilots, AI agents and multi-agent systems that consume untrusted or semi-trusted content. Risk increases when the model can retrieve documents, call tools, write memory, access user-specific data, execute actions, or influence material decisions.

Direct prompt injection usually comes through a user-controlled interaction. Jailbreaking is a subset where the attacker attempts to make the model violate safety protocols. Indirect prompt injection is more subtle: malicious instructions are embedded in external content that the model later reads, such as a document, email, issue title, web page, database row or tool output.

## Governance Considerations

Prompt injection should be treated as a control-design problem, not only a model-behavior problem. Governance should require a threat model for delivery surfaces, propagation behavior and encoding methods. The organization should identify where untrusted content can enter, whether it can persist in memory or retrieval stores, and what privileges the model or agent has when it reads that content.

Useful governance questions include:

- Which content sources can influence model instructions, retrieval context, memory, planning or tool calls?
- Which sources are untrusted, semi-trusted or trusted-but-compromisable?
- Which tools, APIs, documents or identities can be reached if the model follows injected instructions?
- Are input validation, content filtering, context separation and output validation enforced outside the model?
- Are goal-changing, high-impact or externally visible actions gated by policy or human review?
- Are prompt-injection events logged, investigated and fed back into tests, guardrails and monitoring?

For agentic systems, OWASP frames prompt manipulation as part of broader goal hijacking: manipulated natural-language inputs or poisoned external data can redirect objectives, task selection or decision pathways. Governance should therefore evaluate not only a single model response, but the full chain from input to plan, tool call, output and downstream propagation.

## Limits

No single prompt, model instruction or content filter should be treated as a complete defense. Prompt injection can be delivered through content the user did not see and can be encoded in ways that evade simple text filters. Controls should therefore be layered: least privilege, tool-call validation, retrieval hygiene, monitoring, red-team tests, incident response and human gates for material actions.

The local sources used for this note are security frameworks and transparency material, not binding universal law. They support governance expectations and control design; they do not by themselves establish legal obligations for every organization.

## Related Concepts

- [[genai-guardrails]] describes preventive and detective controls around model inputs, outputs and actions.
- [[red-teaming]] tests whether prompt-injection defenses hold against realistic adversarial techniques.
- [[human-oversight]] defines when human review must have authority, context and competence rather than being a superficial approval step.
- [[ai-model-monitoring]] supports ongoing detection of attack patterns, drift and operational anomalies.

## Source References

- SRC-0026, OWASP Top 10 for LLM Applications 2026, pages 10-12. Used for definition, direct and indirect prompt injection, jailbreaking, delivery surfaces, persistence, tool/action blast radius and common examples.
- SRC-0027, OWASP Top 10 for Agentic Applications 2026, pages 10-11. Used for agent goal hijack, indirect prompt injection in agents, least privilege, human approval, intent validation, source sanitation and monitoring.
- SRC-0009, Microsoft Responsible AI Transparency Report, pages 22 and 28. Used as supporting context for indirect prompt injection evaluation and defense research; not used as primary authority because these pages are layout-heavy in extraction.

