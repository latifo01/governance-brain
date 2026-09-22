---
aliases:
- Agentic IAM question
- Question sur l'identité et l'accès délégué des agents
answer_type: boolean
applies_to: AI
brain_id: risk-013-agent-identity-and-access
brain_sha256: 7748e45d83f3e707105c040ad6d04ae8ab2b91ed6c830b54b5d180a25fb90608
depends_on:
  equals: true
  question_id: core-007-agentic-capability
domains:
- AI_SECURITY
- THIRD_PARTIES_SUPPLY_CHAIN
- RISK
evidence_sources:
- AI_NICE_TO_KNOW
id: risk-013-agent-identity-and-access
priority: high
question_en: Do the system's agents have explicit, time-bounded identities and authorizations
  that are verified at each hop, including when they act on a user's behalf or call
  a third-party provider?
question_fr: Les agents du système ont-ils une identité et des autorisations explicites,
  limitées dans le temps et vérifiées à chaque étape, y compris lorsqu'ils agissent
  pour le compte d'un utilisateur ou appellent un fournisseur tiers ?
sources:
- authority: FRAMEWORK
  brain_source_id: SRC-0033
  evidence_ref: security-031-src-0033-ec-001
  id: brain-1a85977f3dd97d2b
  locator: Page 5
  resource: /references/src-0033-c487d3f02c3d4f1e520747a500fd4dba4be0886ea6cca3382b2f3ee065ac80fc.md
  unit_file_sha256: 12523ff8dc7147e47dd2ebe159f63a94c1b867c3a4df128b49ebf00a7d5d2c36
  unit_path: ingest/SRC-0033/units/p0005.md
  unit_sha256: 264accb6207c5c51d86bdfd9773bd54116e4e092031efa98e507df5a4766a642
- authority: FRAMEWORK
  brain_source_id: SRC-0032
  evidence_ref: security-031-src-0032-ec-003
  id: brain-3f6e6fe90a515241
  locator: Page 19
  resource: /references/src-0032-410815680200580613cdd603f553f663b580dd27eb05714d17e38fdbebe05b5e.md
  unit_file_sha256: 87ef192bada3df5527d7a91bc866f013f7f54e4208d5942e5c56772d819e66ff
  unit_path: ingest/SRC-0032/units/p0019.md
  unit_sha256: 1480b65d0ee695fbf009384358fcf4b1ba723042766db018f200c9164c3f82e9
- authority: FRAMEWORK
  brain_source_id: SRC-0032
  evidence_ref: security-031-src-0032-ec-002
  id: brain-40c0ed090ff47dd1
  locator: Page 13
  resource: /references/src-0032-410815680200580613cdd603f553f663b580dd27eb05714d17e38fdbebe05b5e.md
  unit_file_sha256: 23601f1baad383adb2d42ef637fa084021ecfefe50f69600358b352249b104db
  unit_path: ingest/SRC-0032/units/p0013.md
  unit_sha256: eb63df3a1cb8b614bae952c72128f04a4630a2efc35c28344a4983226adc5b10
- authority: FRAMEWORK
  brain_source_id: SRC-0031
  evidence_ref: security-031-src-0031-ec-001
  id: brain-70c2f3204cd8597c
  locator: Page 4
  resource: /references/src-0031-9f7f5988eb6db46576732f579dd81ac75e4e05bdf7a06eb4cebd32eedf4be872.md
  unit_file_sha256: af9ce17eed46704973785b46c1ea60008afb043e4edcab6c06dba21f9308dd94
  unit_path: ingest/SRC-0031/units/p0004.md
  unit_sha256: 3179620b5ae18482cf2b744653dc940b9ef6ae5b1b0a0c480fce413b93a11529
- authority: FRAMEWORK
  brain_source_id: SRC-0032
  evidence_ref: security-031-src-0032-ec-001
  id: brain-7b885e802605e4d6
  locator: Page 11
  resource: /references/src-0032-410815680200580613cdd603f553f663b580dd27eb05714d17e38fdbebe05b5e.md
  unit_file_sha256: 3aefead1972826398eb09cad2caa26cf2ec85d5c84488b8d7f4fadacf0179fed
  unit_path: ingest/SRC-0032/units/p0011.md
  unit_sha256: be3c57ea2b29cc2b5f7e6e2fb3638a5dcb578af6f354aca49465fea9a79b6be1
- authority: FRAMEWORK
  brain_source_id: SRC-0031
  evidence_ref: security-031-src-0031-ec-002
  id: brain-9893a413084e5d1f
  locator: Page 6
  resource: /references/src-0031-9f7f5988eb6db46576732f579dd81ac75e4e05bdf7a06eb4cebd32eedf4be872.md
  unit_file_sha256: bd032eeac1f4333f0f8052ac0550a073f4d8ec2901cff1d2192b4c24adbc37b6
  unit_path: ingest/SRC-0031/units/p0006.md
  unit_sha256: ee2bf1bda188f4e0b0f4ec497c115fe7c1752b50f6a1c528003e8514634f4634
