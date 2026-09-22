# Manuel de construction du Governance Brain

Ce manuel explique comment le dépôt transforme des documents de gouvernance en
une base de connaissance Obsidian contrôlée, traçable et utilisable pour le
context engineering d'un agent. Il décrit le contrat actif du projet. En cas de
contradiction, l'ordre d'autorité est le suivant : `AGENTS.md`, `ROADMAP.md`,
`WORKSHOP.md`, `brain wiki/SCHEMA.md`, puis ce manuel.

## 1. Ce que nous construisons

Le Governance Brain est un ensemble de notes Markdown reliées, de questions
bilingues et d'index de navigation. Il poursuit deux objectifs complémentaires :

1. fournir à un système aval un contexte de gouvernance précis, structuré et
   limité à ce qui est utile pour la tâche en cours ;
2. maintenir un niveau élevé de qualité documentaire grâce à la provenance, aux
   localisateurs, à la revue de l'autorité et à l'approbation humaine.

La séparation des responsabilités est essentielle :

- **Obsidian organise** les connaissances revues et leurs relations ;
- **le Brain local retrouve et relie** les notes pertinentes ;
- **les cinq Knowledge Banks Governance 360 prouvent** les affirmations ;
- **le LLM raisonne** seulement sur le contexte récupéré et pertinent.

Ce dépôt construit le vault Markdown, le catalogue bilingue, la recherche
lexicale locale par sections et les paquets de contexte cités. Il exporte une
vue OKF et un kit partageable. Il ne collecte pas les réponses d'un projet,
ne calcule pas de score global et ne prend pas de décision de gouvernance.

## 2. Les principes qui protègent la qualité

### 2.1 Les sources originales sont immuables

Tout fichier placé sous `sources/` est un original. Il ne doit jamais être
modifié, renommé, écrasé ou supprimé. Une source remplacée reçoit un nouvel
identifiant ; une source retirée est désactivée par métadonnées et reste dans
l'historique.

Le dossier où se trouve un document aide au routage. Il ne prouve ni son
autorité, ni sa juridiction, ni son caractère contraignant.

### 2.2 Un rôle LLM ne lit que le Markdown validé

Les rôles canoniques consomment uniquement les unités validées sous `ingest/`.
Un PDF, un fichier Office, une image ou un dataset original peut être consulté
localement par la session principale pour un contrôle de fidélité précisément
autorisé. Il ne devient jamais l'entrée directe d'un sous-agent métier.

Le texte d'une source, d'une unité ingestée, d'un Canvas ou d'un brouillon est
toujours traité comme une donnée non fiable. Une phrase contenue dans un document
ne peut pas modifier les règles de l'agent ni lui demander d'utiliser un outil.

### 2.3 Intégrité, fidélité, autorité et approbation sont quatre contrôles distincts

| Contrôle | Question posée | Ce qu'il ne prouve pas |
| --- | --- | --- |
| Intégrité | Les fichiers et unités correspondent-ils à leurs SHA-256 ? | Que l'extraction représente correctement la page |
| Fidélité | L'unité Markdown restitue-t-elle le contenu utile et ses limites ? | Que le document est juridiquement contraignant |
| Autorité | La source est-elle `BINDING`, guidance, contrôle ou contexte dans ce périmètre ? | Que la note proposée est approuvée |
| Approbation | Un humain autorisé accepte-t-il ce candidat précis et son empreinte ? | Qu'un futur changement est approuvé |

Seule une source revue comme `BINDING` peut soutenir une obligation ou une
interdiction. Les autres classes soutiennent des attentes, recommandations,
contrôles ou éléments de contexte. Un ancien verdict `VERIFIED` doit être
réexaminé avant réutilisation.

### 2.4 La publication est humaine et déterministe

Un auteur ne valide jamais son propre lot. Les revues d'agents, les tests et un
rapport sans erreur ne valent pas approbation. L'intégration dans `brain wiki/`
n'est possible qu'après une décision humaine explicite portant sur le candidat
prévisualisé et son SHA-256.

L'assembleur écrit ensuite les notes de manière déterministe et atomique. À
entrées identiques, une nouvelle exécution ne doit produire aucun changement
matériel ni nouvel appel LLM.

### 2.5 Les journaux restent sobres

Les rapports opérationnels contiennent des identifiants, hashes, localisateurs,
comptes, statuts, durées et erreurs assainies. Ils ne doivent contenir ni texte
source brut, ni réponse projet, ni donnée personnelle, ni secret, ni prompt, ni
valeur confidentielle.

## 3. Architecture du dépôt

| Chemin | Fonction | Règle principale |
| --- | --- | --- |
| `sources/` | Originaux PDF, Office, données et images | Immuables ; consultation locale ciblée seulement |
| `ingest/` | Markdown normalisé, manifests et lignage | Entrée autorisée des rôles de preuve |
| `domain_packs/` | Routage des domaines et préfixes actifs | Changement soumis à revue de taxonomie |
| `brain wiki/` | Vault Obsidian publié | Contient seulement des notes actives revues |
| `brain wiki/indexes/` | Navigation par domaine ou usage | Liens utiles, sans nouvelle conclusion normative |
| `brain wiki/questions/` | Questions Markdown canoniques | Catalogue publié, sans réponses projet |
| `state/workshop/` | Couverture, brouillons, propositions et revues | Zone de travail avant publication |
| `state/workshop/proposals/<lot>/future-vault/` | Aperçu exact des futurs fichiers du vault | Jamais considéré comme publié |
| `state/workshop/coverage/` | État d'avancement des quinze piliers | Piloté selon la Definition of Done |
| `state/derived/` | Registres reproductibles générés depuis le vault actif | Jamais édité comme contenu canonique |
| `prompts/roles/` | Prompts canoniques indépendants du fournisseur | Aucun nom de modèle codé ici |
| `.opencode/agents/` | Adaptateurs et permissions OpenCode | Couche fournisseur, sous-agents en lecture seule |
| `.codex/agents/` | Adaptateurs de rôles Codex | Référencent les prompts canoniques |
| `.agents/skills/` | Procédures spécialisées réutilisables | Ne remplacent ni revue ni approbation |
| `config/schemas/` | Contrats JSON Schema publics | Évolution additive versionnée ; rupture migrée |
| `config/profiles/` | Politiques réseau et LLM du pipeline | Aucun réseau implicite |
| `src/gov360_brain/` | Adaptateurs, orchestration, validation et assemblage | Transformations déterministes |
| `tests/` | Fixtures synthétiques et contrôles du contrat | Aucun contenu confidentiel |

Les chemins sont relatifs à la racine du dépôt. Le nom `brain wiki/` contient un
espace et doit toujours être cité en shell. Le code Python utilise `pathlib.Path`
plutôt qu'une concaténation de commandes ou un chemin propre à une machine.

## 4. Le contrat des notes du vault

Le contrat actif est défini par `brain wiki/SCHEMA.md` et validé avec
`config/schemas/brain-note.schema.json`. Les anciens schémas v1 ne publient pas
dans le vault actif.

### 4.1 Frontmatter commun

Chaque note active commence par un frontmatter YAML contenant :

```yaml
---
id: human-oversight
title: Human Oversight
type: knowledge
domains: [HUMAN_OVERSIGHT_RESPONSIBLE_AI]
status: active
aliases: []
tags: [oversight]
evidence_sources: [AI_ACT]
---
```

- `id` est unique, stable et en kebab-case ;
- le nom du fichier correspond à l'ID, sauf `README.md` et `SCHEMA.md` ;
- `domains` contient au moins un ID enregistré dans
  `config/brain-domains.json` ;
- `status` vaut `active` ou `deprecated` dans le vault ;
- `aliases` et `tags` sont des listes de chaînes ;
- `evidence_sources` route vers une ou plusieurs Knowledge Banks autorisées.

`evidence_sources` ne constitue pas une preuve. Les références visibles dans le
corps de la note et la revue liée au lot restent nécessaires.

Les seuls types actifs sont `knowledge`, `question` et `index`. Les catégories
historiques comme `rule` ou `guidance` ne sont pas des types de note actifs : la
nature normative est expliquée dans le contenu et dans les preuves revues.

### 4.2 Notes `knowledge`

Une note décrit un concept ou sujet principal. Elle est rédigée en anglais et
peut comporter, quand ils sont utiles :

- `Summary` ;
- `Applicability` ;
- `Governance considerations` ;
- `Related concepts` ;
- `Source references`.

Les sections vides sont omises. Chaque affirmation significative conserve son
périmètre, sa juridiction, sa date d'effet, ses exceptions, ses incertitudes et
ses localisateurs. Une note nécessite normalement deux sources indépendantes.
Une source autoritaire unique suffit lorsqu'elle définit explicitement le sujet,
à condition de documenter cette limite dans la revue.

### 4.3 Notes `question`

Une question ajoute les champs suivants :

```yaml
topic: human-oversight
priority: high
applies_to: AI
answer_type: choice
depends_on:
  question_id: core-003-ai-system-determination
  equals: ai-system
question_fr: "..."
question_en: "..."
options:
  - value: documented
    label_fr: "Documenté"
    label_en: "Documented"
  - value: not-documented
    label_fr: "Non documenté"
    label_en: "Not documented"
```

