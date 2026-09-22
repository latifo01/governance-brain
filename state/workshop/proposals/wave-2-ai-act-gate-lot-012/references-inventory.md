# Wave 2 AI Act decision-gate lot 012 — references inventory and link control

Author stage output for the knowledge proposal. Every claim in the
`future-vault/` overlay traces to a `VERIFIED` record in
`evidence/verified-evidence.jsonl`. Obligations and prohibitions cite only
SRC-0011 as modified by reviewed SRC-0043 (binding combination); SRC-0016 and
SRC-0017 appear only as visibly marked non-binding interpretation. SRC-0022
produced no verified record for this lot and is cited only where a pre-existing
published note already cited it (eu-ai-act, core-011, core-013, legal-001,
which preserve their existing SRC-0022 training references).

## Authority classes

| Source | Class | Use in overlay |
| --- | --- | --- |
| SRC-0011 | BINDING base act (Regulation (EU) 2024/1689) | prohibitions, classification rules, definitions, exceptions — only as modified by SRC-0043 |
| SRC-0043 | BINDING amending act (Regulation (EU) 2026/1744) | 2026 amendment state, operative Article 5(1a)/(1b) and Article 6(1a)-(1c) wording, application dates |
| SRC-0016 | NON_BINDING_INTERPRETIVE (Commission prohibited-practices guidelines) | visibly marked interpretation only |
| SRC-0017 | NON_BINDING_INTERPRETIVE (Commission definition guidelines) | visibly marked interpretation only |

## Evidence mapping per overlay note

### ai-act-prohibited-practices (ADD)

- SRC-0011 page 172: manipulative techniques (EV-128950402031BDF04DF2),
  exploitation of vulnerabilities (EV-83AFC4474A70E735A16C).
- SRC-0011 page 173: untargeted facial-image scraping (EV-022E376D8858F2B77C5B).
- SRC-0011 page 174: real-time remote biometric identification prohibition
  (EV-7439343F311A692CBFA4), emotion inference (EV-7C485FB23DBEF67F2B21),
  biometric categorisation (EV-F823576977867963D62B).
- SRC-0011 pages 175-179, binding conditions: targeted person only
  (EV-1C34C5E725285019D015), safeguards and Article 27/49 duties
  (EV-8B3FB68951E58B06D63C), prior authorisation and emergency rules
  (EV-8CA0E98AC3F51F7D7BD8), necessity/proportionality and no adverse decision
  solely on output (EV-20B43A07EF1645E9D3D2), notification
  (EV-4E980349F20761DAD64D), annual reporting (EV-E8EF947BC14E18A9769E,
  EV-E0EFE312E5D1848C22BB).
- SRC-0011 page 175: Annex II offence and four-year threshold
  (EV-1E1596EF08D31CB00343); Annex II list pages 382-383
  (EV-78E3BD255AA8D83342DD, EV-39F701884BFC0660F5CF).
- SRC-0011 pages 157, 159, 175, 179: scope and dependency boundaries
  (EV-BC83181CAF22832282E4 context, EV-563E637955D79E552070 open-source
  exclusion, EV-06A2171C7E6E3CBB707F GDPR Article 9,
  EV-EC50D631272D235C9FCA other Union-law prohibitions).
- SRC-0043 pages 18, 35 (binding, applying from 2026-12-02): provider
  conditions (EV-64EAF02A89586E6A7F7B), deployer conditions
  (EV-0078537F8DC773B2E064), Article 5(1b) exclusion
  (EV-7FE12009C534966E747F), application date (EV-BEC230C41DFD4315F732);
  recital-level rationale pages 4-6 (EV-DC1C749957A599354A08,
  EV-76234DE596CD9EAD39A5, EV-4524920F6CE662138D27 — marked as recital-level).
