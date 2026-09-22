---
id: risk-013-agent-identity-and-access
title: Agent identity and delegated access
type: question
domains: [AI_SECURITY, THIRD_PARTIES_SUPPLY_CHAIN, RISK]
status: active
aliases:
  - Agentic IAM question
  - Question sur l'identité et l'accès délégué des agents
tags:
  - questionnaire
  - agent-identity
  - access-control
  - delegated-access
evidence_sources: [AI_NICE_TO_KNOW]
topic: agent-identity-and-access
priority: high
applies_to: AI
answer_type: boolean
depends_on:
  question_id: core-007-agentic-capability
  equals: true
question_fr: "Les agents du système ont-ils une identité et des autorisations explicites, limitées dans le temps et vérifiées à chaque étape, y compris lorsqu'ils agissent pour le compte d'un utilisateur ou appellent un fournisseur tiers ?"
question_en: "Do the system's agents have explicit, time-bounded identities and authorizations that are verified at each hop, including when they act on a user's behalf or call a third-party provider?"
---

# Agent identity and delegated access

## Purpose

Determine whether agent actions can be attributed, constrained and revoked
across tools, providers, tenants and delegated workflows.

## Guidance

Answer “yes” only when the project distinguishes agent and on-behalf-of rights,
avoids unnecessary standing privilege, applies least privilege and records the
identity, scope, lifetime and decision path for material authorization events.

## Related knowledge

- [[ai-agent-identity-and-access-control]]
- [[ai-agent-authority-expansion-controls]]
- [[traceability]]

## Source references

- SRC-0031, pages 4, 6 and 16.
- SRC-0032, pages 11 and 13.
- SRC-0033, page 7.
