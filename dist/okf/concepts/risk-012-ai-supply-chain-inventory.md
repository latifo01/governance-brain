---
aliases:
- AI dependency inventory question
- Question sur l'inventaire de la chaîne IA
answer_type: boolean
applies_to: AI
brain_id: risk-012-ai-supply-chain-inventory
brain_sha256: b6f16b6d4026784e7a0b42d1ccdffb16255037a3b8369da3943d7af435d6f554
depends_on:
  equals: true
  question_id: core-003-ai-system-determination
domains:
- AI_SECURITY
- THIRD_PARTIES_SUPPLY_CHAIN
- RISK
- PROCESS
evidence_sources:
- AI_NICE_TO_KNOW
id: risk-012-ai-supply-chain-inventory
priority: high
question_en: Does the project maintain a current inventory of the models, data, software,
  tools, connectors, providers and environments on which the AI system depends, including
  provenance, versions and material changes?
question_fr: Le projet tient-il un inventaire à jour des modèles, données, logiciels,
  outils, connecteurs, fournisseurs et environnements dont dépend le système d'IA,
  avec leur provenance, leurs versions et les changements importants ?
sources:
- authority: FRAMEWORK
  brain_source_id: SRC-0025
  evidence_ref: security-031-src-0025-ec-016
  id: brain-028c9a0407876c7e
  locator: Page 87
  resource: /references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md
  unit_file_sha256: 7414422fd05f495c0069b377b310ff2fb6dafc0ebdbb173b02cf74008ddb1554
  unit_path: ingest/SRC-0025/units/p0087.md
  unit_sha256: cb43734514afbff9455bd869becb5c5d2154c9cd885c1962fa85b52b397b062b
- authority: FRAMEWORK
  brain_source_id: SRC-0025
  evidence_ref: security-031-src-0025-ec-017
  id: brain-3bfeb3db3d4ea22c
  locator: Page 117
  resource: /references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md
  unit_file_sha256: bdeb34433d236944bc027f6fb86bc68f624a892044d5843a870aa1d65f16e7ca
  unit_path: ingest/SRC-0025/units/p0117.md
  unit_sha256: 5d53dfe2b0ca64d5fff08b986cc6cbc55fa3ec663844cc74d05ff05ab679b1f6
- authority: FRAMEWORK
  brain_source_id: SRC-0025
  evidence_ref: security-031-src-0025-ec-004
  id: brain-3deb003b8688c617
  locator: Page 66
  resource: /references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md
  unit_file_sha256: 869ac32d4f39e3546b1a432e7ada00f1e14157850cecdb45520289f93f9fba51
  unit_path: ingest/SRC-0025/units/p0066.md
  unit_sha256: c7cea4caae0c2d991e6bd53552f3b1b68906712c3232e3d672104f535324c0e0
- authority: FRAMEWORK
  brain_source_id: SRC-0025
  evidence_ref: security-031-src-0025-ec-010
  id: brain-4060e4b2d21457e7
  locator: Page 107
  resource: /references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md
  unit_file_sha256: d580f66d96e365c03f6b742c1b694dd992f74f7c4c101035ac1f3f175badda79
  unit_path: ingest/SRC-0025/units/p0107.md
  unit_sha256: ae73ab989a3be2e0869e511781613b2630ddf50d968546417c3e59bd739c676c
- authority: FRAMEWORK
  brain_source_id: SRC-0025
  evidence_ref: security-031-src-0025-ec-006
  id: brain-4393033b94b0d965
  locator: Page 72
  resource: /references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md
  unit_file_sha256: 6f9c62cd2ab4945cd8a4e2fd07e595ffa6b75ed36d59e569687ef8b0c5b5f120
  unit_path: ingest/SRC-0025/units/p0072.md
  unit_sha256: 4caa08e9fcd3ac0274c1ae7900c977f653a8e622e0522f5c5e3285d716cd369b
- authority: FRAMEWORK
  brain_source_id: SRC-0025
  evidence_ref: security-031-src-0025-ec-008
  id: brain-4a55cc262bde6efb
  locator: Page 86
  resource: /references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md
  unit_file_sha256: 4c5ade60ed2e171dc7206c059489498aea37d25302db629b7feabc53d17e012d
  unit_path: ingest/SRC-0025/units/p0086.md
  unit_sha256: f679a7f605a1640485504c54825445a2952ae1b3c939b5da2920268222891ed1
