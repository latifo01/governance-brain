---
id: hallucinations
title: Hallucinations and misinformation
type: knowledge
domains: [AI, RISK]
status: active
aliases:
  - Hallucinations
  - Hallucination
  - Misinformation
  - LLM07
tags:
  - genai-security
  - model-risk
  - misinformation
evidence_sources: [AI_NICE_TO_KNOW]
---

# Hallucinations and misinformation

## Summary

Hallucination is a failure mode in which a language model generates incorrect, unsupported or fabricated content while presenting it with fluency and apparent confidence. In the OWASP Top 10 for LLM Applications 2026 it is treated as one root cause of the broader risk `LLM07:2026 Misinformation`: incorrect, incomplete, unsupported or misleading information that appears credible enough to influence a human decision, an automated workflow or an agent action.

The governance issue is not the error itself but overreliance: humans and systems often treat fluent, confident or well-structured outputs as authoritative. In agentic architectures this overreliance is frequently embedded in system design, because model outputs drive tool calls, code generation, state inference, authorization decisions and inter-agent coordination, turning a false representation into a system-level failure with financial, security, safety or operational consequences.

## Applicability

This note applies to LLM applications, RAG systems, copilots and agentic systems whose outputs are consumed by humans, downstream components or automated actions. Risk increases when outputs feed decision support, workflow triggers, code execution, dependency resolution or agent planning without independent verification.

Documented manifestations include unsupported or false decision support, incorrect state inference in workflows, and fabricated code dependencies: the model may reference non-existent (hallucinated) packages, a supply-chain vector registered under `LLM04:2026 Supply Chain` and demonstrated by package-hallucination research (Spracklen et al., 2025, as cited in SRC-0026).

The CoSAI AI Incident Response Framework classifies hallucination as an AI incident type: leveraging model inaccuracies for harmful purposes, for example false financial forecasts.

## Governance Considerations

- Identify which decisions, workflows or tool actions can be influenced by unverified model output, and gate material ones behind policy checks or human review.
- Distinguish root causes before selecting controls: hallucination, stale or incomplete context, weak grounding, ambiguous prompts, biased or corrupted data, misleading summaries and unvalidated tool outputs each call for different mitigations. Where the root cause is prompt injection, poisoning or supply-chain compromise, those risks should be handled under their own entries.
- Monitor and measure factual grounding in deployed use cases rather than treating fluency as a proxy for correctness.
- Treat hallucinated package names, citations, APIs and entities as security and supply-chain risks, not only quality defects.
- Record hallucination-driven incidents and near misses so response playbooks and tests improve.

## Limits

Misinformation is a failure mode description, not a legal obligation in the local corpus. The sources are security and incident-response frameworks: they support control expectations, not binding requirements for every organization. The prior CDO draft's taxonomy of "factual" versus "faithfulness" hallucination was not found in the local evidence corpus and is therefore not asserted here.

## Related Concepts

- [[prompt-injection]] can deliberately induce misinformation and should be referenced separately when it is the root cause.
- [[ai-model-monitoring]] supports detection of misinformation patterns and drift in deployed systems.
- [[red-teaming]] tests whether grounding and refusal behaviors hold under adversarial prompts.
- [[human-oversight]] defines when a human gate must review model output before material actions.

## Source References

- SRC-0026, OWASP Top 10 for LLM Applications 2026, pages 43-44 (LLM07:2026 Misinformation: definition, root causes including hallucination, overreliance, examples including hallucinated packages) and page 113 (package-hallucination research citation).
- SRC-0028, CoSAI AI Incident Response Framework V1.0, page 11 (hallucination as an AI incident type: leveraging model inaccuracies for harmful purposes) and page 13 (model-output inspection for hallucinations and leakage).
