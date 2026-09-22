---
aliases:
- Open weights
- Open-weight AI model
brain_id: open-weight-models
brain_sha256: a8449e21b99eedd63bed74d7cd8149dd6bbe89092de38138e37410691f9c7040
domains:
- AI
- AI_SECURITY
- MODEL_RISK
- THIRD_PARTIES_SUPPLY_CHAIN
evidence_sources:
- AI_NICE_TO_KNOW
id: open-weight-models
sources:
- authority: GUIDANCE
  brain_source_id: SRC-0026
  evidence_ref: aiconcepts-p1-src-0026-ec-003
  id: brain-5b90587eb3fbe7c1
  locator: Page 69
  resource: /references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md
  unit_file_sha256: 4ad652b46995046a69ce17e0c6637d80c531ff71769aafedca233dba699a803a
  unit_path: ingest/SRC-0026/units/p0069.md
  unit_sha256: b7c508698ac14c3fae1c7753d41844db832719cb089fa7013832cc16886825e1
- authority: FRAMEWORK
  brain_source_id: SRC-0034
  evidence_ref: aiconcepts-p1-src-0034-ec-002
  id: brain-79f5733a3f6fd071
  locator: Page 15
  resource: /references/src-0034-b4133f21b4fb1b6ab9bd39962c2aad1b6f3193dfe84a23fcf9a2edb914a11176.md
  unit_file_sha256: ff39e7b9a97034a9f0714ccbbae1b96be0d72f5cd30f9b12ec991a201a06039f
  unit_path: ingest/SRC-0034/units/p0015.md
  unit_sha256: e01852a1797313c80e9f146a215e07a151fe56220a6e7c716be506f0bf5617ff
- authority: FRAMEWORK
  brain_source_id: SRC-0034
  evidence_ref: aiconcepts-p1-src-0034-ec-001
  id: brain-804225b9009479dc
  locator: Page 7
  resource: /references/src-0034-b4133f21b4fb1b6ab9bd39962c2aad1b6f3193dfe84a23fcf9a2edb914a11176.md
  unit_file_sha256: 9c4aab7169ee5dd17c0bf25a844881c11516365ffe0e0e1ba6f762521cf89ec9
  unit_path: ingest/SRC-0034/units/p0007.md
  unit_sha256: 21018d2b84c3129d75d570222b76c35a07a5260a96cb5c5970cffca8f8c5d6eb
- authority: GUIDANCE
  brain_source_id: SRC-0026
  evidence_ref: aiconcepts-p1-src-0026-ec-001
  id: brain-97919621e2c61b73
  locator: Page 29
  resource: /references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md
  unit_file_sha256: 3977930be1b902ab733a05e9483d790df500d9baac9207913aac3214b6737cf5
  unit_path: ingest/SRC-0026/units/p0029.md
  unit_sha256: 9e407de8648438a981a58e580ce0232d8a6c3cbd7a6a8e09eb1791c4f031ac4a
- authority: FRAMEWORK
  brain_source_id: SRC-0034
  evidence_ref: aiconcepts-p1-src-0034-ec-003
  id: brain-b241d16ff6e001c8
  locator: Page 19
  resource: /references/src-0034-b4133f21b4fb1b6ab9bd39962c2aad1b6f3193dfe84a23fcf9a2edb914a11176.md
  unit_file_sha256: e550b40dc2f90686cddf9b83f56d7d284c4d04ace0eed339b472110c8d9d93ba
  unit_path: ingest/SRC-0034/units/p0019.md
  unit_sha256: 5c1eff0a6421aeb8017decfcf540b89636af476c70283fed92a33d5a8a8f9a92
- authority: FRAMEWORK
  brain_source_id: SRC-0034
  evidence_ref: aiconcepts-p1-src-0034-ec-004
  id: brain-ddbe9d0e4268eeb2
  locator: Page 25
  resource: /references/src-0034-b4133f21b4fb1b6ab9bd39962c2aad1b6f3193dfe84a23fcf9a2edb914a11176.md
  unit_file_sha256: e97464e7c53ea21a5d96421cbfcf3c2228fadb237588ff4002dc67a5d550987f
  unit_path: ingest/SRC-0034/units/p0025.md
  unit_sha256: b023cc6c9feddf914505b3deb4ab4561aca708963bd7396aab98b2baafcea180
- authority: GUIDANCE
  brain_source_id: SRC-0026
  evidence_ref: aiconcepts-p1-src-0026-ec-002
  id: brain-f087d9d57667168c
  locator: Page 29
  resource: /references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md
  unit_file_sha256: 3977930be1b902ab733a05e9483d790df500d9baac9207913aac3214b6737cf5
  unit_path: ingest/SRC-0026/units/p0029.md
  unit_sha256: 9e407de8648438a981a58e580ce0232d8a6c3cbd7a6a8e09eb1791c4f031ac4a
status: stable
tags:
- ai-concepts
- model-risk
- supply-chain
- ai-security
title: Open-weight models
type: knowledge
---


