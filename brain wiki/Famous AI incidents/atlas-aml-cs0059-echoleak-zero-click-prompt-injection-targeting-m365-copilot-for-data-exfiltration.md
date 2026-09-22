---
id: atlas-aml-cs0059-echoleak-zero-click-prompt-injection-targeting-m365-copilot-for-data-exfiltration
title: "EchoLeak: Zero-Click Prompt Injection Targeting M365 Copilot for Data Exfiltration"
type: knowledge
domains: [AI, RISK]
status: active
aliases:
  - "EchoLeak: Zero-Click Prompt Injection Targeting M365 Copilot for Data Exfiltration"
tags:
  - famous-ai-incidents
  - case-study
  - mitre-atlas
  - data-exfiltration
evidence_sources: [AI_NICE_TO_KNOW]
---
# EchoLeak: Zero-Click Prompt Injection Targeting M365 Copilot for Data Exfiltration

## Summary

Aim Security researchers discovered EchoLeak, a zero-click vulnerability in Microsoft 365 Copilot that could allow an attacker to exfiltrate sensitive enterprise data without user interaction.

The attack used a prompt injection delivered via an email sent to a target user. When M365 Copilot retrieved the email as part of its retrieval-augmented generation (RAG) context, the malicious instructions caused Copilot to search the user's accessible Microsoft 365 data and include sensitive information in its response context. The sensitive information was then exfiltrated via requests to attacker-controlled URLs without requiring the victim to open the email or click a link.

The attack chain bypassed multiple protections, including prompt injection defenses, link redaction, and content security policy restrictions.

Microsoft assigned the issue CVE-2025-32711. It has since been remediated with no evidence it was exploited in the wild.

## Applicability

This MITRE ATLAS case study is a contextual security example for threat modeling, control design, detection, testing, and incident response. It describes a demonstrated attack or research proof of concept; it does not establish a universal legal requirement.

## ATLAS mapping

- Case study: \`AML.CS0059\`
- Last modified in the supplied ATLAS release: 2026-06-30
- Related ATLAS techniques: \`AML.T0025\`, \`AML.T0048\`, \`AML.T0051.002\`, \`AML.T0065\`, \`AML.T0066\`, \`AML.T0067\`, \`AML.T0068\`, \`AML.T0070\`, \`AML.T0077\`, \`AML.T0079\`, \`AML.T0085.000\`, \`AML.T0093\`

## Governance considerations

Use this case to test whether the AI system has documented ownership, trusted artifact provenance, least-privilege access, boundary controls, validation, monitoring, and incident response appropriate to its architecture. Treat the scenario as a prompt for evidence collection and control verification; do not infer that the case proves a specific organization has suffered the same exposure.


## Related concepts

- [[prompt-injection]] 
- [[data-leakage]] 
- [[retrieval-augmented-generation]] 
- [[red-teaming]] 
- [[human-oversight]]

## Source references

- SRC-0046, MITRE ATLAS v2026.08 STIX export, JSON pointer \`/objects\`, object \`AML.CS0059\`; source SHA-256: \`6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c\`; unit SHA-256: \`13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab\`.
- Canonical ATLAS record: https://atlas.mitre.org/studies/AML.CS0059
