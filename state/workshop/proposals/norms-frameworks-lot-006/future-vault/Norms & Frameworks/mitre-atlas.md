---
id: mitre-atlas
title: MITRE ATLAS
type: knowledge
domains: [AI, RISK]
status: active
aliases:
  - ATLAS
  - Adversarial Threat Landscape for AI Systems
tags:
  - norms-frameworks
  - adversarial-ai
  - threat-intelligence
evidence_sources: [AI_NICE_TO_KNOW]
---

# MITRE ATLAS

## Summary

MITRE ATLAS (Adversarial Threat Landscape for AI Systems) is a knowledge base of adversarial techniques against AI systems. It emerged following real-world AI attacks, for example model extraction from prediction APIs, and documents 80+ adversarial techniques observed in production environments.

In the local corpus, CoSAI's "Preparing Defenders of AI Systems" characterizes ATLAS as cataloging attacks and adversarial tactics effectively, while lacking the defensive playbooks and countermeasures that exist for general enterprise threats (ATT&CK, D3FEND). CoSAI's AI Incident Response framework applies ATLAS tactics and techniques mapping throughout its detection and response guidance.

## Applicability

This note applies to threat modeling, detection engineering and incident response for AI systems: ATLAS provides the attacker-side vocabulary for classifying adversarial events (see [[red-teaming]] and [[prompt-injection]]).

## Governance Considerations

- Use ATLAS techniques as the taxonomy for AI security tests and detection content; map incidents to techniques for trend analysis.
- Compensate for the noted absence of defensive countermeasures by pairing ATLAS mappings with control frameworks (e.g., [[aiuc-1]] crosswalks, OWASP agentic controls).
- Feed ATLAS-mapped incident data into [[ai-model-monitoring]] detection baselines.

## Limits

ATLAS is described through secondary sources in this corpus (CoSAI documents); no ATLAS primary source is ingested. The technique count is as stated by SRC-0033 and evolves; consult the live knowledge base for current coverage.

## Related Concepts

- [[nist-ai-rmf]] MEASURE function can consume ATLAS-derived threat intelligence.
- [[red-teaming]] operationalizes technique validation.
- [[aiuc-1]] maps security controls against agentic risks that ATLAS-classified attacks exploit.

## Source References

- SRC-0033, CoSAI Preparing Defenders of AI Systems, page 8 (ATLAS emerged from real-world AI attacks such as model extraction from prediction APIs; documents 80+ adversarial techniques observed in production), pages 9-10 (ATLAS catalogs attacks effectively but lacks defensive playbooks and countermeasures compared with ATT&CK/D3FEND).
- SRC-0028, CoSAI AI Incident Response Framework V1.0, pages 14 and 37-61 (ATLAS tactics and techniques mapping applied to detection and response playbooks).
