---
id: third-party-ai-assurance-and-shared-responsibility
title: Third-party AI assurance and shared responsibility
type: knowledge
domains: [THIRD_PARTIES_SUPPLY_CHAIN, AI_SECURITY, AUDIT_ASSURANCE, GOVERNANCE_ACCOUNTABILITY]
status: active
aliases:
  - Shared responsibility for AI services
  - Assurance des fournisseurs IA et responsabilités partagées
tags:
  - third-party-assurance
  - shared-responsibility
  - contracts
  - vendor-risk
  - audit-evidence
evidence_sources: [AI_NICE_TO_KNOW, AI_REGULATION_INTERNAL]
---

# Third-party AI assurance and shared responsibility

## Summary

Shared responsibility makes clear which controls and evidence belong to a model
provider, cloud or tool provider, application developer and operating
organisation. It reduces failed handoffs by connecting the allocation to
contracts, inventories, telemetry, assurance evidence and incident procedures.

## Governance considerations

- Record the service boundary, provider responsibilities, inherited controls,
  customer responsibilities and residual gaps for each material AI supplier.
- Define third-party responsibilities contractually where the service affects
  incident response, data handling, access control, model changes or recovery.
  Keep the allocation aligned with actual connectors, tools and provider APIs.
- Request evidence proportionate to risk, such as model or dataset cards, SBOM
  or AI BOM, API specifications, audit logs, telemetry, testing reports,
  attestations, lineage and control mappings.
- Assess provider security, visibility and concentration risks. Define security
  SLAs, verification rights, change notifications, monitoring, exit or rollback
  arrangements and the evidence needed when a provider cannot expose internals.
- Test handoffs and escalation across organisational boundaries. Connect the
  result to [[ai-incident-response-resilience]] and [[ai-assurance-and-independent-review]].

## Limits

These sources describe accountability frameworks and recommended assurance
patterns. They do not make a provider contract compliant by itself, guarantee a
SOC report's adequacy or establish a legal allocation of responsibility.
Applicable law and negotiated terms require separate review.

## Related concepts

- [[ai-governance-accountability]] covers decision rights and ownership.
- [[ai-assurance-and-independent-review]] covers independent challenge.
- [[traceability]] covers evidence and change lineage.
- [[ai-supply-chain-governance]] covers component and dependency governance.
- [[ai-incident-response-resilience]] covers provider handoffs during incidents.

## Source references

- SRC-0023, pages 17, 21-22, for expert review, vendor due diligence, change
  approval and monitoring of third-party access.
- SRC-0028, pages 21 and 23, for provider/application responsibility splits,
  contract allocation and incident telemetry.
- SRC-0029, pages 5, 7 and 31, for handoff risks, accountability scope and
  evidence categories.
- SRC-0034, page 30, for provider assessments, security SLAs, verification and
  audit evidence at contractual boundaries.
- SRC-0025, pages 107 and 112, for procurement, vendor management and control
  inheritance as guidance context.
