---
id: ai-agent-identity-and-access-control
title: AI agent identity and access control
type: knowledge
domains: [AI_SECURITY, THIRD_PARTIES_SUPPLY_CHAIN, RISK]
status: active
aliases:
  - Agentic IAM
  - Identité et contrôle d'accès des agents IA
tags:
  - agent-identity
  - iam
  - least-privilege
  - delegated-access
  - authorization
evidence_sources: [AI_NICE_TO_KNOW]
---

# AI agent identity and access control

## Summary

Agent identity and access control make an agent's identity, delegated authority,
scope and lifetime explicit at each interaction with a model, tool, service or
tenant. The evidence supports treating agents as governed principals and using
short-lived, least-privilege authorization.

## Governance considerations

- Distinguish the agent's own rights from rights exercised on behalf of a user
  or service, and avoid standing privilege where a time-bound grant is possible.
- Authenticate and authorize each hop across agents, servers, APIs and tools;
  bind higher-assurance identities to signed code or model manifests when the
  deployment requires that assurance.
- Use conservative defaults for unknown or third-party agents, such as
  read-only or restricted scopes, and verify claims, signer identity, lifetime
  and deployment policy before activation.
- Apply tenant isolation and explicit scope- and lifetime-bounded authorization
  to cross-tenant or cross-organisation delegation. Keep immutable, tenant-aware
  lineage logs for authorization decisions and tool calls.
- Revalidate authorization when an agent expands authority, changes tools or
  crosses a trust boundary; connect this review to [[human-in-the-loop-for-ai-agent-actions]].

## Limits

The reviewed papers are security guidance and proposals. They do not define a
universal identity standard, legal duty or required authentication protocol.
Implementation must account for the actual architecture, provider contracts and
applicable law.

## Related concepts

- [[ai-agent-authority-expansion-controls]] covers authority changes.
- [[ai-agent-scope-drift-detection]] covers divergence from intended scope.
- [[human-in-the-loop-for-ai-agent-actions]] covers human approval for risky actions.
- [[traceability]] covers identity and authorization lineage evidence.
- [[data-leakage]] covers disclosure risk from excessive access.

## Source references

- SRC-0025, pages 66 and 116-117, for delegated access, tool-scope verification
  and federated identity controls.
- SRC-0030, pages 3, 17 and 33, for action boundaries, external-agent risk,
  least privilege, testing and monitoring.
- SRC-0031, pages 4, 6 and 16, for first-class agent identities, time-bound
  credentials, signed authorization and tenant isolation.
- SRC-0032, pages 11 and 13, for MCP identity, token exchange and fine-grained
  authorization.
- SRC-0033, page 7, for endpoint authentication, data-sensitive authorization
  and privilege tiers.
