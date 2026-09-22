---
aliases:
- Data leakage
- Sensitive Information Disclosure
- LLM02
brain_id: data-leakage
brain_sha256: ef61a9156de11e91867bcc1121b95f98270de8d533f17a1b4f18dbc2ea1e8d20
domains:
- AI
- RISK
- DATA_PROTECTION
evidence_sources:
- AI_NICE_TO_KNOW
- DATA_AI_CLASSIFICATION
id: data-leakage
sources:
- authority: UNCLASSIFIED
  brain_source_id: SRC-0026
  evidence_ref: provenance-repair-20260920-src-0026-p0047
  id: brain-2534e3aed5fd2daf
  locator: Page 47
  resource: /references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md
  unit_file_sha256: f120ff6cc1c0d559669b31adf6b15ec192f24a4dfd1e8b9c1baa6ffe89710cc9
  unit_path: ingest/SRC-0026/units/p0047.md
  unit_sha256: 413fb969928128c9cbb625df0ac8bffa0a8eaa8a06da3e89a5c236bbe6fd0360
- authority: UNCLASSIFIED
  brain_source_id: SRC-0026
  evidence_ref: provenance-repair-20260920-src-0026-p0018
  id: brain-5682599f10bc542c
  locator: Page 18
  resource: /references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md
  unit_file_sha256: c8f1ca0c308045986310f16fcc62ba36a867852fd4c751ae26783177d3b5da3d
  unit_path: ingest/SRC-0026/units/p0018.md
  unit_sha256: 278cfc30cd0110dfebc7eb3920d62a5073356e41d86a690624f4a98fe5de68f2
- authority: UNCLASSIFIED
  brain_source_id: SRC-0028
  evidence_ref: provenance-repair-20260920-src-0028-p0011
  id: brain-eacbb74d71fa72e4
  locator: Page 11
  resource: /references/src-0028-5722b7682ae060d9373666f4804a3f6d165199bbb4035053adedd46df1730654.md
  unit_file_sha256: b8738804bd8ffd5a3c3cd542e3e08a8e5bab32187e2af0355c3f885f302bcd06
  unit_path: ingest/SRC-0028/units/p0011.md
  unit_sha256: 42ca91fc2b5918c476a01023209a9ccf80700d1e3c32b21c2e234e27b6ec5ebd
status: stable
tags:
- genai-security
- privacy
- data-protection
title: Sensitive information disclosure in AI systems
type: knowledge
---


# Sensitive information disclosure in AI systems

## Summary

Sensitive information disclosure (`LLM02:2026` in the OWASP Top 10 for LLM Applications 2026) occurs when an LLM-integrated system exposes confidential, regulated, privileged or proprietary data through a channel the data subject, controller or system owner did not authorize. The channel is not only the final answer: tool-call arguments, reasoning traces, retrieved chunks, multimodal output, logs, telemetry, embeddings and observable inference properties (timing, token length, log-probabilities, confidence, cache-hit behavior) are all disclosure surfaces, each subject to the same classification and redaction rules.

The governance issue is that AI systems multiply disclosure surfaces across the lifecycle: training-time memorization that can be extracted verbatim, inference-time disclosure of live context (system prompts, RAG chunks, files, tool outputs, memory or other sessions' data), and exposure of hidden control context that materially increases attacker capability.

Section evidence: [^brain-2534e3aed5fd2daf] [^brain-5682599f10bc542c] [^brain-eacbb74d71fa72e4]

## Applicability

This note applies to LLM applications, RAG systems, agents and any AI system that processes sensitive, personal, regulated or proprietary data, including through third-party model APIs.

Documented examples from the local evidence corpus include:

- Memorization of corpus content by models, fine-tunes or LoRA adapters, later reproduced verbatim or in recoverable form; memorization scales with capacity, duplication and context length, and narrow adapters memorize rare examples with high fidelity (SRC-0026, page 18).
- Exposure of sensitive functionality, tool and function schemas, API keys, database credentials or user tokens placed in hidden context (SRC-0026, page 47).
- Disclosure of permissions and user roles through instruction context, which can invite further probing and reveal additional sensitive information (SRC-0026, page 47).
- AI incident response treating unauthorized access and disclosure of restricted information as incident types to detect and respond to (SRC-0028, page 11).

Section evidence: [^brain-2534e3aed5fd2daf] [^brain-5682599f10bc542c] [^brain-eacbb74d71fa72e4]

## Governance Considerations

- Classify and minimize sensitive data before it enters prompts, hidden context, retrieval stores or training corpora.
- Apply output classification and redaction rules to every disclosure surface, not only the visible answer: tool arguments, reasoning traces, retrieved chunks, logs, telemetry and embeddings.
- Treat timing, token-length and confidence side channels as disclosure surfaces in high-risk deployments.
- Govern fine-tuning and adapters: rare-example memorization in narrow adapters is a targeted extraction surface distinct from the base model.
- Keep hidden context free of credentials; the real risk is placing sensitive credentials in the hidden context in the first place.
- Prepare incident response for unauthorized access and disclosure events, including what to detect, contain and notify.

Section evidence: [^brain-2534e3aed5fd2daf] [^brain-5682599f10bc542c] [^brain-eacbb74d71fa72e4]

## Limits

The OWASP entry is a security-control expectation, not a legal determination. Data protection obligations (lawful basis, notification duties) remain governed by the dedicated privacy notes and the applicable Knowledge Banks; this note does not assert them. The prior CDO draft for this concept was a general cybersecurity article on organizational data leaks and breaches; that framing is not AI-specific and was replaced by the ingest-verified LLM disclosure content, keeping the CDO identifier `data-leakage` for lineage.

Section evidence: [^brain-2534e3aed5fd2daf] [^brain-5682599f10bc542c] [^brain-eacbb74d71fa72e4]

## Related Concepts

- [prompt-injection](/concepts/prompt-injection.md) can be used to make an assistant disclose restricted information.
- [genai-guardrails](/concepts/genai-guardrails.md) describes output filtering and redaction controls.
- [human-oversight](/concepts/human-oversight.md) gates high-impact disclosures and actions.
- [hallucinations](/concepts/hallucinations.md) covers the adjacent misinformation failure mode.

Section evidence: [^brain-2534e3aed5fd2daf] [^brain-5682599f10bc542c] [^brain-eacbb74d71fa72e4]

## Source References

- SRC-0026, OWASP Top 10 for LLM Applications 2026, page 18 (LLM02:2026 definition, disclosure surfaces, lifecycle phases) and page 47 (LLM08:2026 boundary: leakage of regulated user or training data belongs to LLM02; examples of sensitive exposure).
- SRC-0028, CoSAI AI Incident Response Framework V1.0, page 11 (unauthorized access and restricted-information disclosure as incident types).


[^brain-2534e3aed5fd2daf]: [SRC-0026](/references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md); locator: Page 47.
[^brain-5682599f10bc542c]: [SRC-0026](/references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md); locator: Page 18.
[^brain-eacbb74d71fa72e4]: [SRC-0028](/references/src-0028-5722b7682ae060d9373666f4804a3f6d165199bbb4035053adedd46df1730654.md); locator: Page 11.
