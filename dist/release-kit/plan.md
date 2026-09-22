# Governance Brain : connaissance, contexte et partage

Programme initial approuvé le 15 septembre 2026 : sections 1 à 5 conservées
ci-dessous. Actualisation du 21 septembre 2026 : diagnostic et améliorations
proposées dans les sections 6 à 12, à partir de l'examen local du 20–21 septembre.
Ces propositions ne constituent ni une validation de leur implémentation ni une
approbation de nouveaux contenus. `ROADMAP.md` conserve l'historique des étapes ;
les reçus et les contrôles reproductibles établissent leur état réel.

Pour reprendre le travail, lire d'abord les sections 6, 9 et 10. Les chiffres du
« Diagnostic de départ » restent un état historique, pas la baseline actuelle.

## 1. Objectif et décisions

Construire un Brain qui retrouve la bonne connaissance, applicable au bon
contexte, avec des preuves vérifiables et des limites explicites.

- Markdown Obsidian reste canonique ; préserver IDs, chemins et frontmatters.
- Ajouter recherche locale et préparation du contexte, sans réponses projet,
  scores ni exécution des décisions de gouvernance.
- Produire OKF v0.2 comme export reproductible, pas comme second vault canonique.
- Conserver une approbation humaine par lot après revue indépendante.
- Préparer un kit reproductible sous Apache-2.0 pour le code original, en
  traitant séparément les droits des contenus tiers.
- Préserver les sources ; les rôles consomment uniquement le Markdown validé.

### Diagnostic de départ

46 sources sont inventoriées, dont 45 extractions disponibles et une source en
quarantaine. Les 2 836 unités correspondent à leurs hashes de fichiers ; 235
portent un indicateur de revue visuelle. La fidélité reste distincte de cette
intégrité. Le vault contient 108 notes : 73 connaissances, 27 questions et 8
index. 25 connaissances n'ont pas de lien entrant. Trois sources ont une
classification explicite enregistrée, toutes BINDING. Deux releases intégrées
ont un verrou de preuves vide. Le constructeur de contexte historique charge
zéro note du contrat actif. Roadmap, couverture et mesures de coûts doivent être
réconciliées. Tests, validation du vault et contrôle des dérivés passent ; ce
n'est pas une validation exhaustive des interprétations juridiques.

## 2. Phase 1 — Preuves et production métier

### Baseline et réconciliation

Produire un diagnostic Markdown et un inventaire JSON liés aux hashes des
entrées : sources, adaptateurs, unités, classifications, fidélité, notes,
questions, liens, releases et approbations. Classer les écarts : preuve
introuvable, revue ancienne, extraction douteuse, contenu incomplet,
contradiction, navigation. Relier chaque note aux artefacts de publication.
Réconcilier ATLAS, AML.M0029, article 22 et vague 2 sans relancer les lots
intégrés. Conserver les reçus historiques ; une correction les référence.

### Bibliothèque de preuves réutilisables

Ajouter des registres versionnés de preuves et de relations entre affirmations
et preuves, sans dupliquer les textes métier. Chaque preuve identifie source
et hash, unité et hashes, locator précis, autorité, périmètre et dates établies,
revues de fidélité et de preuve, notes et sections utilisatrices. La modalité
reste attachée à l'affirmation : une citation BINDING ne rend pas toute une note
contraignante. Importer les reçus avec des adaptateurs explicites ; garder les
liaisons ambiguës à revoir. Ni active, ni VERIFIED historique, ni approbation
générale ne reconstruisent artificiellement une preuve.

Dériver les fragments ATLAS depuis le Markdown validé, avec identifiant et
sélecteur d'objet, hashes et locator parent. Adapter le catalogue pour fonctionner
depuis ingest ; conserver unités et références originales.

### Contrôles et coût

Résoudre les verrous jusqu'aux unités et revues. Vérifier hashes, couverture des
affirmations, indépendance auteur/reviewer, liaison revue/candidat/approbation,
changements de preuve, autorité, contrats et supersession. Une ambiguïté
normative escalade vers le strict ; aucun détecteur lexical ne prétend détecter
toute interprétation juridique. Les anciens formats restent lisibles ; nouvelles
releases et migrations utilisent un contrat renforcé versionné. Réutiliser un
audit dont les entrées et la validité sont inchangées. Construire connaissance
et questions ensemble. Les dérivés inchangés ne déclenchent aucun LLM.

### Matrice 15 piliers × 10 critères

Chaque cellule indique connaissances, questions, preuves, lacunes, dépendances
et prochaine action. Distinguer source absente, disponible non exploitée,
partielle, non revue. Les états COMPLETE nécessitent une justification revue.

| Ordre | Besoin de gouvernance | Sources candidates à examiner |
| --- | --- | --- |
| 1 | Qualification, rôles, AI Act/RGPD, article 22, DPIA/FRIA, transparence et recours | SRC-0010 à SRC-0022, SRC-0043 |
| 2 | Responsabilités, inventaire IA, gates, exceptions, changements, retrait | SRC-0001 à SRC-0006, SRC-0009, SRC-0039 et SRC-0040 |
| 3 | Données, qualité, provenance, validation, biais, suivi et limites | SRC-0005, SRC-0019 à SRC-0022, SRC-0036 à SRC-0040 |
| 4 | Identités, outils, MCP, supply chain, détection et réponse | SRC-0023 à SRC-0035, SRC-0044 et SRC-0046 |
| 5 | Tiers, responsabilités partagées, résilience, incidents et audit | SRC-0001 à SRC-0004, SRC-0028 à SRC-0035, SRC-0041 |
| 6 | Stratégie, valeur, formation, adoption, société et durabilité | Corpus transversal ; lacunes explicites |

Ce routage ne constitue pas une approbation des preuves. Les aperçus ISO ne
permettent pas une couverture intégrale des normes. Chaque sujet précise selon
sa pertinence définition, applicabilité, responsabilité, risque, contrôle,
artefact, suivi, exceptions et preuves. Mettre à jour avant de créer un doublon.
Les incidents expliquent risques et contrôles sans devenir des obligations.
Questions atomiques FR/EN, topics stables et dépendances explicites. Conserver
les limites factuelles utiles, éviter les paragraphes génériques.

Premier pilote : réconcilier qualification, article 22, DPIA/FRIA, questions et
preuves existantes ; compléter uniquement les lacunes démontrées et présenter
un candidat consolidé à l'approbation.

## 3. Phase 2 — LLM Wiki, contexte et OKF

