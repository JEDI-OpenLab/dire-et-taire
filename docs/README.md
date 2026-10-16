# Guide de lecture des documents

## Ordre de lecture conseillé

| N° | Document | Rôle | Question à laquelle il répond |
|---|---|---|---|
| 1 | `scientifique/cadre-scientifique-SIC-village.md` | Cadre théorique général du village | Quel est l'objet de recherche, et avec quels concepts l'étudie-t-on ? |
| 2 | `scientifique/scenario-C4-circulation-savoir-savant.md` | Protocole du scénario C4 « Dire et taire » | Que cherche-t-on précisément, comment, avec quelles mesures ? |
| 3 | `scientifique/projet-spirale-du-silence-formalisation.md` | Formalisations de la spirale du silence | Quelles versions de la théorie servent d'étalon au C4 ? |
| 4 | `revues/revue-adversariale-1-cadre-et-C4.md` | Revue critique n° 1 et décisions prises | Quelles faiblesses ont été repérées, et comment ont-elles été corrigées ? |
| 5 | `technique/socle-technique-le-chonk.md` | Station, passe-plat, traces, agents, bureau des agents | Comment fait-on tourner tout cela ? |
| 6 | `../presentation/dire-et-taire-le-chonk.pptx` | Présentation d'ensemble | Comment présenter le projet en 20 minutes ? |

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
                +-- QR4 = problématique du C4 (C4, 1.3)
                      « Comment un dispositif génératif met-il en scène le dire et le taire
                        autour d'un savoir savant, alors que ses agents, conçus pour toujours
                        répondre, n'ont rien à craindre de la parole ? »
                        |
                        +-- Questions de recherche QR-A à QR-E (C4, 1.4)
                        +-- Hypothèses de travail HT1 à HT4 (C4, 1.5)
                        |     HT1, centrale : le taire est co-produit par l'agencement
                        +-- Hypothèses opérationnelles S1 à S8 (C4, 1.6)
                              |
                              +-- Une condition par instance (C4, 3.0 ; cadre, 6.4)
                              +-- Dispositif (C4, 3), mesures (C4, 4), analyse par instance (C4, 7)
```

## Conventions de rédaction

- Problématiques formulées en « Comment [X] alors que [Y] ».
- Vocabulaire des cadres d'énonciation : « position déclarée en enquête », « position exprimée en scène » ; aucune intériorité prêtée aux agents.
- « Agent » au sens informatique (un programme) ; « agentivité » au sens des sciences sociales (capacité d'agir), conçue comme distribuée entre modèle, dispositif et concepteur (cadre, 1.6).
- Chaque document indique sa version et sa date en en-tête ; chaque révision importante passe par une revue consignée dans `revues/`.