Chaque question :

- mesure un seul intent ;
- possède un texte français et anglais de sens équivalent ;
- utilise un `topic` stable partagé par les questions portant sur la même
  information ;
- choisit `boolean`, `text` ou `choice` comme `answer_type` ;
- fournit au moins deux options bilingues aux valeurs stables pour `choice` ;
- utilise `depends_on: null` ou exactement `question_id` et `equals` ;
- appartient à un graphe de dépendances sans cycle.

Le catalogue est conçu comme un noyau commun, puis des modules conditionnels.
Les notes expriment la sélection possible ; elles n'implémentent ni moteur
d'entretien, ni stockage de réponses, ni scoring.

### 4.4 Le Question Registry

La source canonique actuelle du registre est l'ensemble des notes Markdown
`question` présentes dans le vault. Toute création ou mise à jour est comparée
au catalogue complet selon le texte, le `topic`, l'intent de décision, les
preuves attendues et la sémantique des réponses.

Une correction de formulation qui conserve l'intent peut être un `UPDATE` avec
le même ID. Si l'intent ou la sémantique change, il faut un nouvel ID et une
proposition `SUPERSEDE`, puis préserver l'historique après approbation.

Le registre actif dérivé est maintenant
`state/derived/question-registry.jsonl`. Il est reconstruit avec le Canvas par
`build-derived` et après chaque intégration approuvée. Le fichier
`state/question_registry.jsonl` et les outils associés au publisher v1 restent
historiques lorsqu'ils entrent en conflit avec le contrat Markdown actif.

### 4.5 Notes `index` et liens Obsidian

Un index facilite la navigation. Il ne crée aucune conclusion réglementaire.
Les liens `[[identifiant-stable]]` sont ajoutés seulement lorsqu'une relation
sémantique existe. Toute cible doit déjà exister ou faire partie du même candidat
revu. Une cible absente bloque le lot ; on ne crée jamais une note vide pour
faire disparaître une erreur de lien.

Le rangement physique existant est préservé. La navigation par domaine se fait
avec les notes sous `brain wiki/indexes/`, sans déplacer en masse les anciennes
notes.

## 5. La chaîne de construction, de bout en bout

```text
preuves déjà revues -> release FAST -> domain-builder -> release-reviewer
nouvelle preuve / droit / contrat -> release STRICT -> extraction + audit
les deux circuits -> approbation humaine unique liée au SHA-256
  -> intégration déterministe
  -> registre + Canvas reconstruits automatiquement
  -> brain wiki/ validé
```

Le manifeste v3 décide du circuit. Le validateur force `strict` pour toute
nouvelle preuve, obligation, interdiction, interprétation juridique,
modification de contrat ou supersession. Une release ordinaire accepte au plus
trois shards, 30 notes de connaissance, 50 questions et 120 références. Les
étapes documentaires détaillées ci-dessous restent obligatoires pour le circuit
strict ; le circuit rapide commence directement à l'étape de construction.

### Étape 0 — Préparer l'environnement

Depuis la racine du dépôt :

```sh
uv sync --frozen --extra dev --extra data
uv run python --version
uv run pytest -q
uv run --offline --no-sync python -m gov360_brain.workshop validate
```

`uv` recrée l'environnement à partir de `.python-version`, `pyproject.toml` et
`uv.lock`. Un ancien environnement virtuel Windows ne doit pas être réutilisé
sous Ubuntu.

### Étape 1 — Inventorier une source

```sh
uv run gov360 status
uv run gov360 inventory --domain legal-regulatory
```

Le catalogue calcule le SHA-256, vérifie que le chemin reste sous `sources/` et
contrôle la signature réelle du format. Une archive, un exécutable, un lien
symbolique, un document corrompu ou protégé est mis en quarantaine plutôt que
traité approximativement.

### Étape 2 — Normaliser en Markdown

```sh
uv run gov360 run --domain legal-regulatory --profile no-llm
uv run gov360 validate-ingest --domain legal-regulatory
```

L'adaptateur produit un `document.json`, un aperçu et des unités Markdown
adressables par page, section, diapositive, feuille/plage, lignes ou chemin de
donnée. Chaque unité conserve le `source_id`, le hash source, son propre hash,
le localisateur, le mode d'extraction et les avertissements.

L'écriture passe par un répertoire temporaire, la validation des comptes et
checksums, puis un remplacement atomique. La commande s'arrête à la frontière
Markdown et ne fait aucun appel LLM avec le profil `no-llm`.

### Étape 3 — Contrôler la qualité technique

```sh
uv run --offline --no-sync python -m gov360_brain.workshop quality
```

Ce contrôle détecte notamment les hashes incohérents, le texte anormalement
court, les caractères de remplacement, les avertissements d'extraction et les
pages nécessitant une revue visuelle. Le rapport contient des métadonnées et
statuts, jamais le texte brut.

### Étape 4 — Contrôler localement la fidélité

Les pages utilisées, toutes les pages signalées et un échantillon déterministe
sont comparés aux originaux. Pour un PDF, le texte natif reste prioritaire ; un
rendu Poppler ou un OCR local est utilisé seulement pour une page scannée,
dégradée, tabulaire ou dépendante de sa mise en page.

La revue consigne l'ID source, les hashes, le localisateur, la méthode, le
résultat et les limites. Une dépendance visuelle non résolue reste `UNCERTAIN`.
L'accès à l'original est ciblé, local, autorisé et réservé à cette vérification.

### Étape 5 — Qualifier l'autorité

Après une véritable revue juridique ou CDO :

```sh
uv run gov360 source classify SRC-0001 --normativity GUIDANCE --reviewer reviewer-id
```

Le classement ne modifie pas l'original et ne certifie pas automatiquement les
extraits. `BINDING` doit être choisi seulement lorsque l'autorité, le périmètre,
la juridiction et les dates le justifient.

### Étape 6 — Extraire puis auditer les preuves

Le `source-extractor` reçoit un ensemble borné d'unités validées. Il produit des
éléments atomiques avec localisateurs et hashes, couvre chaque unité assignée et
distingue les propos fidèles des interprétations.

L'`evidence-auditor` relit indépendamment les mêmes unités. Il attribue
`VERIFIED`, `REJECTED` ou `UNCERTAIN`, vérifie les qualificatifs, acteurs,
exceptions, seuils, dates et dépendances visuelles. Seuls les éléments
`VERIFIED` alimentent la synthèse.

### Étape 7 — Proposer la connaissance

Le `knowledge-architect` compare la preuve auditée au vault existant. Il préfère
mettre à jour une note au même intent plutôt que créer un doublon. Il propose
des opérations `ADD`, `UPDATE`, `SUPERSEDE` ou `NOOP`, des liens utiles et les
références exactes.

Les fichiers proposés vivent dans :

```text
state/workshop/proposals/<lot>/future-vault/
```

Le lot conserve aussi un manifeste, l'inventaire des preuves, les contrôles de
fidélité, les conflits, les rapports de validation et de revue, ainsi que le
fichier d'approbation humaine.

### Étape 8 — Proposer les questions

Le `questionnaire-curator` travaille après la revue de la connaissance. Il
recherche d'abord les doublons dans tout le catalogue, rédige les deux langues,
choisit le type de réponse, les options et les dépendances, puis relie la
question aux connaissances concernées.

Un Canvas Obsidian peut servir d'entrée éditoriale ou de vue dérivée. Chaque
nœud pertinent est réconcilié comme existant, proposé, doublon, catégorie,
action ou hors périmètre. Le Canvas ne crée ni preuve, ni exigence, ni
approbation. Markdown reste canonique.

### Étape 9 — Valider un ou plusieurs lots

```sh
uv run --offline --no-sync python -m gov360_brain.workshop validate \
  --proposal state/workshop/proposals/<lot>
```

Pour un candidat composé de plusieurs lots, répéter l'option dans l'ordre :

```sh
uv run --offline --no-sync python -m gov360_brain.workshop validate \
  --proposal state/workshop/proposals/<lot-1> \
  --proposal state/workshop/proposals/<lot-2>
```

Le validateur combine le vault actif et les overlays, puis contrôle le schéma,
les IDs, domaines, banques, liens, questions et dépendances. Deux lots proposant
le même chemin de sortie constituent une erreur.

### Étape 10 — Organiser la revue indépendante

Le `release-reviewer` examine le changement complet : intent unique,
équivalence FR/EN, doublons, topics, réponses, provenance, autorité, liens,
orphelins, conflits, index, dépendances, chemins et Canvas. Le résultat est
`BLOCKED` ou `READY_FOR_HUMAN_APPROVAL`. Dans le circuit strict, un audit de
preuve distinct précède cette revue. Les anciens `questionnaire-reviewer` et
`vault-reviewer` restent disponibles pour les propositions historiques.

Toute erreur ou criticité est corrigée dans la proposition, revalidée, puis
resoumise à une revue indépendante. Une disposition documentée permet de suivre
chaque ronde sans effacer les findings précédents.

### Étape 11 — Prévisualiser et approuver

```sh
uv run --offline --no-sync python -m gov360_brain.workshop integrate \
  --proposal state/workshop/proposals/<lot-1> \
  --proposal state/workshop/proposals/<lot-2>
```

