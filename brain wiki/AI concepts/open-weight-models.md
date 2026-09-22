---
id: open-weight-models
title: Open-weight models
type: knowledge
domains: [AI, AI_SECURITY, MODEL_RISK, THIRD_PARTIES_SUPPLY_CHAIN]
status: active
aliases:
  - Open weights
  - Open-weight AI model
tags:
  - ai-concepts
  - model-risk
  - supply-chain
  - ai-security
evidence_sources: [AI_NICE_TO_KNOW]
---

# Open-weight models

## Summary

An open-weight model is a model whose learned parameter artefacts are made available for download or local use. Weight availability is an access and distribution property; it does not, by itself, establish open-source licensing, reproducible training, trustworthy provenance, safety or unrestricted downstream use. The access mode changes the threat model: OWASP describes extraction, membership-inference and inversion attacks against open-weight deployments as potentially executable offline and without API rate limits (SRC-0026, page 69).

## Applicability

This concept applies when an organisation downloads, mirrors, fine-tunes, quantises, converts, embeds or serves a model whose weights are available outside its own controlled training environment. It also applies to pre-trained checkpoints and adapters used as supply-chain inputs. The relevant boundary includes the repository or registry, artifact format, conversion pipeline, storage, deployment endpoint and all downstream consumers.

## Governance Considerations

- Identify the exact model, version, source, license, checksum, format, adapter and conversion history. A mutable tag or a model card alone is not a substitute for immutable provenance and integrity verification (SRC-0026, page 29; SRC-0034, pages 7 and 25).
- Verify the integrity of pre-trained models and checkpoints before use, protect model storage with access controls, and retain tamper-evident logs for promotion and deployment decisions (SRC-0034, pages 7 and 15).
- Assess whether the open-weight access mode enables offline extraction, membership inference or inversion, then align exposure controls, evaluation, monitoring and release criteria with that threat model (SRC-0026, page 69).
- Treat quantisation, format conversion, merging and adapter application as transformations that require their own validation; assurances for a source artifact do not automatically transfer to the deployed artifact (SRC-0026, page 29; SRC-0034, pages 19 and 25).

## Limits

Open-weight availability does not determine the model's legal status, quality, safety or licensing conditions. The cited security sources describe threats and control expectations; they do not provide a universal certification scheme or guarantee that a particular artifact is malicious or safe. A deployment-specific review remains necessary, including applicable contractual, privacy, intellectual-property and regulatory analysis.

## Related Concepts

- [[gpai-model]]
- [[ai-supply-chain-governance]]
- [[third-party-ai-assurance-and-shared-responsibility]]
- [[ai-model-validation]]
- [[data-leakage]]

## Source References

- SRC-0026, OWASP Top 10 for LLM Applications 2026, page 29 (weak provenance, unsigned artifacts and transformation risks).
- SRC-0026, page 69 (offline extraction, membership inference and inversion risks for open-weight deployments).
- SRC-0034, CoSAI Establish Risks and Controls for the AI Supply Chain, pages 7, 15, 19 and 25 (pre-trained component provenance, checkpoint integrity, model-weight tampering and cryptographic verification).
