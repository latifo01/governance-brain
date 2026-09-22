# Atelier Governance 360

Le livrable autonome est `brain wiki/`. Le dépôt construit, contrôle et exporte
la connaissance et le catalogue bilingue de questions. Il construit également
la recherche locale par sections, les paquets de contexte cités et les exports
OKF. Il ne collecte aucune réponse projet et ne calcule aucun score global.

## Contrat actif

- Lire `AGENTS.md`, `ROADMAP.md` et `brain wiki/SCHEMA.md`.
- Valider les notes avec `config/schemas/brain-note.schema.json`.
- Conserver les types `knowledge`, `question` et `index`, les IDs kebab-case,
  les chemins actuels et les frontmatters existants.
- Garder les brouillons et propositions dans `state/workshop/`.
- Considérer `evidence_sources` comme un routage vers les Knowledge Banks, pas
  comme une preuve de revue.
- Considérer Markdown comme canonique pour les questions. Un Canvas est une vue
  dérivée ou une entrée éditoriale.

Les anciens schémas `vault-frontmatter.schema.json` et
`questionnaire.schema.json`, ainsi que les commandes `generate`, `approve`,
`normalize-vault` et `audit`, appartiennent au workflow v1. Le CLI les bloque
sur le vault actif. Ne pas les employer pour contourner l'atelier.

## Deux circuits de release

Les anciens manifests v1/v2 et leurs reçus restent lisibles pour audit ; les
nouveaux candidats de publication utilisent v3 et des preuves résolues. Ne pas
réécrire les reçus historiques pour leur attribuer une validation rétroactive.

Une release v3 regroupe un domaine cohérent et déclare `risk_tier: fast` ou
`strict` dans son manifeste. Le validateur force le circuit strict lorsqu'il
détecte une nouvelle preuve, une obligation ou interdiction, une interprétation
juridique, une modification de contrat ou une supersession.

Le circuit rapide part uniquement de preuves déjà revues. Un `domain-builder`
produit jusqu'à trois shards dans le même overlay, les contrôles déterministes
sont exécutés, puis un `release-reviewer` indépendant examine le candidat
complet. Le circuit strict ajoute l'extraction et l'audit indépendant des
preuves avant la construction. Les anciens rôles spécialisés restent
disponibles pour ces escalades.

Dans les deux cas, une seule approbation humaine lie le candidat consolidé à son
SHA-256 exact. Les limites ordinaires sont 30 notes de connaissance, 50
questions, 120 références de preuve et trois shards par release. Les index, le
registre de questions et le Canvas sont générés sans LLM.

## Parcours reproductible

1. **Inventorier.** Les fichiers CDO externes peuvent être inventoriés avec :

   ```sh
   uv run --offline --no-sync python -m gov360_brain.workshop inventory --cdo "$CDO_ROOT"
   ```

   L'inventaire conserve les originaux et place les entrées éditoriales dans
   `state/workshop/`. Un Canvas importé suit le même principe.

2. **Contrôler l'intégrité d'ingest.**

   ```sh
   uv run --offline --no-sync python -m gov360_brain.workshop quality
   ```

   Le résultat est technique. Comparer localement aux originaux les pages
   utilisées, les pages signalées et un échantillon déterministe. Consigner
   source ID, hash, locator, méthode, résultat et limites sans mettre le contenu
   brut dans les logs.

3. **Initialiser une release de domaine.**

   ```sh
   uv run --offline --no-sync python -m gov360_brain.workshop release-init \
     RISK risk-release-001 --risk-tier fast
   ```

   Compléter `evidence-lock.json`, le manifeste et au maximum trois shards. Un
   contenu inchangé reste `NOOP` et ne déclenche aucun LLM.

4. **Construire.** Utiliser `/brain-build <release>` pour le circuit rapide. Le
   constructeur compare le catalogue complet, produit ensemble connaissance et
   questions dans `future-vault/`, et escalade tout déclencheur strict. Le
   circuit strict exécute d'abord extraction et audit des preuves.

5. **Revoir.** Utiliser `/brain-review <release>`. Le reviewer consolide les
   contrôles de questions et de vault en un verdict lié au hash exact :
   `BLOCKED` ou `READY_FOR_HUMAN_APPROVAL`. Une revue réussie ne vaut pas
   approbation humaine.
   Pour une release stricte, utiliser `/brain-review-strict <release>` après
   l'audit des preuves ; le modèle de ce contrôle est choisi dans le wrapper fournisseur.

6. **Approuver et intégrer.** Présenter le diff concret et le rapport de revue à
   l'approbateur humain configuré. Seul un assembleur déterministe intègre un lot
   approuvé dans `brain wiki/`. Prévisualiser le candidat sans écriture :

   ```sh
   uv run --offline --no-sync python -m gov360_brain.workshop integrate \
     --proposal state/workshop/proposals/<lot-1> \
     --proposal state/workshop/proposals/<lot-2>
   ```

   Pour une release v3, inscrire également `Candidate SHA-256` dans
   `review/approval.md`. Après le statut `APPROVED`, appliquer le même ordre avec
   `--apply`. L'assembleur revalide le candidat, le rapport indépendant et le
   hash d'approbation, écrit atomiquement, puis reconstruit le registre et le
   Canvas. Une nouvelle exécution inchangée n'écrit aucun artefact.

7. **Valider.**

   ```sh
   uv run --offline --no-sync python -m gov360_brain.workshop validate
   uv run --offline --no-sync python -m gov360_brain.workshop check-derived
   uv run pytest -q
   git status --short -- sources/
   ```

   Lorsque deux lots forment un même candidat d'approbation, répéter
   `--proposal` dans l'ordre d'application. Le validateur combine les overlays
   et bloque les chemins de sortie en conflit.