- authority: FRAMEWORK
  brain_source_id: SRC-0024
  evidence_ref: security-031-src-0024-ec-003
  id: brain-4e4c39d9afb076e7
  locator: Page 22
  resource: /references/src-0024-130442e9d4999ebe7d79c4d415299a345953dabb08c54511a87b91f90492b285.md
  unit_file_sha256: cde8c42cf2c1fdc4b4041f8a8d27eb5b95d5d5424c6d2fcbfadb0dcb17d92ded
  unit_path: ingest/SRC-0024/units/p0022.md
  unit_sha256: ca310bec76188cbfb31d57b0c8de8d932686f7d2ff8de8e3e89c426bf8c16be1
- authority: FRAMEWORK
  brain_source_id: SRC-0024
  evidence_ref: security-031-src-0024-ec-007
  id: brain-631eb97bbfe47359
  locator: Page 156
  resource: /references/src-0024-130442e9d4999ebe7d79c4d415299a345953dabb08c54511a87b91f90492b285.md
  unit_file_sha256: 0b12b7ad6f7e3756914442e6160c24f9dbfcf69f87f8a74a05e4db15b83613b2
  unit_path: ingest/SRC-0024/units/p0156.md
  unit_sha256: 6136efad3fd3a65c3e49e8dfdf36d0d7384552563c5ea4fc4a943acf9fc6127f
- authority: FRAMEWORK
  brain_source_id: SRC-0024
  evidence_ref: security-031-src-0024-ec-004
  id: brain-679d195dc287b0bc
  locator: Page 152
  resource: /references/src-0024-130442e9d4999ebe7d79c4d415299a345953dabb08c54511a87b91f90492b285.md
  unit_file_sha256: 8e4f485b967ac624cad5b35c085f286f88fe16569f885151744b1f9924ae7001
  unit_path: ingest/SRC-0024/units/p0152.md
  unit_sha256: 0d216ba1160dddec41edaaa2edf4f5500d0fc2d4f6254d42eeb0195479afe2f0
- authority: FRAMEWORK
  brain_source_id: SRC-0025
  evidence_ref: security-031-src-0025-ec-014
  id: brain-74cc147aa9a476eb
  locator: Page 73
  resource: /references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md
  unit_file_sha256: 5f336e2e2da060f4dd7ee55f1702d9e810dd6328a6256dfb5aa8860a0f020788
  unit_path: ingest/SRC-0025/units/p0073.md
  unit_sha256: 5f1c48774a24dd30ac6d1156eb77ed98b30cc7a5e7ef0b627f255299581092f8
- authority: FRAMEWORK
  brain_source_id: SRC-0025
  evidence_ref: security-031-src-0025-ec-005
  id: brain-7bc39c4ef21d01eb
  locator: Page 71
  resource: /references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md
  unit_file_sha256: b9c6932c9e7a94347d6d31351f72acfdd3f8e977578430270439c67a4eb26222
  unit_path: ingest/SRC-0025/units/p0071.md
  unit_sha256: f1ff644c973e619e1ec232fdab9f9146928896117d936dff51f4d5b2d3af8d9c
- authority: FRAMEWORK
  brain_source_id: SRC-0034
  evidence_ref: security-031-src-0034-ec-001
  id: brain-83da1770f64cc5f8
  locator: Page 3
  resource: /references/src-0034-b4133f21b4fb1b6ab9bd39962c2aad1b6f3193dfe84a23fcf9a2edb914a11176.md
  unit_file_sha256: afc691dd8675e82208ccb5339e92b4495caf66d055d6b572d08433bc82210eb2
  unit_path: ingest/SRC-0034/units/p0003.md
  unit_sha256: 815c3458e0564aa5d4bba80cbed4ce302fe94e2e7ce90866909ba79385439a35
- authority: FRAMEWORK
  brain_source_id: SRC-0025
  evidence_ref: security-031-src-0025-ec-012
  id: brain-8e49791405ad019e
  locator: Page 116
  resource: /references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md
  unit_file_sha256: dfcaf759598c6841b0d114b7703f808a7562b8622849cad19c09ee21348badb9
  unit_path: ingest/SRC-0025/units/p0116.md
  unit_sha256: ce65ffa4958ce4319fe6c65ebba3184283e802dc7e74342e87b3db38afbd1c4a