Sans `--apply`, cette commande n'écrit pas dans le vault. Elle produit le nombre
de fichiers, le nombre de notes final, le nombre de fichiers qui changeraient et
le SHA-256 du candidat ordonné.

L'approbateur reçoit le diff concret, le rapport de revue, les résultats
de validation, les limites d'autorité et cette empreinte. Le fichier
`review/approval.md` doit contenir :

- `Status: APPROVED` ;
- l'identité de l'approbateur ;
- `Decision: APPROVED` ;
- le périmètre exact et l'empreinte ;
- la justification ;
- la date de décision.

Le manifeste de chaque proposition passe également à `APPROVED`. L'ordre doit
respecter `requires_proposals` : une dépendance est fournie avant le lot qui en
dépend.

### Étape 12 — Intégrer atomiquement

Après l'approbation :

```sh
uv run --offline --no-sync python -m gov360_brain.workshop integrate \
  --proposal state/workshop/proposals/<lot-1> \
  --proposal state/workshop/proposals/<lot-2> \
  --apply
```

L'assembleur vérifie les manifests, décisions, fichiers déclarés, actions,
dépendances, chemins et hashes. Il écrit les notes atomiquement, revalide le
vault actif, marque les manifests `INTEGRATED` et crée
`review/integration-report.json`. En cas d'échec, il restaure l'état antérieur.

### Étape 13 — Valider l'état publié

```sh
uv run --offline --no-sync python -m gov360_brain.workshop validate
uv run pytest -q
git status --short -- sources/
git diff --check
git diff --stat
```

Le résultat attendu est zéro erreur de validation, des tests réussis et aucun
changement causé par l'opération sous `sources/`. Un état préexistant doit être
signalé sans être modifié.

### Étape 14 — Maintenir dans le temps

Le programme est réévalué après une évolution juridique, le remplacement d'une
source, un incident matériel, un changement majeur de modèle ou système, ou à
la date de revue périodique. Les IDs, noms de fichiers, topics et préfixes sont
préservés. Toute évolution de taxonomie suit une proposition revue.

La Wave 5 doit produire un manifeste de release reproductible avec les hashes
de notes, la version de schéma, les domaines, le registre de questions, les
lacunes connues et les approbations.

## 6. Pilotage par roadmap et couverture

Le registre `state/workshop/coverage/coverage-register.json` suit quinze
piliers. Ses états sont :

```text
SOURCE_GAP -> EVIDENCE_READY -> PROPOSAL_READY -> HUMAN_REVIEW
           -> APPROVED -> COMPLETE
```

`COMPLETE` ne signifie pas « beaucoup de notes ». Le domaine doit couvrir ou
justifier explicitement dix axes : définitions, responsabilités, risques,
contrôles du cycle de vie, preuves attendues, métriques et incidents, exceptions
et juridictions, questions communes et conditionnelles, provenance, et index de
domaine.

Les vagues structurent le travail :

1. **Wave 0** : contrat, schéma, rôles, skills et atelier reproductible ;
2. **Wave 1** : noyau de qualification commun et routage des projets ;
3. **Wave 2** : socle européen AI Act, GDPR et droits fondamentaux ;
4. **Wave 3** : risque, sécurité, modèle, opérations et tiers ;
5. **Wave 4** : organisation, assurance, compétences et durabilité ;
6. **Wave 5** : release reproductible et maintenance continue.

Le CDO programme lead choisit une release de domaine cohérente à forte valeur selon
les obligations en vigueur, les droits et risques graves, la capacité de
routage, la disponibilité des preuves et la réutilisation entre projets.

## 7. Rôles et sous-agents

La session principale agit comme orchestrateur. Elle délimite la release, attribue
les entrées, matérialise les sorties proposées, exécute les contrôles et présente
le candidat à l'humain. Les wrappers de revue OpenCode sont en lecture seule.
Dans Codex, un worker peut écrire uniquement l'artefact ou le reçu qui lui est
explicitement attribué ; il ne modifie jamais le vault partagé, les index ou
l'approbation. Ces écritures partagées restent sérialisées par l'orchestrateur.

| Rôle | Responsabilité | Ne fait jamais |
| --- | --- | --- |
| `cdo-program-lead` | Sélectionne la prochaine release, son circuit et ses shards | Écrire connaissance, questions ou approbation |
| `source-extractor` | Extrait des preuves atomiques des unités assignées | Lire les originaux ou publier |
| `evidence-auditor` | Vérifie indépendamment preuve, locator et normativité | Faire confiance aux comptes de l'extracteur |
| `knowledge-architect` | Propose concepts, règles, relations et écarts | Combler une lacune par intuition ou approuver |
| `questionnaire-curator` | Propose les questions FR/EN et leur logique | Collecter des réponses ou calculer un score |
| `questionnaire-reviewer` | Revue indépendante du lot de questions | Modifier ou publier le lot |
| `vault-reviewer` | Revue finale de tous les artefacts | Accorder l'approbation humaine |
| `domain-builder` | Construit un shard rapide de notes et questions | Lire les sources ou modifier le vault actif |
| `release-reviewer` | Revue consolidée indépendante d'une release rapide | Modifier les notes, approuver ou intégrer |

L'auteur et le relecteur sont séparés. La parallélisation est utile entre
sources ou reçus immuables. Les mises à jour partagées, index et intégrations
sont sérialisées par l'orchestrateur déterministe afin d'éviter les collisions.

### Sous-agents dans Codex

`.codex/config.toml` enregistre les rôles spécialisés et accélérés avec un maximum de trois threads
concurrents par session. Chaque wrapper `.codex/agents/*.toml` renvoie au prompt
canonique correspondant dans `prompts/roles/`. Les wrappers ne dupliquent pas le
raisonnement métier et ne fixent pas de modèle fournisseur dans le prompt.

Codex peut reprendre le workflow lorsque les crédits OpenRouter sont épuisés.
Les mêmes séparations auteur/relecteur, limites d'accès et gates humains restent
applicables.

### Sous-agents dans OpenCode

Les wrappers `.opencode/agents/*.md` définissent le mode `subagent`, le modèle
et les permissions. Le `domain-builder` peut écrire uniquement dans l'overlay
de proposition assigné ; le `release-reviewer` uniquement dans son rapport. Ils
ne disposent ni du shell ni du web et ne peuvent pas déléguer. Aucun sous-agent de
gouvernance ne lit `sources/`. Les reviewers finaux n'accèdent pas non plus à
`ingest/` quand leur revue porte sur les rapports et preuves déjà audités.

Les commandes disponibles sont :

- `/brain-next` : sélectionner le prochain lot ;
- `/brain-build RELEASE` : construire les shards d'une release rapide ;
- `/brain-review RELEASE` : produire la revue consolidée indépendante ;
- `/brain-review-strict RELEASE` : revoir une release juridique ou probatoire avec DeepSeek Flash ;
- `/brain-release RELEASE` : prévisualiser puis intégrer une release déjà approuvée ;
- `/brain-canvas-watch` : surveiller les questions et régénérer les vues ;
- `/question-lot DOMAINE_OU_TOPIC` : proposer un lot de questions ;
- `/review-question-lot CHEMIN` : revoir indépendamment un lot de questions ;
- `/review-vault-lot CHEMIN_OU_ENSEMBLE` : effectuer la revue finale.

Ces commandes retournent des propositions ou findings. Elles ne publient rien.

## 8. Skills réutilisables

Les skills de `.agents/skills/` sont des procédures ciblées :

| Skill | Quand l'utiliser | Limite de sortie |
| --- | --- | --- |
| `source-ingestion` | Inventaire, format, normalisation et diagnostic ingest | S'arrête avant la synthèse |
| `pdf-evidence-extraction` | PDF difficiles, OCR local et triage visuel | Ne synthétise pas la connaissance |
| `knowledge-synthesis` | Notes et relations depuis preuves auditées | Propose, ne publie pas |
| `questionnaire-design` | Questions bilingues et dépendances | N'invente pas d'exigence |
| `obsidian-graph` | Assemblage de liens et index approuvés | Ne crée pas de connaissance sans preuve |
| `vault-audit` | Gate schéma, preuve, autorité, liens et approbation | Rapporte, n'approuve pas |

Un skill complète le prompt d'un rôle. Il ne remplace pas `AGENTS.md`, le
schéma, une revue indépendante ou la décision humaine.

## 9. Outils technologiques

### Socle local

- **Ubuntu/WSL** : environnement d'exécution quotidien ;
- **VS Codium** : édition du dépôt et exécution des commandes ;
- **Obsidian** : lecture humaine, navigation, liens et Canvas du vault ;
- **Git** : suivi des contrats, propositions et notes publiées ;
- **Python 3.12+** : runtime du pipeline ;
- **uv** : environnement reproductible et dépendances verrouillées ;
- **pytest** : tests synthétiques et contrôles de régression ;
- **JSON Schema, YAML et Markdown** : contrats, métadonnées et contenu canonique ;
- **SHA-256** : intégrité, provenance et empreinte des candidats ;
- **`pathlib.Path` et écritures atomiques** : portabilité et sécurité des chemins.

### Adaptateurs documentaires

