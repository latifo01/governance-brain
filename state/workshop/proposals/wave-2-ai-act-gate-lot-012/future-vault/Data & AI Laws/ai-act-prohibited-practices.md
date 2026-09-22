---
id: ai-act-prohibited-practices
title: AI Act prohibited practices
type: knowledge
domains: [AI, LEGAL, LEGAL_REGULATORY, RISK]
status: active
aliases:
  - AI Act Article 5
  - prohibited AI practices
  - unacceptable-risk AI practices
tags:
  - ai-act
  - prohibited-practice
  - legal-definition
evidence_sources: [AI_ACT, AI_LEGAL_GUIDANCE]
---

# AI Act prohibited practices

## Summary

Article 5 of the EU AI Act prohibits placing on the market, putting into service or using AI systems in a closed list of practices. This note is the decision-gate knowledge for screening a system and its intended use against those prohibitions; it does not cover downstream obligations.

Authority basis: the prohibitions and their conditions come only from the reviewed binding combination of SRC-0011 (Regulation (EU) 2024/1689) as modified by SRC-0043 (Regulation (EU) 2026/1744). Commission guidelines (SRC-0016, SRC-0017) are used solely as visibly marked non-binding interpretation.

## Prohibited practices and their conditions

Unless a temporal qualifier is stated, each prohibition below is a pre-existing Article 5 rule within Chapters I and II, applicable from 2 February 2025 per the reviewed currentness evidence (SRC-0011 pages 172-175; SRC-0043 pages 18 and 35).

- Manipulative techniques. Placing on the market, putting into service or using AI that employs subliminal, deliberately manipulative or deceptive techniques is prohibited when the technique has the objective or effect of materially distorting behaviour by appreciably impairing informed decision-making, causes a decision that would not otherwise have been taken, and causes or is reasonably likely to cause significant harm (SRC-0011, page 172).
- Exploitation of vulnerabilities. AI that exploits vulnerabilities linked to age, disability or a specific social or economic situation is prohibited when the distortion of behaviour causes or is reasonably likely to cause significant harm to the person or a third party (SRC-0011, page 172).
- Untargeted facial-image scraping. AI systems that create or expand facial-recognition databases through untargeted scraping of facial images from the internet or CCTV footage are prohibited, covering placing on the market, putting into service for that purpose, and use (SRC-0011, page 173).
- Emotion inference in workplaces and education. AI that infers emotions of natural persons in workplaces or educational institutions is prohibited, except for medical or safety reasons (SRC-0011, page 174).
- Biometric categorisation of sensitive attributes. Biometric categorisation that individually categorises natural persons to deduce or infer race, political opinions, trade-union affiliation, religious or philosophical beliefs, sex life or sexual orientation is prohibited; lawfully acquired datasets may still be labelled or filtered on biometric data, and biometric data may be categorised in law enforcement (SRC-0011, page 174).
- Real-time remote biometric identification for law enforcement. Prohibited in publicly accessible spaces except where strictly necessary for an enumerated objective: targeted searches for specified victims or missing persons, prevention of specified serious threats to life, physical safety or terrorist attack, and location or identification of a criminal suspect for investigation, prosecution or execution of a criminal penalty for an offence listed in Annex II carrying a maximum custodial sentence of at least four years in the Member State concerned (SRC-0011, pages 174-175, 382-383).

New prohibitions applying from 2 December 2026 (SRC-0043, page 35): Article 5(1)(ba) and (bb) prohibit AI systems generating or manipulating non-consensual intimate material and child sexual abuse material, subject to the Article 5(1a) and (1b) conditions:

- For providers, the prohibition applies where generation or manipulation is the system's intended purpose, or is a reasonably foreseeable and reproducible outcome without significant technical modification and adequate preventive and corrective safeguards are absent, considering design, training, architecture, capabilities, user-facing functions and reasonably foreseeable misuse (SRC-0043, page 18).
- For deployers, it applies only when the system is used for the purpose of generating or manipulating the specified material (SRC-0043, page 18).
- Article 5(1b) excludes changes that neither increase exposure of depicted intimate parts nor alter the nature of depicted sexually explicit activity (SRC-0043, page 18).
- The child-sexual-abuse-material prohibition preserves cases covered by a national-law "without right" defence, including legitimate authority activity and legitimate compliance evaluation; the operative cross-reference is to Directive 2011/93/EU and national law (SRC-0043, page 6, recital-level explanation; operative wording on page 18).

## Conditions on the law-enforcement biometric exception

Where use of real-time remote biometric identification is permitted, binding conditions apply (all pre-existing and applicable, SRC-0011 pages 175-178):

