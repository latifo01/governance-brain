---
aliases:
- AI Agent Authority Expansion Controls
brain_id: ai-agent-authority-expansion-controls
brain_sha256: 4c1cb7b8d7a0a36d0b380511b38ec9bb5afdb8f3246e75fa85e78a87cb5cc93d
domains:
- AI
- RISK
- PROCESS
evidence_sources:
- AI_NICE_TO_KNOW
id: ai-agent-authority-expansion-controls
status: stable
tags:
- mitre-atlas
- ai-security
- agentic-ai
- authorization
title: AI agent authority expansion controls
type: knowledge
---


# AI agent authority expansion controls

## Summary

AI agent authority expansion controls constrain an agent from autonomously acquiring additional permissions, identities, services, targets or resources during execution. The maximum authority should be granted before runtime and enforced outside the agent, rather than relying only on prompts or model behaviour.

## Governance considerations

Use policy engines, target allowlists, protocol and destination restrictions, approval gates, and credentials explicitly approved for the task. Bound the number, scope, duration and concurrent use of tokens. Record discoveries, denials, exceptions, approvals and scope changes. Propagate the parent constraints to sub-agents; delegation may narrow authority but must not expand it.

This control complements [human-in-the-loop-for-ai-agent-actions](/concepts/human-in-the-loop-for-ai-agent-actions.md), [genai-guardrails](/concepts/genai-guardrails.md), [agentic-ai](/concepts/agentic-ai.md) and [traceability](/concepts/traceability.md). ATLAS is security guidance and does not itself establish a legal obligation.

## Source references

- MITRE ATLAS `AML.M0037`, AI Agent Authority Expansion Controls, https://atlas.mitre.org/mitigations/AML.M0037, source `SRC-0046`, locator `/objects`, unit SHA-256 `13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab`.