- `pypdf` pour le texte natif des PDF ;
- Poppler (`pdftoppm`) pour le rendu local ciblé ;
- Docling et OCR/layout local avec l'extra `pdf-advanced` lorsque nécessaire ;
- `python-docx` pour DOCX ;
- `python-pptx` pour PPTX/PPTM ;
- `openpyxl` pour XLSX/XLSM ;
- Pillow pour les images ;
- `charset-normalizer` pour les encodages texte ;
- `pyarrow` et DuckDB, via l'extra `data`, pour les grands datasets ;
- LibreOffice ou Microsoft Office comme pont local contrôlé pour les formats
  anciens, sans macros ni actualisation de liens.

Les formats pris en charge comprennent PDF, DOCX/ODT, PPTX/PPTM/ODP,
XLSX/XLSM/ODS, CSV/TSV, Markdown/TXT/HTML, JSON/JSONL, XML et images courantes.
Une conversion incertaine est signalée ; aucune valeur n'est inventée.

### OpenCode, Codex et prompts

`prompts/roles/` porte les rôles indépendants des fournisseurs. `.opencode/` et
`.codex/` adaptent ces rôles à l'outil choisi. Cette séparation permet de passer
d'OpenCode à Codex sans réécrire le contrat métier.

`opencode.json` est la source de vérité des modèles OpenRouter. DeepSeek Flash
(`deepseek-v4-flash-0731`) est le modèle principal, y compris pour les tâches
lourdes et toute escalade, remplaçant GLM 5.3 (directive opérateur du 18
septembre 2026). Mistral Small 3.2 est le petit modèle. Qwen3 30B construit les
releases rapides et Mistral les revoient indépendamment. Par directive
opérateur, GPT-5.6 Sol Pro et Claude Opus ne doivent jamais être utilisés ; ils
ne sont pas inscrits dans `opencode.json`. Le routage fournisseur ne se place
jamais dans les prompts canoniques, schémas ou Domain Packs.

## 10. Profils réseau et confidentialité

Le pipeline propose trois profils :

| Profil | Réseau | Usage |
| --- | --- | --- |
| `no-llm` | Aucun | Ingestion, validation et audit locaux |
| `strict-local` | Loopback, réseau privé ou allowlist interne | Endpoint compatible OpenAI contrôlé |
| `approved-remote` | Hôte explicitement autorisé | Appel distant exceptionnel et tracé |

`strict-local` utilise `GOV360_LLM_BASE_URL`, `GOV360_LLM_MODEL` et, si besoin,
`GOV360_LLM_API_KEY`. `approved-remote` exige en plus
`GOV360_AUTHORIZE_REMOTE=true` et `GOV360_LLM_ALLOWED_HOSTS`.

Pour OpenRouter, chaque modèle enregistré demande le routage ZDR et
`data_collection: deny`; le partage de session est désactivé. Ces paramètres ne
constituent pas, à eux seuls, une autorisation d'envoyer une source. Un transfert
distant exige toujours le profil `approved-remote`, l'endpoint approuvé et
l'autorisation explicite du matériel précis.

La session OpenCode principale peut lire localement `sources/` pour les contrôles
de fidélité autorisés et peut lire `ingest/`. Elle ne peut modifier aucun de ces
deux dossiers. Les sous-agents conservent des permissions plus restrictives.
Ne pas lancer OpenCode avec `--auto` dans ce dépôt.

## 11. Utiliser Obsidian correctement

Ouvrir `brain wiki/` comme vault. Les humains peuvent lire et modifier le
Markdown, parcourir `indexes/`, suivre les wikilinks et utiliser les Canvas pour
la navigation ou la préparation éditoriale.

Une modification destinée à être publiée ne doit toutefois pas contourner
l'atelier. Le flux normal reste : proposition sous `state/workshop/`, validation,
double revue, approbation, puis assemblage. Cette discipline maintient la
reproductibilité entre l'édition humaine et le système automatisé.

Les bonnes pratiques Obsidian sont simples :

- une note par concept principal ;
- des titres `#`, `##`, `###` naturels et explicites ;
- des liens rares mais utiles ;
- aucun original officiel ou brouillon dans le vault ;
- aucun renommage d'ID ou de fichier pour une simple amélioration d'affichage ;
- un index par domaine pour naviguer sans imposer une taxonomie par dossier.

## 12. Exemple concret : le lot de fondation du questionnaire

Le lot `questionnaire-foundation-lot-011` illustre le workflow complet :

1. le Canvas original a été conservé comme référence éditoriale avec son hash ;
2. les références de pages ont été contrôlées localement ;
3. les prémisses contraignantes ont été limitées aux sources revues `BINDING` ;
4. treize questions communes ont été proposées et quatre questions juridiques
   mises à jour ;
5. le reviewer questionnaire a signalé puis fait corriger l'intent, la
   classification high-risk, les dépendances et l'équivalence bilingue ;
6. le reviewer vault a fait compléter les index et valider le candidat combiné ;
7. le lot de questions et `domain-navigation-proposal` ont été présentés comme
   un candidat ordonné de 84 notes avec le SHA-256
   `eed55bf3452c727bbdcaa9cdd7d3795c603bbddba36dcbd070fd7501958c6809` ;
8. l'opérateur a approuvé ce périmètre précis ;
9. l'assembleur a intégré 23 fichiers, revalidé le vault et produit un reçu ;
10. les manifests sont maintenant `INTEGRATED`.

Cet exemple montre pourquoi un lot peut être corrigé plusieurs fois avant le
gate humain et pourquoi deux propositions dépendantes doivent être validées et
approuvées ensemble.

## 13. Commandes quotidiennes

### Démarrer une session

```sh
cd "/chemin/vers/le-depot"
uv sync --frozen --extra dev --extra data
opencode
```

Pour Codex, lancer Codex depuis la même racine afin qu'il charge `AGENTS.md` et
la configuration `.codex/`.

### Vérifier OpenCode

```sh
opencode debug config
opencode debug skill
opencode agent list
```

Si la configuration projet empêche le démarrage :

```sh
OPENCODE_DISABLE_PROJECT_CONFIG=1 opencode debug config
```

### Contrôler le dépôt

```sh
uv run --offline --no-sync python -m gov360_brain.workshop validate
uv run --offline --no-sync python -m gov360_brain.workshop check-derived
uv run pytest -q
git status --short --branch
git diff --check
```

### Initialiser et prévisualiser une release

```sh
uv run --offline --no-sync python -m gov360_brain.workshop release-init \
  RISK risk-release-001 --risk-tier fast
uv run --offline --no-sync python -m gov360_brain.workshop validate \
  --proposal state/workshop/proposals/<release>
uv run --offline --no-sync python -m gov360_brain.workshop integrate \
  --proposal state/workshop/proposals/<release>
```

### Lancer le prochain lot avec OpenCode

```text
/brain-next
/brain-build state/workshop/proposals/<release>
/brain-review state/workshop/proposals/<release>
```

Le Canvas actif se trouve dans
`brain wiki/Risk analysis questionnaire.canvas`. `integrate --apply` le met à
jour automatiquement. VS Codium lance également la tâche
`Brain: watch derived questionnaire` à l'ouverture du dossier.

Le résultat doit indiquer le pilier, l'état de couverture, l'objectif borné, les
entrées autorisées, l'auteur, le reviewer, les artefacts, les contrôles, le gate
humain et les critères de sortie.

## Contrats techniques ajoutés par l'exécution du plan

Le plan ajoute trois contrôles locaux qui restent distincts de la publication
du vault :

```bash
uv run gov360 brain research "tool scope monitoring" --allowed-source-ids SRC-0046
uv run gov360 brain impact --source-id SRC-0046
uv run gov360 brain context "lifecycle change rollback human oversight" \
  --token-budget 6000 --require-known-validity
```

`brain research` lit exclusivement les unités Markdown validées sous `ingest/`
et marque chaque résultat `UNREVIEWED_RESEARCH`; il ne constitue jamais un
repli implicite de l'assistance. `brain impact` produit uniquement une liste
de dépendances et de sorties à reconstruire. `brain context` retourne un
paquet cité borné ; la modalité, l'applicabilité, les limites, les conflits,
les restrictions et les bornes temporelles inconnues restent explicites.

Les tâches d'agents peuvent être pré-validées par `brain.harness`. Un brief
lie les hashes d'entrée, le rôle, le reviewer indépendant, la sortie attribuée,
les chemins protégés et le profil réseau. Le harness ne prétend pas fournir à
lui seul une sandbox fournisseur ; l'isolation réelle doit être fournie par le
wrapper ou le runtime local. Les mesures inconnues restent `unknown`.

Les notes, questions et Canvas actifs restent soumis aux circuits de
`WORKSHOP.md`. Aucun de ces contrôles techniques n'approuve une modification
de connaissance.

## 14. Utiliser OpenCode au quotidien

### 14.1 Types d'entrée

OpenCode accepte trois formes d'entrée :

- une **commande terminal** exécute directement `uv`, les tests ou Git ;
- une **commande slash** comme `/brain-next` exécute un workflow versionné dans
  `.opencode/commands/` ;
- un **message libre** précise l'objectif, le périmètre ou la reprise d'un
  travail interrompu.

