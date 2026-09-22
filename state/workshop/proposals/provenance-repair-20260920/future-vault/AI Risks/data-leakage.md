---
id: data-leakage
title: Sensitive information disclosure in AI systems
type: knowledge
domains: [AI, RISK, DATA_PROTECTION]
status: active
aliases:
  - Data leakage
  - Sensitive Information Disclosure
  - LLM02
tags:
  - genai-security
  - privacy
  - data-protection
evidence_sources: [AI_NICE_TO_KNOW, DATA_AI_CLASSIFICATION]
---

# Sensitive information disclosure in AI systems

## Summary

Sensitive information disclosure (`LLM02:2026` in the OWASP Top 10 for LLM Applications 2026) occurs when an LLM-integrated system exposes confidential, regulated, privileged or proprietary data through a channel the data subject, controller or system owner did not authorize. The channel is not only the final answer: tool-call arguments, reasoning traces, retrieved chunks, multimodal output, logs, telemetry, embeddings and observable inference properties (timing, token length, log-probabilities, confidence, cache-hit behavior) are all disclosure surfaces, each subject to the same classification and redaction rules.

The governance issue is that AI systems multiply disclosure surfaces across the lifecycle: training-time memorization that can be extracted verbatim, inference-time disclosure of live context (system prompts, RAG chunks, files, tool outputs, memory or other sessions' data), and exposure of hidden control context that materially increases attacker capability.

## Applicability

This note applies to LLM applications, RAG systems, agents and any AI system that processes sensitive, personal, regulated or proprietary data, including through third-party model APIs.

Documented examples from the local evidence corpus include:

- Memorization of corpus content by models, fine-tunes or LoRA adapters, later reproduced verbatim or in recoverable form; memorization scales with capacity, duplication and context length, and narrow adapters memorize rare examples with high fidelity (SRC-0026, page 18).
- Exposure of sensitive functionality, tool and function schemas, API keys, database credentials or user tokens placed in hidden context (SRC-0026, page 47).
- Disclosure of permissions and user roles through instruction context, which can invite further probing and reveal additional sensitive information (SRC-0026, page 47).
- AI incident response treating unauthorized access and disclosure of restricted information as incident types to detect and respond to (SRC-0028, page 11).

## Governance Considerations

- Classify and minimize sensitive data before it enters prompts, hidden context, retrieval stores or training corpora.
- Apply output classification and redaction rules to every disclosure surface, not only the visible answer: tool arguments, reasoning traces, retrieved chunks, logs, telemetry and embeddings.
- Treat timing, token-length and confidence side channels as disclosure surfaces in high-risk deployments.
- Govern fine-tuning and adapters: rare-example memorization in narrow adapters is a targeted extraction surface distinct from the base model.
- Keep hidden context free of credentials; the real risk is placing sensitive credentials in the hidden context in the first place.
- Prepare incident response for unauthorized access and disclosure events, including what to detect, contain and notify.

## Limits

The OWASP entry is a security-control expectation, not a legal determination. Data protection obligations (lawful basis, notification duties) remain governed by the dedicated privacy notes and the applicable Knowledge Banks; this note does not assert them. The prior CDO draft for this concept was a general cybersecurity article on organizational data leaks and breaches; that framing is not AI-specific and was replaced by the ingest-verified LLM disclosure content, keeping the CDO identifier `data-leakage` for lineage.

## Related Concepts

- [[prompt-injection]] can be used to make an assistant disclose restricted information.
- [[genai-guardrails]] describes output filtering and redaction controls.
- [[human-oversight]] gates high-impact disclosures and actions.
- [[hallucinations]] covers the adjacent misinformation failure mode.

## Source References

- SRC-0026, OWASP Top 10 for LLM Applications 2026, page 18 (LLM02:2026 definition, disclosure surfaces, lifecycle phases) and page 47 (LLM08:2026 boundary: leakage of regulated user or training data belongs to LLM02; examples of sensitive exposure).
- SRC-0028, CoSAI AI Incident Response Framework V1.0, page 11 (unauthorized access and restricted-information disclosure as incident types).
