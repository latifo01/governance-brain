---
aliases:
- Hallucinations
- Hallucination
- Misinformation
- LLM07
brain_id: hallucinations
brain_sha256: 86092207ca553b63d46c845d6f1008b530416876665655e99fb2e6856e9308da
domains:
- AI
- RISK
evidence_sources:
- AI_NICE_TO_KNOW
id: hallucinations
sources:
- authority: UNCLASSIFIED
  brain_source_id: SRC-0028
  evidence_ref: provenance-repair-20260920-src-0028-p0013
  id: brain-0d57fb2dd737c4b4
  locator: Page 13
  resource: /references/src-0028-5722b7682ae060d9373666f4804a3f6d165199bbb4035053adedd46df1730654.md
  unit_file_sha256: 8913b0f8583a0586545a0305d4c743322405d03187394517d36b6a36f5ec8594
  unit_path: ingest/SRC-0028/units/p0013.md
  unit_sha256: e9d93f7e5bc79986760f38bd587c948ea6764949c3848637299c8f15f86b7904
- authority: UNCLASSIFIED
  brain_source_id: SRC-0026
  evidence_ref: provenance-repair-20260920-src-0026-p0043
  id: brain-2126cff5e8afc508
  locator: Page 43
  resource: /references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md
  unit_file_sha256: 88e28d2175d3b1930ce678de0c337536e6e0eadc2be4e497362f66304326e004
  unit_path: ingest/SRC-0026/units/p0043.md
  unit_sha256: 06db05750519a9ac0eba31a934321f1608592b38a838de9c681e291734fd3d36
- authority: UNCLASSIFIED
  brain_source_id: SRC-0026
  evidence_ref: provenance-repair-20260920-src-0026-p0113
  id: brain-7578594faffeb177
  locator: Page 113
  resource: /references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md
  unit_file_sha256: 17bb1246debf611c8cac30ac61aa008b6a311d2507ad430fa0922de5b99c71f4
  unit_path: ingest/SRC-0026/units/p0113.md
  unit_sha256: bb9c7926050031bdb3c66ec6b18eee02395a006a87938057ad5b0bdd91b6e52b
- authority: UNCLASSIFIED
  brain_source_id: SRC-0028
  evidence_ref: provenance-repair-20260920-src-0028-p0011
  id: brain-eacbb74d71fa72e4
  locator: Page 11
  resource: /references/src-0028-5722b7682ae060d9373666f4804a3f6d165199bbb4035053adedd46df1730654.md
  unit_file_sha256: b8738804bd8ffd5a3c3cd542e3e08a8e5bab32187e2af0355c3f885f302bcd06
  unit_path: ingest/SRC-0028/units/p0011.md
  unit_sha256: 42ca91fc2b5918c476a01023209a9ccf80700d1e3c32b21c2e234e27b6ec5ebd
- authority: UNCLASSIFIED
  brain_source_id: SRC-0026
  evidence_ref: provenance-repair-20260920-src-0026-p0044
  id: brain-ec903f664b7714dd
  locator: Page 44
  resource: /references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md
  unit_file_sha256: 34b75ff97d135bb6d8ec2e4a4706f08238c43ae9671defdaefaa0d6e069e8cbb
  unit_path: ingest/SRC-0026/units/p0044.md
  unit_sha256: 139ba0594ce862fa9463fb9b7ff84f829ddd743a3ae64ccc4a84410bdefe689c
status: stable
tags:
- genai-security
- model-risk
- misinformation
title: Hallucinations and misinformation
type: knowledge
---


# Hallucinations and misinformation

## Summary

Hallucination is a failure mode in which a language model generates incorrect, unsupported or fabricated content while presenting it with fluency and apparent confidence. In the OWASP Top 10 for LLM Applications 2026 it is treated as one root cause of the broader risk `LLM07:2026 Misinformation`: incorrect, incomplete, unsupported or misleading information that appears credible enough to influence a human decision, an automated workflow or an agent action.

The governance issue is not the error itself but overreliance: humans and systems often treat fluent, confident or well-structured outputs as authoritative. In agentic architectures this overreliance is frequently embedded in system design, because model outputs drive tool calls, code generation, state inference, authorization decisions and inter-agent coordination, turning a false representation into a system-level failure with financial, security, safety or operational consequences.

Section evidence: [^brain-0d57fb2dd737c4b4] [^brain-2126cff5e8afc508] [^brain-7578594faffeb177] [^brain-eacbb74d71fa72e4] [^brain-ec903f664b7714dd]

