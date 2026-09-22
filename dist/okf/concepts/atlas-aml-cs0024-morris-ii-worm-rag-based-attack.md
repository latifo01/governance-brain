---
aliases:
- 'Morris II Worm: RAG-Based Attack'
brain_id: atlas-aml-cs0024-morris-ii-worm-rag-based-attack
brain_sha256: 65362d073824549d48c6eb0010479aafaf1509ed43b9a535821668805e2c43b7
domains:
- AI
- RISK
evidence_sources:
- AI_NICE_TO_KNOW
id: atlas-aml-cs0024-morris-ii-worm-rag-based-attack
status: stable
tags:
- famous-ai-incidents
- case-study
- mitre-atlas
title: 'Morris II Worm: RAG-Based Attack'
type: knowledge
---

# Morris II Worm: RAG-Based Attack

## Summary

Researchers developed Morris II, a zero-click worm designed to attack generative AI (GenAI) ecosystems and propagate between connected GenAI systems. The worm uses an adversarial self-replicating prompt which uses prompt injection to replicate the prompt as output and perform malicious activity.
The researchers demonstrate how this worm can propagate through an email system with a RAG-based assistant. They use a target system that automatically ingests received emails, retrieves past correspondences, and generates a reply for the user. To carry out the attack, they send a malicious email containing the adversarial self-replicating prompt, which ends up in the RAG database. The malicious instructions in the prompt tell the assistant to include sensitive user data in the response. Future requests to the email assistant may retrieve the malicious email. This leads to propagation of the worm due to the self-replicating portion of the prompt, as well as leaking private information due to the malicious instructions.

## Applicability

This MITRE ATLAS case study is a contextual security example for threat modeling, control design, detection, testing, and incident response. It describes a demonstrated attack or research proof of concept; it does not establish a universal legal requirement.

## ATLAS mapping

- Case study: \`AML.CS0024\`
- Last modified in the supplied ATLAS release: 2026-03-31
- Related ATLAS techniques: \`AML.T0040\`, \`AML.T0048.003\`, \`AML.T0051.000\`, \`AML.T0051.002\`, \`AML.T0053\`, \`AML.T0057\`, \`AML.T0061\`

## Governance considerations

Use this case to test whether the AI system has documented ownership, trusted artifact provenance, least-privilege access, boundary controls, validation, monitoring, and incident response appropriate to its architecture. Treat the scenario as a prompt for evidence collection and control verification; do not infer that the case proves a specific organization has suffered the same exposure.


## Related concepts

- [prompt-injection](/concepts/prompt-injection.md) 
- [retrieval-augmented-generation](/concepts/retrieval-augmented-generation.md) 
- [red-teaming](/concepts/red-teaming.md)

## Source references

- SRC-0046, MITRE ATLAS v2026.08 STIX export, JSON pointer \`/objects\`, object \`AML.CS0024\`; source SHA-256: \`6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c\`; unit SHA-256: \`13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab\`.
- Canonical ATLAS record: https://atlas.mitre.org/studies/AML.CS0024