# Open-weight models

## Summary

An open-weight model is a model whose learned parameter artefacts are made available for download or local use. Weight availability is an access and distribution property; it does not, by itself, establish open-source licensing, reproducible training, trustworthy provenance, safety or unrestricted downstream use. The access mode changes the threat model: OWASP describes extraction, membership-inference and inversion attacks against open-weight deployments as potentially executable offline and without API rate limits (SRC-0026, page 69).

Section evidence: [^brain-5b90587eb3fbe7c1] [^brain-97919621e2c61b73] [^brain-f087d9d57667168c]

## Applicability

This concept applies when an organisation downloads, mirrors, fine-tunes, quantises, converts, embeds or serves a model whose weights are available outside its own controlled training environment. It also applies to pre-trained checkpoints and adapters used as supply-chain inputs. The relevant boundary includes the repository or registry, artifact format, conversion pipeline, storage, deployment endpoint and all downstream consumers.

Section evidence: [^brain-5b90587eb3fbe7c1] [^brain-97919621e2c61b73] [^brain-f087d9d57667168c]

## Governance Considerations

- Identify the exact model, version, source, license, checksum, format, adapter and conversion history. A mutable tag or a model card alone is not a substitute for immutable provenance and integrity verification (SRC-0026, page 29; SRC-0034, pages 7 and 25).
- Verify the integrity of pre-trained models and checkpoints before use, protect model storage with access controls, and retain tamper-evident logs for promotion and deployment decisions (SRC-0034, pages 7 and 15).
- Assess whether the open-weight access mode enables offline extraction, membership inference or inversion, then align exposure controls, evaluation, monitoring and release criteria with that threat model (SRC-0026, page 69).
- Treat quantisation, format conversion, merging and adapter application as transformations that require their own validation; assurances for a source artifact do not automatically transfer to the deployed artifact (SRC-0026, page 29; SRC-0034, pages 19 and 25).

Section evidence: [^brain-5b90587eb3fbe7c1] [^brain-79f5733a3f6fd071] [^brain-804225b9009479dc] [^brain-97919621e2c61b73] [^brain-b241d16ff6e001c8] [^brain-ddbe9d0e4268eeb2] [^brain-f087d9d57667168c]

## Limits

Open-weight availability does not determine the model's legal status, quality, safety or licensing conditions. The cited security sources describe threats and control expectations; they do not provide a universal certification scheme or guarantee that a particular artifact is malicious or safe. A deployment-specific review remains necessary, including applicable contractual, privacy, intellectual-property and regulatory analysis.

Section evidence: [^brain-5b90587eb3fbe7c1] [^brain-79f5733a3f6fd071] [^brain-804225b9009479dc] [^brain-97919621e2c61b73] [^brain-b241d16ff6e001c8] [^brain-ddbe9d0e4268eeb2] [^brain-f087d9d57667168c]

## Related Concepts

- [gpai-model](/concepts/gpai-model.md)
- [ai-supply-chain-governance](/concepts/ai-supply-chain-governance.md)
- [third-party-ai-assurance-and-shared-responsibility](/concepts/third-party-ai-assurance-and-shared-responsibility.md)
- [ai-model-validation](/concepts/ai-model-validation.md)
- [data-leakage](/concepts/data-leakage.md)

## Source References

- SRC-0026, OWASP Top 10 for LLM Applications 2026, page 29 (weak provenance, unsigned artifacts and transformation risks).
- SRC-0026, page 69 (offline extraction, membership inference and inversion risks for open-weight deployments).
- SRC-0034, CoSAI Establish Risks and Controls for the AI Supply Chain, pages 7, 15, 19 and 25 (pre-trained component provenance, checkpoint integrity, model-weight tampering and cryptographic verification).


[^brain-5b90587eb3fbe7c1]: [SRC-0026](/references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md); locator: Page 69.
[^brain-79f5733a3f6fd071]: [SRC-0034](/references/src-0034-b4133f21b4fb1b6ab9bd39962c2aad1b6f3193dfe84a23fcf9a2edb914a11176.md); locator: Page 15.
[^brain-804225b9009479dc]: [SRC-0034](/references/src-0034-b4133f21b4fb1b6ab9bd39962c2aad1b6f3193dfe84a23fcf9a2edb914a11176.md); locator: Page 7.
[^brain-97919621e2c61b73]: [SRC-0026](/references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md); locator: Page 29.
[^brain-b241d16ff6e001c8]: [SRC-0034](/references/src-0034-b4133f21b4fb1b6ab9bd39962c2aad1b6f3193dfe84a23fcf9a2edb914a11176.md); locator: Page 19.
[^brain-ddbe9d0e4268eeb2]: [SRC-0034](/references/src-0034-b4133f21b4fb1b6ab9bd39962c2aad1b6f3193dfe84a23fcf9a2edb914a11176.md); locator: Page 25.
[^brain-f087d9d57667168c]: [SRC-0026](/references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md); locator: Page 29.
