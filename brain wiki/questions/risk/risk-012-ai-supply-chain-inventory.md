---
id: risk-012-ai-supply-chain-inventory
title: AI supply chain inventory and provenance
type: question
domains: [AI_SECURITY, THIRD_PARTIES_SUPPLY_CHAIN, RISK, PROCESS]
status: active
aliases:
  - AI dependency inventory question
  - Question sur l'inventaire de la chaîne IA
tags:
  - questionnaire
  - ai-supply-chain
  - provenance
evidence_sources: [AI_NICE_TO_KNOW]
topic: ai-supply-chain-inventory
priority: high
applies_to: AI
answer_type: boolean
depends_on:
  question_id: core-003-ai-system-determination
  equals: true
question_fr: "Le projet tient-il un inventaire à jour des modèles, données, logiciels, outils, connecteurs, fournisseurs et environnements dont dépend le système d'IA, avec leur provenance, leurs versions et les changements importants ?"
question_en: "Does the project maintain a current inventory of the models, data, software, tools, connectors, providers and environments on which the AI system depends, including provenance, versions and material changes?"
---

# AI supply chain inventory and provenance

## Purpose

Determine whether the project can identify material dependencies and trace their
origin, integrity and change history.

## Guidance

Answer “yes” only when the inventory covers the relevant runtime and development
dependencies and links material artifacts to provenance, version, integrity and
change evidence. Include external tools, managed services and delegated agents
where they cross the system boundary.

## Related knowledge

- [[ai-supply-chain-governance]]
- [[traceability]]
- [[ai-data-quality-and-validation]]

## Source references

- SRC-0024, pages 152 and 155-156.
- SRC-0025, pages 46-47 and 71-73.
- SRC-0034, pages 3 and 7.
