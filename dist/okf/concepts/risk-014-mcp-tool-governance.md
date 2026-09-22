---
aliases:
- MCP tool security question
- Question sur la gouvernance des outils MCP
answer_type: boolean
applies_to: AI
brain_id: risk-014-mcp-tool-governance
brain_sha256: e80e104c010fdcabab7ce52e99e6a349b82fc3dd9bff8e73d72f6f3398b24278
depends_on:
  equals: true
  question_id: core-007-agentic-capability
domains:
- AI_SECURITY
- THIRD_PARTIES_SUPPLY_CHAIN
- RISK
- PROCESS
evidence_sources:
- AI_NICE_TO_KNOW
id: risk-014-mcp-tool-governance
priority: high
question_en: Are MCP servers and other agent tools inventoried, approved, constrained
  by least-privilege authorization, monitored and subject to a controlled update and
  rollback process?
question_fr: Les serveurs MCP et autres outils d'agent sont-ils inventoriés, approuvés,
  limités par des autorisations minimales, surveillés et soumis à une procédure contrôlée
  de mise à jour et de retour arrière ?
sources:
- authority: FRAMEWORK
  brain_source_id: SRC-0044
  evidence_ref: security-031-src-0044-ec-002
  id: brain-03a3d9259e5cdd50
  locator: Sheet mitigations, cells A1:H40
  resource: /references/src-0044-7ea87e5b8ca5d4e67c261026abc331a977231d0d379c41a9f20c1eae2cb326e4.md
  unit_file_sha256: 54ceaa9042f8801898d089f3c5eeeb462eb546c928445d3c9b33c8cb42facbed
  unit_path: ingest/SRC-0044/units/sheet-001-mitigations-001.md
  unit_sha256: 40c394482b3ed721d1dcac04c388ba937504849e80a17b9e30af8a6060fa8527
- authority: FRAMEWORK
  brain_source_id: SRC-0046
  evidence_ref: security-031-src-0046-ec-001
  id: brain-09ab16ed48b0c781
  locator: /objects
  resource: /references/src-0046-6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c.md
  unit_file_sha256: 7b18ef3f2ed64ab84d1204bca642c073f03b8264b4a2fe3bb2f19ab84cbd5241
  unit_path: ingest/SRC-0046/units/key-0003.md
  unit_sha256: 13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab
- authority: FRAMEWORK
  brain_source_id: SRC-0046
  evidence_ref: security-031-src-0046-ec-003
  id: brain-231a550ac94eea16
  locator: /objects
  resource: /references/src-0046-6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c.md
  unit_file_sha256: 7b18ef3f2ed64ab84d1204bca642c073f03b8264b4a2fe3bb2f19ab84cbd5241
  unit_path: ingest/SRC-0046/units/key-0003.md
  unit_sha256: 13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab
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
  brain_source_id: SRC-0044
  evidence_ref: security-031-src-0044-ec-003
  id: brain-4bd407aa458296eb
  locator: Sheet techniques addressed, cells A1:M250
  resource: /references/src-0044-7ea87e5b8ca5d4e67c261026abc331a977231d0d379c41a9f20c1eae2cb326e4.md
  unit_file_sha256: 639dadd05961717046e4d91cf430e86786bb7abbfebc1a2fe0971b54521d7d4e
  unit_path: ingest/SRC-0044/units/sheet-002-techniques addressed-001.md
  unit_sha256: 677e44e260f629f6fbde9d115e590c98dffa5cb0c62021ff2ae0fc8bb8517eed
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
  brain_source_id: SRC-0046
  evidence_ref: security-031-src-0046-ec-002
  id: brain-8ea9ed342c0805c7
  locator: /objects
  resource: /references/src-0046-6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c.md
  unit_file_sha256: 7b18ef3f2ed64ab84d1204bca642c073f03b8264b4a2fe3bb2f19ab84cbd5241
  unit_path: ingest/SRC-0046/units/key-0003.md
  unit_sha256: 13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab
- authority: FRAMEWORK
  brain_source_id: SRC-0044
  evidence_ref: security-031-src-0044-ec-001
  id: brain-c183e28fb6eb2197
  locator: Sheet mitigations, cells A1:H40
  resource: /references/src-0044-7ea87e5b8ca5d4e67c261026abc331a977231d0d379c41a9f20c1eae2cb326e4.md
  unit_file_sha256: 54ceaa9042f8801898d089f3c5eeeb462eb546c928445d3c9b33c8cb42facbed
  unit_path: ingest/SRC-0044/units/sheet-001-mitigations-001.md
  unit_sha256: 40c394482b3ed721d1dcac04c388ba937504849e80a17b9e30af8a6060fa8527
