---
id: retrieval-augmented-generation
title: Retrieval-Augmented Generation (RAG)
type: knowledge
domains: [AI, RISK]
status: active
aliases:
  - RAG
  - Retrieval-Augmented Generation
  - Vector and embedding weaknesses
tags:
  - ai-concepts
  - architecture
  - genai-security
evidence_sources: [AI_NICE_TO_KNOW]
---

# Retrieval-Augmented Generation (RAG)

## Summary

Retrieval-Augmented Generation (RAG) is the most familiar case of an architecture family: LLM applications that convert text, images, code or audio into numerical representations (embeddings) and use similarity search to decide what the model sees. The same machinery underlies vector-backed agent memory, semantic caches and deduplication pipelines. Whenever similarity search sits between a data source and the prompt, the embedding layer becomes part of the application's trust boundary.

The governance point is that RAG moves part of the trust boundary into the retrieval layer: access control applied at the application layer after an embedding-space search has already run does not prevent inference from the index itself.

## Applicability

This concept applies to RAG pipelines, vector-backed agent memory, semantic caches and any similarity-search layer feeding model context.

Documented risks from the local evidence corpus:

- **Cross-tenant leakage via shared similarity search**: in multi-tenant deployments, similarity search frequently runs across the full index before access control is applied; an attacker can probe the index with crafted queries and infer the existence, topic and approximate volume of other tenants' documents from result counts, score distributions and timing — without ever seeing the documents, and even when every document is correctly tagged and every API call authenticated.
- **RAG knowledge base poisoning**: a single optimized poisoned text injected per targeted query can override accurate content in a retrieval corpus, and the attack retains high success against paraphrasing, instructional-prevention and detection-based defenses.
- **Data poisoning surface expansion**: organizations increasingly rely on external datasets, RAG pipelines, shared model repositories and agentic workflows, expanding the poisoning surface.

## Governance Considerations

- Treat the retrieval layer as a trust boundary: apply access control and tenant isolation at or before the embedding-space search, not only at the application layer after results return.
- Monitor result-count, score-distribution and timing side channels as disclosure surfaces in multi-tenant deployments (connects to [[data-leakage]]).
- Govern corpus integrity: ingestion pipelines are an attack surface for poisoning; validate and attribute content before it enters the retrieval corpus (connects to [[prompt-injection]] for indirect injection through retrieved content).
- Vectorless retrieval (e.g. BM25-only, LLM-native tree navigation) inherits the non-geometric risks (poisoning, access control) but has no embedding-geometry attack surface — calibrate controls to the architecture.

## Limits

The risk descriptions come from a security framework (OWASP) and document attacker behavior and control expectations; they are not legal determinations. Individual deployment risk assessment requires the system's architecture documentation.

## Related Concepts

- [[generative-ai]] describes the model side of the pipeline.
- [[prompt-injection]] covers indirect injection through retrieved content.
- [[data-leakage]] covers disclosure surfaces including retrieved chunks and embeddings.
- [[agentic-ai]] extends the same machinery to agent memory.

## Source References

- SRC-0026, OWASP Top 10 for LLM Applications 2026, page 50 (LLM09:2026 Vector and Embedding Weaknesses: definition, RAG as most familiar case, trust boundary, cross-tenant leakage example).
- SRC-0026, page 34 (LLM05:2026 Data and Model Poisoning: external datasets and RAG pipelines expanding the poisoning surface; RAG knowledge base poisoning example).
- SRC-0026, page 52 (boundary with agent-memory attacks and vectorless retrieval inheriting non-geometric risks).
