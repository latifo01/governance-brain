---
id: mcp-and-agent-tool-governance
title: MCP and AI agent tool governance
type: knowledge
domains: [AI_SECURITY, THIRD_PARTIES_SUPPLY_CHAIN, RISK, PROCESS]
status: active
aliases:
  - MCP security governance
  - Gouvernance des outils MCP et des agents IA
tags:
  - mcp
  - agent-tools
  - tool-governance
  - supply-chain
  - secure-lifecycle
evidence_sources: [AI_NICE_TO_KNOW]
---

# MCP and AI agent tool governance

## Summary

MCP servers and other agent tools create a supply-chain and authorization
surface: metadata, schemas, resources and transitive calls can influence what an
agent sees or executes. Governance therefore needs an approved inventory,
traceable calls, constrained permissions and a controlled update lifecycle.

## Governance considerations

- Treat tool metadata and resources from unvetted servers as untrusted. Screen
  for spoofing, typosquatting, schema or resource poisoning and transitive-call
  expansion before a server is approved.
- Trace a request from the initiating user or agent through intermediate servers
  to the final tool and service. Record the identity, scope, token exchange and
  material input or output needed for investigation.
- Use least privilege, short-lived tokens, scope reduction, fine-grained
  authorization and explicit human checkpoints for high-impact or irreversible
  tool calls.
- Keep approved-server allow-lists, central inventories, pinned dependencies,
  signed artifacts, scanning and reproducible builds. Stage updates and retain
  rollback capability.
- Monitor tool calls and detect authority expansion or drift from the intended
  agent scope. Connect tool controls to [[genai-guardrails]] and
  [[ai-incident-response-resilience]].

## Limits

The MCP and ATLAS material describes threats and recommended controls. It does
not make MCP a regulated technology or establish a universal control baseline.
The appropriate controls depend on the server, tool, data and action boundary.

## Related concepts

- [[prompt-injection]] covers malicious instructions and content.
- [[ai-agent-authority-expansion-controls]] covers privileged actions.
- [[ai-agent-scope-drift-detection]] covers runtime divergence.
- [[traceability]] covers call and dependency lineage.
- [[red-teaming]] supports controlled adversarial testing.

## Source references

- SRC-0032, pages 11, 13 and 19, for MCP threats, traceability, authorization,
  signing, scanning, allow-lists and rollback.
- SRC-0025, pages 47, 71-73 and 116-117, for MCP/tool ecosystems, trust
  boundaries and tool-scope verification.
- SRC-0044, selected mitigation and relationship rows, for artifact and
  tool-registry scanning, tool-call logging and controlled testing.
- SRC-0046, AML.T0010.005, AML.T0011.002 and AML.M0036/M0038, for agent-tool
  risks, poisoned tools, authority expansion and scope drift.
