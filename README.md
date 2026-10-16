# Dire et taire

Un village d'agents génératifs pour étudier la circulation d'un savoir savant. Expérimentation de Mistral Large 4 (« Le Chonk »), scénario C4.

> **Problématique** : comment un dispositif génératif met-il en scène le dire et le taire autour d'un savoir savant, alors que ses agents, conçus pour toujours répondre, n'ont rien à craindre de la parole ?

Projet de recherche en sciences de l'information et de la communication, mené dans le cadre de JEDI-OpenLab (Centrale Lille).

## Clef de lecture : la co-agentivité

Dans le village, une réplique n'est jamais l'acte d'un seul agent. Elle est co-produite par un agencement : le modèle de langage (et, derrière lui, son fournisseur), la fiche du persona, l'orchestrateur, l'ordonnanceur, les cadres d'énonciation et le concepteur. Le projet cherche à savoir quelle instance produit le dire et le taire, sous quelles formes et dans quelles proportions.

## Hypothèses de travail

| Code | Hypothèse |
|---|---|
| HT1 | Le taire est co-produit par l'agencement : cadres, ordonnancement et modèle pèsent plus que les dispositions attribuées aux agents *(hypothèse centrale)* |
| HT2 | Le taire prend la forme d'un dire vide : les agents ne se taisent pas, ils neutralisent |
| HT3 | La trivialité co-produite converge vers le lieu commun : la thèse savante devient formule consensuelle |
| HT4 | Une socialité sans climat : alignement local sur l'interlocuteur plutôt que lecture du climat d'opinion |

## Contenu du dépôt

Voir le guide de lecture : `docs/README.md`, et le glossaire : `docs/glossaire.md`.


| Dossier | Contenu |
|---|---|
| `docs/scientifique/` | Cadre scientifique SIC du village, protocole du scénario C4, projet de formalisation de la spirale du silence (étalon théorique du C4) |
| `docs/revues/` | Revues adversariales successives des documents de conception |
| `docs/technique/` | Socle technique : station Ubuntu, passe-plat LiteLLM, traces Langfuse, agents, bureau des agents |
| `docs/visualisations/` | Carte des concepts du C4 : traçabilité des concepts jusqu'aux mesures |
| `presentation/` | Présentation d'ensemble du projet (antérieure aux hypothèses de travail : à mettre à jour) |

## État

Phase de conception (octobre 2026). Prochaines étapes : revue adversariale n° 2, choix des textes sources T0, T2 et T3, préenregistrement (premier temps), mise en place de la station. La carte des concepts (`docs/visualisations/carte-concepts-C4.html`) montre l'état de la traçabilité entre concepts et mesures.

## Conventions

- Les clés d'API ne sont jamais versionnées (fichiers `.env` ignorés).
- Les journaux bruts de simulation ne sont pas versionnés : ils peuvent contenir des extraits d'ouvrages protégés.
- Les documents de conception renvoient parfois à deux documents conservés hors du dépôt : le cadrage général de l'expérimentation (« prototypes-agentiques-le-chonk.md ») et le projet « multivers PISA » (« projet-multivers-PISA-numerique.md »).
