---
id: atlas-aml-cs0028-ai-model-tampering-via-supply-chain-attack
title: "AI Model Tampering via Supply Chain Attack"
type: knowledge
domains: [AI, RISK]
status: active
aliases:
  - "AI Model Tampering via Supply Chain Attack"
tags:
  - famous-ai-incidents
  - case-study
  - mitre-atlas
  - supply-chain
evidence_sources: [AI_NICE_TO_KNOW]
---
# AI Model Tampering via Supply Chain Attack

## Summary

Researchers at Trend Micro, Inc. used service indexing portals and web searching tools to identify over 8,000 misconfigured private container registries exposed on the internet. Approximately 70% of the registries also had overly permissive access controls that allowed write access. In their analysis, the researchers found over 1,000 unique AI models embedded in private container images within these open registries that could be pulled without authentication.

This exposure could allow adversaries to download, inspect, and modify container contents, including sensitive AI model files. This is an exposure of valuable intellectual property which could be stolen by an adversary. Compromised images could also be pushed to the registry, leading to a supply chain attack, allowing malicious actors to compromise the integrity of AI models used in production systems.

## Applicability

This MITRE ATLAS case study is a contextual security example for threat modeling, control design, detection, testing, and incident response. It describes a demonstrated attack or research proof of concept; it does not establish a universal legal requirement.

## ATLAS mapping

- Case study: \`AML.CS0028\`
- Last modified in the supplied ATLAS release: 2025-08-12
- Related ATLAS techniques: \`AML.T0004\`, \`AML.T0007\`, \`AML.T0010.004\`, \`AML.T0015\`, \`AML.T0018.000\`, \`AML.T0018.001\`, \`AML.T0044\`, \`AML.T0048.004\`, \`AML.T0049\`

## Governance considerations

Use this case to test whether the AI system has documented ownership, trusted artifact provenance, least-privilege access, boundary controls, validation, monitoring, and incident response appropriate to its architecture. Treat the scenario as a prompt for evidence collection and control verification; do not infer that the case proves a specific organization has suffered the same exposure.


## Related concepts

- [[traceability]] 
- [[ai-model-validation]] 
- [[red-teaming]] 
- [[human-oversight]]

## Source references

- SRC-0046, MITRE ATLAS v2026.08 STIX export, JSON pointer \`/objects\`, object \`AML.CS0028\`; source SHA-256: \`6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c\`; unit SHA-256: \`13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab\`.
- Canonical ATLAS record: https://atlas.mitre.org/studies/AML.CS0028
