---
aliases:
- Organization Confusion on Hugging Face
brain_id: atlas-aml-cs0027-organization-confusion-on-hugging-face
brain_sha256: 95a4d10cc099d87d672469325533ecddac73b2660348b77b96a345656bd7a13e
domains:
- AI
- RISK
evidence_sources:
- AI_NICE_TO_KNOW
id: atlas-aml-cs0027-organization-confusion-on-hugging-face
sources:
- authority: DATASET
  brain_source_id: SRC-0046
  evidence_ref: be037-src-0046-ec-001
  id: brain-7736d499b5a85ae1
  locator: /objects
  resource: /references/src-0046-6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c.md
  unit_file_sha256: 7b18ef3f2ed64ab84d1204bca642c073f03b8264b4a2fe3bb2f19ab84cbd5241
  unit_path: ingest/SRC-0046/units/key-0003.md
  unit_sha256: 13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab
status: stable
tags:
- famous-ai-incidents
- case-study
- mitre-atlas
- hugging-face
title: Organization Confusion on Hugging Face
type: knowledge
---

# Organization Confusion on Hugging Face

## Summary

MITRE ATLAS identifies `AML.CS0027`, “Organization Confusion on Hugging Face,” as a case study in its dataset. The record describes a researcher creating organization accounts that impersonated real organizations on a public model repository. People from the impersonated organizations requested access believing the accounts were official, which gave the researcher access to models uploaded by those employees and the ability to replace models with malicious versions. The record further describes a demonstration in which malware embedded in an AI model enabled access to a victim environment, with possible follow-on impacts including intellectual-property theft and poisoning of other AI models.

Section evidence: [^brain-7736d499b5a85ae1]

## Applicability

This case is useful as a bounded scenario for threat modeling, artifact provenance, repository identity, access control, model validation, detection and incident response. It documents the ATLAS dataset's description of a researcher demonstration. The record does not establish the prevalence of the technique, a legal violation, or the exposure of every public model repository.

Section evidence: [^brain-7736d499b5a85ae1]

## ATLAS Mapping

- Case study: `AML.CS0027`
- Dataset record title: “Organization Confusion on Hugging Face”
- Scope: public model-repository impersonation, unauthorized model access or replacement, and a demonstrated malicious-model path into a victim environment.

Section evidence: [^brain-7736d499b5a85ae1]

## Governance Considerations

Use the scenario to examine whether repository identities and organization membership are trusted through an explicit process, whether access follows least-privilege decisions, whether model provenance and replacement history are reviewable, and whether downloaded or loaded artifacts are validated and monitored. The scenario also supports testing the escalation path from a supply-chain signal to containment and incident response. These are control-design questions prompted by the documented scenario; the ATLAS record does not prescribe a universal control set.

Section evidence: [^brain-7736d499b5a85ae1]

## Limits

The ATLAS object is a non-binding dataset record. Its description is retained as incident and research context, not as proof of a general security rate, legal breach, organizational liability or universal control failure. Further claims about the affected organizations, dates, prevalence or remediation require the underlying reporting and separate evidence review.

Section evidence: [^brain-7736d499b5a85ae1]

## Related Concepts

- [traceability](/concepts/traceability.md)
- [red-teaming](/concepts/red-teaming.md)
- [human-oversight](/concepts/human-oversight.md)
- [ai-model-validation](/concepts/ai-model-validation.md)

## Source References

- SRC-0046, MITRE ATLAS v2026.08 STIX export, JSON pointer `/objects`, object `AML.CS0027`; source SHA-256: `6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c`; unit SHA-256: `13c6eac080be6463bbeafa9ffd309df83ca5c421052f603bbbb34f8ce96d00ab`.
- Canonical ATLAS record: https://atlas.mitre.org/studies/AML.CS0027


[^brain-7736d499b5a85ae1]: [SRC-0046](/references/src-0046-6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c.md); locator: /objects.
