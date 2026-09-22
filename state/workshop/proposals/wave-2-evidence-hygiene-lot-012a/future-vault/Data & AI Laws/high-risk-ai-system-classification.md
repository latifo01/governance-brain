---
id: high-risk-ai-system-classification
title: High-risk AI system classification
type: knowledge
domains: [AI, LEGAL, LEGAL_REGULATORY, RISK]
status: active
aliases:
  - AI Act Article 6
  - AI Act high-risk classification
  - Annex III high-risk categories
tags:
  - ai-act
  - high-risk-ai
  - legal-definition
evidence_sources: [AI_ACT, AI_LEGAL_GUIDANCE]
---

# High-risk AI system classification

## Summary

Article 6 of the EU AI Act classifies an AI system as high-risk through two routes: the product route (Article 6(1) with Annex I) and the use-case route (Article 6(2) with Annex III). This note is the decision-gate knowledge for that classification; downstream high-risk obligations are outside its scope and this lot.

Authority basis: the classification rules and application dates come only from the reviewed binding combination of SRC-0011 (Regulation (EU) 2024/1689) as modified by SRC-0043 (Regulation (EU) 2026/1744).

## Application dates (binding, SRC-0043, page 35)

- Chapter III Sections 1, 2 and 3 apply from 2 December 2027 to systems classified as high-risk under Article 6(2) and Annex III, except Article 6(5).
- Chapter III Sections 1, 2 and 3 apply from 2 August 2028 to systems classified as high-risk under Article 6(1) and Annex I, except Article 6(5).
- Providers and deployers of high-risk AI systems intended for use by public authorities must take the necessary compliance steps by 2 August 2030.
- For pre-existing high-risk systems outside Article 111(1), the AI Act generally applies after the relevant Chapter III date only where the system design is significantly changed from that date.

Any high-risk classification claim or derived obligation must retain these temporal qualifiers.

## Route 1: Article 6(1) product route (Annex I)

An AI system is high-risk where it is intended to be used as a safety component of, or is itself, a product covered by Annex I legislation and subject to third-party conformity assessment (SRC-0011, pages 179-180; the cumulative rule and its cross-page lineage are completed in the wave-2 evidence-hygiene lot re-extraction).

Clarifications introduced by SRC-0043 (page 18, binding, applying with the Annex I date):

- Article 6(1a) excludes from the safety-component classification systems used solely for non-safety aspects of user assistance, performance optimisation, service efficiency, automation, convenience or quality control.
- Article 6(1b) nevertheless classifies a system as a safety component when its failure or malfunction would endanger health and safety.
- Article 6(1c) states that a product does not satisfy the third-party-assessment condition where such assessment is required solely for risks unrelated to health and safety, such as spectrum distribution or non-health electromagnetic interference.
- The amended safety-component definition (SRC-0043, page 16) defines it by its safety function or by whether its failure or malfunction endangers persons' or property health and safety.

Annex I structure in the reviewed text (SRC-0011, pages 379-381, reviewed as amended by SRC-0043, page 36): Section A completes with in-vitro diagnostic medical devices; Section B lists harmonisation legislation including civil-aviation security, two- or three-wheel vehicles and quadricycles, agricultural and forestry vehicles, marine equipment, rail-system interoperability, motor-vehicle type approval and general vehicle safety (Regulations (EU) 2018/858 and 2019/2144), and civil-aviation legislation concerning unmanned aircraft. Machinery legislation was moved from Section A to Section B so that the limited Article 2(2) regime applies to those machines (SRC-0043, pages 13 and 15: Article 6(1), Article 60a and Articles 102 to 112 apply to Annex I Section B products, with Articles 57, 58 and 59 applying only where high-risk requirements are integrated into the harmonisation legislation).

Limitations on requirements (SRC-0043, pages 15-16, binding): new Article 2(13) permits specific requirements or obligations for Article 6(1) systems to be limited only where Annex I Section A legislation provides equivalent or higher protection and the overall AI Act protection level is not reduced, with the concrete systems, conditions and extent of any limitation depending on delegated acts the Commission must adopt by 2 August 2027. For Annex I Section A products, classification as high-risk does not itself remove a conformity-assessment option allowed by the relevant harmonisation legislation or require third-party assessment solely because a high-risk safety component is present (SRC-0043, page 22).

## Route 2: Article 6(2) use-case route (Annex III)

Annex III lists the following AI uses as high-risk in the reviewed text (SRC-0011, pages 384-388, reviewed as amended by SRC-0043, pages 35-36):