Les commandes slash sélectionnent déjà l'agent et le modèle adaptés. Il n'est
normalement pas nécessaire de changer le modèle à la main.

### 14.2 Modèles à utiliser

La source de vérité est `opencode.json`. Les noms de modèles ne doivent jamais
être copiés dans les prompts canoniques, les schémas ou les Domain Packs.

| Usage | Modèle OpenCode/OpenRouter | Règle |
| --- | --- | --- |
| Session quotidienne, code et outils | `openrouter/deepseek/deepseek-v4-flash-0731` | Modèle principal (remplace GLM 5.3) |
| Cadrage et construction d'une release rapide | `openrouter/qwen/qwen3-30b-a3b-instruct-2507` | `cdo-program-lead` et `domain-builder` |
| Revue indépendante rapide | `openrouter/mistralai/mistral-small-3.2-24b-instruct` | `release-reviewer` et anciens reviewers |
| Audit de preuve ou revue réglementaire stricte | `openrouter/deepseek/deepseek-v4-flash-0731` | Seulement pour le circuit strict |
| Tâches lourdes, blocage complexe, second regard juridique | `openrouter/deepseek/deepseek-v4-flash-0731` | Toute escalade reste sur DeepSeek Flash (directive opérateur 2026-09-18) |
| Inventaire, hashes, schémas, liens, registre et Canvas | Aucun LLM | Utiliser les commandes déterministes |

Gemini Flash Lite et GPT-4.1 Nano restent disponibles pour un classement simple
et borné, mais le pipeline préfère une règle déterministe lorsqu'elle suffit.
DeepSeek Flash est utilisé pour les revues strictes et toutes les escalades.
GPT-5.6 Sol Pro et Claude Opus sont interdits par directive opérateur et ne
sont pas inscrits dans `opencode.json`. Tous les appels OpenRouter conservent
`zdr: true` et `data_collection: deny`.

Règle de coût : une release rapide utilise au maximum un appel de construction
par shard et une revue consolidée. Un input inchangé identifié par hash reste
`NOOP`. Les tâches lourdes restent sur DeepSeek Flash ; aucun inventaire,
génération de Canvas, test ou correction de format ne justifie un appel LLM.

### 14.3 Premier démarrage et premier message

Depuis la racine du dépôt :

```sh
uv sync --frozen --extra dev --extra data
uv run python --version
opencode
```

Premier message recommandé dans une nouvelle session :

```text
Lis AGENTS.md, WORKSHOP.md, ROADMAP.md et brain wiki/SCHEMA.md avant toute
modification. Inspecte ensuite l'état Git, le registre de couverture, les
propositions ouvertes et le vault actif.

Travaille selon le contrat de release v3. Préserve les IDs, chemins, locators,
hashes et frontmatters. Ne modifie jamais sources/ ni ingest/. Ne publie rien et
n'infère aucune approbation humaine. Commence par me donner l'état actuel, le
prochain objectif à forte valeur et son classement fast ou strict.
```

### 14.4 Choisir la prochaine release

Commande courte :

```text
/brain-next
```

Message avec un domaine imposé :

```text
Sélectionne la prochaine release du domaine AI_SECURITY. Compare la couverture,
les notes et questions actives, les preuves déjà revues et les propositions
ouvertes. Classe la release fast ou strict, propose au maximum trois shards et
donne les critères de sortie. Ne crée encore aucun fichier.
```

### 14.5 Construire une release rapide

Initialiser le dossier dans le terminal :

```sh
uv run --offline --no-sync python -m gov360_brain.workshop release-init \
  AI_SECURITY ai-security-release-001 --risk-tier fast
```

Puis lancer dans OpenCode :

```text
/brain-build state/workshop/proposals/ai-security-release-001
```

Message libre équivalent :

```text
Construis la release fast state/workshop/proposals/ai-security-release-001.
Utilise seulement son evidence-lock, les preuves déjà revues, le contexte du
domaine et le catalogue complet des questions. Recherche les doublons avant de
créer un ID. Écris uniquement dans son future-vault et mets à jour l'inventaire
des changements. Si tu rencontres une obligation, une nouvelle preuve, une
interprétation juridique, un changement de contrat ou une supersession, arrête
le shard et demande son passage en strict.
```

Chaque shard reçoit une liste de fichiers sans chevauchement. Trois shards au
maximum peuvent travailler en parallèle. Aucun builder ne modifie le vault
actif.

### 14.6 Construire une release stricte

```sh
uv run --offline --no-sync python -m gov360_brain.workshop release-init \
  LEGAL_REGULATORY legal-regulatory-release-013 --risk-tier strict
```

Message de cadrage :

```text
Traite state/workshop/proposals/legal-regulatory-release-013 par le circuit
strict. Vérifie d'abord l'evidence-lock et les audits existants. Toute
affirmation normative doit être reliée à une source BINDING revue, avec source
ID, hash et locator. Les rôles LLM utilisent uniquement les unités Markdown
validées de ingest/. Consigne les incertitudes, conflits, dates et juridictions.
Ne publie rien.
```

Si un contrôle de fidélité original est nécessaire, l'autorisation doit nommer
la source et rester locale :

```text
Un contrôle local de fidélité est autorisé uniquement pour SRC-XXXX et les
locators suivants : [...]. Compare localement l'original avec les unités ingest
correspondantes. Ne transmets aucun contenu brut à un service distant. Le
rapport contient seulement les IDs, hashes, locators, méthode, verdict et
erreurs assainies.
```

Un envoi distant exige un message séparé qui nomme le profil
`approved-remote`, l'endpoint et le matériel autorisé. Sans ces trois éléments,
OpenCode doit rester sur les opérations locales.

### 14.7 Revoir une release

Release rapide :

```text
/brain-review state/workshop/proposals/ai-security-release-001
```

Release stricte après audit des preuves :

```text
/brain-review-strict state/workshop/proposals/legal-regulatory-release-013
```

Message libre équivalent :

```text
Effectue une revue indépendante de cette release. Vérifie le manifeste,
l'evidence-lock, le future-vault, le catalogue complet, les doublons, le schéma,
les liens, l'autorité, les locators, l'équivalence FR/EN et les dépendances.
Écris uniquement review/release-review.json avec reviewer_identity, reviewed_at,
candidate_sha256, findings et un verdict BLOCKED ou
READY_FOR_HUMAN_APPROVAL. Ne corrige pas les notes et n'accorde aucune
approbation humaine.
```

L'auteur d'un shard ne doit pas être son reviewer.

### 14.8 Prévisualiser, approuver et intégrer

Prévisualisation déterministe :

```sh
uv run --offline --no-sync python -m gov360_brain.workshop integrate \
  --proposal state/workshop/proposals/<release>
```

La sortie fournit `candidate_sha256`, `risk_tiers`, `reviewed`, `approved`, le
nombre de fichiers et les hashes des evidence locks. Après la revue, l'humain
renseigne lui-même `review/approval.md` :

```text
Status: APPROVED

- Approver identity: <identité humaine>
- Decision: APPROVED
- Scope: <release exacte>
- Rationale: <justification>
- Decision date: <AAAA-MM-JJ>
- Candidate SHA-256: <hash de la prévisualisation>
```

OpenCode ne remplit jamais ces valeurs à la place de l'approbateur. Une fois
l'approbation inscrite :

```text
/brain-release state/workshop/proposals/<release>
```

La commande prévisualise de nouveau le candidat et applique seulement si le
manifeste, la revue et l'approbation concordent.

### 14.9 Utiliser le Canvas automatique

La mise à jour intervient après chaque intégration. Pendant l'édition locale,
VS Codium lance la tâche `Brain: watch derived questionnaire`. Elle peut aussi
être démarrée depuis OpenCode :

```text
/brain-canvas-watch
```

Commandes terminal équivalentes :

```sh
uv run --offline --no-sync python -m gov360_brain.workshop build-derived
uv run --offline --no-sync python -m gov360_brain.workshop check-derived
obs "brain wiki"
```

Le Canvas est une vue dérivée. Toute correction se fait dans la question
Markdown correspondante, puis la vue est régénérée.

### 14.10 Demander l'état d'avancement

```text
Donne l'état actuel sans modifier de fichier. Pour chaque release ouverte,
indique le domaine, le circuit, les shards terminés, les contrôles passés, les
findings bloquants, le prochain geste concret et si une décision humaine est
réellement attendue. Indique aussi le nombre de questions actives, les erreurs
du vault et l'état du Canvas dérivé.
```

### 14.11 Reprendre après une interruption ou un changement de modèle

```text
Reprends depuis les artefacts présents. Lis les manifestes, evidence locks,
rapports et diffs avant toute action. Ne répète aucune extraction, génération ou
revue dont les entrées et hashes sont inchangés. Identifie le dernier gate
validé, puis continue à partir de la prochaine étape incomplète avec le modèle
configuré pour ce rôle.
```

Ce message évite de repayer des appels déjà matérialisés.

### 14.12 Diagnostiquer un échec

```text
Analyse cet échec sans modifier les tests ni le vault. Reproduis la commande,
classe la cause entre contrat, preuve, chemin, permission, dépendance ou outil,
et indique le fichier ou ID responsable. Propose ensuite la correction minimale
et les validations nécessaires. Ne change rien tant que la cause réelle n'est
pas établie.
```

