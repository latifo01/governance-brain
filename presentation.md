---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    background: #050505;
    color: #f5f7fa;
    font-family: "Inter", "Aptos", "Segoe UI", sans-serif;
    font-size: 25px;
    line-height: 1.25;
    padding: 58px 72px 54px 72px;
  }
  section::after { color: #8b949e; font-size: 14px; }
  h1 { color: #ffffff; font-size: 48px; letter-spacing: -0.02em; margin-bottom: 24px; }
  h2 { color: #8bd5ff; font-size: 34px; margin-bottom: 18px; }
  h3 { color: #d7e3ee; font-size: 28px; }
  strong { color: #8bd5ff; }
  em { color: #b8c4ce; }
  code { background: #111820; color: #b7f7d0; padding: 2px 6px; border-radius: 4px; }
  pre { background: #0c1117; color: #d6f5df; border: 1px solid #263442; border-radius: 8px; padding: 18px; font-size: 19px; }
  table { font-size: 20px; background: #0b0f14; }
  th { background: #142534; color: #ffffff; }
  td, th { border-color: #263442; }
  blockquote { border-left: 5px solid #49c6ff; color: #d5dde5; padding-left: 18px; }
  .muted { color: #99a7b3; font-size: 17px; }
  .proof { color: #9aa8b5; font-size: 15px; border-top: 1px solid #263442; margin-top: 20px; padding-top: 8px; }
  .accent { color: #b7f7d0; }
  .warning { color: #ffd166; }
---

<!-- _class: lead -->
# Governance Brain
## Construire une connaissance IA evidence-first

### Présentation CDO · 25 min + 5 min de démonstration + 10 min de questions

<div class="muted">Mesures de référence : 20 septembre 2026 · manuel : manuel.md · exécution U01–U08 en cours</div>

<!-- NOTE ORATEUR
Ouvrir par une idée simple : nous ne construisons pas un dossier de résumés LLM. Nous construisons une chaîne de confiance qui permet à un agent de retrouver le bon contexte, avec sa provenance et ses limites.
-->
<!-- PREUVE LOCALE : manuel.md et plan.md -->
<!-- VISUEL : titre minimal, fond noir, une flèche verticale très fine -->

---

# 1 · Le problème CDO

- Un corpus IA mélange droit, guidance, standards, recherche et incidents.
- Un PDF est lisible par un humain, mais instable pour la citation et le retrieval.
- Un LLM sans garde-fou peut confondre une recommandation et une obligation.
- Le besoin réel : **retrouver une connaissance applicable, prouvée et bornée**.

> Question directrice : pouvons-nous expliquer pourquoi une information a été
> donnée, d’où elle vient et ce qui reste incertain ?

<div class="proof">Preuve locale : sources/, state/source_manifest.jsonl, AGENTS.md</div>

<!-- NOTE ORATEUR
Insister sur le risque de gouvernance : le problème n'est pas seulement l'hallucination. C'est aussi la perte de juridiction, de date, d'autorité et de responsabilité lorsque tout devient du texte contextuel indistinct.
-->
<!-- VISUEL : avant/après ; à gauche « corpus non gouverné », à droite « chaîne evidence-first » -->

---

# 2 · L’architecture de confiance

```text
ORIGINAUX IMMUTABLES
        ↓  hash + identifiant
INGEST MARKDOWN VALIDÉ
        ↓  locator + lignée
PREUVES REVUES
        ↓  evidence-lock
PROPOSITION FUTURE-VAULT
        ↓  revue indépendante
APPROBATION HUMAINE DU SHA
        ↓  assembleur déterministe
VAULT · GRAPHE · QUESTIONS · CANVAS
        ↓
RETRIEVAL LOCAL → CONTEXTE CITÉ
```

- Les transformations sont séparées des décisions.
- Le LLM propose ; le validateur et l’humain disposent.
- L’export OKF et le kit Git sont des vues dérivées, jamais un second vault.

<div class="proof">Preuve locale : WORKSHOP.md, plan.md, src/gov360_brain/workshop.py</div>

<!-- NOTE ORATEUR
Cette diapositive est le modèle mental central. Une flèche signifie un contrat, pas une simple copie de texte.
-->
<!-- VISUEL : remplacer le bloc texte par un diagramme en flèches horizontales si le support le permet -->

---

# 3 · Le corpus : 54 fichiers physiques, 47 sources logiques

| Famille | Rôle | Formats / exemples |
| --- | --- | --- |
| EDPB, GDPR, AI Act | droit et guidance européenne | PDF |
| NIST, ISO, OWASP, CoSAI | cadres et contrôles | PDF |
| MITRE ATLAS | menaces, mitigations, incidents | YAML, JSON STIX, XLSX |
| Model risk, ORX, METR | risques et recherche | PDF, Markdown |
| Responsible AI | transparence et contexte | PDF |

- 43 PDF, 1 JSON, 1 XLSX, 1 YAML, 2 Markdown, 6 métadonnées Windows.
- 46 sources `READY_FOR_LLM`, 1 source en quarantaine.
- 46 dossiers `ingest/SRC-XXXX/` validés.

<div class="proof">Preuve locale : sources/, state/source_manifest.jsonl, ingest/*/document.json</div>

<!-- NOTE ORATEUR
Expliquer la différence entre fichier physique et source gouvernée. Plusieurs fichiers peuvent appartenir à une même source logique ; c'est le manifeste qui donne l'identité stable.
-->
<!-- VISUEL : matrice de logos textuels EDPB / EU / NIST / ISO / OWASP / CoSAI / ATLAS -->

---

# 4 · Du document à l’unité Markdown

```text
sources/05_EU_AI_Legislation/<document>.pdf
                 ↓ adaptateur PDF
ingest/SRC-0043/
├── document.json
└── units/
    ├── p0001.md  → Page 1
    ├── p0002.md  → Page 2
    └── ...
```

Une unité porte :

- `source_id` et `source_sha256` ;
- `locator` (`Page 1`, ligne, feuille, objet STIX) ;
- `content_sha256` et `file_sha256` ;
- adaptateur, mode d’extraction et revue visuelle ;
- warnings et métadonnées de lignée.

<div class="proof">Preuve locale : ingest/SRC-0043/document.json et ingest/SRC-0043/units/p0001.md</div>

<!-- NOTE ORATEUR
Le Markdown n'est pas une copie éditoriale : c'est une unité adressable et vérifiable. Il permet au pipeline de savoir exactement quel fragment a soutenu une note.
-->
<!-- VISUEL : zoom d’un frontmatter avec trois callouts : source, locator, hashes -->

---

# 5 · Quatre contrôles que l’on ne confond pas

| Contrôle | Ce qu’il établit | Ce qu’il n’établit pas |
| --- | --- | --- |
| Intégrité | le fichier correspond à son hash | fidélité sémantique |
| Fidélité | l’extrait représente suffisamment l’original | autorité juridique |
| Autorité | binding, guidance, framework ou research | publication |
| Approbation | l’humain accepte un candidat exact | vérité universelle |

- Une extraction réussie n’est pas une preuve juridique.
- Une source `GUIDANCE` ne devient pas une obligation.
- Une note active peut rester inéligible à l’assistance si sa preuve est non résolue.

<div class="proof">Preuve locale : AGENTS.md, config/schemas/brain-evidence.schema.json</div>

<!-- NOTE ORATEUR
C'est le contrôle de qualité le plus important à expliquer au CDO : chaque dimension a une décision et un responsable différents.
-->
<!-- VISUEL : quatre cartes alignées, chacune avec un cadenas différent -->

---

# 6 · Preuve, locator et evidence-lock

```json
{
  "source_id": "SRC-0002",
  "source_sha256": "…",
  "unit_path": "ingest/SRC-0002/units/p0008.md",
  "unit_sha256": "…",
  "unit_file_sha256": "…",
  "locator": "Page 8",
  "authority": "GUIDANCE"
}
```

Une section publiée ajoute une liaison exacte :

```text
note_id + note_sha256
section_id + section_sha256
        ↓
evidence_refs + modality
```

- Toute modification de la section invalide sa liaison précédente.
- Les preuves sont réutilisables sans recopier les PDF.
- Les obligations ne sont permises qu’avec une preuve `BINDING` revue.

<div class="proof">Preuve locale : state/workshop/evidence-library/, config/schemas/brain-evidence.schema.json</div>

<!-- NOTE ORATEUR
Donner l'analogie avec une chaîne de custody : le locator est l'adresse, les hashes sont l'empreinte, l'evidence-lock est la frontière de ce qui est autorisé dans une release.
-->
<!-- VISUEL : schéma note → section → evidence_ref → unité → source -->

---

# 7 · Le vault Obsidian : connaissance canonique

- **Knowledge** : un concept ou un sujet principal, avec applicabilité et limites.
- **Question** : une intention atomique, FR/EN, topic stable et dépendances acycliques.
- **Index** : navigation par domaine, sans nouvelle conclusion normative.
- Les wikilinks expriment des relations sémantiques utiles.
- Le Canvas et le registre sont reconstruits depuis les questions Markdown.

Exemple de note :

```yaml
id: ai-lifecycle
type: knowledge
domains: [AI, PROCESS, MODEL_RISK]
status: active
evidence_sources: [AI_NICE_TO_KNOW]
```

<div class="proof">Preuve locale : brain wiki/SCHEMA.md, config/schemas/brain-note.schema.json</div>

<!-- NOTE ORATEUR
Obsidian est l'interface humaine. Le Brain ne remplace pas le vault : il compile sa structure pour le retrieval et les exports.
-->
<!-- VISUEL : capture contrôlée d’une note Obsidian, avec un lien vers une note voisine -->

---

# 8 · Le harness : rendre l’agent gouvernable

```text
CONTRAT → PÉRIMÈTRE → AGENT SPÉCIALISÉ → RECEIPT / OVERLAY
                              ↓
                     VALIDATION DÉTERMINISTE
                              ↓
                     REVUE INDÉPENDANTE
                              ↓
                 APPROBATION HUMAINE DU HASH
                              ↓
                    ASSEMBLAGE ATOMIQUE
```

Le harness impose :

- lecture préalable de `AGENTS.md`, `WORKSHOP.md`, `ROADMAP.md` et `SCHEMA.md` ;
- sorties assignées et permissions minimales ;
- séparation workers / reviewers / assembleur ;
- aucun accès d’écriture à `sources/` ou `ingest/` ;
- aucun appel distant implicite ;
- publication impossible sans manifest, revue et approval concordants.

<div class="proof">Preuve locale : AGENTS.md, opencode.json, .codex/config.toml, WORKSHOP.md</div>

<!-- NOTE ORATEUR
Le harness est la réponse à « comment contrôlez-vous l'agent ? ». On ne tente pas de rendre le modèle parfait ; on rend ses effets bornés, inspectables et réversibles.
-->
<!-- VISUEL : pipeline avec zones colorées « agent », « contrôle », « humain » -->

---

# 9 · Les rôles : une séparation par responsabilité

| Rôle | Produit | Limite principale |
| --- | --- | --- |
| `source-extractor` | candidats avec locators | ne lit pas les originaux |
| `evidence-auditor` | audit et evidence-lock | ne publie pas |
| `knowledge-architect` | concepts, relations, limites | ne crée pas de preuve |
| `questionnaire-curator` | questions FR/EN | ne stocke pas de réponses |
| `questionnaire-reviewer` | équivalence et dépendances | ne publie pas |
| `vault-reviewer` | schéma, liens, cohérence | ne modifie pas l’overlay |
| `domain-builder` | overlay `future-vault/` | ne touche pas au vault actif |
| `release-reviewer` | revue consolidée | ne valide pas à la place de l’humain |
| `git-helper` | kit local allowlisté | ne commit, tag ni push |

<div class="proof">Preuve locale : prompts/roles/, .opencode/agents/, .codex/agents/</div>

<!-- NOTE ORATEUR
La valeur n'est pas le nombre d'agents. C'est le fait que chaque rôle a une décision claire, une sortie typée et une zone d’écriture limitée.
-->
<!-- VISUEL : swimlane extraction → synthesis → review → release -->

---

# 10 · Skills, fournisseurs et permissions

- Les prompts canoniques sont indépendants du fournisseur.
- `.opencode/agents/` et `.codex/agents/` sont des adaptateurs.
- Les skills couvrent ingestion, PDF, synthèse, questionnaire, graphe et audit.
- OpenCode utilise actuellement `openrouter/deepseek/deepseek-v4-flash-0731` par défaut.
- Routage demandé : ZDR et `data_collection: deny`.

```text
Prompts métier → wrappers OpenCode / Codex → session locale
                         ↓
                 permissions du dépôt
```

<div class="proof">Preuve locale : opencode.json, docs/opencode-setup.md, .agents/skills/</div>

<!-- NOTE ORATEUR
Le changement de modèle ne doit pas changer les contrats métier. Les opérations déterministes n’appellent pas de LLM ; le modèle est réservé aux travaux qui nécessitent une synthèse ou une revue.
-->
<!-- VISUEL : matrice fournisseur / prompt / permission / sortie -->

---

# 11 · Fast lane et strict lane

### Fast lane

```text
preuves déjà revues → domain-builder → validation → release-reviewer
                                  → approval → integrate --apply
```

### Strict lane

```text
unités validées → extraction → audit des preuves → evidence-lock
                 → construction → revue indépendante → approval
                 → integrate --apply
```

Le strict lane est obligatoire pour :

- nouvelle preuve ;
- obligation ou interdiction ;
- interprétation juridique ;
- changement de contrat ;
- supersession.

<div class="proof">Preuve locale : WORKSHOP.md §§ Deux circuits de release et Règles de release</div>

<!-- NOTE ORATEUR
Les lots récents lifecycle/change, AI literacy et sustainability/societal impact ont suivi le strict lane. Le hash de candidat est présenté avant publication.
-->
<!-- VISUEL : comparaison en deux colonnes, avec l’étape supplémentaire d’audit dans strict -->

---

# 12 · Le Brain local : compiler le vault

```text
Markdown actif
   ├── sections adressables
   ├── wikilinks → graphe
   ├── questions → registre + Canvas
   └── evidence bindings → index de preuves
                         ↓
              recherche locale par sections
                         ↓
                paquet de contexte cité
```

- `catalogue.json` : notes et sections.
- `evidence-index.json` : éligibilité et liaisons.
- `coverage-matrix.json` : 15 piliers × 10 critères.
- `navigation.md` : navigation dérivée.
- `reconciliation.json` et `report.md` : diagnostics.

<div class="proof">Preuve locale : state/derived/brain/ et src/gov360_brain/brain/</div>

<!-- NOTE ORATEUR
Le Brain est une compilation locale. Le vault est la source humaine ; le catalogue et les index sont des artefacts reproductibles, pas des contenus édités à la main.
-->
<!-- VISUEL : arbre des dérivés sortant de brain wiki/ -->

---

# 13 · Retrieval : du besoin au contexte cité

Commande de démonstration :

```sh
uv run gov360 brain context \
  "lifecycle change rollback human oversight" \
  --token-budget 6000
```

Le paquet retourne :

- les sections retenues ;
- les notes et liens utiles ;
- les evidence references ;
- les limites, conflits et exclusions ;
- un budget de contexte borné.

Deux modes :

- `assistance` : preuves résolues et revues uniquement ;
- `research` : matériau explicitement non approuvé, jamais en repli silencieux.

<div class="proof">Preuve locale : WORKSHOP.md § Construction et exploitation du Brain local</div>

<!-- NOTE ORATEUR
Le retrieval ne cherche pas à renvoyer « tout ce qui ressemble ». Il filtre d'abord l'éligibilité de la preuve, puis classe les sections dans un budget utile à l'agent.
-->
<!-- VISUEL : question → filtre autorité/date/domaine → top sections → contexte -->

---

# 14 · Mesurer le retrieval sans confondre les objectifs

Suite actuelle : **45 scénarios**.

- 30 recherches positives ;
- 15 cas négatifs, lacunes ou exclusions ;
- 30/30 positifs éligibles ;
- 15/15 négatifs réussis ;
- checkpoint historique : `recall@5 = 0.9667` avec `eval-11-fr` à améliorer ;
- checkpoint courant après l’expansion bilingue de vocabulaire : `recall@5 = 1.0` ;
- cas à améliorer : `eval-11-fr`.

`recall@5` signifie : une note attendue apparaît-elle dans les cinq premiers
IDs de notes distincts retournés pour un scénario répondable ?

<div class="proof">Preuve locale : config/brain-evaluation.json, src/gov360_brain/brain/retrieval.py</div>

<!-- NOTE ORATEUR
Le score mesure la retrouvabilité, pas l'autorité ni la complétude métier. Le seuil configuré est 90 %, mais on conserve le cas manquant comme backlog explicite.
-->
<!-- VISUEL : 30 points verts, 1 point orange, 15 points verts négatifs -->

---

# 15 · Questionnaire et Canvas

- 50 questions Markdown canoniques.
- Questions FR/EN à intention unique.
- `topic` stable pour éviter les doublons.
- `depends_on` acyclique pour les modules conditionnels.
- Registre JSONL et Canvas reconstruits automatiquement.

```text
question.md → question-registry.jsonl → Risk analysis questionnaire.canvas
       ↑                                      ↓
       └──────────── Obsidian / lecture humaine
```

<div class="proof">Preuve locale : brain wiki/questions/, state/derived/question-registry.jsonl, brain wiki/Risk analysis questionnaire.canvas</div>

<!-- NOTE ORATEUR
Le dépôt publie les questions ; il n'exécute pas l'entretien et ne stocke pas les réponses du projet. Cette frontière protège le Brain d'une dérive vers un système de scoring.
-->
<!-- VISUEL : une question bilingue reliée à son topic et à sa dépendance -->

---

# 16 · Démonstration locale en 5 minutes

| Temps | Action | Message |
| ---: | --- | --- |
| 0:00–0:45 | `brain status` | état reproductible, aucun appel LLM |
| 0:45–1:45 | note Obsidian + wikilinks | connaissance lisible et reliée |
| 1:45–2:30 | question + Canvas | Markdown canonique, Canvas dérivé |
| 2:30–3:45 | `brain context` | paquet local cité et borné |
| 3:45–4:30 | `brain evaluate` | retrieval mesuré, cas manquant visible |
| 4:30–5:00 | evidence-lock + approval | publication déterministe et humaine |

```sh
uv run gov360 brain status
uv run gov360 brain validate
uv run gov360 brain build --check
uv run gov360 brain evaluate
```

<div class="proof">Preuve locale : manuel.md et commandes WORKSHOP.md</div>

<!-- NOTE ORATEUR
Ne pas faire défiler sources/ ni ingest/ en détail. Montrer leur structure et ouvrir une unité seulement si la question porte sur la provenance.
-->
<!-- VISUEL : storyboard avec six scènes OBS -->

---

# 17 · Vidéo : le Brain dans Obsidian

La capture prévue doit montrer le vault Obsidian : graphe, note `ai-lifecycle`,
question `gov-009-lifecycle-release-and-rollback` et Canvas de questionnaire.
Le fichier `dist/presentation/governance-brain-demo.gif` est absent du dossier
actuel : la vidéo reste à produire et à vérifier localement.

### Séquence proposée (31 secondes)

1. graphe du vault (0–5 s) ;
2. note knowledge (5–12 s) ;
3. question bilingue (12–19 s) ;
4. Canvas (19–26 s) ;
5. retour au graphe (26–31 s).

### Règles d’enregistrement

- 1920×1080, 30 fps, capture de fenêtre ;
- aucun secret, chemin personnel ou contenu non redistribuable ;
- police terminal 18–22 px ;
- sortie MP4/MKV dans un dossier de présentation séparé si le support l’exige ;
- insérer la vidéo dans une diapositive avec une image de secours.

<div class="proof">Preuve attendue : capture Obsidian locale vérifiée ; non livrée à ce checkpoint</div>

<!-- NOTE ORATEUR
La vidéo montre le workflow ; elle ne devient pas une nouvelle source du Brain. Pour une diffusion externe, utiliser une copie avec IDs, hashes et fixtures synthétiques.
-->
<!-- VISUEL : timeline 0–31 secondes avec les cinq vues Obsidian -->

---

# 18 · État actuel : ce qui est construit

```text
47 sources logiques · 2 863 unités Markdown
177 notes · 50 questions · 11 indexes
971 sections · 514 sections avec preuves revues
170 notes publication-verified · 0 orphan
```

- Validation technique : `valid: true`.
- Findings d’évidence actuels : `0`.
- Appels LLM dans les builds déterministes : `0`.
- Les lots ATLAS, droit, sécurité, model risk, supply chain, lifecycle,
  literacy et societal impact ont alimenté le vault.

<div class="proof">Preuve locale : uv run gov360 brain status</div>

<!-- NOTE ORATEUR
Ces chiffres décrivent l'état technique et de provenance observé. Ils ne sont pas un pourcentage de conformité ni une certification.
-->
<!-- VISUEL : quatre compteurs, pas de graphique trompeur de « complétude » -->

---

# 19 · Limites et travaux ouverts

- La matrice **15 × 10 contient encore 150 cellules `UNASSESSED`**.
- Trois piliers récemment intégrés doivent encore être répercutés dans le registre de couverture.
- `eval-11-fr` est corrigé par le vocabulaire bilingue ; le checkpoint courant
  est `recall@5 = 1.0` (le résultat historique `0.9667` reste documenté).
- Les avertissements historiques de provenance restent explicitement visibles.
- Une source revue n’est pas une garantie d’exhaustivité juridique.
- Le partage de contenus tiers dépend de leurs droits de redistribution.

<div class="proof">Preuve locale : state/derived/brain/coverage-matrix.json, ROADMAP.md, brain evaluate</div>

<!-- NOTE ORATEUR
Présenter les limites comme une capacité de gouvernance : le système sait dire ce qu'il ne sait pas encore. Une cellule non évaluée reste non évaluée.
-->
<!-- VISUEL : backlog en trois colonnes « couverture », « retrieval », « publication » -->

---

# 20 · Ce qui est garanti / ce qui ne l’est pas

| Garanti par le dispositif | Non garanti automatiquement |
| --- | --- |
| provenance, hashes et locators | exhaustivité juridique |
| séparation des autorités | vérité de toute interprétation |
| permissions et zones d’écriture | absence de tout biais documentaire |
| revue indépendante et approval hashée | décision de gouvernance |
| dérivés reproductibles | score global de conformité |
| absence de modification de `sources/` | exactitude future sans maintenance |

> Le Brain gouverne le contexte ; il ne remplace ni le décideur ni la revue spécialisée.

<div class="proof">Preuve locale : AGENTS.md, WORKSHOP.md, plan.md</div>

<!-- NOTE ORATEUR
Cette diapositive doit rester à l'écran pendant les questions. Elle évite la survente du projet.
-->
<!-- VISUEL : deux colonnes équilibrées, vert pâle à gauche, ambre à droite -->

---

# 21 · Roadmap et décisions CDO

### Prochaines étapes

1. mettre à jour le registre des trois piliers récemment intégrés ;
2. évaluer les 150 cellules de couverture critère par critère ;
3. améliorer ou documenter `eval-11-fr` ;
4. réconcilier les warnings historiques ;
5. préparer le kit local avec `git_helper` ;
6. décider séparément d’une publication distante.

### Décisions demandées

- confirmer le Brain comme couche de contexte gouverné ;
- confirmer la priorité à la preuve et à la couverture, pas au volume ;
- nommer le responsable du registre et de la maintenance ;
- valider la politique de revue des changements réglementaires.

<div class="proof">Preuve locale : ROADMAP.md, state/workshop/coverage/coverage-register.json</div>

<!-- NOTE ORATEUR
La demande finale n'est pas « approuver toutes les notes ». C'est valider le modèle opératoire, la priorité de maintenance et le prochain lot contrôlé.
-->
<!-- VISUEL : roadmap en quatre étapes avec un marqueur « maintenant » -->

---

<!-- _class: lead -->
# Conclusion

## Une connaissance gouvernée, un contexte traçable, une décision humaine

> Nous n’avons pas demandé à un modèle de croire un corpus.
>
> Nous avons construit une chaîne où chaque transformation est vérifiable,
> chaque affirmation publiée garde sa preuve et le modèle ne reçoit que le
> contexte pertinent.

<div class="muted">Questions · démonstration · décisions de maintenance</div>

<!-- NOTE ORATEUR
Terminer par la phrase de valeur : la prochaine accélération vient de la fermeture des cellules de couverture et de la maintenance des preuves, pas de la génération incontrôlée de texte.
-->
<!-- PREUVE LOCALE : plan.md, manuel.md et rapports de validation datés -->
