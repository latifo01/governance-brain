---
id: ai-impact-assessment-aiia
title: AI Impact Assessment (AIIA)
type: knowledge
domains:
- RISK
status: draft
aliases:
- AI Impact Assessment
- AI Impact Assessment (AIIA)
- AIIA
tags: []
evidence_sources: []
---

An **AI System Impact Assessment (AISIA or AIIA)** under **ISO/IEC 42001** is a formal, repeatable management process used to evaluate how an artificial intelligence system affects external individuals, vulnerable groups, and society at large.

ISO/IEC 42001 is the international standard for an **AI Management System (AIMS)**. Within this standard, the AIIA acts as the primary tool to ensure AI is developed and deployed responsibly, ethically, and in compliance with legal standards.

### Key Characteristics of an ISO 42001 AIIA

- **Outward-Looking Perspective:** Unlike traditional IT risk assessments (which focus on risks _to the organization_, such as data loss or downtime), an AIIA focuses outward on risks _to external stakeholders_.
- **Separation from Technical Risk Assessment:** ISO 42001 treats impact assessment as a distinct requirement separate from standard operational/cybersecurity risk evaluations.
- **Lifecycle Orientation:** It must be conducted prior to system deployment and updated whenever the system, its context, or its intended use changes materially.
### Core Structure within the ISO 42001 Standard

The requirement for impact assessments appears in two main parts of ISO/IEC 42001:
1. **Mandatory Management System Clauses:**
    - **Clause 6.1.4:** Requires organizations to plan for assessing the impacts of AI systems.
    - **Clause 8.4 (AI System Impact Assessment):** Mandates that organizations execute, document, and maintain impact assessments throughout the system lifecycle.
2. **Annex A Control Objective (A.5 – Assessing Impacts of AI Systems):**
    - **A.5.1:** AI system impact assessment process.
    - **A.5.2:** Implementation of impact assessments.
    - **A.5.3:** Documentation and record retention of impact assessments.
    - **A.5.4:** Assessing impact on individuals, groups of individuals, and societies.
### What an AIIA Must Evaluate
An ISO 42001 impact assessment examines four broad categories:
```
                  ┌─────────────────────────────┐
                  │    ISO 42001 AIIA SCOPE     │
                  └──────────────┬──────────────┘
                                 │
     ┌──────────────────┬────────┴─────────┬──────────────────┐
     ▼                  ▼                  ▼                  ▼
┌─────────┐      ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│Individual│      │  Group &    │    │ Fundamental │    │ Societal &  │
│ Well-   │      │ Vulnerable  │    │ Rights &    │    │ Environ-    │
│ Being   │      │ Populations │    │ Fairness    │    │ mental      │
└─────────┘      └─────────────┘    └─────────────┘    └─────────────┘
```
1. **Impacts on Individuals:** Safety, health, physical/psychological well-being, financial security, autonomy, and privacy.
2. **Impacts on Groups:** Differential performance across demographics, algorithmic bias, discrimination, accessibility, and risks to vulnerable groups (e.g., children, workers, elderly).
3. **Fundamental Rights & Ethics:** Alignment with legal positions, universal human rights, transparency/explainability, and human dignity.
4. **Societal & Environmental Impact:** Influence on democratic processes, labor markets/employment, public safety, energy consumption, and environmental footprint.
### Essential Content of an AIIA Document

While ISO 42001 does not mandate a rigid form, an auditable AIIA record must document:
- **System Boundaries & Intended Purpose:** Scope of operation, data inputs, and intended outputs.
- **Foreseeable Misuse:** Potential unintended or malicious ways the system could be misused.
- **Affected Stakeholders:** Specific categorization of end-users, subject populations, and third parties.
- **Severity & Reversibility:** Judgment on the magnitude of potential harm and whether such harm can be undone.
- **Mitigation Actions & Human Oversight:** Technical controls, human-in-the-loop intervention plans, and clear accountability assignments.

### Link with [[eu-ai-act]] [[fundamental-right-impact-assessment-fria|FRIA]]
The relationship between a **Fundamental Rights Impact Assessment (FRIA)** under the EU AI Act and an **AI Impact Assessment (AIIA)** under the ISO/IEC 42001 standard is essentially one of **legal obligation versus operational methodology**.
- **FRIA** is a _regulatory requirement_ (EU law).
    
- **AIIA** is an _international standard control_ (ISO/IEC 42001, Clause 8.4 & Annex A Control A.5).
    

Organizations use the **AIIA framework provided by ISO 42001** as the internal mechanism to operationalize, execute, and document the **FRIA mandated by the EU AI Act**.

### Key Comparisons

|**Aspect**|**FRIA (EU AI Act - Art. 27)**|**AIIA (ISO/IEC 42001 - Clause 8.4 / Annex A.5)**|
|---|---|---|
|**Nature**|**Legally binding mandate** within the European Union.|**Voluntary international standard** (auditable for certification).|
|**Who Must Perform It?**|Public sector bodies and private entities providing public services that deploy **high-risk AI systems**.|Any organization operating an AI Management System (AIMS) under ISO 42001.|
|**Primary Scope**|Strictly focuses on **EU Charter Fundamental Rights** (non-discrimination, dignity, human oversight, access to justice).|Broader management focus: evaluates impacts on individuals, groups, society, business operations, and environment.|
|**External Submission**|Summary results must be submitted to the relevant **EU Market Surveillance Authority**.|Evaluated by internal and external ISO management system auditors.|

### How They Connect in Practice

1. **AIIA Acts as the Process Infrastructure for a FRIA:**
    
    ISO 42001 requires organizations to establish a formal, repeatable management process for assessing AI impacts (AIIA) throughout the system lifecycle. Rather than inventing a new workflow for the EU AI Act, organizations use their ISO 42001 AIIA framework to perform and document FRIAs.
    
2. **Scope Alignment (Annex A.5):**
    
    Annex A Control A.5.4 of ISO 42001 explicitly lists evaluating the impacts on "universal human rights," "legal positions," "vulnerable groups," and "fairness" as core components of an AIIA. This aligns directly with the mandatory elements of a FRIA under Article 27 of the AI Act.
    
3. **Risk Management vs. Impact Assessment:**
    
    Both frameworks distinguish standard _technical risk management_ (system reliability, accuracy, uptime) from _impact assessments_ (how the AI system affects human beings, rights, and society).
    

By implementing ISO/IEC 42001 and conducting an AIIA, an organization creates the structured documentation and governance controls necessary to demonstrate compliance with the EU AI Act's FRIA obligations.