### 14.13 Message de fin de session

```text
Avant de terminer, exécute les validateurs pertinents, check-derived, les tests
ciblés puis la suite complète si nécessaire, git diff --check et le contrôle de
sources/. Résume les changements, hashes, tests, findings restants, coût ou
nombre d'appels disponible, et donne une seule prochaine commande. Ne publie et
n'approuve rien implicitement.
```

## 15. Utiliser Codex au quotidien

Codex se lance depuis la racine du dépôt afin de charger `AGENTS.md` et les
règles du workspace. Les rôles de `.codex/config.toml` organisent le travail,
mais ne remplacent jamais la revue ni l'approbation humaines.

### 15.1 Démarrer

```sh
cd "/chemin/vers/le-depot"
uv sync --frozen
codex -C "/chemin/vers/le-depot" -s workspace-write -a on-request
```

Pour une tâche bornée et reproductible :

```sh
codex exec -C "/chemin/vers/le-depot" -s workspace-write -a on-request \
  -m <modele-configure> "<message de tâche>"
```

Le modèle se choisit avec `-m` ou un profil Codex (`-p`). Gardez les noms de
modèles hors des prompts canoniques. Utilisez le modèle quotidien pour le
cadrage, un modèle plus fort pour le circuit strict et un second regard pour
les revues difficiles. Les validations, hashes, tests et Canvas restent
déterministes et ne nécessitent aucun appel modèle.

### 15.2 Premier message

```text
Lis AGENTS.md, WORKSHOP.md, ROADMAP.md et brain wiki/SCHEMA.md avant toute
modification. Inspecte l'état Git, les releases ouvertes, les evidence-locks,
les propositions, le vault actif et les artefacts dérivés.

Continue selon le contrat de release v3. Préserve les IDs, frontmatters,
locators et hashes. L'accès en lecture à sources/ est autorisé pour les
contrôles locaux bornés, mais aucune source/ ou ingest/ ne doit être modifiée
et aucun contenu ne doit être envoyé à distance sans profil approved-remote et
autorisation précise. Ne publie rien et n'infère aucune approbation humaine.
Donne d'abord l'état, le prochain lot et son circuit fast ou strict.
```

### 15.3 Construire puis revoir

```sh
uv run --offline --no-sync python -m gov360_brain.workshop release-init \
  AI_SECURITY ai-security-release-001 --risk-tier fast
```

```text
Construis uniquement state/workshop/proposals/ai-security-release-001.
Utilise son evidence-lock et les unités Markdown validées de ingest/. Écris
seulement dans le future-vault et l'inventaire de cette release. Préserve les
IDs, liens, preuves et l'équivalence FR/EN. Passe en strict pour toute
obligation, nouvelle preuve, interprétation, supersession ou changement de
contrat.
```

```text
Revois indépendamment state/workshop/proposals/<release>. Vérifie manifeste,
evidence-lock, schéma, liens, autorité, locators, questions et dépendances.
Écris uniquement review/release-review.json avec candidate_sha256, findings et
BLOCKED ou READY_FOR_HUMAN_APPROVAL. Ne corrige pas les notes et n'approuve
rien.
```

Prévisualisez, renseignez vous-même `review/approval.md` avec le hash exact,
puis appliquez seulement après les gates :

```sh
uv run --offline --no-sync python -m gov360_brain.workshop integrate \
  --proposal state/workshop/proposals/<release>
uv run --offline --no-sync python -m gov360_brain.workshop integrate \
  --proposal state/workshop/proposals/<release> --apply
```

### 15.4 Reprendre et terminer

```sh
codex resume --last
codex review
uv run --offline --no-sync python -m gov360_brain.workshop validate
uv run --offline --no-sync python -m gov360_brain.workshop check-derived
uv run pytest -q
git diff --check
git status --short -- sources/
```

Message de reprise :

```text
Reprends depuis les artefacts présents. Lis manifests, evidence-locks, rapports,
approbations et diffs avant toute action. Ne répète aucune étape dont les
entrées et hashes sont inchangés. Identifie le dernier gate validé, continue à
l'étape suivante et signale toute décision humaine réellement nécessaire.
```

## 16. Dépannage

### Le validateur signale un lien cassé

Corriger le lien vers un ID existant ou inclure la note cible dans le même lot.
Ne pas créer de placeholder. Vérifier aussi que le lien emploie l'ID stable et
non un titre d'affichage ambigu.

### Une question ressemble à une question existante

Comparer l'intent, le `topic`, les preuves attendues et les options. Utiliser
`NOOP` si elle est redondante, `UPDATE` si la formulation change sans toucher à
l'intent, ou un nouvel ID avec `SUPERSEDE` si le sens change.

### Une dépendance de question échoue

La cible doit exister dans le vault ou dans le candidat combiné. Le champ ne
contient que `question_id` et `equals`. Rechercher un cycle et vérifier que la
valeur de `equals` correspond bien à une valeur de réponse stable.

### Une preuve semble normative mais la source n'est pas `BINDING`

Reformuler comme recommandation, contrôle ou contexte, ou demander une revue
d'autorité. Ne changer jamais la classification sur la seule base du titre du
document.

### Une page PDF est pauvre ou visuelle

Marquer la dépendance, rendre la page localement, comparer au Markdown, puis
utiliser un OCR local seulement si le texte natif est inutilisable. Conserver le
résultat `UNCERTAIN` tant que la fidélité n'est pas établie.

### `uv sync --frozen` échoue

Vérifier `.python-version`, la plateforme et le message exact. Ne régénérer pas
automatiquement `uv.lock`. Un lock réellement incompatible doit être analysé et
la décision documentée.

### OpenCode ne voit pas un agent ou une commande

Relancer OpenCode depuis la racine, exécuter `opencode debug config`,
`opencode debug skill` et `opencode agent list`, puis vérifier le frontmatter du
wrapper concerné. Les prompts métier restent dans `prompts/roles/`.

### Le modèle OpenRouter configuré n'a plus de crédit

Continuer avec Codex ou sélectionner un modèle déjà enregistré dans
`opencode.json`. Modifier seulement la couche fournisseur ou le wrapper du rôle.
Reprendre depuis les artefacts et rapports existants ; ne pas refaire une étape
déterministe inchangée et ne pas affaiblir les règles d'accès pour contourner le
problème.

### L'intégration avec `--apply` est refusée

Vérifier que chaque proposition est sous `state/workshop/proposals/`, possède
`future-vault/`, un `manifest.json` cohérent, les dépendances dans le bon ordre,
un manifest `APPROVED` et un `approval.md` complet. Refaire la prévisualisation
et confirmer que son empreinte correspond exactement à celle approuvée.

### Le vault actif est invalide après une modification

Ne pas modifier les tests pour masquer le problème. Identifier d'abord le
contrat violé. L'assembleur tente de restaurer l'état antérieur en cas d'échec ;
conserver le rapport et corriger la proposition.

## 17. Routine recommandée

Au début d'une session :

1. lire `AGENTS.md`, puis les contrats concernés ;
2. consulter le registre de couverture et les lots ouverts ;
3. choisir un seul objectif borné ;
4. vérifier l'état Git avant toute écriture ;
5. utiliser uniquement les entrées autorisées.

Pendant le travail :

1. préserver IDs, hashes, locators et chemins ;
2. séparer faits documentaires et interprétations ;
3. traiter les contradictions explicitement ;
4. garder les sorties d'agents dans les propositions ;
5. exécuter les validations après tout changement de contrat ou de lot.

Avant publication :

1. vérifier fidélité et autorité ;
2. obtenir la revue indépendante consolidée et, dans le circuit strict, l'audit de preuve ;
3. prévisualiser le candidat ordonné ;
4. faire approuver le diff et son SHA-256 par l'humain ;
5. appliquer avec l'assembleur déterministe ;
6. revalider, tester et vérifier l'intégrité Git et `sources/`.

Cette méthode conserve la fonction de chaque couche : les documents originaux
restent la matière de référence, `ingest/` fournit une représentation vérifiable,
l'atelier transforme les preuves en propositions revues, Obsidian organise la
connaissance publiée, et le Brain local sélectionne le contexte nécessaire à
son propre raisonnement.

## 18. Brain local, preuves réutilisables et partage

Les nouvelles publications utilisent le manifeste v3 avec preuves résolues. Les
releases v1/v2 restent lisibles comme reçus historiques, sans approbation rétroactive.
Les diagnostics sont dans `state/derived/brain/` : `baseline.json`,
`reconciliation.json`, `coverage-matrix.json`, `report.md` et `navigation.md`.
Le registre de preuves accompagne les notes sous
`state/workshop/evidence-library/` et suit `brain-evidence.schema.json`.

Cette évolution est décrite dans `plan.md`. Son avancement vérifiable provient de
`gov360 brain status`, des diagnostics de réconciliation et de la matrice de
couverture, pas du nombre de pages du manuel. Les chapitres précédents décrivent
aussi des lots historiques : leur état actuel doit être lu dans leurs manifests.

### 18.1 Du document au contexte

