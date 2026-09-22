---
id: core-008-users-affected-people
title: Users and affected people
type: question
domains: [AI, RISK, HUMAN_OVERSIGHT_RESPONSIBLE_AI]
status: active
aliases: [AI users and affected persons]
tags: [questionnaire, common-core, stakeholders]
evidence_sources: [AI_NICE_TO_KNOW]
topic: users-affected-people
priority: high
applies_to: AI
answer_type: boolean
depends_on:
  question_id: core-003-ai-system-determination
  equals: "yes"
question_fr: "Le projet identifie-t-il les utilisateurs directs, les décideurs, les opérateurs, les personnes concernées et les groupes susceptibles de subir des effets sans utiliser directement le système ?"
question_en: "Does the project identify direct users, decision makers, operators, affected people and groups that may experience impacts without directly using the system?"
---

# Users and affected people

## Purpose

Make human impact and stakeholder routes visible beyond the people operating
the interface.

## Guidance

Answer yes only when groups, roles, use context, expected benefits, potential
harms and available feedback or contestation channels are documented.

## Related knowledge

- [[nist-ai-rmf]]
- [[human-oversight]]

## Source references

- SRC-0039, pages 11 and 13-15, for people who may be harmed without being direct users and potentially impacted groups.
- SRC-0039, pages 31, 34 and 42, for intended users, affected communities and end-user roles.
