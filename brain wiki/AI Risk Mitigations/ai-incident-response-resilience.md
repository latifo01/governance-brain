---
id: ai-incident-response-resilience
title: AI incident response and operational resilience
type: knowledge
domains: [OPERATIONAL_RESILIENCE_INCIDENTS, AI_SECURITY, RISK]
status: active
aliases:
  - AI incident response lifecycle
  - Résilience opérationnelle des systèmes d’IA
tags:
  - incidents
  - operational-resilience
  - incident-response
  - recovery
  - playbooks
evidence_sources: [AI_NICE_TO_KNOW, AI_REGULATION_INTERNAL]
---

# AI incident response and operational resilience

## Summary

AI incident response is the coordinated ability to govern, identify, protect,
detect, respond to and recover from incidents affecting an AI system. AI
systems add incident surfaces such as model artefacts, prompts, retrieval
stores, tool calls, agent memory and non-deterministic outputs. A resilient
arrangement preserves evidence, limits harm, restores from trusted baselines
and feeds lessons into later controls (SRC-0028, pages 6-7 and 22-24).
The ORX Reference Taxonomy supplies a non-binding operational-risk vocabulary
that can help distinguish causes, events, impacts and controls when an AI
incident is classified; it is a reference for adaptation rather than a
standard (SRC-0041, pages 2, 4 and 8).

## Applicability

This concept applies to deployed AI systems, AI-enabled services and agentic
workflows whose compromise or failure can affect confidentiality, integrity,
availability, safety, rights or business continuity. The response depth should
reflect the system architecture, affected data, operational dependency and
incident severity. The CoSAI framework is technical guidance, not a universal
legal reporting rule; reporting duties require a separate jurisdictional and
sector assessment (SRC-0028, pages 21-23).

## Governance considerations

- Define AI-specific incident types, roles, escalation routes and playbooks
  across preparation, detection, response, recovery and improvement. Include
  AI/ML, security, operations, legal and relevant business participants
  (SRC-0028, pages 7, 21 and 23).
- Maintain inventories and telemetry for models, datasets, prompts,
  dependencies, APIs, tool executions and affected components. During triage,
  classify the incident, estimate scope and impact, identify affected users or
  data, and preserve interaction logs, configurations, versions and network or
  API evidence (SRC-0028, pages 6, 15-16 and 23).
- Use architecture-specific containment and recovery. Examples include
  isolating components, disabling tools, revoking credentials, quarantining
  retrieval data, rolling back to trusted model versions and validating the
  restored system before return to production (SRC-0028, pages 17 and 23-24).
- Preserve forensic copies and chain of custody, document containment and
  remediation actions, test the effectiveness of fixes, and record root cause,
  detection gaps and lessons learned (SRC-0028, pages 17 and 24, 30-34).
- Use structured playbooks with named activities, targets, authentication,
  versioning and integrity markings when response automation crosses tools or
  organisational boundaries (SRC-0028, pages 24-27).

## Evidence to retain

Retain the incident policy and playbooks; role and escalation matrix; system,
model and dependency inventory; monitoring and alert records; triage and impact
assessment; forensic evidence register; containment and recovery decisions;
validation results; communications; remediation tracking; and post-incident
lessons learned. Remove or protect personal data before sharing incident
material outside the authorised response group (SRC-0028, pages 16-17 and
21-24).

## Limits

SRC-0028 is a technical incident-response framework and maps to other
frameworks; it does not establish a generally applicable reporting deadline or
legal obligation. Its examples are patterns for adaptation, not proof that a
particular organisation has implemented them. Legal, privacy and contractual
notification decisions remain outside this note.

## Related concepts

- [[ai-model-monitoring]] connects detection signals to accountable action.
- [[traceability]] covers lineage and evidence across system components.
- [[data-leakage]] covers disclosure as an AI incident surface.
- [[ai-governance-accountability]] connects incidents to ownership and lifecycle decisions.
- [[red-teaming]] supports adversarial exercises and response validation.

## Source references

- SRC-0028, *AI Incident Response Framework V1.0*, pages 6-7, 15-17 and 21-27 (AI incident lifecycle, triage, evidence, containment, recovery, roles, playbooks and communications).
- SRC-0028, pages 30-34 (illustrative detection, containment, remediation and incident-record workflows).
- SRC-0041, *ORX Reference Taxonomy summary report*, pages 2, 4 and 8 (operational-risk reference status and cause/event/impact/control model).
