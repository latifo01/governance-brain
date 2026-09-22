---
id: atlas-aml-cs0027-organization-confusion-on-hugging-face
title: "Organization Confusion on Hugging Face"
type: knowledge
domains: [AI, RISK]
status: active
aliases:
  - "Organization Confusion on Hugging Face"
tags:
  - famous-ai-incidents
  - case-study
  - mitre-atlas
  - hugging-face
evidence_sources: [AI_NICE_TO_KNOW]
---
# Organization Confusion on Hugging Face

## Summary

threlfall_hax, a security researcher, created organization accounts on Hugging Face, a public model repository, that impersonated real organizations. These false Hugging Face organization accounts looked legitimate so individuals from the impersonated organizations requested to join, believing the accounts to be an official site for employees to share models. This gave the researcher full access to any AI models uploaded by the employees, including the ability to replace models with malicious versions. The researcher demonstrated that they could embed malware into an AI model that provided them access to the victim organization's environment. From there, threat actors could execute a range of damaging attacks such as intellectual property theft or poisoning other AI models within the victim's environment.

## Applicability

This MITRE ATLAS case study is a contextual security example for threat modeling, control design, detection, testing, and incident response. It describes a demonstrated attack or research proof of concept; it does not establish a universal legal requirement.

## ATLAS mapping

- Case study: \`AML.CS0027\`
- Last modified in the supplied ATLAS release: 2025-08-12
- Related ATLAS techniques: \`AML.T0007\`, \`AML.T0010.003\`, \`AML.T0011.000\`, \`AML.T0016.000\`, \`AML.T0018.000\`, \`AML.T0018.002\`, \`AML.T0021\`, \`AML.T0025\`, \`AML.T0044\`, \`AML.T0048\`, \`AML.T0048.004\`, \`AML.T0055\`, \`AML.T0072\`, \`AML.T0073\`, \`AML.T0074\`, \`AML.T0115.001\`

## Governance considerations

Use this case to test whether the AI system has documented ownership, trusted artifact provenance, least-privilege access, boundary controls, validation, monitoring, and incident response appropriate to its architecture. Treat the scenario as a prompt for evidence collection and control verification; do not infer that the case proves a specific organization has suffered the same exposure.


## Related concepts

- [[traceability]] 
- [[red-teaming]] 
- [[human-oversight]]

## Source references

- SRC-0046, MITRE ATLAS v2026.08 STIX export, JSON pointer \`/objects\`, object \`AML.CS0027\`; source SHA-256: \`6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c\`; unit SHA-256: \`13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab\`.
- Canonical ATLAS record: https://atlas.mitre.org/studies/AML.CS0027
