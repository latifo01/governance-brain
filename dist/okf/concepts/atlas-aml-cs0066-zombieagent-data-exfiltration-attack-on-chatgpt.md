---
aliases:
- 'ZombieAgent: Data Exfiltration Attack on ChatGPT'
brain_id: atlas-aml-cs0066-zombieagent-data-exfiltration-attack-on-chatgpt
brain_sha256: ae98323eb16095683397df638ced44b08e282d1518bd490e6f3bdb535d225253
domains:
- AI
- RISK
evidence_sources:
- AI_NICE_TO_KNOW
id: atlas-aml-cs0066-zombieagent-data-exfiltration-attack-on-chatgpt
status: stable
tags:
- famous-ai-incidents
- case-study
- mitre-atlas
- data-exfiltration
title: 'ZombieAgent: Data Exfiltration Attack on ChatGPT'
type: knowledge
---

# ZombieAgent: Data Exfiltration Attack on ChatGPT

## Summary

ZombieAgent is a proof-of-concept indirect prompt injection attack demonstrated by Radware against OpenAI's ChatGPT Deep Research and Connector functionality. The attacks showed how instructions concealed in externally controlled content, such as emails and documents, could be ingested and executed by ChatGPT during normal user activity. The demonstration used Gmail as the injection source, but any ChatGPT Connector such as Outlook, Google Drive, Jira, or Teams could be similarly abused.

The Radware Security Researchers sent a malicious email containing concealed instructions to a Gmail inbox connected to ChatGPT. When the user later asked ChatGPT to perform an ordinary inbox-related task, ChatGPT retrieved the email and executed its instructions. The user did not open, click, or knowingly interact with the malicious email.

The injected instructions caused ChatGPT to collect information from connected services and exfiltrate it through URL requests. OpenAI had introduced a control preventing ChatGPT from dynamically constructing or modifying URLs which could be used to exfiltrate data via query parameters. The researchers bypassed this control by supplying an indexed dictionary of preconstructed static URLs and instructing ChatGPT to open URLs corresponding to individual characters to exfiltrate the collected data.

The researchers also showed that the malicious instructions could manipulate ChatGPT's Memory. The injected memories instructed ChatGPT to retain sensitive information from future conversations and to retrieve and execute a designated attacker-controlled email during later interactions. This created a persistent mechanism for repeated collection and exfiltration across chat sessions.

The researchers also demonstrated how the malicious prompt could be propagated. A compromised agent could collect email addresses from the victim's mailbox and use its connected email capabilities to send additional messages containing the malicious prompt to those contacts. Recipients whose AI agents later processed the poisoned messages could become additional victims.

## Applicability

This MITRE ATLAS case study is a contextual security example for threat modeling, control design, detection, testing, and incident response. It describes a demonstrated attack or research proof of concept; it does not establish a universal legal requirement.

## ATLAS mapping

- Case study: \`AML.CS0066\`
- Last modified in the supplied ATLAS release: 2026-07-31
- Related ATLAS techniques: \`AML.T0051.001\`, \`AML.T0053\`, \`AML.T0053\`, \`AML.T0054\`, \`AML.T0065\`, \`AML.T0068\`, \`AML.T0079\`, \`AML.T0080.000\`, \`AML.T0085.001\`, \`AML.T0085.001\`, \`AML.T0086\`, \`AML.T0093\`

## Governance considerations

Use this case to test whether the AI system has documented ownership, trusted artifact provenance, least-privilege access, boundary controls, validation, monitoring, and incident response appropriate to its architecture. Treat the scenario as a prompt for evidence collection and control verification; do not infer that the case proves a specific organization has suffered the same exposure.


## Related concepts

- [prompt-injection](/concepts/prompt-injection.md) 
- [data-leakage](/concepts/data-leakage.md) 
- [agentic-ai](/concepts/agentic-ai.md) 
- [red-teaming](/concepts/red-teaming.md)

## Source references

- SRC-0046, MITRE ATLAS v2026.08 STIX export, JSON pointer \`/objects\`, object \`AML.CS0066\`; source SHA-256: \`6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c\`; unit SHA-256: \`13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab\`.
- Canonical ATLAS record: https://atlas.mitre.org/studies/AML.CS0066
