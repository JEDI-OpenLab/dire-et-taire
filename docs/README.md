# Guide de lecture des documents

## Ordre de lecture conseillé

| N° | Document | Rôle | Question à laquelle il répond |
|---|---|---|---|
| 0 | `glossaire.md` | Définitions, paternité des notions, références d'origine | Que veut dire ce terme, et d'où vient-il ? (à consulter en continu) |
| 1 | `scientifique/cadre-scientifique-SIC-village.md` | Cadre théorique général du village | Quel est l'objet de recherche, et avec quels concepts l'étudie-t-on ? |
| 2 | `scientifique/scenario-dire-et-taire.md` | Protocole du scénario « Dire et taire » | Que cherche-t-on précisément, comment, avec quelles mesures ? |
| 3 | `scientifique/preenregistrement-premier-temps.md` | Ébauche du premier temps du préenregistrement | Qu'est-ce qui sera déposé avant toute génération ? |
| 4 | `scientifique/projet-spirale-du-silence-formalisation.md` | Formalisations de la spirale du silence | Quelles versions de la théorie servent d'étalon au scénario ? |
| 5 | `revues/revue-adversariale-1-cadre-et-scenario.md` et `revues/revue-adversariale-2-cadre-et-scenario.md` | Revues critiques n° 1 et n° 2, avec les décisions prises | Quelles faiblesses ont été repérées, et comment ont-elles été corrigées ? |
| 6 | `technique/socle-technique-le-chonk.md` | Station, passe-plat, traces, agents, bureau des agents | Comment fait-on tourner tout cela ? |
| 7 | `visualisations/carte-concepts.html` | Carte des concepts du scénario (page à ouvrir dans un navigateur) | Chaque concept mène-t-il à une mesure, et chaque hypothèse à une règle de décision ? |
| 8 | `../analyses/puissance/` | Simulations de puissance des règles de décision | Le plan a-t-il une chance de trancher ? |
| 9 | `../presentation/dire-et-taire-le-chonk.pptx` | Présentation d'ensemble, antérieure aux hypothèses de travail et à la clef de lecture : à mettre à jour | Comment présenter le projet en 20 minutes ? |

## Architecture du raisonnement scientifique

```
Clef de lecture : la co-agentivité (cadre, section 1)
  Chaque énoncé est co-produit par un agencement : modèle et fournisseur, fiche,
  orchestrateur, ordonnanceur, cadres d'énonciation, concepteur.
        |
Problématique générale du village (cadre, 3.1)
  « Comment une simulation sociale générative fait-elle circuler et se transformer
    des énoncés, alors qu'aucune des voix qui la peuplent ne parle seule ? »
        |
        +-- Questions de recherche QR1 à QR4 (cadre, 3.2) ; QR2 = la part des instances
                |
                +-- QR4 = problématique du scénario (scénario, 1.3)
                      « Comment un dispositif génératif met-il en scène le dire et le taire
                        autour d'un savoir savant, alors que ses agents, conçus pour toujours
                        répondre, n'ont rien à craindre de la parole ? »
                        |
                        +-- Questions de recherche QR-A à QR-E (scénario, 1.4)
                        +-- Hypothèses de travail HT1 à HT4 (scénario, 1.5)
                        |     HT1, centrale : le taire est co-produit par l'agencement
                        +-- Hypothèses opérationnelles HO1 à HO11 (scénario, 1.6), principales,
                        |     secondaires, descriptives ou exploratoires
                        +-- Règles de décision à trois issues (scénario, 7)
                              |
                              +-- Inventaire : instances, stimuli, instruments (cadre, 1.1 ; scénario, 3.0)
                              +-- Un contraste de référence par instance (scénario, 3.0 ; cadre, 6.4)
                              +-- Dispositif (scénario, 3), mesures (scénario, 4), analyse par instance (scénario, 7)
```

## Conventions de rédaction

- Problématiques formulées en « Comment [X] alors que [Y] ».
- Vocabulaire des cadres d'énonciation : « position déclarée en enquête », « position exprimée en scène » ; aucune intériorité prêtée aux agents.
- « Agent » au sens informatique (un programme) ; « agentivité » au sens des sciences sociales (capacité d'agir), conçue comme distribuée entre modèle, dispositif et concepteur (cadre, 1.2 et 1.3).
- Chaque document indique sa version et sa date en en-tête ; chaque révision importante passe par une revue consignée dans `revues/`.
- Jamais de tiret cadratin ni de tiret demi-cadratin comme ponctuation ; les signes « − » des codes G−, K− et −2 sont des signes moins.