- authority: FRAMEWORK
  brain_source_id: SRC-0044
  evidence_ref: security-031-src-0044-ec-004
  id: brain-e8ffc6941499bff5
  locator: Sheet techniques addressed, cells A251:M347
  resource: /references/src-0044-7ea87e5b8ca5d4e67c261026abc331a977231d0d379c41a9f20c1eae2cb326e4.md
  unit_file_sha256: 55f5d77efd51b35bc13ee0f62530cff19de35075e3a79eb324cb69bc16e4d837
  unit_path: ingest/SRC-0044/units/sheet-002-techniques addressed-002.md
  unit_sha256: 89bcc4d4fe2305e1a36664bba417292f8ab116337b3ed9a8da7c78ffb1752f1b
status: stable
tags:
- questionnaire
- mcp
- agent-tools
- supply-chain
title: MCP and agent tool governance
topic: mcp-tool-governance
type: question
---


# MCP and agent tool governance

## Purpose

Determine whether tool metadata, dependencies, calls and updates are governed as
part of the AI supply chain and authorization boundary.

Section evidence: [^brain-03a3d9259e5cdd50] [^brain-09ab16ed48b0c781] [^brain-231a550ac94eea16] [^brain-3f6e6fe90a515241] [^brain-40c0ed090ff47dd1] [^brain-4bd407aa458296eb] [^brain-7b885e802605e4d6] [^brain-8ea9ed342c0805c7] [^brain-c183e28fb6eb2197] [^brain-e8ffc6941499bff5]

## Guidance

Answer “yes” only when the project screens untrusted servers and schemas,
traces calls, uses approved sources and constrained tokens, scans or verifies
dependencies, stages changes and can roll back to a trusted configuration.

Section evidence: [^brain-03a3d9259e5cdd50] [^brain-09ab16ed48b0c781] [^brain-231a550ac94eea16] [^brain-3f6e6fe90a515241] [^brain-40c0ed090ff47dd1] [^brain-4bd407aa458296eb] [^brain-7b885e802605e4d6] [^brain-8ea9ed342c0805c7] [^brain-c183e28fb6eb2197] [^brain-e8ffc6941499bff5]

## Related knowledge

- [mcp-and-agent-tool-governance](/concepts/mcp-and-agent-tool-governance.md)
- [ai-agent-authority-expansion-controls](/concepts/ai-agent-authority-expansion-controls.md)
- [prompt-injection](/concepts/prompt-injection.md)
- [traceability](/concepts/traceability.md)

## Source references

- SRC-0032, pages 11, 13 and 19.
- SRC-0044, selected mitigation and relationship rows.
- SRC-0046, AML.T0010.005, AML.T0011.002 and AML.M0036/M0038.


[^brain-03a3d9259e5cdd50]: [SRC-0044](/references/src-0044-7ea87e5b8ca5d4e67c261026abc331a977231d0d379c41a9f20c1eae2cb326e4.md); locator: Sheet mitigations, cells A1:H40.
[^brain-09ab16ed48b0c781]: [SRC-0046](/references/src-0046-6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c.md); locator: /objects.
[^brain-231a550ac94eea16]: [SRC-0046](/references/src-0046-6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c.md); locator: /objects.
[^brain-3f6e6fe90a515241]: [SRC-0032](/references/src-0032-410815680200580613cdd603f553f663b580dd27eb05714d17e38fdbebe05b5e.md); locator: Page 19.
[^brain-40c0ed090ff47dd1]: [SRC-0032](/references/src-0032-410815680200580613cdd603f553f663b580dd27eb05714d17e38fdbebe05b5e.md); locator: Page 13.
[^brain-4bd407aa458296eb]: [SRC-0044](/references/src-0044-7ea87e5b8ca5d4e67c261026abc331a977231d0d379c41a9f20c1eae2cb326e4.md); locator: Sheet techniques addressed, cells A1:M250.
[^brain-7b885e802605e4d6]: [SRC-0032](/references/src-0032-410815680200580613cdd603f553f663b580dd27eb05714d17e38fdbebe05b5e.md); locator: Page 11.
[^brain-8ea9ed342c0805c7]: [SRC-0046](/references/src-0046-6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c.md); locator: /objects.
[^brain-c183e28fb6eb2197]: [SRC-0044](/references/src-0044-7ea87e5b8ca5d4e67c261026abc331a977231d0d379c41a9f20c1eae2cb326e4.md); locator: Sheet mitigations, cells A1:H40.
[^brain-e8ffc6941499bff5]: [SRC-0044](/references/src-0044-7ea87e5b8ca5d4e67c261026abc331a977231d0d379c41a9f20c1eae2cb326e4.md); locator: Sheet techniques addressed, cells A251:M347.
