---
id: ai-supply-chain-governance
title: AI supply chain governance
type: knowledge
domains: [AI_SECURITY, THIRD_PARTIES_SUPPLY_CHAIN, RISK, PROCESS]
status: active
aliases:
  - AI supply chain risk management
  - Gouvernance de la chaîne d'approvisionnement IA
tags:
  - ai-supply-chain
  - third-party-risk
  - provenance
  - aibom
  - software-integrity
evidence_sources: [AI_NICE_TO_KNOW, AI_REGULATION_INTERNAL]
---

# AI supply chain governance

## Summary

AI supply chain governance keeps an inventory and evidence trail for the models,
datasets, software, tools, connectors, services and deployment infrastructure on
which an AI system depends. The reviewed material treats this as a risk and
control practice rather than a universal legal requirement.

## Applicability

The depth of governance should reflect external dependencies, trust boundaries,
delegated access, data sensitivity, system impact and the ability to inspect or
replace a component. It is especially relevant to systems using foundation-model
providers, MCP servers, plugins, managed connectors, model registries or
cross-organisation agents.

## Governance considerations

- Maintain a component inventory covering model and dataset versions, providers,
  training or retrieval lineage where available, runtime environments,
  connectors, tools and external registries.
- Preserve provenance, version, origin, checksum or content hash, transformation
  and change information for material artifacts. AI BOM and dependency records
  should remain linked to the system and deployment context.
- Assess the trustworthiness and integrity of external libraries, models,
  datasets, packages and services. Use signing, verification, scanning,
  dependency pinning and approved-source workflows where proportionate.
- Record how a compromised or unavailable dependency can propagate through
  downstream projects, and define containment, rollback and restoration from a
  trusted configuration.
- Reassess the inventory and control evidence when a provider, model, tool,
  connector, version, access scope or deployment boundary changes.

## Limits

The sources are frameworks, threat models and security guidance. They support
risk identification, controls and evidence expectations; they do not establish
legal obligations, a mandatory certification or a fixed AI BOM format.
Regulatory conclusions require a separate review of the applicable primary
source.

## Related concepts

- [[traceability]] links component changes to evidence and decisions.
- [[ai-data-quality-and-validation]] covers data quality and provenance limits.
- [[ai-agent-authority-expansion-controls]] addresses authority changes during operation.
- [[ai-incident-response-resilience]] connects supply-chain compromise to response and recovery.

## Source references

- SRC-0024, pages 20, 22, 152, 155-156, for supply-chain definitions,
  external-library trust, AI BOM, integrity checks and provenance.
- SRC-0025, pages 46-47, 66, 71-73 and 116-117, for agent dependency
  inventories, trust boundaries, delegated access and supply-chain mitigations.
- SRC-0034, pages 3, 7 and 30, for lifecycle supply-chain scope, provenance
  fields and third-party service assurance.
- SRC-0035, pages 4, 7 and 11, for signing, attestation and verification
  across organisational boundaries.
- SRC-0044, mitigation and relationship rows, for code signing, artifact
  scanning, AI BOM, provenance and integrity monitoring.
- SRC-0046, AML.T0010.005, AML.T0011.002 and AML.M0025/M0033/M0036/M0038,
  for agent tools, poisoned tools, provenance, validation, authority controls
  and scope-drift detection.
