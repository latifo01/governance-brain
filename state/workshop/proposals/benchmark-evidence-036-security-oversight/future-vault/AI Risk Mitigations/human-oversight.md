---
id: human-oversight
title: Human oversight
type: knowledge
domains: [AI, RISK, LEGAL, PROCESS]
status: active
aliases:
  - Human oversight
  - Supervision humaine
  - Contrôle humain
tags:
  - human-oversight
  - ai-act
  - governance
evidence_sources: [AI_NICE_TO_KNOW, AI_REGULATION_INTERNAL]
---

# Human oversight

## Summary

Human oversight is a governance process in which human roles, responsibilities and intervention mechanisms are defined, assessed and documented for the relevant AI use. NIST describes human-AI configurations as ranging from autonomous to manual and emphasises that the appropriate arrangement depends on context.

Effective oversight requires more than naming a reviewer. The design should make the reviewer’s information, competence, authority, time, escalation route and ability to challenge or stop an action explicit.

## Applicability

Oversight is particularly relevant where an AI system can influence material decisions, change goals, call tools, access sensitive information, modify records or propagate outputs to other systems. The appropriate degree and form of oversight should follow the risk context and the system’s human-AI configuration.

For agentic systems, high-impact or goal-changing actions may warrant a human gate, output validation and scoped access. These are control-design recommendations from security guidance and should be assessed against the system’s actual authority and consequences.

## Governance Considerations

A reviewable oversight design should:

- define the human roles and responsibilities for decision-making, supervision, escalation and intervention;
- document the information, uncertainty, limitations and context available to the reviewer;
- assess competence, training, time, authority and the ability to interrupt, reject or defer an output;
- apply human approval gates, output validation, isolation and monitoring where downstream impact warrants them;
- record oversight decisions and test whether the workflow creates automation bias or makes rejection impracticable.

The design should be assessed and documented under the organization’s governance process. OWASP recommendations for human approval and NIST expectations for documented oversight are non-binding guidance and framework material.

## Limits

NIST AI RMF is a voluntary framework and does not itself create legal obligations. OWASP guidance describes security controls rather than a universal oversight pattern. This note deliberately does not generalize the unresolved real-time remote biometric identification pages from SRC-0016; no AI Act obligation or universal two-person rule is asserted here.

## Related Concepts

- [[genai-guardrails]]
- [[prompt-injection]]
- [[red-teaming]]
- [[ai-model-documentation]]

## Source References

- SRC-0039, pages 32 and 45, for documented human oversight processes, differentiated human-AI roles and contextual configurations.
- SRC-0027, pages 11 and 33, for human approval of high-impact or goal-changing actions and human gates before high-risk outputs propagate.
- SRC-0026, pages 10-12, for the agentic and privilege-related attack context that can make human gates relevant.
