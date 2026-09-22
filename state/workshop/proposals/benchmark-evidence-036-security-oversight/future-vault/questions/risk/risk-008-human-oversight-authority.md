---
id: risk-008-human-oversight-authority
title: Human oversight authority
type: question
domains: [AI, RISK, LEGAL, PROCESS]
status: active
aliases:
  - Oversight authority
tags:
  - questionnaire
  - human-oversight
evidence_sources: [AI_NICE_TO_KNOW]
topic: human-oversight-authority
priority: high
applies_to: AI
answer_type: boolean
depends_on: null
question_fr: "Les personnes chargées de la supervision humaine disposent-elles de l’information, de la formation, du temps et de l’autorité nécessaires pour interpréter, contester, interrompre ou rejeter le résultat du système ?"
question_en: "Do the people responsible for human oversight have the information, training, time and authority needed to interpret, challenge, interrupt or reject the system output?"
---

# Human oversight authority

## Purpose

This question checks whether human oversight is operationally meaningful and whether the assigned people have defined roles, usable information and practical authority to intervene.

## Guidance

Answer "yes" only when the oversight process defines responsibilities, competence or training, access to relevant context and uncertainty, time to review, escalation routes and authority to challenge, defer, reject, interrupt or stop an output where the risk context requires it.

For agentic or high-impact workflows, verify whether human approval gates and output validation are placed before consequential actions or downstream propagation. NIST and OWASP support this as contextual governance and control guidance; they do not create a universal legal rule.

## Related Knowledge

- [[human-oversight]]
- [[genai-guardrails]]

## Source References

- SRC-0039, pages 32 and 45, for documented oversight processes, human roles and contextual human-AI configurations.
- SRC-0027, pages 11 and 33, for human approval, intent validation and gates before high-impact or high-risk propagation.
- SRC-0026, pages 10-12, for the security and privilege context in which human intervention may be relevant.
