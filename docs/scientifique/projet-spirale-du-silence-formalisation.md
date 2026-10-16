# Formaliser une théorie verbale : la spirale du silence

*Projet de recherche agentique avec Mistral Large 4 (« Le Chonk »). Domaine : sciences de l'information et de la communication. Projet mené par l'ingénieur pédagogique (SIC). Version 1.2 du 17 octobre 2026 (codes « C4 » retirés ; version 1.1 du 16 octobre : suites de la revue n° 2). Sert d'étalon théorique au scénario « Dire et taire » (QR-E et HO3 ; contrepoint de HT4). Le calendrier de ce projet n'est pas articulé à celui du scénario : l'étalonnage du scénario s'appuie d'abord sur des modèles publiés (Sohn et Geidner, 2016 ; Ross et al., 2019 ; Aranda et al., 2024), et sur les formalisations de ce projet seulement si elles existent au moment de l'analyse.*

---

## 1. Le problème

### 1.1 Une théorie classique, une controverse de cinquante ans

La théorie de la spirale du silence (Noelle-Neumann, 1974, 1993) soutient que les individus, par **peur de l'isolement**, observent en permanence le **climat d'opinion** autour d'eux grâce à une sorte de « sens quasi statistique ». Lorsqu'ils pensent que leur opinion est minoritaire ou en recul, ils tendent à se taire. Ce silence rend leur opinion encore moins visible, ce qui renforce l'impression qu'elle est minoritaire et pousse d'autres personnes à se taire : la spirale. Les médias y jouent un rôle central par la consonance, la cumulation et l'omniprésence de leurs messages. La théorie prévoit aussi des exceptions : un **noyau dur** qui continue de s'exprimer malgré tout, et une **avant-garde** qui assume d'être minoritaire.

C'est l'une des théories les plus citées en communication politique et en études de l'opinion publique. Pourtant, après un demi-siècle de travaux empiriques :

- les méta-analyses trouvent une relation **faible** entre la perception du soutien à sa propre opinion et la disposition à s'exprimer (Glynn, Hayes et Shanahan, 1997 ; Matthes, Knoll et von Sikorski, 2018) ;
- les revues critiques soulignent l'imprécision conceptuelle de la théorie et la diversité de ses opérationnalisations (Scheufele et Moy, 2000) ;
- le débat s'est déplacé vers les réseaux sociaux numériques sans être tranché (Hampton et al., 2014).

### 1.2 Hypothèse de travail : une théorie sous-déterminée

Une partie de l'impasse pourrait venir de la forme même de la théorie. Elle est formulée en langage naturel, et ses énoncés admettent **plusieurs traductions précises, incompatibles entre elles**. Quel est le « climat d'opinion » perçu : celui des proches, celui des médias, celui de la société entière ? La peur de l'isolement est-elle un trait stable ou un état qui varie ? Se taire modifie-t-il aussi l'opinion privée ? Selon les réponses, la théorie prédit des dynamiques collectives très différentes.

La psychologie a fait de ce diagnostic un programme de recherche : la **« crise de la théorie »** (Oberauer et Lewandowsky, 2019), qui appelle à formaliser les théories verbales pour en révéler les hypothèses implicites et les contradictions (Smaldino, 2017 ; Guest et Martin, 2021 ; Robinaugh et al., 2021 ; van Rooij et Baggio, 2021).

### 1.3 Pourquoi un agent change la donne

Formaliser une théorie est long : relire les textes fondateurs, repérer chaque ambiguïté, coder chaque variante, l'explorer, documenter. On le fait habituellement pour **une** version. Un agent capable de lire tout le corpus fondateur d'un coup (un million de tokens de contexte), d'écrire et de tester du code, et de tenir un registre de ses choix permet de faire ce qu'aucune équipe ne fait faute de temps : **cartographier l'espace entier des formalisations admissibles** et comparer leurs comportements.

---

## 2. État de l'art et positionnement