```text
Sources immuables → Markdown validé → Preuves revues
  → Propositions → Revue → Approbation → Vault canonique
  → Catalogue de sections / graphe / questions / Canvas
      → Recherche locale → Contexte cité
      → Export OKF → Bundle portable
```

Retenir de [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
la compilation progressive, les relations, contradictions et index. Les
découvertes d'exploration deviennent des propositions soumises à revue.

### Catalogue et maintenance

Construire catalogue des notes et sections, graphe des liens et preuves,
navigation complète, couverture et historique. Sections adressables par ID de
note, chemin de titres, hash et références. Une modification de preuve indique
les sections affectées ; seuls leurs artefacts sont reconstruits. La navigation
est dérivée ; les nouvelles relations métier sont justifiées et revues.

### Recherche et interface

Ajouter `gov360 brain status`, `validate`, `build`, `context`, `evaluate`,
`export`, `bootstrap`, `release-kit`, en conservant les commandes existantes.
Utiliser SQLite FTS5/BM25, alias et vocabulaire FR/EN versionné, sans service
distant ni embeddings. Filtrer accès, domaine, juridiction, date et revue avant
classement ; expansion du graphe bornée à un saut ; joindre les preuves ;
retourner lacunes, conflits et exclusions. Le paquet versionné dispose par
défaut de 6 000 tokens estimés pour l'ensemble sérialisé. Ne pas stocker de
réponses projet. Assistance : preuves résolues et sections revues seulement.
Recherche documentaire : contenu non approuvé clairement identifié, activé
explicitement, jamais en repli automatique.

### Export OKF

Cibler [OKF v0.2](https://raw.githubusercontent.com/GoogleCloudPlatform/open-knowledge-format/main/SPEC.md)
et enregistrer la révision utilisée. Produire sous dist un bundle avec liens
Markdown standards, index et log générés, mapping IDs/chemins, provenance,
sources et cycle de vie attestés. Convertir active en stable uniquement dans
l'export. Ne remplir verified que pour une vérification attestée ; distinguer
approbation de publication et vérification du contenu. Attribution des
affirmations uniquement lorsque la liaison aux preuves est établie. Export
public limité aux droits explicitement autorisés ; export local avec références
accessibles au détenteur du corpus.

### Évaluation

45 scénarios FR/EN couvrant 15 piliers : 30 recherches soutenues et 15 cas de
lacune, conflit, exclusion ou non-applicabilité. Cas réels par IDs, jamais de
texte brut dans les tests ; fixtures techniques synthétiques. Objectifs :
référence attendue dans le top 5 pour au moins 90 % des cas répondables ; 100 %
des citations résolubles ; aucune fuite de contenu exclu ; lacunes explicites ;
NOOP sans appel LLM. Séparer préparation des preuves et score de récupération.

## 4. Organisation, documentation et kit Git

Quatre responsabilités : CDO programme lead ; extraction/audit indépendant ;
domain builder ; release reviewer indépendant. Assemblage et artefacts par
outils déterministes. Maximum trois shards indépendants. Mesurer appels,
tokens, temps, reprises et coûts disponibles ; une mesure absente est unknown,
pas zéro. Modèles dans profils, escalade sur tâches sensibles.

Aligner AGENTS, WORKSHOP, ROADMAP, SCHEMA, README, manue, documentation
opérationnelle, prompts, wrappers, commandes et skills. Le manuel décrit les
responsabilités, commandes, messages types, reprise, preuve/connaissance/contexte,
revue, approbation, maintenance et reconstruction. Un contrat canonique par
sujet, les autres documents y renvoient.

Préparer le kit dans un dossier distinct, par liste autorisée, sans historique
Git actuel. Inclure code original Apache-2.0, contrats, profils sans secrets,
documentation et tests synthétiques ; manifeste de sources (IDs, hashes,
chemins relatifs, adaptateurs et acquisition connue) ; seulement les contenus
et métadonnées autorisés. Exclure originaux, extractions, citations brutes,
caches, configurations personnelles et contenus de droits inconnus.

Bootstrap retrouve les fichiers locaux par hash, conserve les IDs, reconstruit
ingest et vérifie les hashes attendus. Une divergence impose une revue, pas une
réécriture de l'approbation. Ne pas promettre la reproduction à l'octet des
synthèses LLM.

Créer git_helper : prompt canonique, wrappers Codex/OpenCode. Vérifier le kit,
tester la reconstruction propre, préparer liste de commit, notes de release et
manifeste de hashes. Push et publication distante seulement après autorisation
explicite distincte.

## 5. Exécution et réception

1. Enregistrer ce plan et la baseline.
2. Réconcilier états, preuves et contrats.
3. Matrice de couverture et pilote métier.
4. Catalogue, graphe, contexte et évaluations.
5. Export OKF.
6. Revue et dossier d'approbation du pilote.
7. Documentation et kit pour git_helper.
8. Poursuite des lots métier suivant la matrice.

Tester preuves absentes/altérées, revue périmée, auteur identique au reviewer,
mauvais hash d'approbation ; compatibilité IDs/frontmatter/liens/FR-EN ;
atomicité, reprise, NOOP ; accès, modalités mixtes, supersession et budget ;
OKF alias/espaces/ancres/provenance/droits ; reconstruction propre avec sources
présentes, absentes ou différentes ; suite existante et tests ciblés.

La réception distingue socle technique, contenus effectivement revus/publiés et
couverture restant à construire. Aucun pourcentage de complétude ne découle du
seul nombre de notes.

## 6. Diagnostic actualisé et décision CDO proposée

Le dépôt dispose maintenant d'une chaîne opérationnelle de connaissance :
ingestion avec provenance, preuves revues, propositions, approbations liées aux
hashes, publication déterministe, catalogue de sections et recherche locale.
La priorité est de rendre ses garanties mesurables jusqu'au contexte consommé
par l'agent, puis d'étendre la couverture là où les preuves manquent réellement.
Créer davantage de notes sans réconcilier ces états augmenterait le travail de
revue sans démontrer une amélioration de l'assistance.

### 6.1 Périmètre de l'analyse

Lecture de `AGENTS.md`, `WORKSHOP.md`, `ROADMAP.md`, `brain wiki/SCHEMA.md`, du
programme initial, des rôles, wrappers, skills et commandes ; inspection des
contrats, du code de production, des tests, des inventaires, reçus et dérivés.
Tous les dossiers racine sont examinés dans la section 7. Les originaux sont
inventoriés et contrôlés par hash, sans être utilisés comme contenu par un rôle.
Les environnements, caches, dépendances installées et l'historique Git ne font
pas l'objet d'une lecture exhaustive de leur contenu. L'analyse est locale ;
elle ne constitue pas une nouvelle vérification juridique auprès des éditeurs.

L'arbre Git comporte déjà de nombreuses modifications et des fichiers non
suivis. Cette actualisation modifie uniquement `plan.md` ; elle ne réinitialise
pas ces travaux. Le fichier est actuellement ignoré par `.gitignore` : il faudra
traiter explicitement son inclusion dans la documentation partageable du lot U08.

### 6.2 Baseline constatée

| Objet | État constaté | Portée de la mesure |
| --- | --- | --- |
| Sources logiques | 47 : 46 prêtes pour les rôles, 1 en quarantaine | Manifestes ; pas 47 preuves d'autorité équivalente |
| Ingestion | 46 `document.json`, 2 863 unités, 46 aperçus Markdown | 2 909 fichiers Markdown au total ; aperçus et unités distincts |
| Indicateurs visuels | 236 unités marquées `REVIEW_REQUIRED` | Ne pas assimiler ce nombre à 236 revues encore ouvertes : consulter les reçus de fidélité |
| Vault | 177 notes : 116 connaissances, 50 questions, 11 index | Les 11 index comprennent les deux fichiers d'entrée humains |
| Sections | 971, dont 514 avec preuves résolues et revues | Les 457 autres ne sont pas toutes des affirmations défectueuses : navigation et références sont aussi sectionnées |
| Publication | 170 notes avec chaîne de publication vérifiée ; 5 avertissements | Publication, éligibilité du contexte et autorité restent distinctes |
| Graphe | 0 connaissance sans lien entrant | Un lien entrant ne mesure pas la pertinence sémantique du graphe |
| Preuves | 37 reçus, 772 références ; 0 anomalie technique de preuve | Ni certificat de fidélité universelle ni avis juridique |
| Dates et périmètre | 772 références sans bornes `valid_from`/`valid_until` ; 213 sans juridiction | Métadonnées inconnues, pas preuves d'obsolescence ou d'applicabilité universelle |
| Couverture | 150 cellules générées `UNASSESSED` | Le générateur ne projette pas les décisions approuvées par critère |
| Registre des piliers | 2 `APPROVED`, 10 `EVIDENCE_READY`, 3 `SOURCE_GAP` | Statuts au niveau pilier, distincts de ceux des cellules |
| Questions | 50 questions ; 32 dépendances | Schéma valide ; équivalence FR/EN et intention restent des objets de revue |
| Retrieval | Checkpoint historique : 30/30 positifs éligibles, 29/30 dans le top 5 ; 15/15 négatifs réussis. Checkpoint courant : 30/30 et 15/15 | Historique `recall_at_5 = 0.9666666666666667`; courant `recall_at_5 = 1.0` après vocabulaire bilingue, scénarios inchangés |
| Tests | 112 tests réussis | Garanties techniques couvertes par ces tests uniquement |
| Propositions | 46 manifests : 43 `INTEGRATED`, 1 `PROPOSAL_READY`, 2 `DRAFT` | Plusieurs manifests peuvent partager un candidat ; ne pas compter 43 publications indépendantes |

Références locales : `state/source_manifest.jsonl`, `ingest/*/document.json`,
`state/derived/brain/baseline.json`, `evidence-index.json`, `coverage-matrix.json`
dans ce même dossier, `state/workshop/coverage/coverage-register.json`, les
manifests de `state/workshop/proposals/` et la commande `gov360 brain evaluate`.
Les contrôles recalculés priment sur les sorties enregistrées devenues anciennes.

### 6.3 Travaux à conserver et à réutiliser

- Les lots AI concepts P0/P1/P2, les contrôles et incidents ATLAS, la
  qualification juridique, l'article 22, DPIA/FRIA et l'article 35, ainsi que
  les lots de sécurité, tiers, validation, traçabilité et gouvernance sont
  présents dans l'historique intégré. Ne pas recommencer leur synthèse.
- `p0-coverage-completion-20260920` a intégré 24 fichiers : 18 connaissances,
  2 index et 4 questions, avec 96 références revues pour les 20 cellules P0.
  Candidat approuvé :
  `62efa5e600896f498e0316f434d0ea544c8bafb8c4e77f67b7471ce9e9b48f7d`.
  Sa carte de couverture est un point d'entrée pour U01 ; elle n'autorise pas
  à déclarer toutes les autres cellules complètes.
- La décision de registre `coverage-state-p0-20260920` porte le hash
  `61b7c7e46b1448fe4ce0e0fbebb58b34c3589172f301105304764f07f249b975`.
  Un reçu de métadonnées n'est pas un reçu de publication de note.
- Les lots `strict-ai-lifecycle-change-001`, `strict-people-ai-literacy-001`
  et `strict-sustainability-societal-impact-001` partagent le candidat intégré
  `9bc17ff79c9e722b3db777f24a01323260bb66b6040f4641d8d343ef09fb715e`.
  Les trois piliers encore `SOURCE_GAP` doivent être réexaminés à la lumière
  de ces apports, sans promotion automatique à `COMPLETE`.
- Les réparations de provenance et de liens sont réutilisables. Les cinq
  avertissements de filiation restants concernent `mit-ai-risk-initiative`,
  `digital-omnibus`, `sr-11-7`, `2022-air-canada-chatbot` et
  `2023-chevrolet-of-watsonville`. Les traiter individuellement ; ne pas
  fabriquer d'approbation rétroactive.

La structure `plan-finalization-20260920` contient un manifeste `DRAFT` et des
ébauches techniques isolées pour couverture, retrieval et ATLAS. Les trois
sessions parallèles ont été interrompues pour cette analyse. Aucun de ces
fichiers ne constitue une implémentation intégrée ou revue. Son `execution.json`
reste un état de lancement (`IN_PROGRESS`) et référence `pland.md`, absent au
moment du contrôle. À la reprise, réconcilier ce reçu d'exécution avec les
artefacts réellement livrés, sans attribuer de succès aux contrôles `PENDING`.

## 7. Analyse de tous les dossiers

Comptages hors `node_modules` et `__pycache__`. Ce tableau localise les enjeux ;
il ne prescrit pas de déplacement massif de dossiers.

| Dossier | Constat | Suite proposée |
| --- | --- | --- |
| `sources/` | 54 fichiers physiques, dont 43 PDF et 6 annexes Windows ; différent des 47 sources logiques | Préserver intégralement ; exploiter manifestes et hashes ; vérification locale ciblée selon autorisation |
| `ingest/` | 2 955 fichiers, dont 46 documents de validation | Réutiliser les unités valides ; extraction avancée ciblée et versionnée, jamais réécriture silencieuse |
| `brain wiki/` | 177 Markdown, 1 Canvas, 5 fichiers Obsidian | Conserver noms, IDs, frontmatters et navigation ; améliorer les liens seulement avec justification |
| `config/` | 21 fichiers : schémas, domaines, benchmark, vocabulaire, droits et profils | Versionner toute évolution ; distinguer contrats actifs et historiques |
| `domain_packs/` | 10 packs et 1 modèle | Réutiliser leur routage ; aucun nouveau domaine sans lacune et revue explicites |
| `src/` | 39 modules Python ; ingestion, atelier, preuves, retrieval, dérivés et partage | Corriger les écarts U01–U05 par changements ciblés et tests synthétiques |
| `tests/` | 14 fichiers Python ; 112 cas exécutés | Ajouter les cas de contrat manquants, conserver les régressions actuelles |
| `prompts/` | 10 rôles canoniques | Clarifier entrées/sorties et responsabilités ; aucun modèle dans les prompts |
| `.codex/` | 1 configuration et 10 wrappers TOML, syntaxe analysable | Vérifier le comportement effectif lors de la reprise ; ne pas déduire les permissions de la seule syntaxe |
| `.opencode/` | 10 agents et 10 commandes, configuration locale et dépendances | Tester résolution des rôles, permissions et commandes avec la version installée |
| `.agents/` | 6 skills et leurs références | Conserver un rôle procédural ; aligner après changements de contrats, sans dupliquer les règles |
| `.vscode/` | Tâche de surveillance des dérivés | Vérifier VSCodium, lancement unique et arrêt propre ; documenter l'usage indépendant de l'éditeur |
| `state/` | Manifestes, classifications, preuves, propositions et sorties générées | Séparer état attesté, diagnostics et caches ; voir détail ci-dessous |
| `dist/` | Exports, kit, copies de concepts et configuration Obsidian | Identifier propriétaire et commande de reconstruction de chaque sortie ; ne pas traiter une copie comme canonique |
| `docs/` | Démarrage Ubuntu, OpenCode et mapping OKF | Aligner avec les commandes effectivement testées |
| `tools/` | 2 scripts PowerShell historiques | Conserver comme historique ; ne pas les remettre dans le circuit actif sans besoin démontré |
| `proposals/` | Aucun fichier actuellement | Le chemin de travail reste `state/workshop/proposals/` ; documenter cette distinction |
| `.git/` | Historique et état local avec de nombreux changements | Ne pas transférer l'historique dans le kit ; aucune remise à zéro |
| `.venv/` | Environnement local généré | Reconstruction par `uv`, hors partage et hors corpus |
| `.pytest_cache/`, `.pytest_tmp/` | Résultats temporaires de tests | Hors preuves, hors kit ; ne pas les interpréter comme des reçus métier |

Dans `state/`, les responsabilités doivent rester lisibles :

| Sous-ensemble | Utilisation et point de vigilance |
| --- | --- |
| `state/derived/brain/` | Catalogue, baseline, preuves, couverture, navigation et réconciliation ; reconstruire depuis les entrées, jamais corriger à la main |
| `state/derived/` | Registre de questions, catalogue ATLAS et manifests ; Canvas reconstruit dans le vault |
| `state/workshop/evidence-library/` | Preuves et liaisons affirmation/section ; validité liée aux hashes et à la revue |
| `state/workshop/coverage/` | Registre des piliers et lacunes ; `criterion-reviews.json` est attendu par le code mais absent |
| `state/workshop/proposals/` | Candidats et historique des lots ; les diagnostics sans manifest ne sont pas des releases |
| `state/workshop/reviews/` | Revues ; préserver identité, indépendance, hash et portée |
| `state/workshop/brain-upgrade/` | Baseline et reçus techniques/fidélité ; ne pas généraliser une vérification ciblée à tout le corpus |
| `state/workshop/cdo-reference/`, `drafts/`, `questionnaire-canvas/` | Entrées éditoriales et références ; jamais preuves d'autorité |
| `state/workshop/release-preparation/` | Dossier de partage ; l'accord local historique n'autorise pas une publication Git distante |
| `state/legacy/`, `state/legacy-vault-v1/` | Imports et contrats historiques ; conserver l'interdiction de leurs writers sur le vault actif |
| `state/runs/` | Exécutions locales ; journaliser uniquement métadonnées autorisées, pas les textes sources |

Lors de l'inventaire initial, `manue.md` et `manuel.md` étaient des copies identiques,
tandis que `outils.md` et `fonctionnement.md` renvoyaient au manuel. Au démarrage
de l'exécution, seul `manuel.md` subsiste ; l'opérateur confirme ce nom comme
référence pédagogique unique le 21 septembre 2026. U07 doit aligner les liens et
prévoir une redirection compatible pour l'autre nom après vérification des liens.
`all_show.md` et `presentation.md` sont des supports de communication, pas des
registres de validation. Aucun fichier vidéo/GIF de présentation n'est constaté
dans `dist/` lors de cet inventaire : sa réalisation et sa vérification restent
à prouver, même si la conversation précédente les évoquait.

## 8. Écarts à corriger en priorité

Les sévérités ci-dessous priorisent le programme ; elles ne constituent pas un
verdict de conformité juridique.

| ID / priorité | Écart vérifié | Effet et traitement |
| --- | --- | --- |
| A01 / P0 | `coverage_matrix()` lit les revues mais génère toujours `UNASSESSED` | Les avancées métier ne sont pas projetées par critère ; U01 |
| A02 / P0 | Des statuts de piliers et passages de ROADMAP précèdent les derniers lots | Réconcilier avec reçus et couverture précise, préserver l'historique ; U01/U07 |
| A03 / P0 | `_SECTION_FIELDS` omet `modality` pourtant présent dans le catalogue | Le contexte perd la distinction obligation/recommandation/contexte ; U02 |
| A04 / P0 | Dates d'applicabilité non renseignées ; revue sans politique explicite d'expiration | Ne pas promettre la validité à une date donnée ; qualifier les inconnues et impacts ; U02 |
| A05 / P0 | Cinq filiations de publication restent non résolues | Maintenir les exclusions nécessaires, préparer une remédiation bornée ; U01/U06 |
| A06 / P1 | Mode `research` limité au Markdown publié non résolu | L'exploration explicite du Markdown validé d'ingest prévue au plan reste à livrer ; U05 |
| A07 / P1 | `atlas_catalog()` relit le JSON original malgré le contrôle de l'unité | Achever sa dérivation déterministe depuis ingest validé ; U05 |
| A08 / P1 | `eval-11-fr` retourne des voisins peu pertinents et une omission pour budget | Corriger classement/vocabulaire/sélection sans modifier les réponses attendues pour gagner le test ; U04 |
| A09 / P1 | Compilation complète et index FTS en mémoire reconstruits à chaque requête | Mesurer le coût avant de choisir un cache à invalidation sûre ; U04 |
| A10 / P1 | Permissions d'édition OpenCode couvrant plusieurs propositions/revues | Restreindre au lot attribué lorsque le runtime le permet ; tests négatifs ; U03 |
| A11 / P1 | Certains reviewers n'ont accès ni à ingest ni au shell | Fournir un paquet attesté suffisant ou escalader vers l'auditeur ; ne pas déclarer une vérification impossible ; U03 |
| A12 / P1 | Commandes mélangeant `subtask` et `subagent` ; revue stricte et rôle décrit comme fast | Vérifier le runtime avant correction, clarifier le contrat ; U03 |
| A13 / P1 | Télémétrie de nombreux lots incomplète | Conserver `unknown`, instrumenter les prochains lots ; U03 |
| A14 / P1 | Canvas non courant au contrôle textuel, mais JSON identique au recalcul | Régénérer par l'outil, sans modifier les questions ni créer une revue métier artificielle ; U07 |
| A15 / P1 | Catalogue dérivé, export OKF et kit enregistrés non courants | Reconstruire après réconciliation, vérifier le NOOP et les droits explicites ; U07/U08 |
| A16 / P2 | Dépendances PDF avancées optionnelles mais chaîne courante surtout native | Ne pas présenter Docling/OCR comme utilisé partout ; traitement ciblé des lacunes utiles ; U05 |
| A17 / P2 | Documentation dupliquée et indicateurs historiques présentés sans date | Une référence par sujet, preuves locales et date de mesure ; U07 |

Fichiers de diagnostic principaux : `src/gov360_brain/brain/catalogue.py`,
`retrieval.py`, `evidence.py`, `portability.py` dans le même dossier,
`src/gov360_brain/derived.py`, `src/gov360_brain/adapters/pdf.py`,
`config/schemas/brain-context.schema.json`, `.opencode/agents/`,
`.opencode/commands/`, et les reçus de `state/workshop/`.

## 9. Programme complémentaire proposé : huit lots vérifiables

Les priorités P0/P1/P2 ci-dessus sont celles de cette actualisation, distinctes
des noms historiques des lots AI concepts. Aucun gain de coût ou délai chiffré
n'est promis sans mesure. Les nouveaux champs ci-dessous sont des propositions,
pas des champs déjà disponibles dans les contrats.

### U01 — Réconcilier la couverture et les publications

**Résultat utile :** savoir ce qui est effectivement couvert, à quel niveau,
par quelles notes et preuves, et pourquoi une lacune reste ouverte.

1. Rejouer les reçus existants, commencer par les 20 cellules P0 et les trois
   lots lifecycle/literacy/sustainability. Séparer intégration de note,
   approbation de métadonnées et décision de complétude d'un critère.
2. Proposer un contrat versionné de revue par cellule : pilier, critère,
   justification, notes/sections/questions, références de preuves, hashes des
   entrées, auteur/reviewer, décision et approbation associée si nécessaire.
3. Adapter le projecteur de couverture pour consommer uniquement des décisions
   valides. Entrée absente, ambiguë ou périmée : diagnostic explicite ; aucune
   promotion déduite d'un chevauchement de domaines.
4. Classer les 150 cellules : couverture attestée, partielle, preuve disponible
   à revoir, source manquante ou revue non réalisée. Mapper les états au contrat
   adopté ; ne pas inventer de statuts directement dans les dérivés.
5. Préparer le traitement des cinq filiations historiques ; laisser le blocage
   en place lorsque le reçu adéquat manque.

**Livrables :** contrat de revue, projecteur testé, dossier de réconciliation et
backlog par cellule. **Réception :** chaque changement de statut est traçable ;
reçu altéré ou hash périmé refusé ; seconde exécution sans diff ; les cellules
sans décision restent non évaluées. La fin du lot technique n'exige pas de
prétendre toutes les cellules complètes. **Circuit : strict**, car contrat.

**Checkpoint U01 — 21 septembre 2026 :** le dossier
`state/workshop/proposals/coverage-reconciliation-u01-20260921/` contient les
150 cellules, le contrat de proposition, le rapport et la référence exacte au
lot P0 approuvé. Il recommande 18 cellules `EVIDENCE_APPROVED`, 2
`NAVIGATION_ONLY`, 100 `REVIEW_REQUIRED` et 30 `SOURCE_GAP`. Le registre actif
et les dérivés ne sont pas modifiés ; la revue indépendante et la projection
déterministe restent à faire.

### U02 — Préserver la qualification dans le contexte de l'agent

**Résultat utile :** l'agent voit ce qui relève d'une obligation, recommandation,
définition ou information contextuelle, avec la portée réellement établie.

- Transmettre `modality` du binding jusqu'au paquet de contexte ; incrémenter
  la version du schéma et tester la compatibilité des consommateurs.
- Distinguer date du document, date d'application, date de revue et éventuelle
  échéance de revue. Une borne manquante reste inconnue. N'inventer aucune date
  à partir de la date d'extraction ou de la publication d'une note.
- Définir une politique explicite pour les demandes sensibles à l'actualité :
  signalement d'incertitude, exclusion ou escalade selon le cas, plutôt qu'une
  assurance générale « à jour ».
- Relier un changement de source/preuve/revue aux sections, questions et exports
  affectés. Invalider leur éligibilité et leurs caches de façon déterministe.
- Préserver conflits, applicabilité et restrictions d'accès dans le contexte,
  y compris dans une note mêlant droit et guidance.

**Réception :** fixtures de modalités mixtes, juridiction absente, dates connues
et inconnues, révocation/supersession et hash modifié ; aucune obligation issue
d'une source non `BINDING` revue ; absence de repli automatique sur research.
**Circuit : strict** pour contrat et toute nouvelle qualification de preuve.

### U03 — Rendre le harness moins coûteux et réellement contrôlable

**Résultat utile :** une tâche bornée, un responsable d'écriture, une revue
indépendante et un paquet minimal d'entrées par agent.

| Rôle canonique | Responsabilité attendue dans la suite |
| --- | --- |
| `cdo_program_lead` | Choisir le prochain manque utile, la portée et les critères de sortie ; ne pas attribuer d'approbation |
| `source_extractor` | Extraire les candidats des seules unités validées assignées avec locators |
| `evidence_auditor` | Vérifier fidélité attestée, autorité, portée et validité des preuves indépendamment de l'extraction |
| `knowledge_architect` | Concevoir les ajouts/modifications justifiés, vérifier doublons et relations |
| `questionnaire_curator` | Produire les questions atomiques FR/EN, topics et dépendances |
| `questionnaire_reviewer` | Revoir intention, doublons, équivalence et dépendances |
| `vault_reviewer` | Revoir schéma, liens, provenance et cohérence du candidat |
| `domain_builder` | Construire ensemble notes et questions dans le seul overlay attribué |
| `release_reviewer` | Revue consolidée indépendante ; escalade stricte lorsque nécessaire |
| `git_helper` | Préparer kit et dossier local après contrôles ; aucune publication distante implicite |

Le circuit fast réutilise des preuves revues et ne déclenche pas tous ces rôles
systématiquement. Le strict ajoute les étapes justifiées par les changements.
Les spécialistes interviennent sur un défaut identifié, pas pour répéter une
revue inchangée.

Créer un brief immuable par tâche : objectif, fichiers d'entrée et hashes,
preuves autorisées, chemin de sortie, fichiers interdits, critères de sortie,
profil de traitement et informations d'autorisation distante le cas échéant.
Tester que l'agent ne peut pas écrire dans le lot voisin, le vault, les preuves
historiques ou l'approbation. Le coordinateur assemble ; le reviewer ne s'approuve
pas lui-même. Pour les reviewers privés d'ingest, rendre vérifiable le paquet
fourni ou confier la vérification documentaire au rôle qui y est autorisé.

Conserver les rôles indépendants du fournisseur. Tester Codex et OpenCode avec
des fixtures locales, sans appel distant non autorisé. L'affectation de modèles
reste dans les wrappers/profils ; cette analyse ne change pas les choix existants
et ne fait aucune promesse de tarif. Les sessions Luna high précédentes restent
des travaux interrompus, à reprendre seulement selon la tâche effectivement lancée.

**Réception :** commandes reconnues par le runtime testé, permissions négatives
vérifiées, sortie par lot, absence de secret/contenu brut dans les logs,
mesures disponibles de durée/appels/tokens/coût ; valeurs absentes `unknown`.
La réutilisation d'un audit exige les mêmes hashes, portée et validité.

### U04 — Améliorer la recherche sans masquer ses limites

**Résultat utile :** le bon contexte cité dans un budget explicite, avec une
performance reproductible et des exclusions compréhensibles.

1. Diagnostiquer `eval-11-fr` : vocabulaire FR/EN, poids titre/section, voisins du
   graphe et occupation du budget. Conserver les IDs attendus du benchmark.
2. Versionner les améliorations lexicales générales et les vérifier sur des
   paraphrases indépendantes ; ne pas coder une réponse spéciale au scénario.
3. Clarifier la métrique actuelle : pour chaque scénario positif éligible, au
   moins un ID attendu doit apparaître parmi les cinq premières notes uniques
   du paquet. C'est un taux de succès par scénario ; il ne mesure pas le rappel
   de toutes les preuves pertinentes ni la qualité d'une réponse LLM.
4. Conserver les 45 cas de référence, ajouter séparément une suite d'extension
   pour dates, permissions, questions conditionnelles, conflits et abstention.
5. Mesurer latence à froid/chaud et coût de compilation ; n'introduire un index
   persistant/cache que si le gain est démontré. Clé d'invalidation : contenu,
   schémas, vocabulaire, accès, revues, dates et état de publication pertinents.

**Réception :** seuil initial ≥ 0,90 conservé ; cible de réparation 30/30 succès
sur les positifs actuels, 15/15 négatifs maintenus, citations résolubles, aucune
fuite via le graphe ou le cache. Le checkpoint historique était 30/30 prêts,
29/30 hits et `recall@5 = 0,9667` avec `eval-11-fr` à améliorer ; le progrès U04
atteint localement 30/30 hits et `recall@5 = 1,0` sans modifier les scénarios.
Budget mesuré sur le paquet entier ; les
omissions restent signalées. Pas d'embeddings ni de service distant requis.

### U05 — Exploiter ingest et cibler la fidélité utile

**Résultat utile :** explorer le corpus non encore synthétisé sans confondre
recherche documentaire et assistance fondée sur des connaissances publiées.

- Ajouter une voie explicite de recherche dans les unités validées sous
  `ingest/`, avec source ID, hashes, locator, restrictions et label de recherche
  non approuvée. Les unités invalides/quarantainées restent exclues.
- Dériver ATLAS depuis l'unité Markdown validée et son sélecteur d'objet ;
  conserver le hash parent et vérifier la parité des objets/relations. Le
  code actuel contrôle l'unité mais ouvre encore le JSON original.
- Prioriser la fidélité sur les pages `REVIEW_REQUIRED` nécessaires aux lacunes
  choisies. Résoudre d'abord les reçus existants ; ne pas réexaminer toutes les
  pages par défaut.
- Utiliser rendu visuel, extraction de tableaux ou OCR local uniquement selon
  le défaut constaté. Le pipeline courant utilise notamment `pypdf` ; la
  présence de dépendances optionnelles `docling`/`pdfplumber` ne prouve pas leur
  utilisation. Un reçu ciblé PyMuPDF existe ; il ne valide pas tout le corpus.
- Si une extraction corrigée change un hash, produire une version/candidature
  traçable et analyser les utilisateurs de l'ancienne unité. Ne pas remplacer
  silencieusement l'unité ayant servi à une approbation.

**Réception :** ATLAS reconstructible depuis ingest validé sans lecture de
l'original par le rôle ; locators conservés ; tests de hash altéré et unité
invalide ; research isolé de l'assistance ; registre de fidélité distinguant
signal initial, revue effectuée et problème restant. **Circuit strict** pour
nouvelles preuves, nouvelles extractions utilisées ou contrats.

### U06 — Compléter la connaissance selon la valeur pour l'assistance

**Résultat utile :** répondre aux besoins réels d'un agent de gouvernance, sans
produire de doublons ou de fausse exhaustivité.

Après U01, sélectionner les cellules non couvertes selon impact, fréquence
d'utilisation, caractère transversal, disponibilité des preuves et effort de
revue. Examiner d'abord ce que le corpus et les notes couvrent déjà.

| Besoin utilisateur de l'agent | Complément à examiner, seulement si une lacune est confirmée |
| --- | --- |
| Cadrer l'usage et décider du niveau de contrôle | Finalité, valeur attendue, alternatives, proportionnalité, responsabilités et gates |
| Justifier qualité et limites | Adéquation des données/modèles, représentativité, incertitude, validation et critères d'acceptation |
| Gouverner une IA agentique | Autorité déléguée, outils/MCP, identités, actions irréversibles, supervision et arrêt |
| Gérer l'exploitation | Changements, dérive, incidents, retour d'expérience, recours et retrait |
| Maîtriser les dépendances | Tiers, composants, responsabilités partagées, concentration, réversibilité et sortie |
| Maintenir un dispositif responsable | Littératie, organisation, assurance indépendante, impacts sociétaux et durabilité |

Pour chaque sujet retenu : partir de la note existante, qualifier l'applicabilité,
expliciter acteur/action/artefact lorsque la preuve le permet, relier les concepts
utiles et ajouter une question seulement si son intention n'existe pas déjà.
Les incidents éclairent le risque ; ils ne créent pas une obligation. Le RGPD
reste conditionné au traitement de données personnelles ; il ne suffit pas à
établir toute la qualité des données. Une source normative partielle ne permet
pas d'affirmer la couverture de la norme entière.

**Livrables :** petits candidats v3 avec preuves revues, notes, questions FR/EN,
carte de couverture et revue indépendante. **Réception :** aucun ajout non
étayé ; chaque gain de couverture démontré ; approbation humaine du hash avant
assemblage. Si le corpus ne suffit pas, livrer une lacune qualifiée et une
proposition d'acquisition ; ne pas compenser par l'invention.

### U07 — Unifier l'expérience Obsidian et la documentation

**Résultat utile :** un contributeur comprend où travailler, comment reprendre
un lot et ce que le Brain sait effectivement fournir.

- Conserver les dossiers/IDs existants et les index métier ; ne pas déplacer
  les connaissances pour obtenir une arborescence plus esthétique.
- Régénérer le Canvas par le constructeur déterministe, vérifier le NOOP puis
  le watcher à l'ajout d'une question approuvée. Son écart actuel est de
  sérialisation : le JSON comparé au recalcul est sémantiquement identique.
- Faire de `manuel.md` la référence pédagogique (choix confirmé par l'opérateur
  le 21 septembre 2026), avec liens depuis les anciens
  noms ; aligner les guides Ubuntu/Codex/OpenCode et les messages types.
- Mettre `ROADMAP.md` à jour avec jalons datés, travaux intégrés et backlog
  actuel. Ne pas effacer les anciens résultats 1,0 du benchmark ; indiquer
  qu'ils décrivent un checkpoint antérieur au résultat actuel 0,9667.
- Actualiser `presentation.md` depuis des mesures datées et renvoyer au manuel.
  `all_show.md` est absent de l'état de travail du 21 septembre au soir ; ne pas
  le recréer comme deuxième manuel ni conserver de liens vers ce fichier absent.
  Pour une démonstration Obsidian, capturer localement navigation, concept,
  références, graphe et Canvas dans un périmètre autorisé. Vérifier le fichier
  vidéo/GIF produit, sa lisibilité, sa durée et l'absence de données sensibles.

**Réception :** un parcours documenté fonctionne sous les deux outils, sans
contenu canonique dupliqué, sans chemin personnel et sans confusion entre export
et vault actif. Une capture n'est pas une preuve de retrieval ou d'approbation.

### U08 — Livrer un kit reproductible et une release locale explicite

**Résultat utile :** un détenteur légitime du corpus peut reprendre le travail
avec les outils, contrats et procédures nécessaires.

1. Réconcilier le périmètre du kit et celui de l'export OKF ; l'un distribue les
   outils, l'autre une vue dérivée de connaissances selon les droits établis.
2. Refaire les contrôles `--check`, reconstruire dans le dossier de sortie
   prévu et vérifier qu'une seconde exécution ne produit pas de diff.
3. Inclure une documentation complète et portable, dont ce programme selon
   l'allowlist retenue ; exclure sources, ingest, citations brutes, secrets,
   configuration personnelle et historique Git de travail.
4. Tester bootstrap dans un environnement propre avec fixtures synthétiques,
   puis les contrôles autorisés sur le corpus local : présent, absent, hash
   différent. Les synthèses LLM et approbations ne sont pas recréées par magie
   à partir des PDF ; documenter ce qui se reconstruit et ce qui exige une
   décision de droits ou un transfert séparé autorisé.
5. Faire préparer par `git_helper` le manifeste de fichiers/hashes, la liste de
   changements, les résultats, limites et instructions de reprise. Soumettre
   le dossier concret avant toute publication distante.

**Réception :** kit validé et courant, reconstruction testée, droits connus ou
exclusions explicites, aucune fuite de contenu protégé ; commandes documentées
et testées. Un kit local prêt ne signifie pas une release distante publiée.

**Extension de transmission privée approuvée le 22 septembre 2026 :** conserver
le `release-kit` public filtré et construire séparément un handoff complet pour
`github.com/latifo01/governance-brain`, visibilité privée. Le handoff inclut le
corpus et ingest exacts autorisés, le vault, l'atelier et les dérivés, sans
historique Git de travail, environnement virtuel, cache ni credential. Son
manifeste lie chaque fichier à son hash et précise que le transfert privé ne
vaut ni licence publique ni approbation métier. La réception ajoute un clone
neuf sous Windows, le chargement OpenCode, une CI Linux/Windows et un rapport
`git_helper` indépendant avant le premier push.

## 10. Ordre d'exécution et parallélisation

```text
Baseline et périmètres figés
    ├── U01 : couverture / reçus
    ├── U02 : contexte qualifié
    └── U03 : harness / permissions
             ↓ revue et intégration technique séquentielle
    ├── U04 : retrieval / mesures  ← contrat U02 stabilisé
    ├── U05 : ingest / ATLAS       ← contrat U02 si paquet partagé
    └── U06 : lots métier         ← critères U01 et preuves auditées
             ↓
         U07 : dérivés / documentation / démonstration
             ↓
         U08 : kit / dossier de release local
```

Limiter à trois chantiers indépendants simultanés. U02 et U04 touchent le
retrieval : leur intégration est séquentielle ; leur diagnostic peut être
parallèle. U01 et U05 peuvent nécessiter des hooks de catalogue communs : le
coordinateur seul les assemble. Les workers écrivent dans des overlays
distincts ; aucune écriture concurrente dans le registre, les index ou le vault.

Le premier livrable recommandé est **U01**, avec la projection des décisions
déjà attestées pour les 20 cellules P0 et le relevé des décisions manquantes.
En parallèle, U02 et U03 peuvent préparer des candidats techniques isolés.
Une nouvelle preuve, interprétation, obligation, supersession ou modification
de contrat force le strict. L'approbation du plan n'approuve pas à l'avance les
hashes des futurs candidats de connaissance.

Pour maîtriser le coût : réutiliser les preuves revues inchangées, sélectionner
les unités utiles avant les appels, fournir un contexte borné par tâche,
assembler connaissance et questions avec la même preuve, automatiser les
dérivés et consolider la revue du candidat. Mesurer les reprises évitées et le
coût des prochaines exécutions ; ne pas reconstituer des coûts historiques
inconnus avec des zéros.

## 11. Vérification et critères de réception globaux

Contrôles exécutés pendant l'analyse locale, sans publication ni modification
des originaux. Les commandes sont à lancer depuis la racine avec l'environnement
`uv`. Un cache temporaire local a été utilisé lors de l'exécution.

| Commande / contrôle | Résultat constaté |
| --- | --- |
| `uv run --offline --no-sync python -m gov360_brain.workshop validate` | PASS : 177 notes, aucune erreur |
| `uv run --offline --no-sync gov360 brain validate` | PASS technique : 0 erreur, 5 avertissements, 514 sections revues |
| `uv run --offline --no-sync gov360 brain evaluate` | PASS : 30/30 prêts, 30/30 hits, 15/15 négatifs, recall@5 1,0 ; le checkpoint historique était 0,9667 |
| `uv run --offline --no-sync pytest -q --basetemp=/tmp/brain-plan-current-pytest` | PASS : 112 cas |
| `uv run --offline --no-sync python -m gov360_brain.workshop check-derived` | Écart : `valid=true`, `current=false`, zéro écriture ; Canvas seul concerné |
| `uv run --offline --no-sync gov360 brain build --check` | Écart : valide mais non courant ; 5 sorties à reconstruire, zéro écriture, baseline des sources inchangée |
| `uv run --offline --no-sync gov360 brain export --check` | Écart : export local valide mais non courant ; candidat de 219 fichiers, aucune écriture |
| `uv run --offline --no-sync gov360 brain release-kit --check` | Écart : kit valide mais non courant ; candidat de 146 fichiers, 47 sources inventoriées, aucune écriture |
| Comparaison JSON Canvas existant/recalculé | Identiques ; écart textuel de sérialisation |
| Analyse TOML `.codex/` | 11 fichiers analysables ; ne prouve pas l'exécution complète des agents |
| Comparaison au snapshot `plan-finalization-20260920/analysis/initial-inputs.json` avant édition du plan | 3 224 fichiers protégés inchangés ; parmi les 116 entrées d'implémentation, seul `pland.md` était absent |

Les contrôles de fraîcheur `gov360 brain build --check`, `export --check` et
`release-kit --check` doivent être renouvelés après toute intégration. Une
prévisualisation valide mais `current=false` n'est pas une sortie reconstruite.
Les sorties enregistrées de la baseline peuvent précéder le nouveau manifeste
de travail ; ne pas interpréter un changement de hash du catalogue comme un
changement automatique de connaissance.

La réception finale exige trois bilans séparés :

| Bilan | Critère de réussite |
| --- | --- |
| Socle technique | Tests et contrats valides, contexte qualifié, exclusions sûres, dérivés et kit courants, NOOP démontré |
| Connaissance publiée | Chaque modification intégrée liée à des preuves revues et à l'approbation humaine du candidat exact |
| Couverture métier | Chaque cellule avec décision justifiée ou lacune explicite ; aucun `COMPLETE` déduit du volume, du retrieval ou de la seule présence d'une note |

Le programme peut livrer un socle exploitable tout en conservant des lacunes
métier déclarées. Il ne peut être présenté comme une base de gouvernance
exhaustive tant que ces lacunes ne sont pas résolues. Le goal d'exécution
précédemment ouvert n'est pas déclaré achevé par cette mise à jour documentaire.

## 12. Invariants conservés et message de reprise

- Originaux immuables ; accès local ponctuel aux originaux pour une vérification
  de fidélité spécifiquement autorisée. Les rôles consomment ingest validé.
- Pas de transfert tiers implicite : profil `approved-remote`, endpoint et
  matière explicitement autorisés avant tout envoi de contenu.
- Intégrité, fidélité, autorité, applicabilité et approbation sont des garanties
  différentes ; aucun test ou hash ne les remplace toutes.
- Markdown canonique ; types, IDs, frontmatters, domaines et locators préservés.
  Le Canvas, le graphe, les catalogues et OKF restent des sorties dérivées.
- Pas de collecte de réponses projet, de score global ou de décision automatique
  de gouvernance dans ce dépôt.
- Pas de refonte globale, de nouveau fournisseur, d'embeddings, de déplacement
  du vault ou de dépendance supplémentaire sans besoin mesuré.
- Publication par assembleur après revue et approbation exacte ; Git distant
  soumis à une autorisation distincte sur un dossier concret.

Message suggéré pour lancer le prochain lot :

> Lis AGENTS.md, WORKSHOP.md, brain wiki/SCHEMA.md, ROADMAP.md et les sections
> 6 à 12 de plan.md. Commence U01 par les décisions existantes des 20 cellules
> P0 et la comparaison des reçus aux notes actives. Réutilise les preuves
> auditées, ne déduis aucune complétude des domaines ou du nombre de notes.
> Prépare un candidat technique et un dossier de réconciliation dans un lot
> attribué sous state/workshop/proposals/. Conserve les reçus historiques.
> Toute modification de contrat ou de preuve suit le strict. Fournis les
> tests, les décisions manquantes, le diff et la prochaine action précise.
> N'intègre aucun nouveau contenu métier sans l'approbation humaine de son hash.
