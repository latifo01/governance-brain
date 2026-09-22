---
aliases:
- AML.M0029
- Human In-the-Loop for AI Agent Actions
brain_id: human-in-the-loop-for-ai-agent-actions
brain_sha256: f3fb1dba58983257b9b9482311042f3f5dbe89fbe0877cf35ff7a85540e7d0c8
domains:
- AI
- RISK
- PROCESS
evidence_sources:
- AI_NICE_TO_KNOW
id: human-in-the-loop-for-ai-agent-actions
status: stable
tags:
- ai-security
- agentic-ai
- human-oversight
- mitre-atlas
title: Human in the loop for AI agent actions
type: knowledge
---


# Human in the loop for AI agent actions

## Summary

Human in the loop for AI agent actions is a MITRE ATLAS mitigation identified as `AML.M0029`. It places an authorised human decision point before selected agent actions, so that tool use and consequential operations can be reviewed, approved, rejected or stopped. ATLAS classifies this as security knowledge and guidance; it does not create a legal obligation.

## Applicability

The mitigation is relevant to agentic systems that invoke tools or can affect external systems, data or records. Its reviewed ATLAS relationships connect it to [agentic-ai](/concepts/agentic-ai.md) tool invocation (`AML.T0053`), exfiltration through tool invocation (`AML.T0086`) and data destruction through tool invocation (`AML.T0101`). The required approval boundary should be selected from the system's threat model and impact, with particular attention to sensitive, irreversible, privileged or externally visible actions.

## Governance Considerations

The system owner should define which actions require approval, who is authorised and competent to decide, what context and proposed tool arguments the reviewer receives, and how rejection, interruption and escalation work. Approval should be enforced by a control outside the model where possible; a prompt alone is not an adequate security boundary. Approval, denial, exception and intervention events should be recorded using the project's sanitised audit and monitoring controls.

This mitigation complements [human-oversight](/concepts/human-oversight.md) and [genai-guardrails](/concepts/genai-guardrails.md). Guardrails can validate tool requests and route them to the human gate; human oversight supplies the authority to make or stop the decision. The control should be tested for bypasses, excessive approval burden and automation bias, and reviewed when tools, permissions, objectives or threat techniques change.

## Limits

Human approval does not by itself establish that an action is lawful, safe or proportionate. It can also be ineffective when the reviewer lacks authority, context, time or a practical stop mechanism. Legal or regulatory conclusions require separate reviewed binding evidence.

## Source References

- SRC-0044, MITRE ATLAS v2026.08, sheet `mitigations`, cells A31:G31. Reviewed evidence for the AML.M0029 identity, name, URL, STIX identifier and lifecycle metadata. Source SHA-256: `7ea87e5b8ca5d4e67c261026abc331a977231d0d379c41a9f20c1eae2cb326e4`.
- SRC-0044, MITRE ATLAS v2026.08, sheet `techniques addressed`, rows 279-281. Reviewed evidence for the relationships to AML.T0053, AML.T0086 and AML.T0101. Unit content SHA-256: `89bcc4d4fe2305e1a36664bba417292f8ab116337b3ed9a8da7c78ffb1752f1b`.
- Evidence audit: `state/workshop/proposals/aml-m0029-lot-014/evidence/audit-src-0044.json`, verdict `AUDITED`; audit SHA-256: `9576c7f8908b28fa596d1565e1b00f37db8ed9c7a5e90208a22d5313de617b48`.