- SRC-0016 (interpretation, marked): pages 7, 9-13, 16-19, 21
  (EV-A19BFE1C05C8D89FC7FC, EV-A770F0F0822C50E3A760, EV-4ADAF9C344DB667EE347,
  EV-ED4FC477E2B726EA6095, EV-930F92C52019D62C8C20, EV-B9E1BA098254C800E174,
  EV-F19D1CADE217C2572D77, EV-EC57E2D581BCCF833F5C, EV-BEB424D227BFFD955C1F,
  EV-E28A74BB56DC7FE317F4, EV-3FF49B3C53F40C13D314, EV-3AF6DDF406E54D56A34).
- SRC-0016 page 12 (interpretation): national-security exclusion reading
  (EV-347BBE87F663CC2927B9).

### high-risk-ai-system-classification (ADD)

- SRC-0011 page 179: Article 6(1) cumulative product route
  (EV-3AFB826E9C884A3C4E0F, cross-page lineage noted).
- SRC-0043 page 18 (binding): Article 6(1a) exclusion
  (EV-7A41D64BF3477B6EE63D), 6(1b) override (EV-6F379101642E35A6FF74),
  6(1c) non-health third-party assessment (EV-0BC1561D98EE6CA5CF92).
- SRC-0043 page 16 (binding): amended safety-component definition
  (EV-59F047615588CBAAF770).
- SRC-0011 pages 379-381 with SRC-0043 pages 35-36 (binding): Annex I
  Section A/B structure (EV-00FD1B0E9AB10F134A29, EV-A9B8A4784FFADA4B7490,
  EV-1DB8D166DCA435961852); machinery move rationale (EV-0250F5241F88CA474226
  recital-level, page 13); operative limited Article 2(2) regime
  (EV-E580D7991904512B4BD8, page 15).
- SRC-0043 pages 15-16, 22 (binding): Article 2(13) limitation and delegated
  acts by 2027-08-02 (EV-273E947D57FCADEF429D, EV-33F8DB2EC5D040452CBE),
  Annex I Section A conformity-assessment options
  (EV-4BAA4B8278341A8EB7BE).
- SRC-0011 pages 180-181 (Article 6(3) route; unit-level binding flags are an
  audit-time registry residue for EV-816A08EA0F494702D35B and
  EV-0290ED06EE7B2D0A1DF9 — see vault-review.md W-1/W-2 adjudication; only
  EV-DD66A306EC8F0D228806 and EV-5C2B244CB3F69F98A357 are binding-usable rows): Article 6(3) derogation
  (EV-DD66A306EC8F0D228806), Commission delegated act power
  (EV-0290ED06EE7B2D0A1DF9), provider documentation and Article 49(2)
  registration (EV-5C2B244CB3F69F98A357), profiling override
  (EV-816A08EA0F494702D35B).
- SRC-0011 pages 384-388 with SRC-0043 (binding, Annex III entries):
  biometrics (EV-A1FB29DDB3A13FEEEDA0), critical infrastructure
  (EV-A6765D10D2B9CC1AA363), education (EV-077F10A72FE1E07A4FCE),
  employment/recruitment (EV-9EC04CB21995D92E3EE9, EV-76AA42057ADA6A500669),
  essential services and benefits (EV-ADBA3F900A7C1087AD7C), law enforcement
  (EV-587A3702EF8669C6A950, EV-0500C1078FBCC44D7C48), migration/asylum/border
  (EV-3C68287A3BCDE624EFE4). Annex III pages beyond 388 were not verified in
  this lot and the note states that limit.
- SRC-0043 page 35 (binding, application dates): 2027-12-02 Annex III
  (EV-2A030E0892959466CB6C), 2028-08-02 Annex I (EV-32D4ED772BF6E91C0663),
  2030-08-02 public-authority systems (EV-11FE2DADD11C643EDFFB), transition
  rule (EV-1710820AA9F35ECAF499).
- SRC-0016 pages 16-17 (interpretation, marked): Article 5/Article 6 gate
  relationship (EV-EC57E2D581BCCF833F5C, EV-BEB424D227BFFD955C1F).

