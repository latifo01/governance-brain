---
aliases:
- Malicious Models on Hugging Face
brain_id: atlas-aml-cs0031-malicious-models-on-hugging-face
brain_sha256: 7669691a0f9378a90558c86ba2e59ad65e2febedcad4e629c786afac34f012bc
domains:
- AI
- RISK
evidence_sources:
- AI_NICE_TO_KNOW
id: atlas-aml-cs0031-malicious-models-on-hugging-face
status: stable
tags:
- famous-ai-incidents
- case-study
- mitre-atlas
- hugging-face
title: Malicious Models on Hugging Face
type: knowledge
---

# Malicious Models on Hugging Face

## Summary

Researchers at ReversingLabs have identified malicious models containing embedded malware hosted on the Hugging Face model repository. The models were found to execute reverse shells when loaded, which grants the threat actor command and control capabilities on the victim's system. Hugging Face uses Picklescan to scan models for malicious code, however these models were not flagged as malicious. The researchers discovered that the model files were seemingly purposefully corrupted in a way that the malicious payload is executed before the model ultimately fails to de-serialize fully. Picklescan relied on being able to fully de-serialize the model.

Since becoming aware of this issue, Hugging Face has removed the models and has made changes to Picklescan to catch this particular attack. However, pickle files are fundamentally unsafe as they allow for arbitrary code execution, and there may be other types of malicious pickles that Picklescan cannot detect.

## Applicability

This MITRE ATLAS case study is a contextual security example for threat modeling, control design, detection, testing, and incident response. It describes a demonstrated attack or research proof of concept; it does not establish a universal legal requirement.

## ATLAS mapping

- Case study: \`AML.CS0031\`
- Last modified in the supplied ATLAS release: 2025-04-22
- Related ATLAS techniques: \`AML.T0010\`, \`AML.T0011.000\`, \`AML.T0018.002\`, \`AML.T0072\`, \`AML.T0076\`, \`AML.T0115.001\`

## Governance considerations

Use this case to test whether the AI system has documented ownership, trusted artifact provenance, least-privilege access, boundary controls, validation, monitoring, and incident response appropriate to its architecture. Treat the scenario as a prompt for evidence collection and control verification; do not infer that the case proves a specific organization has suffered the same exposure.


## Related concepts

- [traceability](/concepts/traceability.md) 
- [ai-model-validation](/concepts/ai-model-validation.md) 
- [red-teaming](/concepts/red-teaming.md)

## Source references

- SRC-0046, MITRE ATLAS v2026.08 STIX export, JSON pointer \`/objects\`, object \`AML.CS0031\`; source SHA-256: \`6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c\`; unit SHA-256: \`13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab\`.
- Canonical ATLAS record: https://atlas.mitre.org/studies/AML.CS0031
