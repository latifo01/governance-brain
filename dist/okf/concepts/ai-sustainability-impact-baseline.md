---
aliases:
- Environmental impact baseline for AI
- AI sustainability metrics
- Référentiel d'impact environnemental de l'IA
brain_id: ai-sustainability-impact-baseline
brain_sha256: ed81ecf2db057feb30307893714a481553da492a7ac5f792a214b38d74ebe284
domains:
- HUMAN_OVERSIGHT_RESPONSIBLE_AI
- RISK
- PROCESS
evidence_sources:
- AI_NICE_TO_KNOW
id: ai-sustainability-impact-baseline
sources:
- authority: FRAMEWORK
  brain_source_id: SRC-0040
  evidence_ref: ssi-org29-src-0040-p0035
  id: brain-3ab7a71c0ee92e21
  locator: Page 35
  resource: /references/src-0040-65d6101d806502875aadb0fd19a75c3a9cc9a5e9461129e9398a39192d8202d2.md
  unit_file_sha256: 33509b9fb484e8c7ea15a5be744838eee0e5640531e22482f21e0f00791e3126
  unit_path: ingest/SRC-0040/units/p0035.md
  unit_sha256: 98a2b39b2884a60b87b4f74adef7445be8064bdee3b2844445576ed7e8e89ffc
- authority: FRAMEWORK
  brain_source_id: SRC-0040
  evidence_ref: ssi-org29-src-0040-p0127
  id: brain-81ed4d497578be3b
  locator: Page 127
  resource: /references/src-0040-65d6101d806502875aadb0fd19a75c3a9cc9a5e9461129e9398a39192d8202d2.md
  unit_file_sha256: 7cc18ffd51556447fcef55617687efb6df8da4444e0110b062c519c0df705339
  unit_path: ingest/SRC-0040/units/p0127.md
  unit_sha256: 583e279e769939699e63fd75cb269e5ffc94aeda32cbfcc2a3914e37a1853acc
- authority: FRAMEWORK
  brain_source_id: SRC-0040
  evidence_ref: ssi-org29-src-0040-p0059
  id: brain-8edcd2ee7a3e44a6
  locator: Page 59
  resource: /references/src-0040-65d6101d806502875aadb0fd19a75c3a9cc9a5e9461129e9398a39192d8202d2.md
  unit_file_sha256: cac576a5deeb75cdd32ba3befb6c2d9bf75b7e3d6cc0932fc0c59c129003d4a2
  unit_path: ingest/SRC-0040/units/p0059.md
  unit_sha256: b5f9e80ca7bebc58a3dd24ffc8dee8842017ac2bbc59d5d8daf37d7bd3d2355f
- authority: FRAMEWORK
  brain_source_id: SRC-0040
  evidence_ref: ssi-org29-src-0040-p0036
  id: brain-9964e8bf22e783c5
  locator: Page 36
  resource: /references/src-0040-65d6101d806502875aadb0fd19a75c3a9cc9a5e9461129e9398a39192d8202d2.md
  unit_file_sha256: d323c488e78cfeb7e405fbf1251f413ba1e129360dc7d1c580d287de0b991bf1
  unit_path: ingest/SRC-0040/units/p0036.md
  unit_sha256: 134f9f3b8be4acb77b287e6feb5bbf5156aa16c6b95edc904dd70109ed8a4fcd
status: stable
tags:
- sustainability
- environmental-impact
- impact-assessment
- metrics
title: AI sustainability impact baseline
type: knowledge
---


# AI sustainability impact baseline

## Summary

An AI sustainability impact baseline defines the system boundary, lifecycle stage, material impacts, indicators, data sources and comparison point used to understand environmental effects. It allows decision-makers to distinguish measured change from assumption and to connect resource trade-offs to system design, deployment and retirement decisions.

Section evidence: [^brain-81ed4d497578be3b]

## Applicability

Use this concept when compute, infrastructure, data processing, model use, supplier services or deployment scale may materially affect energy, water, emissions or other environmental conditions. The boundary should be proportionate to the system and transparent about what is measured and what remains unknown.

Section evidence: [^brain-8edcd2ee7a3e44a6]

## Governance considerations

- Define the lifecycle and infrastructure boundary, including relevant suppliers and repeated training or inference activity.
- Record the baseline, measurement period, data quality, assumptions and materiality rationale for each selected indicator.
- Consider impacts across affected groups and environmental ecosystems, including trade-offs between performance, access, safety, fairness and resource use.
- Assign an owner, review cadence and escalation route for material deviations or newly identified impacts.
- Link the indicators to design, procurement, deployment, monitoring and decommissioning decisions; retain the evidence used for significant trade-offs.

Section evidence: [^brain-3ab7a71c0ee92e21]

## Limits

The NIST AI RMF Playbook material used here is a voluntary framework. It does not prescribe a universal environmental metric, boundary, threshold or reporting obligation. Applicable environmental, sectoral, procurement and disclosure requirements must be analysed separately.

Section evidence: [^brain-9964e8bf22e783c5]

## Related concepts

- [ai-societal-impact-and-stakeholder-engagement](/concepts/ai-societal-impact-and-stakeholder-engagement.md)
- [ai-impact-assessment-aiia](/concepts/ai-impact-assessment-aiia.md)
- [ai-model-monitoring](/concepts/ai-model-monitoring.md)
- [ai-lifecycle](/concepts/ai-lifecycle.md)

## Source references

- SRC-0040, pages 28-30 (context, impact assessment and affected groups).
- SRC-0040, pages 59 and 127 (impact indicators, environmental ecosystems, data quality and context-specific metrics).


[^brain-3ab7a71c0ee92e21]: [SRC-0040](/references/src-0040-65d6101d806502875aadb0fd19a75c3a9cc9a5e9461129e9398a39192d8202d2.md); locator: Page 35.
[^brain-81ed4d497578be3b]: [SRC-0040](/references/src-0040-65d6101d806502875aadb0fd19a75c3a9cc9a5e9461129e9398a39192d8202d2.md); locator: Page 127.
[^brain-8edcd2ee7a3e44a6]: [SRC-0040](/references/src-0040-65d6101d806502875aadb0fd19a75c3a9cc9a5e9461129e9398a39192d8202d2.md); locator: Page 59.
[^brain-9964e8bf22e783c5]: [SRC-0040](/references/src-0040-65d6101d806502875aadb0fd19a75c3a9cc9a5e9461129e9398a39192d8202d2.md); locator: Page 36.
