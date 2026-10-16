# Dire et taire

Un village d'agents génératifs pour étudier la circulation d'un savoir savant. Expérimentation de Mistral Large 4 (« Le Chonk »), scénario C4.

> **Problématique** : comment un dispositif génératif met-il en scène le dire et le taire autour d'un savoir savant, alors que ses agents, conçus pour toujours répondre, n'ont rien à craindre de la parole ?

Projet de recherche en sciences de l'information et de la communication, mené dans le cadre de JEDI-OpenLab (Centrale Lille).

## Hypothèses de travail

| Code | Hypothèse |
|---|---|
| HT1 | Le taire comme dire vide : les agents ne se taisent pas, ils neutralisent |
| HT2 | Le taire est écrit par le dispositif : les cadres d'énonciation comptent plus que les attributs des personas |
| HT3 | La trivialité converge vers le lieu commun : la thèse savante devient formule consensuelle |
| HT4 | Une socialité sans climat : alignement sur l'interlocuteur plutôt que lecture du climat d'opinion |

## Contenu du dépôt

Voir le guide de lecture : `docs/README.md`.


| Dossier | Contenu |
|---|---|
| `docs/scientifique/` | Cadre scientifique SIC du village, protocole du scénario C4, projet de formalisation de la spirale du silence (étalon théorique du C4) |
| `docs/revues/` | Revues adversariales successives des documents de conception |
| `docs/technique/` | Socle technique : station Ubuntu, passe-plat LiteLLM, traces Langfuse, agents, bureau des agents |
| `presentation/` | Présentation d'ensemble du projet |

## État

Phase de conception (octobre 2026). Prochaines étapes : revue adversariale n° 2, choix des sources S0 et S3, mise en place de la station.

## Conventions

- Les clés d'API ne sont jamais versionnées (fichiers `.env` ignorés).
- Les journaux bruts de simulation ne sont pas versionnés : ils peuvent contenir des extraits d'ouvrages protégés.
- Les documents de conception renvoient parfois au cadrage général de l'expérimentation (« prototypes-agentiques-le-chonk.md »), conservé hors du dépôt.
