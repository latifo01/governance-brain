---
id: ai-governance-accountability
title: AI governance accountability
type: knowledge
domains: [AI, GOVERNANCE_ACCOUNTABILITY, AUDIT_ASSURANCE, HUMAN_OVERSIGHT_RESPONSIBLE_AI]
status: active
aliases:
  - AI governance and accountability
  - Gouvernance et responsabilité de l'IA
tags:
  - governance
  - accountability
  - lifecycle
  - auditability
  - change-management
evidence_sources: [AI_LEGAL_GUIDANCE, AI_NICE_TO_KNOW]
---

# AI governance accountability

## Summary

AI governance accountability is the organisational arrangement that connects
decision rights, named roles, lifecycle controls and evidence for an AI system.
It makes the system's purpose, suppliers, human involvement, design decisions,
changes and observed incidents traceable. The EDPB AI leaflet proposal presents
accountability as traceability of design decisions supported by documentation and
evidence, especially when several organisations develop, supply or reuse an AI
component (SRC-0002, page 4).

## Applicability

This concept applies when an AI system crosses organisational boundaries, uses
third-party models or services, influences decisions about people, or changes
after deployment. The controls should be scaled to the system's purpose,
operating context, risk profile and lifecycle. The EDPB material is a guidance
proposal rather than a binding rule; the Microsoft report is an example of one
organisation's responsible AI programme and is contextual evidence only.

## Governance considerations

- Identify the system owner, suppliers and their roles, and the governance
  functions involved (for example controller, processor, DPO and auditor). Record
  the intended purpose, operating context, excluded uses and the influence of the
  system on a decision process (SRC-0002, pages 9-10).
- Define how human operators handle outputs, including who can approve, reject,
  review or escalate a result. Keep the decision authority and escalation route
  visible alongside the system documentation (SRC-0001, page 17; SRC-0002,
  pages 9-10).
- Maintain version control for datasets, code, libraries, configuration and
  other material components. Reassess risk when the implementation changes, keep
  records of abnormal behaviour and incidents, and retain monitoring evidence
  that allows expected and observed behaviour to be compared (SRC-0001, page 17).
- Treat documentation as a lifecycle control. Revisit the system record after a
  major change and define update triggers or review dates; dynamic systems may
  require more frequent updates and monitoring (SRC-0002, pages 8 and 10).
- Use a repeatable policy-to-implementation path that links policy intake,
  review, engineering instructions, launch preparation, monitoring and incident
  response. Microsoft's report illustrates this as an internal practice, not as
  a universal requirement (SRC-0009, page 6).
- Provide role-specific AI literacy and responsible-AI training so that people
  who develop, provide, operate or oversee the system can act within their
  responsibilities. The level and content should reflect the role and system
  context (SRC-0009, page 26).

## Evidence to retain

A governance review can request a concise evidence set: the owner and supplier
register; purpose, context and excluded-use record; role and decision-rights
matrix; version and change history; risk reassessment decisions; monitoring and
incident records; human review and escalation records; and the current system or
algorithmic leaflet. These artefacts are evidence of a control design and its
operation, not proof that the system is lawful or safe by themselves.

## Limits

The EDPB sources used here describe audit and transparency proposals and
checklists. They are not classified as binding law. The Microsoft source reports
Microsoft's own governance and training practices and should not be treated as a
standard for every organisation. The cited Microsoft page has an extraction
warning requiring fidelity review, so claims here remain limited to the
descriptive text and are not based on its diagram. No current legal currency,
sector-specific threshold or jurisdictional conclusion is established by this
note.

## Related concepts

- [[ai-model-monitoring]] connects lifecycle monitoring to recorded decisions,
  thresholds, exceptions and remediation.
- [[ai-model-documentation]] describes the documentation that supports traceability.
- [[human-oversight]] covers human review and intervention around AI outputs.
- [[data-protection-impact-assessments-dpia]] addresses privacy-impact analysis
  where personal data processing is involved.
- [[nist-ai-rmf]] provides a broader voluntary risk-management reference.

## Source references

- SRC-0001, *AI Auditing - Checklist for AI Auditing*, page 11 (DPO involvement)
  and page 17 (version control, reassessment, monitoring, incidents and human
  intervention). Classified GUIDANCE.
- SRC-0002, *AI Auditing - Proposal for AI leaflets*, pages 4, 8-11 (traceability,
  accountability chain, update triggers, roles, purpose, human handling and
  auditability). Classified GUIDANCE.
- SRC-0003, *AI Auditing - Proposal for Algo-scores*, page 7 (governance
  positions, documentation and post-market monitoring as a proposed transparency
  label). Classified GUIDANCE.
- SRC-0009, *Microsoft Responsible AI Transparency Report*, pages 6, 26 and 28
  (one organisation's policy-to-implementation pipeline, role-specific literacy
  and research-informed oversight). Classified RESEARCH; page 6 carries an
  extraction warning.
