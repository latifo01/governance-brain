---
id: atlas-aml-cs0015-compromised-pytorch-dependency-chain
title: "Compromised PyTorch Dependency Chain"
type: knowledge
domains: [AI, RISK]
status: active
aliases:
  - "Compromised PyTorch Dependency Chain"
tags:
  - famous-ai-incidents
  - case-study
  - mitre-atlas
  - supply-chain
evidence_sources: [AI_NICE_TO_KNOW]
---
# Compromised PyTorch Dependency Chain

## Summary

Linux packages for PyTorch's pre-release version, called Pytorch-nightly, were compromised from December 25 to 30, 2022 by a malicious binary uploaded to the Python Package Index (PyPI) code repository.  The malicious binary had the same name as a PyTorch dependency and the PyPI package manager (pip) installed this malicious package instead of the legitimate one.

This supply chain attack, also known as "dependency confusion," exposed sensitive information of Linux machines with the affected pip-installed versions of PyTorch-nightly. On December 30, 2022, PyTorch announced the incident and initial steps towards mitigation, including the rename and removal of `torchtriton` dependencies.

## Applicability

This MITRE ATLAS case study is a contextual security example for threat modeling, control design, detection, testing, and incident response. It describes a demonstrated attack or research proof of concept; it does not establish a universal legal requirement.

## ATLAS mapping

- Case study: \`AML.CS0015\`
- Last modified in the supplied ATLAS release: 2025-03-14
- Related ATLAS techniques: \`AML.T0010.001\`, \`AML.T0025\`, \`AML.T0037\`

## Governance considerations

Use this case to test whether the AI system has documented ownership, trusted artifact provenance, least-privilege access, boundary controls, validation, monitoring, and incident response appropriate to its architecture. Treat the scenario as a prompt for evidence collection and control verification; do not infer that the case proves a specific organization has suffered the same exposure.


## Related concepts

- [[traceability]] 
- [[ai-model-monitoring]] 
- [[red-teaming]]

## Source references

- SRC-0046, MITRE ATLAS v2026.08 STIX export, JSON pointer \`/objects\`, object \`AML.CS0015\`; source SHA-256: \`6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c\`; unit SHA-256: \`13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab\`.
- Canonical ATLAS record: https://atlas.mitre.org/studies/AML.CS0015