## Couverture CDO

`state/workshop/coverage/coverage-register.json` suit les quinze piliers du
programme et leur état. Les états autorisés sont `SOURCE_GAP`,
`EVIDENCE_READY`, `PROPOSAL_READY`, `HUMAN_REVIEW`, `APPROVED` et
`COMPLETE`. La définition de fini est dans `ROADMAP.md`.

Les sept domaines macro et les dix Domain Packs actifs sont enregistrés dans
`config/brain-domains.json`. Une nouvelle valeur nécessite une proposition de
taxonomie revue. `domain-add` ne doit être utilisé qu'après cette approbation.

## Transmission privée au CDO

Le kit public et le dépôt privé de continuité ont deux contrats différents.
`gov360 brain release-kit` reste une liste de code et de procédures sans
originaux, ingest, vault métier ou historique Git. `gov360 brain handoff`
construit le snapshot privé autorisé par `config/private-handoff-policy.json` :
corpus exact, ingest validé, vault actif, état d'atelier et dérivés. Son
manifeste lie chaque fichier à son SHA-256 et rappelle que cette autorisation ne
constitue ni licence publique ni approbation d'une connaissance.

Construire puis contrôler le snapshot :

```sh
uv run gov360 brain handoff --output dist/cdo-handoff
uv run gov360 brain handoff --output dist/cdo-handoff --check
```

Le builder ne crée pas de dépôt Git, ne pousse rien et n'ajoute aucun
collaborateur. `git_helper` prépare ensuite le rapport local. La création du
remote et le push exigent une cible privée et l'autorisation opérateur
correspondante.

## Règles de release

Chaque release v3 contient un manifeste, `evidence-lock.json`, les futurs
fichiers du vault, un rapport de revue consolidé, `metrics.json` et un fichier
d'approbation humaine. Les statuts de proposition
ne doivent jamais être confondus avec le `status: active` que portera une note
après intégration approuvée.

Les sources et les chemins de téléchargement restent intacts. Ne stocker aucun
chemin absolu de poste dans un manifeste. Le dossier
`state/legacy-vault-v1/` reste historique. Les verdicts v1 et les contrôles
d'intégrité d'ingest doivent être réexaminés avant réutilisation.

## Registre et Canvas dérivés

Les questions Markdown actives sont l'unique source de vérité. Générer ou
contrôler les sorties avec :

```sh
uv run --offline --no-sync python -m gov360_brain.workshop build-derived
uv run --offline --no-sync python -m gov360_brain.workshop check-derived
uv run --offline --no-sync python -m gov360_brain.workshop watch-derived --interval 1
```

Les sorties sont `state/derived/question-registry.jsonl` et
`brain wiki/Risk analysis questionnaire.canvas`. L'intégration approuvée les
reconstruit dans sa transaction. La tâche VS Codium versionnée lance aussi le
watcher à l'ouverture du dossier.

## Construction et exploitation du Brain local

Le programme d'architecture approuvé est enregistré dans `plan.md`. Distinguer
les résultats techniques reproductibles de la couverture métier revue.

```sh
uv run gov360 brain status
uv run gov360 brain validate
uv run gov360 brain build
uv run gov360 brain build --check
uv run gov360 brain context "human oversight" --token-budget 6000
uv run gov360 brain evaluate
uv run gov360 brain export --output dist/okf
uv run gov360 brain export --output dist/okf --check
uv run gov360 brain release-kit --output dist/release-kit
```

`status` et les rapports de baseline/réconciliation établissent l'état courant.
Les sorties de `build` se trouvent dans `state/derived/brain/` : `baseline.json`,
`catalogue.json`, `evidence-index.json`, `coverage-matrix.json`,
`reconciliation.json`, `report.md` et `navigation.md`. Les sidecars revus sous
`state/workshop/evidence-library/` suivent
`config/schemas/brain-evidence.schema.json`.
La matrice des quinze piliers et dix critères oriente la prochaine release ; le
nombre de notes ne constitue jamais un pourcentage de complétude métier.

| État observé | Utilisation autorisée | Action suivante |
| --- | --- | --- |
| Note active, preuves résolues et revues | Contexte d'assistance dans son périmètre | Maintenir dates et revue |
| Note active historique, chaîne de preuve incomplète | Navigation humaine, diagnostic | Réconcilier reçus et preuves ; ne pas inférer leur validité |
| Unité ingest validée mais preuve non revue | Recherche explicitement demandée | Extraction ciblée et audit |
| Hash incohérent, locator absent ou autorité inconnue | Signalement du blocage | Réparer/revoir avant assistance |
| Proposition revue sans approbation du hash exact | Candidat à présenter | Approbation humaine puis assembleur |

`context` utilise le mode `assistance` par défaut. Le mode `research` doit être
explicitement demandé et conserve la distinction entre matériau documentaire et
connaissance approuvée. Les réponses projet ne sont jamais enregistrées.

Les quatre responsabilités sont le pilotage CDO, l'extraction et son audit
indépendant, la construction du domaine, puis la revue indépendante de release.
Les rôles spécialisés restent disponibles ; les petits contrôles déterministes
ne déclenchent pas d'agent. Réutiliser un audit seulement pour ses mêmes entrées,
son même périmètre et une validité inchangée.

Le kit local partageable est préparé par `git_helper`, sans historique du dépôt
de travail ni contenu à droits non établis. Le destinataire fournit ses sources,
puis lance `uv run gov360 brain bootstrap --source-root sources` en aperçu.
`--apply` exécute la reconstruction autorisée ; toute divergence de hash exige
une nouvelle revue. La synthèse LLM n'est pas reproductible à l'octet près.
