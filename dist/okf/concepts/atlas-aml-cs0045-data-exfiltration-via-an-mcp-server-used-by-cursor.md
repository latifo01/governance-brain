---
aliases:
- Data Exfiltration via an MCP Server used by Cursor
brain_id: atlas-aml-cs0045-data-exfiltration-via-an-mcp-server-used-by-cursor
brain_sha256: 12abe39452763b37c72ad02fcec14aa489eaca9848aa111adb15cc460689919f
domains:
- AI
- RISK
evidence_sources:
- AI_NICE_TO_KNOW
id: atlas-aml-cs0045-data-exfiltration-via-an-mcp-server-used-by-cursor
status: stable
tags:
- famous-ai-incidents
- case-study
- mitre-atlas
- mcp
- data-exfiltration
title: Data Exfiltration via an MCP Server used by Cursor
type: knowledge
---

# Data Exfiltration via an MCP Server used by Cursor

## Summary

The Backslash Security Research Team demonstrated that a Model Context Protocol (MCP) tool can be used as a vector for an indirect prompt injection attack on Cursor, potentially leading to the execution of malicious shell commands.

The Backslash Security Research Team created a proof-of-concept MCP server capable of scraping webpages. When a user asks Cursor to use the tool to scrape a site containing a malicious prompt, the prompt is injected into Cursor's context. The prompt instructs Cursor to execute a shell command to exfiltrate the victim's AI agent configuration files containing credentials. Cursor does prompt the user before executing the malicious command, potentially mitigating the attack.

## Applicability

This MITRE ATLAS case study is a contextual security example for threat modeling, control design, detection, testing, and incident response. It describes a demonstrated attack or research proof of concept; it does not establish a universal legal requirement.

## ATLAS mapping

- Case study: \`AML.CS0045\`
- Last modified in the supplied ATLAS release: 2026-01-30
- Related ATLAS techniques: \`AML.T0048.000\`, \`AML.T0051.001\`, \`AML.T0053\`, \`AML.T0065\`, \`AML.T0068\`, \`AML.T0068\`, \`AML.T0078\`, \`AML.T0079\`, \`AML.T0079\`, \`AML.T0083\`, \`AML.T0086\`

## Governance considerations

Use this case to test whether the AI system has documented ownership, trusted artifact provenance, least-privilege access, boundary controls, validation, monitoring, and incident response appropriate to its architecture. Treat the scenario as a prompt for evidence collection and control verification; do not infer that the case proves a specific organization has suffered the same exposure.


## Related concepts

- [prompt-injection](/concepts/prompt-injection.md) 
- [data-leakage](/concepts/data-leakage.md) 
- [agentic-ai](/concepts/agentic-ai.md) 
- [traceability](/concepts/traceability.md) 
- [red-teaming](/concepts/red-teaming.md)

## Source references

- SRC-0046, MITRE ATLAS v2026.08 STIX export, JSON pointer \`/objects\`, object \`AML.CS0045\`; source SHA-256: \`6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c\`; unit SHA-256: \`13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab\`.
- Canonical ATLAS record: https://atlas.mitre.org/studies/AML.CS0045
