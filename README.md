# Dire et taire

Un village d'agents génératifs pour étudier la circulation d'un savoir savant. Expérimentation de Mistral Large 4 (« Le Chonk »), scénario « Dire et taire ».

> **Problématique** : comment un dispositif génératif met-il en scène le dire et le taire autour d'un savoir savant, alors que ses agents, conçus pour toujours répondre, n'ont rien à craindre de la parole ?

Projet de recherche en sciences de l'information et de la communication, mené dans le cadre de JEDI-OpenLab (Centrale Lille).

## Clef de lecture : la co-agentivité

Dans le village, une réplique n'est jamais l'acte d'un seul agent. Elle est co-produite par un agencement : le modèle de langage (et, derrière lui, son fournisseur), la fiche du persona, l'orchestrateur, l'ordonnanceur, les cadres d'énonciation et le concepteur. Le projet cherche à savoir quelle instance produit le dire et le taire, sous quelles formes et dans quelles proportions.

## Hypothèses de travail

| Code | Hypothèse |
|---|---|
| HT1 | Le taire est co-produit par l'agencement : à contrastes déclarés, et la fiche du persona recevant son étendue maximale, au moins une instance non individuelle (cadre d'énonciation d'abord, puis gazette, ordonnancement, modèle) pèse plus que les dispositions attribuées aux agents *(hypothèse centrale, relative aux contrastes déclarés)* |
| HT2 | Le taire prend la forme d'un dire vide : les agents ne se taisent pas, ils neutralisent, et davantage pour la thèse moralement chargée que pour un livre sans enjeu |
| HT3 | La trivialité co-produite converge vers le lieu commun : la thèse savante devient formule consensuelle, plus vite que par la seule transmission |
| HT4 | Une socialité sans climat : alignement local sur l'interlocuteur plutôt que lecture du climat d'opinion, l'effet du climat restant sous l'effet humain moyen |

Chaque hypothèse de travail a une règle de décision préenregistrée, à trois issues : soutenue, réfutée, indéterminée.

## Contenu du dépôt

Voir le guide de lecture : `docs/README.md`, et le glossaire : `docs/glossaire.md`.


| Dossier | Contenu |
|---|---|
| `docs/scientifique/` | Cadre scientifique SIC du village, protocole du scénario « Dire et taire », préenregistrement, projet de formalisation de la spirale du silence (étalon théorique du scénario) |
| `docs/revues/` | Revues adversariales successives des documents de conception |
| `docs/technique/` | Socle technique : station Ubuntu, passe-plat LiteLLM, traces Langfuse, agents, bureau des agents |
| `docs/visualisations/` | Carte des concepts du scénario : traçabilité des concepts jusqu'aux mesures et aux règles de décision |
| `site/` | Mini-site de présentation du projet (publié par GitHub Pages) ; `site-src/` contient ses fragments et le script qui l'assemble (`python3 site-src/build.py`) |
| `analyses/puissance/` | Simulations de puissance des règles de décision (issues de la revue n° 2), à rejouer avec les variances du pilote |

## État

Conception terminée, installation de la station en cours (octobre 2026). Documents en vigueur : cadre scientifique 6.7, scénario 11.6, glossaire 3.6, socle technique 4.2. La revue adversariale n° 2 est faite et ses dix-sept décisions sont consignées. Le projet ne compte plus qu'un scénario ; la rumeur de la boulangerie est gardée comme prolongement possible, selon les résultats (cadre, section 7). Un volet réflexif sur la complexité et l'incertitude, au sens d'Edgar Morin, donne au projet un intérêt pour l'ingénierie pédagogique, avec une lecture de l'émergence et de l'observateur dans l'observation (cadre, 2.6).

**Station, au 19 octobre 2026** (détail dans le journal du socle technique, section 12) : Ubuntu 26.04.1 LTS, accès par clé SSH seulement, pare-feu, Docker 29.9.1, Langfuse 4.63.0 et passe-plat LiteLLM 1.106.0 en service, clés virtuelles par usage créées (sans budget : la consommation est suivie en tokens) ; un premier appel à un modèle ILaaS aboutit et apparaît dans les traces. En attente : la clé de Le Chonk (AMUE). À décider : le remplaçant du second juge (Qwen 3.6, retiré par ILaaS), le traitement de Mistral Medium (publié sans version datée), le niveau de raisonnement des modèles qui raisonnent, et l'étiquetage des appels dans les traces.

Prochaines étapes : fin de l'installation (OpenCode, environnements Python avec Concordia et Inspect AI, sauvegardes, bureau des agents v0, recette), programmation du village, test d'accès et de débit (une journée simulée sur des fiches provisoires), relecture par un modèle d'un autre fournisseur, choix des textes sources T0, T2 et T3, construction des 40 personas, préenregistrement (premier temps, ébauche dans `docs/scientifique/preenregistrement-premier-temps.md`). La carte des concepts (`docs/visualisations/carte-concepts.html`) montre l'état de la traçabilité entre concepts et mesures.

## Conventions

- Les clés d'API ne sont jamais versionnées (fichiers `.env` ignorés).
- Les journaux bruts de simulation ne sont pas versionnés : ils peuvent contenir des extraits d'ouvrages protégés.
- Les documents de conception renvoient parfois à deux documents conservés hors du dépôt : le cadrage général de l'expérimentation (« prototypes-agentiques-le-chonk.md ») et le projet « multivers PISA » (« projet-multivers-PISA-numerique.md »).