```text
sources immuables → ingest validé → preuves auditées
    → propositions de notes et questions → revue indépendante
    → approbation du SHA-256 exact → vault Markdown
    → sections + graphe + registre + Canvas
    → recherche locale et contexte cité / export OKF
```

Une preuve réutilisable désigne une source, son hash, une unité et son hash,
un locator et une revue applicable. Chaque affirmation garde son autorité : une
note citant une loi et un guide ne transforme pas le guide en obligation.
Les fragments ATLAS restent liés à leur unité parent et à leur identifiant
stable. Toute ambiguïté est un blocage à résoudre, jamais un audit inventé.

| Situation | Conséquence pour l'agent |
| --- | --- |
| Note active et preuves revues résolues | Utilisable en assistance dans son périmètre |
| Note active héritée, preuves non résolues | Visible dans Obsidian ; diagnostic et réconciliation nécessaires |
| Ingest valide sans revue de fond | Recherche documentaire explicite uniquement |
| Hash, autorité ou locator manquant | Lacune signalée ; ne pas affirmer une obligation |
| Proposition prête et non approuvée | Présenter le hash exact à l'humain |

### 18.2 Commandes terminal

Depuis la racine, après `uv sync --frozen` :

```sh
uv run gov360 brain status
uv run gov360 brain validate
uv run gov360 brain build
uv run gov360 brain build --check
uv run gov360 brain context "human oversight" --token-budget 6000
uv run gov360 brain context "DPIA" --mode research
uv run gov360 brain evaluate
uv run gov360 brain export --output dist/okf
uv run gov360 brain export --output dist/okf --check
uv run gov360 brain release-kit --output dist/release-kit
uv run gov360 brain bootstrap --source-root sources
```

`build` reconstruit les artefacts locaux ; `--check` détecte les sorties périmées.
La recherche emploie SQLite FTS5/BM25 et du vocabulaire FR/EN, sans appel distant.
Le budget par défaut est estimé à 6 000 tokens pour le paquet complet. Les filtres
`--domains`, `--jurisdiction` et `--as-of` précisent le contexte demandé ; consulter
`uv run gov360 brain context --help` pour les valeurs acceptées.

`assistance` sélectionne la connaissance dont les preuves sont résolues et
revues. `research` est explicitement documentaire ; un manque de résultat ne
bascule jamais automatiquement vers ce mode. Les réponses projet ne sont ni
collectées ni stockées. Aucun résultat ne remplace une décision de gouvernance.

L'export OKF est dérivé et reproductible. Il transforme les liens Obsidian en
liens Markdown standards et conserve la traçabilité. Il ne faut pas y modifier
une note à la main. Le vault est la seule version canonique. La présence d'une
note active ne permet pas d'inventer une date ou un auteur de vérification OKF.

### 18.3 Répartition des rôles et coûts

Le CDO choisit un besoin couvert insuffisamment dans la matrice des quinze piliers
et dix critères. L'extracteur fournit les candidats ; un auditeur distinct
contrôle les preuves. Le constructeur travaille sur un overlay borné ; un
reviewer indépendant examine le candidat complet. Les outils reconstruisent
les sorties partagées. Les rôles spécialisés historiques restent disponibles
pour un contrôle ciblé.

Les modèles sont ceux des profils et wrappers réellement chargés. Le tableau
historique du §14.2 décrit la configuration du dépôt, pas une garantie de
performance, de disponibilité ou de prix chez un fournisseur. La migration
n'impose aucun nouveau nom de modèle. Pour réduire le coût, réutiliser les audits
encore valides, produire ensemble connaissance et questions partageant une preuve,
et utiliser des commandes déterministes pour les hashes, inventaires et index.
Des métriques absentes restent `unknown` ; ne jamais compter un coût inconnu à zéro.

### 18.4 Messages types dans Codex ou OpenCode

Reprise de programme :

```text
Lis AGENTS.md, WORKSHOP.md, ROADMAP.md, brain wiki/SCHEMA.md et plan.md.
Consulte le statut Brain, la réconciliation des releases et la couverture 15×10.
Sélectionne le prochain besoin non couvert, sans relancer une release intégrée.
Prépare un candidat borné avec preuves précises, revue indépendante et contrôles.
Présente le diff et son hash avant toute nouvelle publication de connaissance.
```

Construction d'un lot existant :

```text
Construis uniquement la release indiquée et son overlay assigné, à partir de
son evidence-lock et des unités ingest validées. Réutilise les notes existantes.
Préserve IDs, liens, modalité de chaque affirmation et équivalence FR/EN.
Escalade en strict toute nouvelle preuve, obligation, interprétation juridique,
supersession ou évolution de contrat. Signale les lacunes sans les inventer.
```

Contrôle du contexte :

```text
Utilise gov360 brain context en mode assistance pour mon sujet de gouvernance.
Explique les sections et références retenues, les filtres et les lacunes.
Ne transforme pas une recherche infructueuse en réponse fondée sur ta mémoire.
```

OpenCode conserve `/brain-next`, `/brain-build RELEASE`, `/brain-review RELEASE`,
`/brain-review-strict RELEASE` et `/brain-release RELEASE`. Le rôle de préparation
Git est accessible par `@git-helper` ou `/brain-git-helper` ; dans Codex, demander
explicitement le rôle `git_helper`.

### 18.5 Partager une construction reproductible

Le kit est produit dans un dossier séparé par liste de fichiers autorisés.
Il ne copie pas l'historique Git de travail, les sources, les extractions, les
citations brutes, les secrets ni les configurations personnelles. Apache-2.0
s'applique au code original ; les contenus tiers gardent leurs propres droits.
L'export public exclut les contenus sans décision de redistribution explicite.

Le destinataire place ses originaux localement et lance `bootstrap` en aperçu,
puis `--apply` pour la reconstruction autorisée. L'identification par hash préserve
les IDs. Un fichier absent ou différent est signalé ; une extraction de hash
différent requiert une nouvelle revue. Les synthèses LLM ne sont pas promises
identiques à l'octet près.

Message pour préparer une release :

```text
Utilise git_helper pour préparer le kit local autorisé et son rapport de release.
Vérifie les exclusions, les droits, la reconstruction et les tests ; présente
la liste des fichiers, leurs hashes, les changements et les blocages restants.
Ne pousse pas vers un remote et ne publie aucune release distante.
```

Le statut « prêt à partager » exige des tests réussis dans un dossier propre.
L'approbation d'un lot de connaissance ne vaut pas permission de publication Git.

Le dépôt privé de continuité du CDO est un autre produit. Sur autorisation
explicite de l'opérateur, `gov360 brain handoff` inclut les originaux, ingest,
vault, preuves, propositions et dérivés liés à la cible privée enregistrée dans
`config/private-handoff-policy.json`. Cette autorisation ne rend pas le contenu
redistribuable publiquement et ne change aucune qualification de preuve.

## 19. Référence consolidée — exécution locale, formats et reprise

Cette section rassemble les détails opérationnels qui étaient auparavant
répartis entre `outils.md` et `fonctionnement.md`. `manuel.md` est désormais la
source d’apprentissage unique ; `outils.md` reste un pointeur de compatibilité
et l’ancien doublon `fonctionnement.md` a été retiré.

### 19.1 Outils et dépendances

| Composant | Rôle | Statut |
| --- | --- | --- |
| Python 3.12+ | Runtime et CLI `gov360` | requis |
| `uv` | Environnement, verrouillage et synchronisation | requis |
| `pypdf` | Extraction native page par page des PDF | requis |
| Poppler (`pdftoppm`) | Rendu PDF local ciblé | optionnel |
| `python-docx`, `python-pptx`, `openpyxl` | Formats Office | requis pour les formats concernés |
| Pillow | Images et métadonnées | requis pour les images |
| `charset-normalizer` | Encodages CSV/TXT/JSON/XML | requis |
| `pyarrow` | Grands datasets Parquet | extra `data` |
| Docling/OCR local | PDF difficiles et mise en page complexe | extra `pdf-advanced`, optionnel |
| VS Codium, Obsidian et Git | Édition, lecture humaine et versionnement | outils de travail |

Les modèles locaux ou les ponts LibreOffice/Microsoft Office sont optionnels et
restent strictement locaux. Le rendu Office est opt-in, avec macros, liens et
connexions désactivés :

```powershell
$env:GOV360_OFFICE_RENDERING = '1'
uv run gov360 run --domain finance --profile strict-local
```

Les formats pris en charge sont PDF, DOCX/ODT, PPTX/PPTM/ODP, XLSX/XLSM/ODS,
CSV/TSV, Markdown/TXT/HTML, JSON/JSONL, XML et PNG/JPEG/TIFF. Les adaptateurs
conservent les unités natives, les formules et valeurs cache séparées, les
feuilles masquées, les tableaux, graphiques, images, liens externes et
métadonnées utiles. Une valeur manquante ou un recalcul impossible reste
`UNCERTAIN` ; aucune valeur n'est inventée.

Les CSV, TSV et JSON volumineux sont traités en flux. Jusqu'à 50 000 lignes et
25 MiB, les fragments peuvent être matérialisés en Markdown. Au-delà, l'ingest
produit un schéma, un rapport de qualité, un échantillon explicitement non
exhaustif et des partitions Parquet locales sous `ingest/SRC-XXXX/data/`. Un
échantillon ne soutient ni une obligation ni une statistique globale.

