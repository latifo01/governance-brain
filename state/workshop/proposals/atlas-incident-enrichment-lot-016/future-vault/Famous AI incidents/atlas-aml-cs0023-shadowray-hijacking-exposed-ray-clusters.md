---
id: atlas-aml-cs0023-shadowray-hijacking-exposed-ray-clusters
title: "ShadowRay: Hijacking Exposed Ray Clusters"
type: knowledge
domains: [AI, RISK]
status: active
aliases:
  - "ShadowRay: Hijacking Exposed Ray Clusters"
tags:
  - famous-ai-incidents
  - case-study
  - mitre-atlas
evidence_sources: [AI_NICE_TO_KNOW]
---
# ShadowRay: Hijacking Exposed Ray Clusters

## Summary

Ray is an open-source Python framework for scaling production AI workflows. Ray's Job API allows for arbitrary remote execution by design. However, it does not offer authentication, and the default configuration may expose the cluster to the internet. Researchers at Oligo discovered that Ray clusters have been actively exploited for at least seven months. Adversaries can use victim organization's compute power and steal valuable information. The researchers estimate the value of the compromised machines to be nearly 1 billion USD.

Five vulnerabilities in Ray were reported to Anyscale, the maintainers of Ray. Anyscale promptly fixed four of the five vulnerabilities. However, the fifth vulnerability CVE-2023-48022 remains disputed. Anyscale maintains that Ray's lack of authentication is a design decision, and that Ray is meant to be deployed in a safe network environment. The Oligo researchers deem this a "shadow vulnerability" because in disputed status, the CVE does not show up in static scans.

## Applicability

This MITRE ATLAS case study is a contextual security example for threat modeling, control design, detection, testing, and incident response. It describes a demonstrated attack or research proof of concept; it does not establish a universal legal requirement.

## ATLAS mapping

- Case study: \`AML.CS0023\`
- Last modified in the supplied ATLAS release: 2026-07-31
- Related ATLAS techniques: \`AML.T0006\`, \`AML.T0010.003\`, \`AML.T0025\`, \`AML.T0035\`, \`AML.T0048.000\`, \`AML.T0049\`, \`AML.T0055\`

## Governance considerations

Use this case to test whether the AI system has documented ownership, trusted artifact provenance, least-privilege access, boundary controls, validation, monitoring, and incident response appropriate to its architecture. Treat the scenario as a prompt for evidence collection and control verification; do not infer that the case proves a specific organization has suffered the same exposure.


## Related concepts

- [[prompt-injection]] 
- [[ai-model-validation]] 
- [[red-teaming]]

## Source references

- SRC-0046, MITRE ATLAS v2026.08 STIX export, JSON pointer \`/objects\`, object \`AML.CS0023\`; source SHA-256: \`6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c\`; unit SHA-256: \`13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab\`.
- Canonical ATLAS record: https://atlas.mitre.org/studies/AML.CS0023
