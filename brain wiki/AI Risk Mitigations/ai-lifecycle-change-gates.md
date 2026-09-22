---
id: ai-lifecycle-change-gates
title: AI lifecycle change gates
type: knowledge
domains: [PROCESS, MODEL_RISK, GOVERNANCE_ACCOUNTABILITY]
status: active
aliases:
  - Material AI change control
  - AI release gate
  - Contrôle des changements du cycle de vie IA
tags:
  - lifecycle
  - change-management
  - release-control
  - model-risk
evidence_sources: [AI_NICE_TO_KNOW, AI_LEGAL_GUIDANCE]
---

# AI lifecycle change gates

## Summary

An AI lifecycle change gate is a documented decision point that determines whether a change can proceed, requires additional validation, must be restricted or should be rolled back. The gate connects technical change records to purpose, context, risk, human roles and evidence.

## Applicability

Use the gate for material changes to training or operational data, model or prompt logic, code and libraries, configuration, interfaces, suppliers, user population, purpose or operating environment. The materiality threshold should be defined in the project governance record and applied consistently.

## Governance considerations

- Identify the changed component, owner, supplier and affected lifecycle stage.
- Record the reason for change, expected benefits, foreseeable harms and affected users or communities.
- Reassess whether the intended purpose, operating boundary, risk profile and human oversight remain valid.
- Define the validation, testing, security, data-quality and documentation work required before release.
- Record the decision, approver, restrictions, rollback conditions and post-release monitoring plan.
- Link the change to version history, incidents, exceptions and any later reassessment.

## Limits

The evidence supports a documented control pattern. It does not prescribe one change taxonomy, approval threshold or release method, and it does not establish a universal legal duty. Applicable law, sector rules and contractual controls must be assessed separately.

## Related concepts

- [[ai-lifecycle]]
- [[gov-002-lifecycle-change-reassessment]]
- [[ai-model-validation]]
- [[ai-model-monitoring]]
- [[traceability]]

## Source references

- SRC-0001, page 17, for version control, formal reassessment and monitoring mechanisms across implementation changes.
- SRC-0002, pages 8 and 10, for dynamic documentation, major-change review, ownership, suppliers, roles and existing evidence.
- SRC-0039, page 19, for ongoing testing and monitoring of validity, robustness and reliability.