- The use may be deployed only to confirm the identity of the specifically targeted person, considering the seriousness, probability and scale of harm if not used and the consequences for the rights and freedoms of all affected persons (page 175).
- Necessary and proportionate safeguards under authorising national law apply, including temporal, geographical and personal limitations; the authority must complete a fundamental-rights impact assessment under Article 27 and register the system under Article 49; in a duly justified emergency, use may start before registration if registration follows without undue delay (page 176).
- Each use requires prior authorisation from a judicial authority or a binding independent administrative authority; in a duly justified emergency, use may start if authorisation is requested without undue delay and no later than 24 hours; if refused, use must stop immediately and all data, results and outputs must be discarded and deleted immediately (page 176).
- The authorising authority may approve use only on objective evidence or clear indications of necessity and proportionality for an enumerated purpose; use must be strictly limited in time and geographical and personal scope; no decision producing adverse legal effects may be based solely on the system output (page 177).
- Each use must be notified to the relevant market-surveillance and national data-protection authorities, following national rules and containing at least the Article 5(6) information, excluding sensitive operational data (page 177).
- Notified authorities report annually to the Commission, which publishes aggregated reports excluding sensitive operational information (pages 178-179).

## Scope and actor boundaries

- The prohibitions cover placing on the market, putting into service and using; the real-time remote biometric-identification category applies specifically to use (SRC-0011, page 172; interpretation in SRC-0016, page 9).
- The free and open-source licence exclusion is unavailable when the system is placed on the market or put into service within Article 5 (SRC-0011, page 159).
- Article 5 does not affect GDPR Article 9 for biometric processing outside law enforcement (SRC-0011, page 175) and does not displace prohibitions arising under other Union-law provisions (SRC-0011, page 179).

Interpretation (non-binding, SRC-0016): screening is a case-specific assessment and guideline examples are indicative rather than determinative (page 7); "use" is read broadly across the lifecycle and across integration into services, processes, infrastructure or larger systems, including misuse that may amount to a screened practice (page 10); provider and deployer responsibility is assessed by role and control, one operator may hold both roles, and staff or contractors acting under an organisation's procedures are generally treated as acting for that deployer (pages 10-11); a dual-use system offered for excluded and non-excluded purposes remains in scope for the non-excluded route (page 13); a specific deployment can meet a prohibited-practice condition even when the broader use is high-risk, and an Article 6(3) non-high-risk outcome does not remove Article 5 screening (pages 16-17); the guidelines recommend proportionate safeguards, use restrictions, instructions, human oversight and responsive action when a provider becomes aware of screened misuse (page 18, expressed as Commission expectation). Passing the Article 5 gate does not establish compliance with other applicable Union law, including data protection, equality, employment, consumer and fundamental-rights rules (SRC-0016, pages 19, 21).

## Decision-gate use

Before market placement or deployment, record the use context, each potentially relevant Article 5 category, the actors and roles (provider, deployer, or both), the evidence relied on, the temporal status of the category screened (pre-existing and applicable, or new and applying from 2 December 2026), the legal reviewer, and the conclusion with a redesign or stop decision where needed. See [[core-011-prohibited-practice-screening]] for the canonical assessment question and [[legal-001-ai-act-classification-record]] for the classification record.

## Limits and uncertainties

- The Commission guidelines are expressly non-binding; their examples and breadth of "use" must not be treated as binding rules (SRC-0016, pages 6-7, 10).
- The meaning of "national security" and "exclusive purpose" for the military, defence and national-security exclusion requires legal review against binding authority (SRC-0016, page 12); the exclusion itself is binding (SRC-0011, page 157).
- Applicability of the national-law "without right" defence for the child-sexual-abuse-material prohibition requires jurisdiction-specific legal review (SRC-0043, page 6).
- Downstream obligations, penalties and enforcement are outside this note and this lot.
- This note does not classify any specific system; classification requires the recorded assessment process.

## Related concepts

- [[eu-ai-act]] is the routing overview; this note is the dedicated Article 5 decision gate.
- [[high-risk-ai-system-classification]] is the next gate when no prohibited practice is identified.
- [[ai-system]] defines the regulatory unit screened by this gate.
- [[european-ai-office-eaio]] and [[ai-board]] are the institutional context.

## Source references

- SRC-0011, Regulation (EU) 2024/1689 official text, pages 157, 159, 172-179, 382-383 (Article 5 prohibitions, conditions, exceptions, scope boundaries; Annex II offence list), reviewed as modified by SRC-0043.
- SRC-0043, Regulation (EU) 2026/1744 official text, pages 4-6, 18, 35 (new prohibited-content practices, provider/deployer conditions, application from 2 December 2026).
- SRC-0016, Commission prohibited-practices guidelines, pages 6-21 (non-binding interpretation of screening, roles, use, exclusions and parallel law).
- SRC-0017, Commission definition guidelines, pages 2-3, 11-12 (non-binding interpretation of the AI-system definition screened at this gate).
