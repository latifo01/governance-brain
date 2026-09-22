---
id: genai-guardrails
title: GenAI guardrails
type: knowledge
domains: [AI, RISK, PROCESS]
status: active
aliases:
  - Guardrails
  - Garde-fous GenAI
  - Contrôles GenAI
tags:
  - genai-security
  - controls
  - guardrails
evidence_sources: [AI_NICE_TO_KNOW, AI_REGULATION_INTERNAL]
---

# GenAI guardrails

## Summary

GenAI guardrails are preventive, detective or response controls placed around model inputs, retrieved context, tool calls, model outputs and downstream actions. They help enforce boundaries that the model cannot reliably enforce by itself, especially when the system reads untrusted content or can act through tools.

Guardrails are not one control. They are a control architecture: input validation, prompt-injection detection, retrieval filtering, schema enforcement, tool authorization, output validation, policy gates, monitoring, escalation, and human review for high-impact actions. They reduce the blast radius of [[prompt-injection]] and provide signals for [[red-teaming]] and [[ai-model-monitoring]].

## Applicability

Guardrails apply to LLM applications, RAG systems, copilots, chatbots, model-serving platforms and agentic systems. They matter most when the AI system handles sensitive data, provides advice in material workflows, influences decisions, executes tools, retrieves documents, writes persistent memory or interacts with external users.

For simple informational use cases, guardrails may focus on scope, content safety and factual grounding. For agentic or high-impact systems, guardrails should cover authorization, tool invocation, data access, execution boundaries, circuit breakers, anomaly detection, audit logging and human approval.

## Governance Considerations

A CDO-level guardrail design should be tied to risk, not vendor feature names. The governance record should define:

- the boundaries the guardrails are expected to enforce;
- where the controls run, including before the model, after retrieval, before tool execution, after model output and before downstream propagation;
- who owns thresholds, exceptions and policy changes;
- what evidence shows the control works for the intended context;
- how failures, bypasses and near misses are logged, investigated and remediated;
- how guardrails are updated when threats, models, tools or data sources change.

OWASP agentic guidance supports treating natural-language inputs and connected data sources as untrusted before they influence goal selection, planning or tool calls. It also points to least privilege, locked and auditable goals, runtime validation of user and agent intent, sanitation of connected data sources, continuous monitoring and human approval for high-impact or goal-changing actions.

For agentic workflows, guardrails should be enforced outside the model where possible. Important patterns include scoped tool credentials, external policy engines, planner-executor separation, quotas, progress caps, circuit breakers, rate limits, signed audit logs and policy gates before outputs propagate to other systems.

## Limits

Guardrails can fail. They may be bypassed by obfuscation, multimodal payloads, indirect prompt injection, new jailbreak techniques, weak policy definitions or poor placement in the architecture. A system prompt is not a reliable security boundary. Content filters alone do not compensate for excessive tool privilege or missing approval gates.

Guardrails should therefore be tested, monitored and revised. Their failure modes should be documented as residual risks, and high-impact decisions should not depend only on a hidden model instruction or unreviewed automated classifier.

## Related Concepts

- [[prompt-injection]] is a major threat that guardrails seek to contain.
- [[red-teaming]] challenges the effectiveness of guardrails before and after deployment.
- [[human-oversight]] provides governance authority for actions that require human judgment or approval.
- [[ai-model-monitoring]] records guardrail signals and detects changes in behavior.

## Source References

- SRC-0026, OWASP Top 10 for LLM Applications 2026, pages 10-12 and 30. Used for prompt-injection surfaces, persistence, agentic execution and red-team/evaluation guidance for third-party models and production pipelines.
- SRC-0027, OWASP Top 10 for Agentic Applications 2026, pages 11, 33 and 38. Used for least privilege, human approval, intent validation, source sanitation, policy engines, output validation, human gates, blast-radius controls, monitoring, containment and audit logs.
- SRC-0039, NIST AI RMF 1.0, pages 32, 35-38. Used for documented internal risk controls, measurement, monitoring and risk treatment framing.

