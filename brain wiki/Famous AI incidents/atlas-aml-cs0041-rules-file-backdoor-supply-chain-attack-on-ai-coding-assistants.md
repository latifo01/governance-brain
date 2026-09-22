---
id: atlas-aml-cs0041-rules-file-backdoor-supply-chain-attack-on-ai-coding-assistants
title: "Rules File Backdoor: Supply Chain Attack on AI Coding Assistants"
type: knowledge
domains: [AI, RISK]
status: active
aliases:
  - "Rules File Backdoor: Supply Chain Attack on AI Coding Assistants"
tags:
  - famous-ai-incidents
  - case-study
  - mitre-atlas
  - supply-chain
evidence_sources: [AI_NICE_TO_KNOW]
---
# Rules File Backdoor: Supply Chain Attack on AI Coding Assistants

## Summary

Pillar Security researchers demonstrated how adversaries can compromise AI-generated code by injecting malicious instructions into rules files used to configure AI coding assistants like Cursor and GitHub Copilot. The attack uses invisible Unicode characters to hide malicious prompts that manipulate the AI to insert backdoors, vulnerabilities, or malicious scripts into generated code. These poisoned rules files are distributed through open-source repositories and developer communities, creating a scalable supply chain attack that could affect millions of developers and end users through compromised software.

Vendor Response to Responsible Disclosure:
- Cursor: Determined that this risk falls under the users' responsibility.
- GitHub Copilot: Implemented a new security feature that displays a warning when a file's contents include hidden Unicode text on github.com.

## Applicability

This MITRE ATLAS case study is a contextual security example for threat modeling, control design, detection, testing, and incident response. It describes a demonstrated attack or research proof of concept; it does not establish a universal legal requirement.

## ATLAS mapping

- Case study: \`AML.CS0041\`
- Last modified in the supplied ATLAS release: 2025-11-07
- Related ATLAS techniques: \`AML.T0010.001\`, \`AML.T0048.003\`, \`AML.T0051.000\`, \`AML.T0054\`, \`AML.T0065\`, \`AML.T0067\`, \`AML.T0068\`, \`AML.T0079\`, \`AML.T0081\`

## Governance considerations

Use this case to test whether the AI system has documented ownership, trusted artifact provenance, least-privilege access, boundary controls, validation, monitoring, and incident response appropriate to its architecture. Treat the scenario as a prompt for evidence collection and control verification; do not infer that the case proves a specific organization has suffered the same exposure.


## Related concepts

- [[prompt-injection]] 
- [[traceability]] 
- [[red-teaming]]

## Source references

- SRC-0046, MITRE ATLAS v2026.08 STIX export, JSON pointer \`/objects\`, object \`AML.CS0041\`; source SHA-256: \`6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c\`; unit SHA-256: \`13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab\`.
- Canonical ATLAS record: https://atlas.mitre.org/studies/AML.CS0041
