---
id: ai-lifecycle
title: AI lifecycle
type: knowledge
domains: [AI, PROCESS, MODEL_RISK, GOVERNANCE_ACCOUNTABILITY]
status: active
aliases:
  - AI system lifecycle
  - Cycle de vie de l'IA
tags:
  - ai-concepts
  - lifecycle
  - governance
evidence_sources: [AI_NICE_TO_KNOW, AI_REGULATION_INTERNAL]
---

# AI lifecycle

## Summary

The AI lifecycle is the connected set of activities through which an AI system is conceived, designed, developed, evaluated, deployed, operated, monitored, changed and retired. The lifecycle is socio-technical: it includes data, models, software, infrastructure, users, affected people, governance decisions and operating context. NIST places risk management across these stages and treats Test, Evaluation, Verification and Validation (TEVV) as work that continues throughout the lifecycle.

## Applicability

Use this concept when establishing an inventory, assigning accountability, planning assurance, assessing a change or deciding whether evidence remains current. The relevant stages and actors vary by system. A model provider, application developer, integrator, deployer, operator, evaluator and auditor may hold different responsibilities, and one organisation can hold several roles.

## Governance Considerations

A lifecycle record connects the system purpose and context to data and input preparation, model development, integration, deployment, operation, monitoring, change control and retirement. Each transition can carry forward assumptions, limitations, evaluation results, approvals, incidents and decisions. TEVV activities should be planned for the stage they address and revisited when the system, data, context or intended use changes. [[ai-model-documentation]], [[ai-model-validation]] and [[ai-model-monitoring]] provide operational controls for this record.

## Limits

The lifecycle is a governance map, not a universal process model or a certification. Stages can overlap, iterate or be performed by different parties. A lifecycle inventory does not by itself demonstrate safety, legality, fairness or fitness for a particular use; those conclusions require context-specific evidence and review.

## Related Concepts

- [[ai-system]]
- [[ai-model-validation]]
- [[ai-model-monitoring]]
- [[ai-model-documentation]]
- [[traceability]]

## Source References

- SRC-0039, NIST AI RMF 1.0, pages 10-11 and 21-22 (lifecycle dimensions and trustworthiness measurement), page 14 (TEVV across the lifecycle), pages 26-27 (iterative functions and full product lifecycle), pages 40-41 (actor tasks and lifecycle TEVV).
- SRC-0036, SR 26-2, pages 6 and 14 (model lifecycle and monitoring context).