- authority: FRAMEWORK
  brain_source_id: SRC-0031
  evidence_ref: security-031-src-0031-ec-003
  id: brain-ab35074e14356a26
  locator: Page 16
  resource: /references/src-0031-9f7f5988eb6db46576732f579dd81ac75e4e05bdf7a06eb4cebd32eedf4be872.md
  unit_file_sha256: 8ffe82bf362eea49a0c2579159fab6ea6a72af10a619d1f3ecefc3bf94dd3449
  unit_path: ingest/SRC-0031/units/p0016.md
  unit_sha256: 825469e1da1de7f3130a25e07f9c92c77aa103102b7f4027593022e6926211aa
- authority: FRAMEWORK
  brain_source_id: SRC-0033
  evidence_ref: security-031-src-0033-ec-002
  id: brain-dbcf0980f708fcb2
  locator: Page 7
  resource: /references/src-0033-c487d3f02c3d4f1e520747a500fd4dba4be0886ea6cca3382b2f3ee065ac80fc.md
  unit_file_sha256: d98b349d67aedde3b7a3584ca821cb2f3fc1b6bdf6208da51f25f97829204feb
  unit_path: ingest/SRC-0033/units/p0007.md
  unit_sha256: 5d7ab7cf68795642e8d03263071dc2f77c3b8c97c8dc730243f5455cdf7fda38
status: stable
tags:
- questionnaire
- agent-identity
- access-control
- delegated-access
title: Agent identity and delegated access
topic: agent-identity-and-access
type: question
---


# Agent identity and delegated access

## Purpose

Determine whether agent actions can be attributed, constrained and revoked
across tools, providers, tenants and delegated workflows.

Section evidence: [^brain-1a85977f3dd97d2b] [^brain-3f6e6fe90a515241] [^brain-40c0ed090ff47dd1] [^brain-70c2f3204cd8597c] [^brain-7b885e802605e4d6] [^brain-9893a413084e5d1f] [^brain-ab35074e14356a26] [^brain-dbcf0980f708fcb2]

## Guidance

Answer “yes” only when the project distinguishes agent and on-behalf-of rights,
avoids unnecessary standing privilege, applies least privilege and records the
identity, scope, lifetime and decision path for material authorization events.

Section evidence: [^brain-1a85977f3dd97d2b] [^brain-3f6e6fe90a515241] [^brain-40c0ed090ff47dd1] [^brain-70c2f3204cd8597c] [^brain-7b885e802605e4d6] [^brain-9893a413084e5d1f] [^brain-ab35074e14356a26] [^brain-dbcf0980f708fcb2]

## Related knowledge

- [ai-agent-identity-and-access-control](/concepts/ai-agent-identity-and-access-control.md)
- [ai-agent-authority-expansion-controls](/concepts/ai-agent-authority-expansion-controls.md)
- [traceability](/concepts/traceability.md)

## Source references

- SRC-0031, pages 4, 6 and 16.
- SRC-0032, pages 11 and 13.
- SRC-0033, page 7.


[^brain-1a85977f3dd97d2b]: [SRC-0033](/references/src-0033-c487d3f02c3d4f1e520747a500fd4dba4be0886ea6cca3382b2f3ee065ac80fc.md); locator: Page 5.
[^brain-3f6e6fe90a515241]: [SRC-0032](/references/src-0032-410815680200580613cdd603f553f663b580dd27eb05714d17e38fdbebe05b5e.md); locator: Page 19.
[^brain-40c0ed090ff47dd1]: [SRC-0032](/references/src-0032-410815680200580613cdd603f553f663b580dd27eb05714d17e38fdbebe05b5e.md); locator: Page 13.
[^brain-70c2f3204cd8597c]: [SRC-0031](/references/src-0031-9f7f5988eb6db46576732f579dd81ac75e4e05bdf7a06eb4cebd32eedf4be872.md); locator: Page 4.
[^brain-7b885e802605e4d6]: [SRC-0032](/references/src-0032-410815680200580613cdd603f553f663b580dd27eb05714d17e38fdbebe05b5e.md); locator: Page 11.
[^brain-9893a413084e5d1f]: [SRC-0031](/references/src-0031-9f7f5988eb6db46576732f579dd81ac75e4e05bdf7a06eb4cebd32eedf4be872.md); locator: Page 6.
[^brain-ab35074e14356a26]: [SRC-0031](/references/src-0031-9f7f5988eb6db46576732f579dd81ac75e4e05bdf7a06eb4cebd32eedf4be872.md); locator: Page 16.
[^brain-dbcf0980f708fcb2]: [SRC-0033](/references/src-0033-c487d3f02c3d4f1e520747a500fd4dba4be0886ea6cca3382b2f3ee065ac80fc.md); locator: Page 7.