| Travaux | Ce qu'ils font | Limite au regard de notre question |
|---|---|---|
| Sohn et Geidner (2016) ; Sohn (2022) | Modèles à base d'agents de la spirale du silence ; rôle de la taille du réseau personnel, interaction réseaux sociaux et médias de masse | Une formalisation choisie par les auteurs |
| Ross et al. (2019) ; Cabrera et al. (2021) | Modèles à base d'agents : effet des robots sociaux, rôle de la structure communautaire | Une formalisation, orientée vers une question appliquée |
| Aranda et al. (2024) | Modèle mathématique de la spirale du silence sur réseaux d'influence (extension de DeGroot), deux variantes | Deux variantes, non dérivées systématiquement des textes |
| Zhong et al. (2025) | Agents fondés sur des modèles de langage : une dynamique de type spirale n'apparaît que lorsque l'historique et la persona sont combinés | Le mécanisme de peur de l'isolement est absent des agents ; opérationnalisation de la majorité arbitraire, reconnue par les auteurs |
| Yang et al. (2026) | Simulation multi-agents distinguant évaluation interne et expression publique ; un indice de « pression du silence » réduit la prise de parole | Les indices sont des traces générées, non des mesures validées |

**Positionnement** : à notre connaissance (à confirmer par la revue de l'étape 1), aucun travail ne dérive **systématiquement des textes fondateurs** l'ensemble des formalisations admissibles de la théorie pour comparer leurs comportements. C'est la contribution visée.

---

## 3. Problématique et questions de recherche

> **La spirale du silence est-elle une théorie, ou une famille de théories ? En dérivant des textes fondateurs l'ensemble des formalisations admissibles, peut-on montrer qu'une partie des résultats empiriques contradictoires s'explique par la sous-détermination de la théorie, et identifier les observations qui permettraient de départager ses versions ?**

| Code | Question |
|---|---|
| **QR1** | Combien de formalisations distinctes et défendables les textes fondateurs autorisent-ils, et sur quels points de décision divergent-elles ? |
| **QR2** | Ces formalisations produisent-elles toutes une spirale ? Dans quelles conditions (paramètres, réseaux, médias) ? |
| **QR3** | Certaines formalisations sont-elles compatibles avec le constat empirique d'une relation individuelle faible tout en produisant une spirale collective nette ? (Question du passage micro-macro.) |
| **QR4** | Quelles prédictions observables distinguent les formalisations, et quels dispositifs d'enquête permettraient de les tester ? |
| **QR5** (réflexive, SIC) | Qu'est-ce que le passage du texte au code fait à la théorie ? Que perd-elle, que gagne-t-elle, qu'est-ce que l'agent « comprend » de travers ? |

---

## 4. Méthode

### 4.1 Étape 1 : corpus fondateur et propositions de la théorie (2 semaines)

**Corpus** : textes fondateurs de Noelle-Neumann (1974, 1991, 1993), revues critiques (Scheufele et Moy, 2000), méta-analyses (Glynn et al., 1997 ; Matthes et al., 2018), travaux de mesure (Hayes, Glynn et Shanahan, 2005). Textes acquis via les abonnements institutionnels.

**Travail de l'agent (Le Chonk, corpus entier en contexte)** :
1. extraire les **propositions** de la théorie : chaque affirmation causale ou descriptive, avec sa **citation exacte** et sa localisation (texte, page) ;
2. regrouper les propositions par concept : climat d'opinion, sens quasi statistique, peur de l'isolement, expression, noyau dur, avant-garde, médias, enjeux à composante morale.

**Vérificateur automatique** : chaque citation est recherchée mot pour mot dans le corpus. Une citation introuvable est rejetée. C'est la parade aux références inventées.

**Validation humaine** : l'ingénieur pédagogique valide la liste, puis en recode un échantillon à l'aveugle après au moins trois semaines ; accord mesuré entre ses deux codages et avec l'agent (kappa de Cohen).

### 4.2 Étape 2 : les points de décision (1 semaine)

L'agent repère chaque endroit où les propositions laissent plusieurs traductions possibles. Liste de départ, à compléter :

| Code | Point de décision | Options possibles (exemples) |
|---|---|---|
| D1 | Source du climat d'opinion perçu | Voisins dans le réseau ; médias ; combinaison pondérée ; groupe de référence |
| D2 | Dimension temporelle | Climat présent ; **tendance** perçue (l'opinion qui monte ou qui recule) ; les deux |
| D3 | Peur de l'isolement | Trait fixe ; état qui varie ; seuil individuel |
| D4 | Expression | Binaire (parler, se taire) ; continue (intensité) |
| D5 | Effet du silence sur l'opinion privée | Aucun ; conversion progressive ; conversion au-delà d'un seuil |
| D6 | Noyau dur et avant-garde | Absents ; proportion fixe ; émergents (agents peu sensibles à l'isolement) |
| D7 | Rôle des médias | Absent ; signal consonant ; cumulatif ; omniprésent |
| D8 | Domaine de validité | Tous les enjeux ; seulement les enjeux à forte composante morale |
| D9 | Ce que voient les autres | Seulement ceux qui parlent ; aussi le silence (le silence est-il un signal ?) |

Chaque option doit être **rattachée à au moins une proposition de l'étape 1**. Une option sans ancrage textuel est exclue. Les combinaisons incompatibles avec une proposition explicite sont éliminées.

**Revue adverse** : un second modèle (`qwen-3.8-27b`) relit chaque option et cherche à montrer qu'elle trahit le texte. Les désaccords sont tranchés par l'ingénieur pédagogique et consignés.

**Résultat** : l'**espace des formalisations admissibles**, avec pour chaque formalisation la liste de ses choix et leurs justifications textuelles.

### 4.3 Étape 3 : implémentation et tests de conformité (2 semaines)

1. L'agent implémente chaque formalisation comme un modèle à base d'agents en Python (Mesa et networkx), décrit selon le protocole **ODD** (Grimm et al., 2020).
2. **Tests de conformité aux propositions** : chaque proposition de la théorie devient un test automatique de propriété. Par exemple : « toutes choses égales par ailleurs, un agent qui se perçoit minoritaire et craint fortement l'isolement s'exprime moins qu'un agent qui se perçoit majoritaire ». Les tests sont générés avec la bibliothèque de tests par propriétés Hypothesis.
3. Une formalisation qui échoue à un test est corrigée ou rejetée.

C'est le **vérificateur** du projet, l'équivalent modeste de ce que Lean fait pour une preuve : il garantit que chaque modèle respecte ce que la théorie affirme explicitement.

### 4.4 Étape 4 : exploration (2 semaines)

Pour chaque formalisation :
- simulations sur plusieurs topologies de réseau (petit monde, sans échelle, communautés) et plusieurs distributions initiales d'opinions ;
- **analyse de sensibilité globale** (indices de Sobol, bibliothèque SALib) sur les paramètres libres ;
- indicateurs de sortie : apparition d'une spirale (oui, non, partielle), part finale de silencieux, survie du noyau dur, écart entre opinion exprimée et opinion privée, vitesse de la dynamique.

Puis **classification** des formalisations selon leurs comportements : lesquelles produisent une spirale robuste, lesquelles seulement dans des conditions étroites, lesquelles jamais.

### 4.5 Étape 5 : confrontation aux résultats empiriques (1 semaine)

- **Le paradoxe micro-macro** (QR3) : pour chaque formalisation, on simule une « enquête » sur les agents (relation individuelle entre perception du climat et expression) et on compare la force de cette relation à celle des méta-analyses. Une formalisation qui produit une spirale collective nette avec une relation individuelle faible lèverait en partie le paradoxe empirique de la théorie.
- **Prédictions discriminantes** (QR4) : on recherche les observables qui diffèrent le plus entre familles de formalisations (par exemple : effet du silence des autres sur sa propre expression, rôle de la tendance perçue par rapport au climat présent), et on propose pour chacune un dispositif d'enquête qui permettrait de trancher.

### 4.6 Étape 6 (option) : retour au village génératif

On place les mêmes points de décision dans le village simulé (agents fondés sur des modèles de langage) et on compare la dynamique obtenue aux formalisations mathématiques. **De quelle formalisation le village génératif se rapproche-t-il le plus ?** Et, si une spirale apparaît chez des agents qui n'ont pas de peur de l'isolement, d'où vient-elle ? Ce pont relie ce projet au scénario « Dire et taire » (QR-E).

### 4.7 Volet réflexif (QR5)

Le carnet de conception consigne chaque traduction du texte vers le code, chaque désaccord entre l'agent, le relecteur adverse et l'humain, et les contresens de l'agent. Ce matériau est analysé comme un corpus : ce que la mise en code fait à une théorie de la communication.

---

## 5. Les vérificateurs du projet

| Vérificateur | Ce qu'il contrôle | Automatique ? |
|---|---|---|
| Recherche des citations mot pour mot | Aucune proposition ni option sans ancrage textuel réel | Oui |
| Tests de propriétés | Chaque modèle respecte les propositions explicites de la théorie | Oui |
| Reproductibilité | Mêmes résultats à graine égale ; code et environnements versionnés | Oui |
| Revue adverse par un second modèle | Fidélité des options au texte | Semi-automatique |
| Validation humaine et accord entre codeurs | Propositions, options, interprétation | Non |

---

## 6. Protocole de test et indicateurs de réussite

**Préenregistrement** : questions, liste des points de décision initiaux, indicateurs de sortie, critères d'exclusion des options.

| Indicateur | Cible |
|---|---|
| Accord humain et agent sur l'extraction des propositions | Kappa ≥ 0,7 |
| Citations vérifiées mot pour mot | 100 % |
| Formalisations admissibles identifiées | Au moins 10 distinctes |
| Formalisations passant tous les tests de conformité | Toutes celles retenues |
| Prédictions discriminantes formulées | Au moins 3, chacune avec un dispositif d'enquête proposé |

**Comparaison entre modèles** : l'étape 2 est rejouée avec `mistral-medium` (version datée) et `qwen-3.8-27b` à la place de Le Chonk. Trouvent-ils les mêmes points de décision ? C'est aussi une mesure de ce que chaque architexte « lit » dans une théorie.

**Critère de réussite** : le projet est réussi s'il démontre, de façon vérifiable, que les textes fondateurs autorisent des formalisations aux comportements collectifs qualitativement différents, et s'il formule au moins trois prédictions discriminantes testables. Si toutes les formalisations se comportent de la même façon, le résultat est aussi publiable : la théorie serait plus robuste à sa propre imprécision qu'on ne le pense.

---

## 7. Outils (macOS, Linux, Windows via WSL2)

| Besoin | Outil |
|---|---|
| Lecture du corpus, extraction, génération de code | Le Chonk via OpenCode et Inspect AI |
| Relecture adverse | `qwen-3.8-27b` (ILaaS) |
| Vérification des citations | Script Python de recherche exacte et approchée dans le corpus |
| Modèles à base d'agents | Python, Mesa, networkx |
| Tests de propriétés | pytest et Hypothesis |
| Analyse de sensibilité | SALib |
| Documentation des modèles | Protocole ODD |
| Visualisation | matplotlib ; page web du bureau des agents pour explorer l'espace des formalisations |

---

## 8. Déroulé (9 semaines, charge d'une journée par semaine)

| Semaine | Étape |
|---|---|
| Semaines 1 et 2 | Corpus, extraction des propositions, vérification des citations, validation |
| Semaine 3 | Points de décision, revue adverse, espace des formalisations |
| Semaines 4 et 5 | Implémentation, tests de conformité |
| Semaines 6 et 7 | Exploration, sensibilité, classification |
| Semaine 8 | Confrontation empirique, prédictions discriminantes |
| Semaine 9 | Rédaction ; volet réflexif |

---

## 9. Risques et parades

| Risque | Parade |
|---|---|
| L'agent invente des propositions ou des citations | Vérification mot pour mot obligatoire |
| L'agent « lisse » la théorie vers une version manuel | Revue adverse ; validation humaine ; comparaison entre modèles |
| Explosion combinatoire des formalisations | Élimination des combinaisons incompatibles avec le texte ; regroupement par familles de comportement |
| Résultats trop dépendants des paramètres libres | Analyse de sensibilité globale ; présentation par régions de paramètres |
| Accès aux textes fondateurs | Abonnements institutionnels ; aucun texte protégé redistribué |

---

## 10. Livrables et valorisation

1. Le **registre des propositions** de la théorie, avec citations vérifiées.
2. La **carte des points de décision** et l'espace des formalisations admissibles.
3. Le code des modèles (licence libre), décrits selon ODD, avec leurs tests de conformité.
4. Les résultats d'exploration et les prédictions discriminantes.
5. Un article méthodologique et théorique. Revues envisageables : *International Journal of Public Opinion Research*, *Communication Methods and Measures*, *Journal of Artificial Societies and Social Simulation*, *Questions de communication*, *Réseaux*.
6. Un billet de retour d'expérience : ce qu'un agent fait d'une théorie de sciences humaines.

---

## 11. Bibliographie

### Textes fondateurs et débats sur la spirale du silence
- Glynn, C. J., Hayes, A. F., & Shanahan, J. (1997). Perceived support for one's opinions and willingness to speak out: A meta-analysis of survey studies on the "spiral of silence". *Public Opinion Quarterly*, 61(3), 452-463.
- Hampton, K. N., Rainie, L., Lu, W., Dwyer, M., Shin, I., & Purcell, K. (2014). *Social Media and the "Spiral of Silence"*. Washington, DC : Pew Research Center.
- Hayes, A. F., Glynn, C. J., & Shanahan, J. (2005). Willingness to self-censor: A construct and measurement tool for public opinion research. *International Journal of Public Opinion Research*, 17(3), 298-323.
- Matthes, J., Knoll, J., & von Sikorski, C. (2018). The "spiral of silence" revisited: A meta-analysis on the relationship between perceptions of opinion support and political opinion expression. *Communication Research*, 45(1), 3-33.
- Noelle-Neumann, E. (1974). The spiral of silence: A theory of public opinion. *Journal of Communication*, 24(2), 43-51.
- Noelle-Neumann, E. (1991). The theory of public opinion: The concept of the spiral of silence. *Communication Yearbook*, 14, 256-287.
- Noelle-Neumann, E. (1993). *The Spiral of Silence: Public Opinion, Our Social Skin* (2e éd.). Chicago : University of Chicago Press.
- Scheufele, D. A., & Moy, P. (2000). Twenty-five years of the spiral of silence: A conceptual review and empirical outlook. *International Journal of Public Opinion Research*, 12(1), 3-28.

### Opinion publique : notions voisines et regards critiques
- Bourdieu, P. (1973). L'opinion publique n'existe pas. *Les Temps modernes*, 318, 1292-1309.
- Champagne, P. (1990). *Faire l'opinion. Le nouveau jeu politique*. Paris : Minuit.
- Kuran, T. (1995). *Private Truths, Public Lies: The Social Consequences of Preference Falsification*. Cambridge, MA : Harvard University Press.
- Prentice, D. A., & Miller, D. T. (1993). Pluralistic ignorance and alcohol use on campus: Some consequences of misperceiving the social norm. *Journal of Personality and Social Psychology*, 64(2), 243-256.

### Modèles computationnels de la spirale du silence
- Aranda, J., Díaz, J. F., Gaona, D., & Valencia, F. (2024). The Sound of Silence in Social Networks. *arXiv:2410.19685*.
- Cabrera, B., Ross, B., Röchert, D., Brünker, F., & Stieglitz, S. (2021). The influence of community structure on opinion expression: An agent-based model. *Journal of Business Economics*, 91(9). https://doi.org/10.1007/s11573-021-01064-7
- Ross, B., Pilz, L., Cabrera, B., Brachten, F., Neubaum, G., & Stieglitz, S. (2019). Are social bots a real threat? An agent-based model of the spiral of silence to analyse the impact of manipulative actors in social networks. *European Journal of Information Systems*, 28(4), 394-412.
- Sohn, D. (2022). Spiral of silence in the social media era: A simulation approach to the interplay between social networks and mass media. *Communication Research*, 49(1), 139-166.
- Sohn, D., & Geidner, N. (2016). Collective dynamics of the spiral of silence: The role of ego-network size. *International Journal of Public Opinion Research*, 28(1), 25-45. https://doi.org/10.1093/ijpor/edv005
- Yang, K., Peng, T.-Q., Lee, S., & Liu, H. (2026). Think-Before-Speak: From Internal Evaluation to Public Expression in Multi-Agent Social Simulation. *arXiv:2606.03137* (v2 du 1er juillet 2026 ; communication à l'atelier SciSoc Agents & LLMs de KDD 2026).
- Zhong, M., Fang, M., Shi, Z., Huang, Y., Zheng, S., Du, Y., Chen, L., & Wang, J. (2025). Spiral of Silence in Large Language Model Agents. *Findings of the Association for Computational Linguistics: EMNLP 2025*, 23238-23253. *arXiv:2510.02360*.

### Formalisation des théories et modélisation
- Epstein, J. M. (2008). Why model? *Journal of Artificial Societies and Social Simulation*, 11(4), 12.
- Granovetter, M. (1978). Threshold models of collective behavior. *American Journal of Sociology*, 83(6), 1420-1443.
- Grimm, V., Railsback, S. F., Vincenot, C. E., et al. (2020). The ODD protocol for describing agent-based and other simulation models: A second update to improve clarity, replication, and structural realism. *Journal of Artificial Societies and Social Simulation*, 23(2), 7.
- Guest, O., & Martin, A. E. (2021). How computational modeling can force theory building in psychological science. *Perspectives on Psychological Science*, 16(4), 789-802.
- Oberauer, K., & Lewandowsky, S. (2019). Addressing the theory crisis in psychology. *Psychonomic Bulletin & Review*, 26(5), 1596-1618.
- Robinaugh, D. J., Haslbeck, J. M. B., Ryan, O., Fried, E. I., & Waldorp, L. J. (2021). Invisible hands and fine calipers: A call to use formal theory as a toolkit for theory construction. *Perspectives on Psychological Science*, 16(4), 725-743.
- Smaldino, P. E. (2017). Models are stupid, and we need more of them. In R. R. Vallacher, S. J. Read, & A. Nowak (dir.), *Computational Social Psychology* (p. 311-331). New York : Routledge.
- van Rooij, I., & Baggio, G. (2021). Theory before the test: How to build high-verisimilitude explanatory theories in psychological science. *Perspectives on Psychological Science*, 16(4), 682-697.
- Varenne, F. (2018). *From Models to Simulations*. Londres : Routledge.

### Outils et méthodes
- Herman, J., & Usher, W. (2017). SALib: An open-source Python library for sensitivity analysis. *Journal of Open Source Software*, 2(9), 97.
- MacIver, D. R., Hatfield-Dodds, Z., et al. (2019). Hypothesis: A new approach to property-based testing. *Journal of Open Source Software*, 4(43), 1891.
- Saltelli, A., Ratto, M., Andres, T., et al. (2008). *Global Sensitivity Analysis: The Primer*. Chichester : Wiley.

*Toutes les références sont à contrôler (pagination, numéros) au moment de la rédaction de l'article. Celle de Cabrera et al. (2021) est donnée avec son DOI, sans pagination ; les références de 2024 à 2026 ont été vérifiées par la revue n° 2.*
