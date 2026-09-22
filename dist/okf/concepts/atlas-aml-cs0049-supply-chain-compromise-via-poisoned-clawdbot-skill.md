---
aliases:
- Supply Chain Compromise via Poisoned ClawdBot Skill
brain_id: atlas-aml-cs0049-supply-chain-compromise-via-poisoned-clawdbot-skill
brain_sha256: 617d8564721ca87c51950b0a745bcd7349b88674d31e22b7756b14b56ae1a2e7
domains:
- AI
- RISK
evidence_sources:
- AI_NICE_TO_KNOW
id: atlas-aml-cs0049-supply-chain-compromise-via-poisoned-clawdbot-skill
status: stable
tags:
- famous-ai-incidents
- case-study
- mitre-atlas
- supply-chain
title: Supply Chain Compromise via Poisoned ClawdBot Skill
type: knowledge
---

# Supply Chain Compromise via Poisoned ClawdBot Skill

## Summary

A security researcher demonstrated a proof-of-concept supply chain attack using a poisoned ClawdBot Skill shared on ClawdHub, a Skill registry for agents. The poisoned Skill contained a prompt injection that caused ClawdBot to execute a shell command that reached the researcher's server. Although the researcher here used this access simply to warn users about the danger, they could have instead delivered a malicious payload and compromised the user's system. The security researcher recorded 16 different users who downloaded and executed the poisoned Skill in the first 8 hours of it being published on ClawdHub.

## Applicability

This MITRE ATLAS case study is a contextual security example for threat modeling, control design, detection, testing, and incident response. It describes a demonstrated attack or research proof of concept; it does not establish a universal legal requirement.

## ATLAS mapping

- Case study: \`AML.CS0049\`
- Last modified in the supplied ATLAS release: 2026-07-31
- Related ATLAS techniques: \`AML.T0008.002\`, \`AML.T0010.005\`, \`AML.T0011.002\`, \`AML.T0017\`, \`AML.T0048\`, \`AML.T0051.001\`, \`AML.T0053\`, \`AML.T0065\`, \`AML.T0074\`, \`AML.T0110.000\`, \`AML.T0111\`, \`AML.T0115.002\`

## Governance considerations

Use this case to test whether the AI system has documented ownership, trusted artifact provenance, least-privilege access, boundary controls, validation, monitoring, and incident response appropriate to its architecture. Treat the scenario as a prompt for evidence collection and control verification; do not infer that the case proves a specific organization has suffered the same exposure.


## Related concepts

- [prompt-injection](/concepts/prompt-injection.md) 
- [agentic-ai](/concepts/agentic-ai.md) 
- [traceability](/concepts/traceability.md) 
- [red-teaming](/concepts/red-teaming.md) 
- [human-oversight](/concepts/human-oversight.md)

## Source references

- SRC-0046, MITRE ATLAS v2026.08 STIX export, JSON pointer \`/objects\`, object \`AML.CS0049\`; source SHA-256: \`6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c\`; unit SHA-256: \`13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab\`.
- Canonical ATLAS record: https://atlas.mitre.org/studies/AML.CS0049