- authority: FRAMEWORK
  brain_source_id: SRC-0025
  evidence_ref: security-031-src-0025-ec-011
  id: brain-965344936e9d924f
  locator: Page 112
  resource: /references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md
  unit_file_sha256: 0203798eea42eb1d46666e869f6b4907af317830266a7c41a9a954a689f25f21
  unit_path: ingest/SRC-0025/units/p0112.md
  unit_sha256: 043a31172830180535b11f37407a0dce35834db276846955c847091b0fb0f9b0
- authority: FRAMEWORK
  brain_source_id: SRC-0025
  evidence_ref: security-031-src-0025-ec-003
  id: brain-9a7c723a86a92e17
  locator: Page 54
  resource: /references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md
  unit_file_sha256: 82a7af14ae37b566c088f7eb9174296bf92922fec1447e3be88058f00b8350dd
  unit_path: ingest/SRC-0025/units/p0054.md
  unit_sha256: 8bab0de3c1c59f243337a41385a1dab23f307b13612f700612cef9b022697fde
- authority: FRAMEWORK
  brain_source_id: SRC-0025
  evidence_ref: security-031-src-0025-ec-009
  id: brain-a80d6e1d8634f06c
  locator: Page 101
  resource: /references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md
  unit_file_sha256: 5fab9a4ee0f35f52e37ef6e20957559eb76b0615e426621a673b086efe76e450
  unit_path: ingest/SRC-0025/units/p0101.md
  unit_sha256: 343e2d62793548107fffb1d0f7e487f56c4ea784c04a357aaef18cf28900c1e0
- authority: FRAMEWORK
  brain_source_id: SRC-0025
  evidence_ref: security-031-src-0025-ec-002
  id: brain-bba351c56a847cbe
  locator: Page 47
  resource: /references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md
  unit_file_sha256: b798653c609c90f764b5c43915568dad08c22d7653ea9df28d43d3686bc3ba24
  unit_path: ingest/SRC-0025/units/p0047.md
  unit_sha256: 82e780983654233502534121130905c8743449733e69b91a3a37b33e30cb2264
- authority: FRAMEWORK
  brain_source_id: SRC-0025
  evidence_ref: security-031-src-0025-ec-001
  id: brain-cb2af1899d5f664f
  locator: Page 46
  resource: /references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md
  unit_file_sha256: 8a7798ac26c7bb82b0a7738e3f4798ba143ffde1a14419a508f20eb45b481399
  unit_path: ingest/SRC-0025/units/p0046.md
  unit_sha256: 1bc6df9d8632df1bdad0ed8c94f7e1314be687abd9e6e147ca1f953e0f99b02c
- authority: FRAMEWORK
  brain_source_id: SRC-0034
  evidence_ref: security-031-src-0034-ec-003
  id: brain-d0eb2d4bb6aab0f7
  locator: Page 30
  resource: /references/src-0034-b4133f21b4fb1b6ab9bd39962c2aad1b6f3193dfe84a23fcf9a2edb914a11176.md
  unit_file_sha256: 2569cf08c77360c0b4b40ef5d08bc359ecb2e3b7048af604e1669612d7a68bcb
  unit_path: ingest/SRC-0034/units/p0030.md
  unit_sha256: ad0bf714836bd091d73f9228c5a2e70a9367b59fbcb2fb1c97ac5dea4724a007
- authority: FRAMEWORK
  brain_source_id: SRC-0034
  evidence_ref: security-031-src-0034-ec-002
  id: brain-d33d513e3909778c
  locator: Page 7
  resource: /references/src-0034-b4133f21b4fb1b6ab9bd39962c2aad1b6f3193dfe84a23fcf9a2edb914a11176.md
  unit_file_sha256: 9c4aab7169ee5dd17c0bf25a844881c11516365ffe0e0e1ba6f762521cf89ec9
  unit_path: ingest/SRC-0034/units/p0007.md
  unit_sha256: 21018d2b84c3129d75d570222b76c35a07a5260a96cb5c5970cffca8f8c5d6eb
- authority: FRAMEWORK
  brain_source_id: SRC-0025
  evidence_ref: security-031-src-0025-ec-013
  id: brain-dd56cd1de558e692
  locator: Page 55
  resource: /references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md
  unit_file_sha256: 1ef43541a96f302c28e9d11cb14c051d3990ddc723c7d27ac348ade264dfac32
  unit_path: ingest/SRC-0025/units/p0055.md
  unit_sha256: 2c045243791fbc02b9e555438c5733f9a63d64845eed1752a84e9d3a0e38d0cb