### 19.2 Inventaire CDO et propositions

Les brouillons CDO sont des intrants éditoriaux, jamais des preuves. Pour les
inventorier sans les publier :

```sh
uv run --offline --no-sync python -m gov360_brain.workshop inventory \
  --cdo "$CDO_ROOT"
```

L'atelier conserve une référence locale, produit des brouillons normalisés sous
`state/workshop/drafts/` et écrit `state/workshop/cdo-inventory.json`. Une note
vide devient `EMPTY_BACKLOG`; une note non prouvée reste
`EDITORIAL_REVIEW_REQUIRED`. La vérification contre `ingest/` est obligatoire
avant toute proposition de connaissance.

### 19.3 Reprise, fan-out et idempotence

La normalisation peut répartir les fichiers sur des workers légers, mais les
adaptateurs lourds et les écritures partagées restent sérialisés. Chaque job
possède un receipt et une clé d'idempotence. Si la taille et la date d'un fichier
n'ont pas changé, une nouvelle exécution ne reconvertit pas la source et ne
relance pas de modèle.

Pour surveiller un dépôt sans traiter les fichiers temporaires :

```sh
uv run gov360 watch --domain finance --profile strict-local --require-ready
```

Avec `--require-ready`, le traitement attend le marqueur adjacent
`<fichier>.ready`. Un redémarrage reprend les unités stables ; il ne contourne
ni les hashes ni les gates de revue.

### 19.4 Commandes de contrôle regroupées

Depuis la racine, après `uv sync --frozen` :

```sh
uv run gov360 status
uv run gov360 inventory --domain finance
uv run gov360 source classify SRC-0001 --normativity GUIDANCE --reviewer reviewer-id
uv run gov360 run --domain finance --profile no-llm
uv run gov360 validate-ingest --domain finance
uv run --offline --no-sync python -m gov360_brain.workshop quality
uv run --offline --no-sync python -m gov360_brain.workshop validate
uv run --offline --no-sync python -m gov360_brain.workshop check-derived
uv run gov360 retire --source-id SRC-0042
```

`retire` modifie uniquement les métadonnées du manifeste ; l'original reste
préservé. Les anciennes commandes v1 `generate`, `approve`,
`normalize-vault` et `audit` ne doivent pas être lancées sur le vault actif
lorsqu'elles contredisent le contrat v3.

### 19.5 Artefacts et garanties de la chaîne

Les principaux artefacts d'atelier sont `extraction-quality.json`, les reçus de
fidélité, `cdo-inventory.json`, les propositions sous
`state/workshop/proposals/` et les rapports d'intégration. Les sorties dérivées
(`state/derived/`, le registre de questions, le Canvas, le catalogue Brain et
les exports OKF) sont reconstruisibles et ne sont jamais éditées comme contenu
canonique.

La chaîne garantit la provenance par source, unité, hash et locator, la
préservation des originaux, l'accès des rôles au seul Markdown validé, des
transformations idempotentes et une approbation humaine liée au candidat. Elle
ne garantit pas la fidélité par le seul hash, l'autorité juridique d'une source
non classée `BINDING`, la qualité d'un brouillon CDO ni une décision de
conformité pour un projet particulier.

## 20. Reprise complète par le CDO

### 20.1 Carte de la chaîne

Le diagramme source PlantUML se trouve dans
`docs/architecture/governance-brain-lifecycle.puml`; sa version SVG est lisible
directement dans GitHub. Il sépare le corpus immuable, les transformations
déterministes, les rôles de preuve, la construction, les gates indépendants,
le Brain publié et sa maintenance.

![Governance Brain lifecycle](docs/architecture/governance-brain-lifecycle.svg)

### 20.2 Ce qui se passe lorsqu'un nouveau document arrive

1. Ajouter le fichier sous `sources/` sans modifier aucun original existant.
2. Lancer l'inventaire et attribuer un nouveau `SRC-XXXX`; conserver chemin,
   format et SHA-256 dans le manifeste.
3. Exécuter l'adaptateur local approprié avec le profil `no-llm`. Il produit
   `document.json`, `overview.md` et des unités Markdown adressables par page,
   section, feuille, ligne, clé ou autre locator stable.
4. Exécuter `validate-ingest` et la qualité d'extraction. Un hash cohérent prouve
   l'intégrité, pas la fidélité de la page.
5. Comparer localement les pages, tableaux ou images utilisées lorsque le
   document ou l'unité porte `REVIEW_REQUIRED` ou lorsque la mise en page est
   déterminante. Consigner résultat, méthode, locator et limites sans recopier
   le texte dans les logs.
6. Faire qualifier la source : `BINDING`, guidance, contrôle, recherche ou
   contexte, avec juridiction, applicabilité, dates et supersession. Seul le
   premier cas peut soutenir une obligation ou interdiction.
7. Faire extraire les candidats de preuve par `source_extractor` depuis les
   seules unités assignées, puis faire revoir hashes, locators, fidélité et
   autorité par `evidence_auditor`.
8. Choisir le circuit. Toute nouvelle preuve, interprétation juridique,
   obligation, supersession ou modification de contrat force le strict ; le
   fast réutilise exclusivement une preuve déjà revue.
9. Le `knowledge_architect` conçoit la modification sans dupliquer les notes ;
   le `questionnaire_curator` ajoute une question uniquement si une intention
   assessable manque. Le `questionnaire_reviewer` vérifie FR/EN, topic et
   dépendances.
10. Le `domain_builder` matérialise uniquement le `future-vault/` attribué. Les
    notes actives, preuves historiques, index partagés et approbations restent
    hors de sa zone d'écriture.
11. Les validateurs calculent le candidat exact. `vault_reviewer` et
    `release_reviewer` recherchent les défauts sans modifier ni approuver le lot.
12. Présenter le diff et le SHA-256 à l'approbateur humain. L'assembleur
    déterministe intègre uniquement une approbation portant sur ce hash exact,
    puis reconstruit catalogue, graphe, Question Registry et Canvas.

Commandes de départ :

```sh
uv run gov360 inventory --domain <domain-pack>
uv run gov360 run --domain <domain-pack> --profile no-llm
uv run gov360 validate-ingest --domain <domain-pack>
uv run --offline --no-sync python -m gov360_brain.workshop quality
uv run --offline --no-sync python -m gov360_brain.workshop release-init \
  <DOMAIN> <release-id> --risk-tier strict
```

### 20.3 Fonctionnement des sous-agents

Le coordinateur crée une tâche bornée contenant objectif, entrées et hashes,
preuves autorisées, identité de l'auteur et du reviewer, sortie attribuée,
interdictions et critères de sortie. Un sous-agent ne reçoit pas le dépôt comme
zone d'écriture générale. Il remet un artefact immuable ou un overlay ; le
coordinateur l'inspecte avant intégration. Les spécialistes n'approuvent jamais
leur travail, les reviewers ne construisent jamais le candidat et seul
l'assembleur déterministe écrit dans le vault actif.

OpenCode charge les wrappers sous `.opencode/agents/` et les commandes sous
`.opencode/commands/`. Les prompts métier restent dans `prompts/roles/` et les
procédures réutilisables sous `.agents/skills/`. Le modèle et le fournisseur
peuvent changer sans modifier ces contrats. Les permissions du runtime sont une
barrière supplémentaire ; elles ne remplacent pas les hashes, la revue ou la
décision humaine.

### 20.4 Écrire et reprendre un lot

Un lot v3 contient au minimum son manifeste, un evidence-lock, son overlay
`future-vault/`, l'inventaire des changements et un dossier `review/`. Les IDs
et chemins déclarés doivent correspondre exactement aux fichiers proposés. Une
reprise commence par lire le manifeste et les hashes, vérifier l'état du vault,
rejouer la validation sans écriture et traiter les findings. Ne jamais réécrire
un reçu historique pour rendre le nouveau lot valide.

Le message OpenCode recommandé est :

```text
Lis AGENTS.md, WORKSHOP.md, ROADMAP.md, brain wiki/SCHEMA.md, plan.md et
manuel.md. Inspecte le statut Brain et les preuves du lot assigné. Écris
uniquement dans son future-vault et son inventaire. Préserve IDs, frontmatters,
liens, locators et équivalence FR/EN. Escalade vers le strict pour toute nouvelle
preuve, obligation, interprétation, supersession ou modification de contrat.
Présente les findings et le hash exact ; ne publie rien.
```

### 20.5 Cloner, vérifier et continuer sous Windows

Suivre `docs/windows-setup.md`. Après le clone privé, la commande suivante doit
passer avant tout nouveau lot :

```powershell
PowerShell -ExecutionPolicy Bypass -File .\tools\setup-windows.ps1 -CheckOnly
```

Le dépôt complet contient déjà les originaux et ingest autorisés. `bootstrap`
doit donc répondre `NOOP` pour les sources reconstructibles. Un écart de hash,
une unité manquante, un dérivé périmé ou un test Windows en échec bloque la
reprise jusqu'à diagnostic ; aucun test ne doit être assoupli pour masquer le
problème.