## Applicability

This note applies to LLM applications, RAG systems, copilots and agentic systems whose outputs are consumed by humans, downstream components or automated actions. Risk increases when outputs feed decision support, workflow triggers, code execution, dependency resolution or agent planning without independent verification.

Documented manifestations include unsupported or false decision support, incorrect state inference in workflows, and fabricated code dependencies: the model may reference non-existent (hallucinated) packages, a supply-chain vector registered under `LLM04:2026 Supply Chain` and demonstrated by package-hallucination research (Spracklen et al., 2025, as cited in SRC-0026).

The CoSAI AI Incident Response Framework classifies hallucination as an AI incident type: leveraging model inaccuracies for harmful purposes, for example false financial forecasts.

Section evidence: [^brain-0d57fb2dd737c4b4] [^brain-2126cff5e8afc508] [^brain-7578594faffeb177] [^brain-eacbb74d71fa72e4] [^brain-ec903f664b7714dd]

## Governance Considerations

- Identify which decisions, workflows or tool actions can be influenced by unverified model output, and gate material ones behind policy checks or human review.
- Distinguish root causes before selecting controls: hallucination, stale or incomplete context, weak grounding, ambiguous prompts, biased or corrupted data, misleading summaries and unvalidated tool outputs each call for different mitigations. Where the root cause is prompt injection, poisoning or supply-chain compromise, those risks should be handled under their own entries.
- Monitor and measure factual grounding in deployed use cases rather than treating fluency as a proxy for correctness.
- Treat hallucinated package names, citations, APIs and entities as security and supply-chain risks, not only quality defects.
- Record hallucination-driven incidents and near misses so response playbooks and tests improve.

Section evidence: [^brain-0d57fb2dd737c4b4] [^brain-2126cff5e8afc508] [^brain-7578594faffeb177] [^brain-eacbb74d71fa72e4] [^brain-ec903f664b7714dd]

## Limits

Misinformation is a failure mode description, not a legal obligation in the local corpus. The sources are security and incident-response frameworks: they support control expectations, not binding requirements for every organization. The prior CDO draft's taxonomy of "factual" versus "faithfulness" hallucination was not found in the local evidence corpus and is therefore not asserted here.

Section evidence: [^brain-0d57fb2dd737c4b4] [^brain-2126cff5e8afc508] [^brain-7578594faffeb177] [^brain-eacbb74d71fa72e4] [^brain-ec903f664b7714dd]

## Related Concepts

- [prompt-injection](/concepts/prompt-injection.md) can deliberately induce misinformation and should be referenced separately when it is the root cause.
- [ai-model-monitoring](/concepts/ai-model-monitoring.md) supports detection of misinformation patterns and drift in deployed systems.
- [red-teaming](/concepts/red-teaming.md) tests whether grounding and refusal behaviors hold under adversarial prompts.
- [human-oversight](/concepts/human-oversight.md) defines when a human gate must review model output before material actions.

Section evidence: [^brain-0d57fb2dd737c4b4] [^brain-2126cff5e8afc508] [^brain-7578594faffeb177] [^brain-eacbb74d71fa72e4] [^brain-ec903f664b7714dd]

## Source References

- SRC-0026, OWASP Top 10 for LLM Applications 2026, pages 43-44 (LLM07:2026 Misinformation: definition, root causes including hallucination, overreliance, examples including hallucinated packages) and page 113 (package-hallucination research citation).
- SRC-0028, CoSAI AI Incident Response Framework V1.0, page 11 (hallucination as an AI incident type: leveraging model inaccuracies for harmful purposes) and page 13 (model-output inspection for hallucinations and leakage).


[^brain-0d57fb2dd737c4b4]: [SRC-0028](/references/src-0028-5722b7682ae060d9373666f4804a3f6d165199bbb4035053adedd46df1730654.md); locator: Page 13.
[^brain-2126cff5e8afc508]: [SRC-0026](/references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md); locator: Page 43.
[^brain-7578594faffeb177]: [SRC-0026](/references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md); locator: Page 113.
[^brain-eacbb74d71fa72e4]: [SRC-0028](/references/src-0028-5722b7682ae060d9373666f4804a3f6d165199bbb4035053adedd46df1730654.md); locator: Page 11.
[^brain-ec903f664b7714dd]: [SRC-0026](/references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md); locator: Page 44.