- authority: FRAMEWORK
  brain_source_id: SRC-0024
  evidence_ref: security-031-src-0024-ec-002
  id: brain-e03670eff59d8819
  locator: Page 20
  resource: /references/src-0024-130442e9d4999ebe7d79c4d415299a345953dabb08c54511a87b91f90492b285.md
  unit_file_sha256: 0b9e7b37e5fa351400c57634e290009278def7073c8279bd0ed86d395b5225f7
  unit_path: ingest/SRC-0024/units/p0020.md
  unit_sha256: 0c150f500dc13a3cca54c3f67cf1a5ed7e606729d66b3453affb5d95062731de
- authority: FRAMEWORK
  brain_source_id: SRC-0024
  evidence_ref: security-031-src-0024-ec-005
  id: brain-e36669729ede851a
  locator: Page 155
  resource: /references/src-0024-130442e9d4999ebe7d79c4d415299a345953dabb08c54511a87b91f90492b285.md
  unit_file_sha256: c7a9a1075271482a06856c3cc26e4bdcd81f31cfe8c36b9b81708d0f246ba5da
  unit_path: ingest/SRC-0024/units/p0155.md
  unit_sha256: 47e28fccda5c479fa335a8239aa24424dcd28fa85cfa2bb438f65d5ae948f54b
- authority: FRAMEWORK
  brain_source_id: SRC-0024
  evidence_ref: security-031-src-0024-ec-006
  id: brain-f8f6dc75fde7d2bb
  locator: Page 24
  resource: /references/src-0024-130442e9d4999ebe7d79c4d415299a345953dabb08c54511a87b91f90492b285.md
  unit_file_sha256: 64160aa2c956a6bc723f20f5df19e125bb1b449b3a2dc4fef96c2ae9333147d4
  unit_path: ingest/SRC-0024/units/p0024.md
  unit_sha256: c27cca66bcbd78babbc8d3a6c7ac9c1f44aee807862c7f2361df2a2440bc4710
status: stable
tags:
- questionnaire
- ai-supply-chain
- provenance
title: AI supply chain inventory and provenance
topic: ai-supply-chain-inventory
type: question
---


# AI supply chain inventory and provenance

## Purpose

Determine whether the project can identify material dependencies and trace their
origin, integrity and change history.

Section evidence: [^brain-028c9a0407876c7e] [^brain-3bfeb3db3d4ea22c] [^brain-3deb003b8688c617] [^brain-4060e4b2d21457e7] [^brain-4393033b94b0d965] [^brain-4a55cc262bde6efb] [^brain-4e4c39d9afb076e7] [^brain-631eb97bbfe47359] [^brain-679d195dc287b0bc] [^brain-74cc147aa9a476eb] [^brain-7bc39c4ef21d01eb] [^brain-83da1770f64cc5f8] [^brain-8e49791405ad019e] [^brain-965344936e9d924f] [^brain-9a7c723a86a92e17] [^brain-a80d6e1d8634f06c] [^brain-bba351c56a847cbe] [^brain-cb2af1899d5f664f] [^brain-d0eb2d4bb6aab0f7] [^brain-d33d513e3909778c] [^brain-dd56cd1de558e692] [^brain-e03670eff59d8819] [^brain-e36669729ede851a] [^brain-f8f6dc75fde7d2bb]

## Guidance

Answer “yes” only when the inventory covers the relevant runtime and development
dependencies and links material artifacts to provenance, version, integrity and
change evidence. Include external tools, managed services and delegated agents
where they cross the system boundary.

Section evidence: [^brain-028c9a0407876c7e] [^brain-3bfeb3db3d4ea22c] [^brain-3deb003b8688c617] [^brain-4060e4b2d21457e7] [^brain-4393033b94b0d965] [^brain-4a55cc262bde6efb] [^brain-4e4c39d9afb076e7] [^brain-631eb97bbfe47359] [^brain-679d195dc287b0bc] [^brain-74cc147aa9a476eb] [^brain-7bc39c4ef21d01eb] [^brain-83da1770f64cc5f8] [^brain-8e49791405ad019e] [^brain-965344936e9d924f] [^brain-9a7c723a86a92e17] [^brain-a80d6e1d8634f06c] [^brain-bba351c56a847cbe] [^brain-cb2af1899d5f664f] [^brain-d0eb2d4bb6aab0f7] [^brain-d33d513e3909778c] [^brain-dd56cd1de558e692] [^brain-e03670eff59d8819] [^brain-e36669729ede851a] [^brain-f8f6dc75fde7d2bb]

