---
id: red-teaming
title: Red teaming
type: knowledge
domains: [AI, RISK, PROCESS]
status: active
aliases:
  - Red-teaming
  - Red team
  - Tests adversariaux
tags:
  - genai-security
  - testing
  - adversarial-ai
evidence_sources: [AI_NICE_TO_KNOW]
---

# Red teaming

## Summary

Red teaming is an adversarial testing practice used to simulate attacks, misuse or failure scenarios before they occur in production. For AI systems, red teaming probes whether a model, application or agent can be induced to violate intended boundaries, produce unsafe outputs, leak information, misuse tools, bypass guardrails or behave incorrectly in a specific deployment context.

In governance terms, red teaming is a risk-discovery and control-evidence activity. It should inform go/no-go decisions, release gates, mitigations, monitoring and remediation priorities. It is not a replacement for validation, security testing, privacy review, impact assessment or continuous monitoring.

## Applicability

Red teaming is especially relevant for generative AI, multimodal AI, RAG systems, copilots and agentic systems. It is useful when ordinary benchmark tests are unlikely to cover adversarial behavior, multilingual/cultural edge cases, jailbreaks, prompt injection, tool misuse, data leakage, unsafe content, or failures caused by context manipulation.

The practice can occur before deployment, during release readiness, after significant model or system changes, and periodically in production. The intensity should be proportionate to the system's risk, autonomy, data sensitivity, user population, downstream consequences and exposure to untrusted content.

## Governance Considerations

A review-ready red-team program should define scope, adversary goals, excluded actions, safety constraints, test environments, data handling rules, success criteria, reporting format, remediation ownership and retest expectations. Findings should connect to specific controls, not remain as isolated anecdotes.

For GenAI systems, scenarios should include:

- direct prompt injection and jailbreak attempts;
- indirect prompt injection through retrieved content, documents, emails, tool outputs or memory;
- attempts to trigger unauthorized tool calls or goal changes;
- attempts to exfiltrate sensitive data or system instructions;
- multilingual, multimodal and obfuscated attacks where relevant;
- overreliance, unsafe advice or inappropriate human-AI interaction patterns;
- guardrail bypass and post-mitigation regression tests.

Red teaming should produce governance memory: what was tested, what worked, what failed, what was accepted as residual risk, what was remediated, and which release or operating decision changed because of the results. For high-impact systems, independence matters: testers should have enough distance from the build team and enough technical competence to create credible challenge.

## Limits

Red teaming does not prove that a system is safe. It samples plausible attacks and failure modes; it does not exhaust the threat space. Results can become stale as models, prompts, tools, retrieval corpora, policies and attacker techniques change. A clean red-team report should therefore be treated as time-bound evidence, not permanent assurance.

Vendor or platform red-team features can support the process, but the organization remains responsible for deciding whether the scenarios, languages, data, users, tools and deployment context match its own risk profile.

## Related Concepts

- [[genai-guardrails]] are tested and improved through red-team findings.
- [[prompt-injection]] is a priority threat family for GenAI and agentic red teaming.
- [[ai-model-validation]] and [[ai-model-monitoring]] provide the broader assurance and lifecycle control framework.
- [[human-oversight]] can be tested for real authority and resistance to automation bias.

## Source References

- SRC-0009, Microsoft Responsible AI Transparency Report, pages 9, 16, 22 and 28. Used as supporting context for red teaming operations, release readiness, tooling, adversarial techniques and measurement research; extraction is layout-heavy, so these pages are treated as secondary support.
- SRC-0026, OWASP Top 10 for LLM Applications 2026, page 30. Used for AI red teaming and evaluations in third-party model selection and production robustness testing.
- SRC-0027, OWASP Top 10 for Agentic Applications 2026, pages 33 and 38. Used for agentic guardrails, output validation, human gates, behavioral monitoring and containment testing.
- SRC-0039, NIST AI RMF 1.0, pages 33-36. Used for TEVV, measurement, documentation, independent review and risk tracking.

