---
aliases:
- RAG
- Retrieval-Augmented Generation
- Vector and embedding weaknesses
brain_id: retrieval-augmented-generation
brain_sha256: d5727fc8b234c68269f603a506fdaa8efd63eab4a80f8c29d93bfc9e2917df2a
domains:
- AI
- RISK
evidence_sources:
- AI_NICE_TO_KNOW
id: retrieval-augmented-generation
sources:
- authority: GUIDANCE
  brain_source_id: SRC-0026
  evidence_ref: concepts-lin4-src-0026-p0050
  id: brain-41c44cae6e0ba80b
  locator: Page 50
  resource: /references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md
  unit_file_sha256: a4f745833a21720398a71d9cefc1f5f8627e75384f693536f9c6352e1de07399
  unit_path: ingest/SRC-0026/units/p0050.md
  unit_sha256: b3278ab44440c5a90c0bc436e636fbec7d15a2b0458f737ad95df73f4b3fae0a
- authority: GUIDANCE
  brain_source_id: SRC-0026
  evidence_ref: concepts-lin4-src-0026-p0034
  id: brain-52d87eb6ddbfef16
  locator: Page 34
  resource: /references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md
  unit_file_sha256: c9763d9ac2e09800d3063cf311a2b24697bee066c8149fce0f8179a9b54899dd
  unit_path: ingest/SRC-0026/units/p0034.md
  unit_sha256: 9037a1a9b2303ac5cfb92ce49349b96fdb2b7b8ec2443eacfc3037c384dc5bf6
- authority: GUIDANCE
  brain_source_id: SRC-0026
  evidence_ref: concepts-lin4-src-0026-p0052
  id: brain-fb22e2219c5d38dc
  locator: Page 52
  resource: /references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md
  unit_file_sha256: ab565519d08465bcafc5b494a14ba4c4e791d1281e8245fcf1bb61608dbe1c48
  unit_path: ingest/SRC-0026/units/p0052.md
  unit_sha256: ce72f6a5f742ecdd54ca093134d7d41f9d2c8a0dd94e420d826dd7ae6598d04f
status: stable
tags:
- ai-concepts
- architecture
- genai-security
title: Retrieval-Augmented Generation (RAG)
type: knowledge
---


# Retrieval-Augmented Generation (RAG)

## Summary

Retrieval-Augmented Generation (RAG) is the most familiar case of an architecture family: LLM applications that convert text, images, code or audio into numerical representations (embeddings) and use similarity search to decide what the model sees. The same machinery underlies vector-backed agent memory, semantic caches and deduplication pipelines. Whenever similarity search sits between a data source and the prompt, the embedding layer becomes part of the application's trust boundary.

The governance point is that RAG moves part of the trust boundary into the retrieval layer: access control applied at the application layer after an embedding-space search has already run does not prevent inference from the index itself.

Section evidence: [^brain-41c44cae6e0ba80b]

## Applicability

This concept applies to RAG pipelines, vector-backed agent memory, semantic caches and any similarity-search layer feeding model context.

Documented risks from the local evidence corpus:

- **Cross-tenant leakage via shared similarity search**: in multi-tenant deployments, similarity search frequently runs across the full index before access control is applied; an attacker can probe the index with crafted queries and infer the existence, topic and approximate volume of other tenants' documents from result counts, score distributions and timing — without ever seeing the documents, and even when every document is correctly tagged and every API call authenticated.
- **RAG knowledge base poisoning**: a single optimized poisoned text injected per targeted query can override accurate content in a retrieval corpus, and the attack retains high success against paraphrasing, instructional-prevention and detection-based defenses.
- **Data poisoning surface expansion**: organizations increasingly rely on external datasets, RAG pipelines, shared model repositories and agentic workflows, expanding the poisoning surface.

Section evidence: [^brain-41c44cae6e0ba80b] [^brain-52d87eb6ddbfef16]

## Governance Considerations

- Treat the retrieval layer as a trust boundary: apply access control and tenant isolation at or before the embedding-space search, not only at the application layer after results return.
- Monitor result-count, score-distribution and timing side channels as disclosure surfaces in multi-tenant deployments (connects to [data-leakage](/concepts/data-leakage.md)).
- Govern corpus integrity: ingestion pipelines are an attack surface for poisoning; validate and attribute content before it enters the retrieval corpus (connects to [prompt-injection](/concepts/prompt-injection.md) for indirect injection through retrieved content).
- Vectorless retrieval (e.g. BM25-only, LLM-native tree navigation) inherits the non-geometric risks (poisoning, access control) but has no embedding-geometry attack surface — calibrate controls to the architecture.

Section evidence: [^brain-41c44cae6e0ba80b] [^brain-52d87eb6ddbfef16] [^brain-fb22e2219c5d38dc]

## Limits

The risk descriptions come from a security framework (OWASP) and document attacker behavior and control expectations; they are not legal determinations. Individual deployment risk assessment requires the system's architecture documentation.

Section evidence: [^brain-41c44cae6e0ba80b]

## Related Concepts

- [generative-ai](/concepts/generative-ai.md)
- [prompt-injection](/concepts/prompt-injection.md)
- [data-leakage](/concepts/data-leakage.md)
- [agentic-ai](/concepts/agentic-ai.md)

## Source References

- SRC-0026, OWASP Top 10 for LLM Applications 2026, page 50 (LLM09:2026 Vector and Embedding Weaknesses: definition, RAG as most familiar case, trust boundary, cross-tenant leakage example).
- SRC-0026, page 34 (LLM05:2026 Data and Model Poisoning: external datasets and RAG pipelines expanding the poisoning surface; RAG knowledge base poisoning example).
- SRC-0026, page 52 (boundary with agent-memory attacks and vectorless retrieval inheriting non-geometric risks).


[^brain-41c44cae6e0ba80b]: [SRC-0026](/references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md); locator: Page 50.
[^brain-52d87eb6ddbfef16]: [SRC-0026](/references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md); locator: Page 34.
[^brain-fb22e2219c5d38dc]: [SRC-0026](/references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md); locator: Page 52.
