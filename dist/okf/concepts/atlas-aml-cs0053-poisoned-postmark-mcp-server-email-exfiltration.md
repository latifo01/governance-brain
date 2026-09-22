---
aliases:
- Poisoned Postmark MCP Server Email Exfiltration
brain_id: atlas-aml-cs0053-poisoned-postmark-mcp-server-email-exfiltration
brain_sha256: 3e2f9a28befd1efb9ccf2e3b88047ef7311ad905dbda7be20279b5dbce89b64a
domains:
- AI
- RISK
evidence_sources:
- AI_NICE_TO_KNOW
id: atlas-aml-cs0053-poisoned-postmark-mcp-server-email-exfiltration
status: stable
tags:
- famous-ai-incidents
- case-study
- mitre-atlas
- supply-chain
- mcp
- data-exfiltration
title: Poisoned Postmark MCP Server Email Exfiltration
type: knowledge
---

# Poisoned Postmark MCP Server Email Exfiltration

## Summary

A bad actor successfully exfiltrated emails from users of the Postmark's MCP server via a supply chain attack. Postmark is an email delivery service that allows organizations to send marketing and transactional emails via API. The Postmark MCP server allows users to interact with Postmark via AI agents.

The bad actor impersonated Postmark, by registering the `postmark-mcp` package name on npm. They initially published the legitimate versions of the MCP server. After the package became popular and reached over 1,000 downloads per week, the bad actor performed a rugpull and uploaded a malicious version of the package. The malicious version added the bad actor's email address in the BCC line of all emails sent by the MCP tool. Users who upgraded to this version and continued to use the tool would have all emails exfiltrated to the bad actor.

## Applicability

This MITRE ATLAS case study is a contextual security example for threat modeling, control design, detection, testing, and incident response. It describes a demonstrated attack or research proof of concept; it does not establish a universal legal requirement.

## ATLAS mapping

- Case study: \`AML.CS0053\`
- Last modified in the supplied ATLAS release: 2026-03-31
- Related ATLAS techniques: \`AML.T0010.005\`, \`AML.T0011.002\`, \`AML.T0017\`, \`AML.T0048\`, \`AML.T0073\`, \`AML.T0086\`, \`AML.T0109\`, \`AML.T0110.001\`, \`AML.T0115.002\`

## Governance considerations

Use this case to test whether the AI system has documented ownership, trusted artifact provenance, least-privilege access, boundary controls, validation, monitoring, and incident response appropriate to its architecture. Treat the scenario as a prompt for evidence collection and control verification; do not infer that the case proves a specific organization has suffered the same exposure.


## Related concepts

- [data-leakage](/concepts/data-leakage.md) 
- [agentic-ai](/concepts/agentic-ai.md) 
- [traceability](/concepts/traceability.md) 
- [red-teaming](/concepts/red-teaming.md)

## Source references

- SRC-0046, MITRE ATLAS v2026.08 STIX export, JSON pointer \`/objects\`, object \`AML.CS0053\`; source SHA-256: \`6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c\`; unit SHA-256: \`13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab\`.
- Canonical ATLAS record: https://atlas.mitre.org/studies/AML.CS0053
