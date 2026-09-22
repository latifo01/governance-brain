---
aliases:
- Data Exfiltration via Remote Poisoned MCP Tool
brain_id: atlas-aml-cs0054-data-exfiltration-via-remote-poisoned-mcp-tool
brain_sha256: d4592547f80a772aa3050cc37a9494555e7ec1e0fa9ebd75837731fb9c151581
domains:
- AI
- RISK
evidence_sources:
- AI_NICE_TO_KNOW
id: atlas-aml-cs0054-data-exfiltration-via-remote-poisoned-mcp-tool
status: stable
tags:
- famous-ai-incidents
- case-study
- mitre-atlas
- mcp
- data-exfiltration
title: Data Exfiltration via Remote Poisoned MCP Tool
type: knowledge
---

# Data Exfiltration via Remote Poisoned MCP Tool

## Summary

Researchers at Invariant Labs demonstrated that AI agents configured with remote Model Context Protocol (MCP) Tools can be vulnerable to model poisoning attacks. They show that an MCP Tool can contain malicious prompts in its docstring description, which is ingested into the AI agent's context, modifying its behavior.

They demonstrate this attack with a proof-of-concept MCP Tool that instructs the agent to perform additional actions before using the tool. The agent is instructed to read files containing credentials from the victim's machine and store their contents in one of the input variables to the tool. When the tool runs, the victim's credentials are exfiltrated to the poisoned MCP server.

## Applicability

This MITRE ATLAS case study is a contextual security example for threat modeling, control design, detection, testing, and incident response. It describes a demonstrated attack or research proof of concept; it does not establish a universal legal requirement.

## ATLAS mapping

- Case study: \`AML.CS0054\`
- Last modified in the supplied ATLAS release: 2026-07-31
- Related ATLAS techniques: \`AML.T0010.005\`, \`AML.T0011.002\`, \`AML.T0048.003\`, \`AML.T0051.001\`, \`AML.T0053\`, \`AML.T0055\`, \`AML.T0065\`, \`AML.T0086\`, \`AML.T0098\`, \`AML.T0110.000\`, \`AML.T0115.002\`

## Governance considerations

Use this case to test whether the AI system has documented ownership, trusted artifact provenance, least-privilege access, boundary controls, validation, monitoring, and incident response appropriate to its architecture. Treat the scenario as a prompt for evidence collection and control verification; do not infer that the case proves a specific organization has suffered the same exposure.


## Related concepts

- [prompt-injection](/concepts/prompt-injection.md) 
- [data-leakage](/concepts/data-leakage.md) 
- [agentic-ai](/concepts/agentic-ai.md) 
- [traceability](/concepts/traceability.md) 
- [red-teaming](/concepts/red-teaming.md)

## Source references

- SRC-0046, MITRE ATLAS v2026.08 STIX export, JSON pointer \`/objects\`, object \`AML.CS0054\`; source SHA-256: \`6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c\`; unit SHA-256: \`13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab\`.
- Canonical ATLAS record: https://atlas.mitre.org/studies/AML.CS0054
