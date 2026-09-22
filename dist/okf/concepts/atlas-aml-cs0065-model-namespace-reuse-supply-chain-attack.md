---
aliases:
- Model Namespace Reuse Supply Chain Attack
brain_id: atlas-aml-cs0065-model-namespace-reuse-supply-chain-attack
brain_sha256: b694c4be1adf8bb19a8e6df6594ba463a73d915e1e245e872281f54b764b46c4
domains:
- AI
- RISK
evidence_sources:
- AI_NICE_TO_KNOW
id: atlas-aml-cs0065-model-namespace-reuse-supply-chain-attack
status: stable
tags:
- famous-ai-incidents
- case-study
- mitre-atlas
- supply-chain
- hugging-face
title: Model Namespace Reuse Supply Chain Attack
type: knowledge
---

# Model Namespace Reuse Supply Chain Attack

## Summary

Unit 42 researchers demonstrated an AI supply chain attack in which an attacker reclaims a deleted Hugging Face author namespace and publishes a malicious model under the same historical Author/ModelName identifier. Applications and model catalogs that retain unpinned references to that identifier may resolve and deploy the adversary-controlled replacement rather than the originally trusted artifact.

The attack can affect deleted models and models whose ownership was transferred to a new Hugging Face author. In the ownership-transfer scenario, Hugging Face redirects requests for the old path to the new model location, allowing stale references to continue working. If the original author namespace is later deleted and reclaimed by an attacker, the attacker can recreate the old path and cause it to resolve to a malicious model instead of the legitimate redirected model.

Unit 42 demonstrated this technique against Hugging Face-backed model catalogs in Google Vertex AI and Azure AI Foundry. The researchers embedded reverse-shell payloads in replacement models and obtained code execution in the deployed endpoint environments. They also identified reusable model references in open-source code repositories, documentation, default arguments, example notebooks, and downstream model registries, which could expose users who do not directly interact with Hugging Face.

## Applicability

This MITRE ATLAS case study is a contextual security example for threat modeling, control design, detection, testing, and incident response. It describes a demonstrated attack or research proof of concept; it does not establish a universal legal requirement.

## ATLAS mapping

- Case study: \`AML.CS0065\`
- Last modified in the supplied ATLAS release: 2026-07-31
- Related ATLAS techniques: \`AML.T0010.003\`, \`AML.T0011.000\`, \`AML.T0018.002\`, \`AML.T0021\`, \`AML.T0072\`, \`AML.T0074\`, \`AML.T0095\`, \`AML.T0115.001\`

## Governance considerations

Use this case to test whether the AI system has documented ownership, trusted artifact provenance, least-privilege access, boundary controls, validation, monitoring, and incident response appropriate to its architecture. Treat the scenario as a prompt for evidence collection and control verification; do not infer that the case proves a specific organization has suffered the same exposure.


## Related concepts

- [traceability](/concepts/traceability.md) 
- [red-teaming](/concepts/red-teaming.md)

## Source references

- SRC-0046, MITRE ATLAS v2026.08 STIX export, JSON pointer \`/objects\`, object \`AML.CS0065\`; source SHA-256: \`6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c\`; unit SHA-256: \`13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab\`.
- Canonical ATLAS record: https://atlas.mitre.org/studies/AML.CS0065