- Biometrics, where use is permitted by applicable Union or national law: remote biometric identification (excluding verification solely confirming that a specific person is who they claim to be), sensitive or protected-attribute biometric categorisation, and emotion recognition.
- AI safety components used to manage or operate critical digital infrastructure, road traffic, or the supply of water, gas, heating or electricity.
- Education and vocational training at institutions at all levels: access, admission or assignment; learning-outcome assessment including learning guidance; evaluation of the appropriate educational level; and monitoring or detection of prohibited exam behaviour.
- Employment: recruitment or selection of natural persons, including targeted job advertisements, application analysis and filtering, and candidate evaluation; decisions affecting work relationships, promotion or termination; task allocation based on behaviour, personality traits or personal characteristics; and performance or behaviour monitoring and evaluation.
- Access to essential private services, public services and benefits: public-authority eligibility and benefit decisions; personal creditworthiness or credit scores (except financial-fraud detection); life and health insurance risk assessment or pricing; and emergency-call evaluation or prioritisation, emergency dispatch, and emergency-healthcare triage.
- Law enforcement, where authorised by applicable Union or national law: victim-risk assessment; polygraphs or similar tools; evidence-reliability assessment; offending or reoffending risk assessment that is not based solely on profiling; assessment of personality, characteristics or criminal history; and criminal-offence profiling as defined by Article 3(4) of Directive (EU) 2016/680.
- Migration, asylum and border-control management, where authorised: polygraphs or similar tools; individual security, irregular-migration or health risk assessment; and assistance with asylum, visa or residence-permit applications and related complaints, including evidence-reliability assessment.

The reviewed evidence covers Annex III through page 388 of SRC-0011; any further Annex III categories on later pages were not verified in this lot and must not be asserted from this note.

## Derogation and profiling override

- An Annex III AI system is not high-risk when it poses no significant risk of harm to health, safety or fundamental rights, including by not materially influencing decision outcomes, and one of the listed conditions is met: narrow procedural task, improvement of a previously completed human activity, pattern or deviation detection without replacing or influencing prior human assessment absent proper human review, or a preparatory task for an Annex III assessment (SRC-0011, page 180; Chapter III Sections 1-3 apply from 2 December 2027 for this route).
- An Annex III AI system that profiles natural persons remains high-risk despite the derogation (SRC-0011, page 181).
- A provider treating an Annex III system as not high-risk must document that assessment before market placement or putting into service, register the system under Article 49(2), and supply the documentation when requested by a competent national authority (SRC-0011, page 181).
- The Commission may amend the derogation conditions by delegated act under Article 97 on concrete and reliable evidence (SRC-0011, page 181).

## Decision-gate use

Classification should record the intended purpose, the organisational role, the route relied on (Annex I product route or Annex III use-case route), the specific annex categories considered, any profiling, any claimed derogation documented before market placement or putting into service, the applicable application date for the route used, the legal reviewer, and the evidence and version relied on. See [[core-013-high-risk-ai-classification]] for the canonical assessment question and [[legal-001-ai-act-classification-record]] for the classification record. A non-high-risk outcome does not remove the independent [[ai-act-prohibited-practices]] screening gate, and the two gates can both apply to the same deployment (SRC-0016, pages 16-17, non-binding interpretation).

## Limits and uncertainties

- This note does not cover downstream high-risk obligations, conformity-assessment substance, GPAI, Article 50 transparency, or post-market monitoring and incidents; those are reserved for later lots.
- The Annex I Section B limited regime and Article 2(13) limitation depend on future delegated acts (SRC-0043, page 16).
- Application-date claims are bounded by the reviewed amendment; the Brain records the version assessed and this note must be rechecked against later amendments.
- This note does not classify any specific system.

## Related concepts

- [[eu-ai-act]] is the routing overview; this note is the dedicated Article 6 decision gate.
- [[ai-act-prohibited-practices]] is the preceding screening gate.
- [[ai-system]] defines the regulatory unit classified at this gate.
- [[fundamental-right-impact-assessment-fria]] is a downstream obligation trigger for certain Annex III systems, outside this lot's scope.

## Source references

- SRC-0011, Regulation (EU) 2024/1689 official text, pages 179-181 (Article 6, derogation, profiling override, provider documentation; amended Article 2(2) scope), pages 382-388 (Annex II and Annex III entries), reviewed as modified by SRC-0043.
- SRC-0043, Regulation (EU) 2026/1744 official text, pages 13, 15-16, 18, 22, 35-36 (Annex I restructuring, Article 2(13), safety-component definition, Article 6(1a)-(1c) clarifications, application dates).
- SRC-0016, Commission prohibited-practices guidelines, pages 16-17 (non-binding interpretation of the relationship between the Article 5 and Article 6 gates).
