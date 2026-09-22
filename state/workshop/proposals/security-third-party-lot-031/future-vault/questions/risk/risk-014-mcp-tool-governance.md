---
id: risk-014-mcp-tool-governance
title: MCP and agent tool governance
type: question
domains: [AI_SECURITY, THIRD_PARTIES_SUPPLY_CHAIN, RISK, PROCESS]
status: active
aliases:
  - MCP tool security question
  - Question sur la gouvernance des outils MCP
tags:
  - questionnaire
  - mcp
  - agent-tools
  - supply-chain
evidence_sources: [AI_NICE_TO_KNOW]
topic: mcp-tool-governance
priority: high
applies_to: AI
answer_type: boolean
depends_on:
  question_id: core-007-agentic-capability
  equals: true
question_fr: "Les serveurs MCP et autres outils d'agent sont-ils inventoriés, approuvés, limités par des autorisations minimales, surveillés et soumis à une procédure contrôlée de mise à jour et de retour arrière ?"
question_en: "Are MCP servers and other agent tools inventoried, approved, constrained by least-privilege authorization, monitored and subject to a controlled update and rollback process?"
---

# MCP and agent tool governance

## Purpose

Determine whether tool metadata, dependencies, calls and updates are governed as
part of the AI supply chain and authorization boundary.

## Guidance

Answer “yes” only when the project screens untrusted servers and schemas,
traces calls, uses approved sources and constrained tokens, scans or verifies
dependencies, stages changes and can roll back to a trusted configuration.

## Related knowledge

- [[mcp-and-agent-tool-governance]]
- [[ai-agent-authority-expansion-controls]]
- [[prompt-injection]]
- [[traceability]]

## Source references

- SRC-0032, pages 11, 13 and 19.
- SRC-0044, selected mitigation and relationship rows.
- SRC-0046, AML.T0010.005, AML.T0011.002 and AML.M0036/M0038.
