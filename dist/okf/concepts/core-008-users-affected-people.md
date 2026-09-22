---
aliases:
- AI users and affected persons
answer_type: boolean
applies_to: AI
brain_id: core-008-users-affected-people
brain_sha256: 48eed1b01f2fe3b0713fed00185759fc9e34f586fd25a23b0e3799be8e16a8d8
depends_on:
  equals: 'yes'
  question_id: core-003-ai-system-determination
domains:
- AI
- RISK
- HUMAN_OVERSIGHT_RESPONSIBLE_AI
evidence_sources:
- AI_NICE_TO_KNOW
id: core-008-users-affected-people
priority: high
question_en: Does the project identify direct users, decision makers, operators, affected
  people and groups that may experience impacts without directly using the system?
question_fr: Le projet identifie-t-il les utilisateurs directs, les décideurs, les
  opérateurs, les personnes concernées et les groupes susceptibles de subir des effets
  sans utiliser directement le système ?
status: stable
tags:
- questionnaire
- common-core
- stakeholders
title: Users and affected people
topic: users-affected-people
type: question
---


# Users and affected people

## Purpose

Make human impact and stakeholder routes visible beyond the people operating
the interface.

## Guidance

Answer yes only when groups, roles, use context, expected benefits, potential
harms and available feedback or contestation channels are documented.

## Related knowledge

- [nist-ai-rmf](/concepts/nist-ai-rmf.md)
- [human-oversight](/concepts/human-oversight.md)

## Source references

- SRC-0039, pages 11 and 13-15, for people who may be harmed without being direct users and potentially impacted groups.
- SRC-0039, pages 31, 34 and 42, for intended users, affected communities and end-user roles.
