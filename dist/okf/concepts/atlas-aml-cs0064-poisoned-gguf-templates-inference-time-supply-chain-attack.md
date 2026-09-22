---
aliases:
- 'Poisoned GGUF Templates: Inference-Time Supply Chain Attack'
brain_id: atlas-aml-cs0064-poisoned-gguf-templates-inference-time-supply-chain-attack
brain_sha256: 8e271461e8e60ec739f97f2303cc0fb48b36bcc8225803e76b505570341afb8b
domains:
- AI
- RISK
evidence_sources:
- AI_NICE_TO_KNOW
id: atlas-aml-cs0064-poisoned-gguf-templates-inference-time-supply-chain-attack
status: stable
tags:
- famous-ai-incidents
- case-study
- mitre-atlas
- supply-chain
- data-exfiltration
title: 'Poisoned GGUF Templates: Inference-Time Supply Chain Attack'
type: knowledge
---

# Poisoned GGUF Templates: Inference-Time Supply Chain Attack

## Summary

Researchers from Pillar Security and Fujitsu Research of Europe demonstrated an inference-time supply-chain backdoor in which poisoned chat templates alter model and agent behavior without modifying model weights. The backdoor is embedded in trusted prompt-construction logic, allowing it to remain dormant until triggered and evade defenses that inspect only external prompt content.

The researchers demonstrated the attack using GPT-Generated Unified Format (GGUF), a widely used model format that packages quantized weights, configuration metadata, and chat-template logic in one artifact. An adversary can modify a template and redistribute the artifact; when a lexical, semantic, or contextual trigger occurs, the template injects attacker-controlled instructions into the context sent to the model.

The attack was validated across eighteen models from seven families and four inference engines. In controlled evaluations, it manipulated model responses, redirected agent tool use, exfiltrated sensitive data, and inserted attacker-controlled code into generated software.

## Applicability

This MITRE ATLAS case study is a contextual security example for threat modeling, control design, detection, testing, and incident response. It describes a demonstrated attack or research proof of concept; it does not establish a universal legal requirement.

## ATLAS mapping

- Case study: \`AML.CS0064\`
- Last modified in the supplied ATLAS release: 2026-07-31
- Related ATLAS techniques: \`AML.T0002.001\`, \`AML.T0010.003\`, \`AML.T0011.000\`, \`AML.T0017.000\`, \`AML.T0018.003\`, \`AML.T0031\`, \`AML.T0048.003\`, \`AML.T0051.002\`, \`AML.T0053\`, \`AML.T0067\`, \`AML.T0074\`, \`AML.T0086\`, \`AML.T0115.001\`

## Governance considerations

Use this case to test whether the AI system has documented ownership, trusted artifact provenance, least-privilege access, boundary controls, validation, monitoring, and incident response appropriate to its architecture. Treat the scenario as a prompt for evidence collection and control verification; do not infer that the case proves a specific organization has suffered the same exposure.


## Related concepts

- [prompt-injection](/concepts/prompt-injection.md) 
- [data-leakage](/concepts/data-leakage.md) 
- [agentic-ai](/concepts/agentic-ai.md) 
- [traceability](/concepts/traceability.md) 
- [red-teaming](/concepts/red-teaming.md)

## Source references

- SRC-0046, MITRE ATLAS v2026.08 STIX export, JSON pointer \`/objects\`, object \`AML.CS0064\`; source SHA-256: \`6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c\`; unit SHA-256: \`13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab\`.
- Canonical ATLAS record: https://atlas.mitre.org/studies/AML.CS0064