## Related knowledge

- [ai-supply-chain-governance](/concepts/ai-supply-chain-governance.md)
- [traceability](/concepts/traceability.md)
- [ai-data-quality-and-validation](/concepts/ai-data-quality-and-validation.md)

## Source references

- SRC-0024, pages 152 and 155-156.
- SRC-0025, pages 46-47 and 71-73.
- SRC-0034, pages 3 and 7.


[^brain-028c9a0407876c7e]: [SRC-0025](/references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md); locator: Page 87.
[^brain-3bfeb3db3d4ea22c]: [SRC-0025](/references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md); locator: Page 117.
[^brain-3deb003b8688c617]: [SRC-0025](/references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md); locator: Page 66.
[^brain-4060e4b2d21457e7]: [SRC-0025](/references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md); locator: Page 107.
[^brain-4393033b94b0d965]: [SRC-0025](/references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md); locator: Page 72.
[^brain-4a55cc262bde6efb]: [SRC-0025](/references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md); locator: Page 86.
[^brain-4e4c39d9afb076e7]: [SRC-0024](/references/src-0024-130442e9d4999ebe7d79c4d415299a345953dabb08c54511a87b91f90492b285.md); locator: Page 22.
[^brain-631eb97bbfe47359]: [SRC-0024](/references/src-0024-130442e9d4999ebe7d79c4d415299a345953dabb08c54511a87b91f90492b285.md); locator: Page 156.
[^brain-679d195dc287b0bc]: [SRC-0024](/references/src-0024-130442e9d4999ebe7d79c4d415299a345953dabb08c54511a87b91f90492b285.md); locator: Page 152.
[^brain-74cc147aa9a476eb]: [SRC-0025](/references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md); locator: Page 73.
[^brain-7bc39c4ef21d01eb]: [SRC-0025](/references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md); locator: Page 71.
[^brain-83da1770f64cc5f8]: [SRC-0034](/references/src-0034-b4133f21b4fb1b6ab9bd39962c2aad1b6f3193dfe84a23fcf9a2edb914a11176.md); locator: Page 3.
[^brain-8e49791405ad019e]: [SRC-0025](/references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md); locator: Page 116.
[^brain-965344936e9d924f]: [SRC-0025](/references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md); locator: Page 112.
[^brain-9a7c723a86a92e17]: [SRC-0025](/references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md); locator: Page 54.
[^brain-a80d6e1d8634f06c]: [SRC-0025](/references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md); locator: Page 101.
[^brain-bba351c56a847cbe]: [SRC-0025](/references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md); locator: Page 47.
[^brain-cb2af1899d5f664f]: [SRC-0025](/references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md); locator: Page 46.
[^brain-d0eb2d4bb6aab0f7]: [SRC-0034](/references/src-0034-b4133f21b4fb1b6ab9bd39962c2aad1b6f3193dfe84a23fcf9a2edb914a11176.md); locator: Page 30.
[^brain-d33d513e3909778c]: [SRC-0034](/references/src-0034-b4133f21b4fb1b6ab9bd39962c2aad1b6f3193dfe84a23fcf9a2edb914a11176.md); locator: Page 7.
[^brain-dd56cd1de558e692]: [SRC-0025](/references/src-0025-50b12699a427e653a3e879b28def402203b79aa0121df840cf5ffdfd8fb640c2.md); locator: Page 55.
[^brain-e03670eff59d8819]: [SRC-0024](/references/src-0024-130442e9d4999ebe7d79c4d415299a345953dabb08c54511a87b91f90492b285.md); locator: Page 20.
[^brain-e36669729ede851a]: [SRC-0024](/references/src-0024-130442e9d4999ebe7d79c4d415299a345953dabb08c54511a87b91f90492b285.md); locator: Page 155.
[^brain-f8f6dc75fde7d2bb]: [SRC-0024](/references/src-0024-130442e9d4999ebe7d79c4d415299a345953dabb08c54511a87b91f90492b285.md); locator: Page 24.