### ai-system (UPDATE)

- Adds binding definition locator SRC-0011 page 159 (EV-0C8A1E341D9AC0B039F3)
  previously absent from the note; keeps SRC-0015 and SRC-0017 references and
  re-labels the guidelines as non-binding interpretation (SRC-0017 pages 3,
  5-6, 11-12: EV-77A79C39A280CB84C643, EV-881454FE69C185AABC88,
  EV-2CE24CD1205FB0528B36, EV-1176095A0B8FE88F6BB0, EV-FB806990EA8EB441E604).
- Adds the decision-gate routing links already validated against existing
  note IDs.

### eu-ai-act (UPDATE)

- Preserves overview role and all existing sections; adds links to the two
  dedicated gate notes; replaces the unverified "Digital Omnibus" limits
  paragraph with the reviewed SRC-0043 basis; adds the binding application
  dates with the SRC-0043 page 35 locators (EV-2A030E0892959466CB6C,
  EV-32D4ED772BF6E91C0663, EV-11FE2DADD11C643EDFFB); adds SRC-0043 source
  reference. No existing claim removed.

### Question note UPDATEs (link/reference review only)

All four preserve frontmatter exactly: topic, priority, applies_to,
answer_type, depends_on, question wording and options are byte-identical to
the active vault notes. Changes:

- core-003: source-reference correction only — the binding Article 3(1)
  definition locator (SRC-0011 page 159) replaces the imprecise pages 162-163
  citation for the definition itself; pages 162-163 retained for surrounding
  Article 3 definitions.
- core-011: adds [[ai-act-prohibited-practices]] to Related knowledge and the
  SRC-0043 pages 18/35 reference for the 2026-amended Article 5 practices.
- core-013: adds [[high-risk-ai-system-classification]] to Related knowledge
  and the SRC-0043 pages 18/35 reference for the amended clarifications and
  route-specific application dates.
- legal-001: adds [[high-risk-ai-system-classification]] to Related knowledge
  and the SRC-0043 pages 18/35 reference.

### ai-act-index (UPDATE)

- Adds [[ai-act-prohibited-practices]] and [[high-risk-ai-system-classification]]
  under Classification and impact assessment; both targets exist in the
  overlay. No other changes.

## NOOP record

- core-010-eu-ai-act-scope: NOOP. The jurisdiction/scope gate intent, links
  ([[eu-ai-act]], [[ai-system]]) and sources (SRC-0011 pages 156-159,
  162-165) remain valid; the verified scope evidence for this lot
  (EV-72A6D8766E68ACCE8A6F, EV-61C72E9C0E07D8DAA3A6,
  EV-BC83181CAF22832282E4) supports no semantic change to the question, and
  the lot forbids new questionnaire intent. No overlay file is emitted.

## Materialization record

- Both ADD notes rest on more than two independent reviewed sources (binding
  SRC-0011 + SRC-0043; interpretive SRC-0016/SRC-0017). No single-source
  exception applies.
- No taxonomy change is proposed; all domains used (AI, LEGAL, LEGAL_REGULATORY,
  RISK, PROCESS) are registered.

## Open uncertainties for reviewer attention

1. Annex III categories on SRC-0011 pages after 388 were not part of the
   verified evidence; the high-risk note states this limit explicitly and must
   not be read as an exhaustive Annex III list.
2. SRC-0043 page 1 (act identification) is marked REVIEW_REQUIRED in the
   evidence; the application-date and operative-provision claims rely on
   later pages (18, 35-36), not page 1.
3. The EU AI Act note's pre-existing SRC-0010 and SRC-0022 references were not
   re-verified in this lot; they are preserved unchanged, not re-asserted.
4. The national-security and "without right" defence boundaries are recorded
   as requiring jurisdiction-specific legal review (SRC-0016 page 12;
   SRC-0043 page 6).
