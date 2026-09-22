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

A material-change gate should identify changes to data, code, models, libraries, configuration, suppliers, interfaces, purpose or operating context. The gate records the impact assessment, risk reassessment, required validation, approval or restriction, release decision and post-release monitoring. A lifecycle record should also retain the reason for a rollback, pause or retirement decision and the evidence needed to resume or close the system safely. This is a governance pattern supported by guidance and framework material, not a universal legal requirement.

## Limits

The lifecycle is a governance map, not a universal process model or a certification. Stages can overlap, iterate or be performed by different parties. A lifecycle inventory does not by itself demonstrate safety, legality, fairness or fitness for a particular use; those conclusions require context-specific evidence and review.

## Related Concepts

- [[ai-system]]
- [[ai-lifecycle-change-gates]]
- [[ai-model-validation]]
- [[ai-model-monitoring]]
- [[ai-model-documentation]]
- [[traceability]]

## Source References

- SRC-0039, NIST AI RMF 1.0, page 19 (ongoing testing and monitoring for validity, reliability and robustness).
- SRC-0036, SR 26-2, pages 6 and 14 (model lifecycle and monitoring context).
- SRC-0001, page 17 (version control, reassessment and monitoring after implementation changes).
- SRC-0002, pages 8 and 10 (dynamic documentation, update triggers, system owner, suppliers, roles and existing evidence).
