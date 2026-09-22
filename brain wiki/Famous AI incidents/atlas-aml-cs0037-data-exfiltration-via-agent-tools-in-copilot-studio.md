---
id: atlas-aml-cs0037-data-exfiltration-via-agent-tools-in-copilot-studio
title: "Data Exfiltration via Agent Tools in Copilot Studio"
type: knowledge
domains: [AI, RISK]
status: active
aliases:
  - "Data Exfiltration via Agent Tools in Copilot Studio"
tags:
  - famous-ai-incidents
  - case-study
  - mitre-atlas
  - data-exfiltration
evidence_sources: [AI_NICE_TO_KNOW]
---
# Data Exfiltration via Agent Tools in Copilot Studio

## Summary

Researchers from Zenity demonstrated how an organization's data can be exfiltrated via prompt injections that target an AI-powered customer service agent.

The target system is a customer service agent built by Zenity in Copilot Studio. It is modeled after an agent built by McKinsey to streamline its customer service needs. The AI agent listens to a customer service email inbox where customers send their engagement requests. Upon receiving a request, the agent looks at the customer's previous engagements, understands who the best consultant for the case is, and proceeds to send an email to the respective consultant regarding the request, including all of the relevant context the consultant will need to properly engage with the customer.

The Zenity researchers begin by performing targeting to identify an email inbox that is managed by an AI agent. Then they use prompt injections to discover details about the AI agent, such as its knowledge sources and tools. Once they understand the AI agent's capabilities, the researchers are able to craft a prompt that retrieves private customer data from the organization's RAG database and CRM, and exfiltrate it via the AI agent's email tool.

Vendor Response: Microsoft quickly acknowledged and fixed the issue. The prompts used by the Zenity researchers in this exercise no longer work, however other prompts may still be effective.

## Applicability

This MITRE ATLAS case study is a contextual security example for threat modeling, control design, detection, testing, and incident response. It describes a demonstrated attack or research proof of concept; it does not establish a universal legal requirement.

## ATLAS mapping

- Case study: \`AML.CS0037\`
- Last modified in the supplied ATLAS release: 2025-11-26
- Related ATLAS techniques: \`AML.T0006\`, \`AML.T0047\`, \`AML.T0051\`, \`AML.T0051.002\`, \`AML.T0065\`, \`AML.T0065\`, \`AML.T0084.000\`, \`AML.T0084.001\`, \`AML.T0084.001\`, \`AML.T0084.002\`, \`AML.T0085.000\`, \`AML.T0085.001\`, \`AML.T0086\`, \`AML.T0093\`

## Governance considerations

Use this case to test whether the AI system has documented ownership, trusted artifact provenance, least-privilege access, boundary controls, validation, monitoring, and incident response appropriate to its architecture. Treat the scenario as a prompt for evidence collection and control verification; do not infer that the case proves a specific organization has suffered the same exposure.


## Related concepts

- [[prompt-injection]] 
- [[data-leakage]] 
- [[retrieval-augmented-generation]] 
- [[agentic-ai]] 
- [[traceability]] 
- [[red-teaming]]

## Source references

- SRC-0046, MITRE ATLAS v2026.08 STIX export, JSON pointer \`/objects\`, object \`AML.CS0037\`; source SHA-256: \`6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c\`; unit SHA-256: \`13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab\`.
- Canonical ATLAS record: https://atlas.mitre.org/studies/AML.CS0037
