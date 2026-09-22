---
aliases:
- AI Agent Scope Drift Detection
brain_id: ai-agent-scope-drift-detection
brain_sha256: cbf653c0eb8550037e32e23719c49763502f3a0a8ebee58a4afb82aef4ea5580
domains:
- AI
- RISK
- PROCESS
evidence_sources:
- AI_NICE_TO_KNOW
id: ai-agent-scope-drift-detection
status: stable
tags:
- mitre-atlas
- ai-security
- agentic-ai
- runtime-monitoring
title: AI agent scope drift detection
type: knowledge
---


# AI agent scope drift detection

## Summary

AI agent scope drift detection continuously evaluates whether planned actions remain consistent with the authorized objective. Material deviation may indicate unintended behaviour, excessive autonomy or movement beyond the approved scope.

## Governance considerations

Monitor changes in objectives or task hierarchy, unrelated long-term goals, inconsistent tool use, access attempts outside scope, progressive authority expansion, persistence, privilege escalation and unrelated lateral movement. Detection responses can include pausing execution, restricting tools, requiring external approval, returning to an authorized plan or terminating the task.

Scope drift detection complements [ai-agent-authority-expansion-controls](/concepts/ai-agent-authority-expansion-controls.md), [human-in-the-loop-for-ai-agent-actions](/concepts/human-in-the-loop-for-ai-agent-actions.md), [ai-model-monitoring](/concepts/ai-model-monitoring.md) and [agentic-ai](/concepts/agentic-ai.md). ATLAS is security guidance and does not itself establish a legal obligation.

## Source references

- MITRE ATLAS `AML.M0038`, AI Agent Scope Drift Detection, https://atlas.mitre.org/mitigations/AML.M0038, source `SRC-0046`, locator `/objects`, unit SHA-256 `13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab`.
