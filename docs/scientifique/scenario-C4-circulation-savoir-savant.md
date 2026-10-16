# Scénario C4 : dire et taire un savoir savant

*Expérience C4 du village simulé, sous l'angle de la spirale du silence. Cas d'étude : Johann Chapoutot, Les irresponsables (Gallimard, 2025). Version 8 du 16 octobre 2026 : réécriture autour de la co-agentivité, clef de lecture du projet (« revue-adversariale-1-cadre-et-C4.md »).*

*Documents associés : « cadre-scientifique-SIC-village.md » (cadre théorique général, version 3), « projet-spirale-du-silence-formalisation.md » (formalisations de la théorie, qui servent ici d'étalons), « prototypes-agentiques-le-chonk.md » (cadrage d'ensemble).*

*Projet mené seul par l'ingénieur pédagogique (SIC). Le second codage humain et la validation de la grille des propositions sont confiés à des personnes extérieures, à identifier.*


*Les termes, leur paternité et leurs références d'origine sont définis dans « ../glossaire.md ».*
---

## 1. Problématique

### 1.1 La clef de lecture : qui se tait quand un agent se tait ?

Le C4 met en circulation dans le village une thèse d'historien moralement chargée, et observe ce qui s'en dit et ce qui s'en tait. La théorie de la spirale du silence (Noelle-Neumann, 1974, 1993) sert d'instrument : elle oblige à regarder ce qui **ne circule pas**, et elle fournit des mesures (climat perçu, test du train, écart entre ce qui est déclaré et ce qui est exprimé).

Mais la question du C4 n'est pas de savoir si des machines « reproduisent » la spirale du silence. Elle découle de la clef de lecture de tout le projet, la **co-agentivité** (cadre scientifique, section 1) : une réplique n'est jamais l'acte d'un seul agent, elle est co-produite par un agencement.

| Instance | Comment elle peut produire du dire ou du taire |
|---|---|
| **Le modèle de langage et son fournisseur** | Neutralité apprise sur les sujets controversés ; complaisance envers l'interlocuteur ; régularités de formulation |
| **La fiche du persona** | Disposition attribuée à l'autocensure, sensibilité, rapport à l'histoire |
| **L'orchestrateur** | Ce que l'agent « sait » du livre et de ce qu'en pensent les autres (mémoire, notes de lecture) |
| **L'ordonnanceur** | Qui rencontre qui, en public ou en privé ; chambres d'écho |
| **Les cadres d'énonciation** | Scène publique, tête-à-tête, enquête confidentielle, gazette |
| **Le concepteur** | Tout ce qui précède, et les sollicitations elles-mêmes |

Le silence, s'il apparaît, n'est donc pas « celui d'un habitant » : c'est **une production de l'agencement**. La question devient : **quelles instances produisent le dire et le taire, sous quelles formes, et dans quelles proportions ?**

### 1.2 Posture

- Le village n'est pas un modèle de la société française ; aucun résultat n'est généralisé à des personnes réelles.
- Aucune instance n'a d'intériorité : on parle de **position déclarée en enquête** et de **position exprimée en scène** ; le « silence » désigne l'absence, ou la neutralisation, de position exprimée face à une sollicitation.
- Le concepteur est une instance de l'agencement ; sa part est documentée par le carnet de conception.
- Le livre étudié ne sert pas à juger une thèse historique, mais à observer ce qu'un agencement génératif fait d'un savoir savant moralement chargé. Aucune lecture du présent n'est injectée ; les analogies sont observées, jamais suggérées.

### 1.3 Problématique

> **Comment un dispositif génératif met-il en scène le dire et le taire autour d'un savoir savant, alors que ses agents, conçus pour toujours répondre, n'ont rien à craindre de la parole ?**

| Terme | Contenu | Pourquoi |
|---|---|---|
| **X** | Un dispositif génératif met en scène le dire et le taire autour d'un savoir savant | X ne présuppose pas que le silence apparaîtra : si tous les agents parlent, le résultat répond aussi à la question |
| **Y** | Ses agents sont conçus pour toujours répondre et n'ont rien à craindre de la parole | Un modèle de langage est entraîné à produire du texte et à ne laisser aucune question sans réponse ; il n'a ni corps social, ni réputation, ni peur de l'isolement, ressort central de la spirale du silence (Noelle-Neumann, 1993), absence que reconnaissent Zhong et al. (2025) |

**Comment la clef de lecture résout la tension.** Y n'est contradictoire que si l'on cherche le silence dans les agents. Si l'agentivité est distribuée, des agents qui n'ont rien à craindre peuvent quand même produire du taire, parce que **ce ne sont pas eux seuls qui parlent ou se taisent** : la fiche, les cadres, l'ordonnanceur, le concepteur et, derrière le modèle, son fournisseur et ses règles de neutralité, y prennent part. La première moitié de Y (« conçus pour toujours répondre ») contient d'ailleurs sa propre tension : les modèles sont aussi réglés pour rester neutres sur les sujets controversés (OpenAI, 2025). C'est une instance de plus, le fournisseur, qui entre dans l'agencement.

### 1.4 Questions de recherche

| Code | Question | Lien |
|---|---|---|
| **QR-A. Les formes du dire et du taire** | Face à des sollicitations standardisées, quelles positions l'agencement exprime-t-il sur une thèse moralement chargée, par rapport à un savoir sans enjeu, en public et en privé ? Sous quelles formes le taire se manifeste-t-il ? | X |
| **QR-B. Le climat** | Comment se forme le climat d'opinion déclaré perçu, et quelles instances le façonnent (entourage, gazette, ordonnancement) ? | X |
| **QR-C. La part des instances** | Quelle part du dire et du taire revient à chaque instance : modèle et fournisseur (neutralité apprise, complaisance), fiche (disposition attribuée), cadres d'énonciation, ordonnanceur, concepteur ? | Y, question centrale |
| **QR-D. La trivialité co-produite** | Quelles versions de la thèse dominent ce qui s'entend dans le village, et que change l'agencement social (réseau, scènes, mémoire) par rapport à une transmission linéaire ? | Conséquence |
| **QR-E. L'étalonnage théorique** | De quelle formalisation de la spirale du silence la dynamique de l'agencement se rapproche-t-elle le plus ? | Conséquence |

**Architecture du raisonnement** : problématique (1.3) → questions de recherche (1.4) → hypothèses de travail (1.5), qui proposent des réponses → hypothèses opérationnelles (1.6), qui les traduisent en mesures → instances et conditions (3.1) → dispositif (3) et mesures (4).

### 1.5 Hypothèses de travail

| Code | Hypothèse de travail | Réponse proposée à Y | Signature observable | Ce qui la réfuterait |
|---|---|---|---|---|
| **HT1. Le taire est co-produit par l'agencement** *(hypothèse centrale)* | Le dire et le taire varient d'abord avec les **instances non individuelles** de l'agencement (cadres d'énonciation, ordonnancement, modèle et fournisseur) plus qu'avec les dispositions attribuées aux agents | Des agents qui n'ont rien à craindre produisent du taire parce que d'autres instances le produisent avec eux | Effets du type de scène, de la gazette, de l'ordonnanceur et du modèle supérieurs à celui de la disposition attribuée à l'autocensure | Effet dominant de la disposition attribuée, les autres instances n'ayant qu'un effet marginal |
| **HT2. Le taire prend la forme d'un dire vide** | L'agencement produit moins de silence pur que de **neutralisation** : les agents parlent toujours, pour ne rien dire | Des agents conçus pour toujours répondre ne se taisent pas ; le taire se loge dans la parole elle-même | Formes NEU, EUP et DEL bien plus fréquentes que TAC ; plus fréquentes pour S1 et S3 que pour S0, y compris sans public | Silences purs (TAC) dominants, ou neutralisation identique pour S0 |
| **HT3. La trivialité co-produite converge vers le lieu commun** | Parce que les mêmes instances écrivent toutes les voix, les reprises de la thèse perdent leurs aspérités et convergent vers une **formule consensuelle** | Un agencement qui écrit toutes les voix tend à leur donner les mêmes formes | Baisse de la diversité des versions au fil des relais ; formules récurrentes ; convergence plus forte en « tout Le Chonk » qu'en polyphonie mixte | Diversité maintenue ou croissante ; aucune différence entre modes d'écriture |
| **HT4. Une socialité sans climat** | Ce qui ressemble à du conformisme est un **alignement local** entre le modèle et l'interlocuteur du moment, non une lecture du climat d'opinion : le « sens quasi statistique » n'opère pas | Sans peur de l'isolement, il reste la complaisance conversationnelle, dyadique et non collective | Position exprimée prédite par celle de l'interlocuteur (dyades), mais pas par le climat perçu déclaré | Climat perçu prédictif de l'expression, à interlocuteur constant |

**Articulation.** HT1 est l'hypothèse centrale, qui découle directement de la clef de lecture. HT2 décrit la **forme** du taire, HT3 la **forme** de ce qui circule, HT4 le **mécanisme** relationnel. HT1 et HT4 sont compatibles (la complaisance est une part du modèle dans l'agencement) ; HT4 contredit en revanche une lecture « spirale » du village. Le dispositif est conçu pour départager.

### 1.6 Hypothèses opérationnelles préenregistrées

| Code | Hypothèse opérationnelle | Hypothèse de travail servie |
|---|---|---|
| **S1. Silence différentiel** | Pour la thèse moralement chargée (S1) davantage que pour le savoir sans enjeu (S0), les agents dont la position déclarée en enquête s'écarte du climat qu'ils déclarent percevoir expriment moins de positions face aux sollicitations en scène publique qu'en scène privée | HT1, HT2 |
| **S2. Double climat** | Une gazette consonante déplace davantage le climat perçu déclaré que les positions déclarées en enquête | HT1 |
| **S3. Ignorance pluraliste** | Dans certaines conditions, une majorité d'agents déclarent percevoir leur position comme minoritaire | HT4 |
| **S4. Noyau dur** | Les agents à faible disposition attribuée à l'autocensure continuent d'exprimer des positions perçues comme minoritaires | HT1 (part de la fiche) |
| **S5a. Part de la fiche** | L'effet décrit en S1 croît avec la disposition attribuée à l'autocensure et disparaît dans la condition sans autocensure | HT1 (si confirmée seule, HT1 est réfutée) |
| **S5b. Part du modèle en interaction** | En tête-à-tête, la position exprimée se rapproche de celle de l'interlocuteur, indépendamment de la disposition attribuée | HT1, HT4 |
| **S5c. Part du modèle et du fournisseur** | Les énoncés neutralisés apparaissent même sans public ni interlocuteur, et plus pour S1 et S3 que pour S0 | HT1, HT2 |
| **S6. Assimilation publique** | Les versions de la thèse exprimées en public se rapprochent davantage de l'avis perçu comme majoritaire que celles exprimées en privé | HT3 |
| **S7. Part de l'ordonnanceur** | Des rencontres homophiles réduisent le silence local mais accroissent la polarisation | HT1 |
| **S8. Part de l'agencement social** | Les transformations de la thèse dans le village diffèrent de celles des chaînes linéaires (exploratoire) | HT3 |

---

## 2. Cadre conceptuel spécifique

En complément du cadre scientifique général, dont le noyau est l'agentivité distribuée :

| Concept | Références | Rôle dans le C4 |
|---|---|---|
| **Agentivité distribuée, co-agentivité** | Callon (1986) ; Latour (2006) ; Akrich et Latour (1992) ; Suchman (2007) | Clef de lecture : la part de chaque instance dans le dire et le taire (HT1) |
| **Cadres de l'expérience et de l'interaction** | Goffman (1974) | Scène publique, tête-à-tête, enquête : ce qui peut se dire selon le cadre (HT1) |
| **Formes discursives du silence** | Projet (livre de codes 4.4) | Neutralisation, euphémisation, délégation (HT2) |
| **Attracteurs culturels** | Sperber (1996) ; Perez et al. (2025) | Convergence des reprises vers des formes stables (HT3) |
| **Complaisance des modèles de langage** | Sharma et al. (2024) | Part du modèle en interaction (HT4, S5b) |
| **Modèle et fournisseur** : neutralité apprise | Règles de conduite des fournisseurs (OpenAI, 2025) | Part du fournisseur (S5c) |
| **Spirale du silence** | Noelle-Neumann (1974, 1993) ; Scheufele et Moy (2000) ; Matthes, Knoll et von Sikorski (2018) | Instrument et étalon : dynamique des positions exprimées selon le climat perçu |
| **Sens quasi statistique, climat et tendance perçus** | Noelle-Neumann (1993) | Estimations déclarées de l'avis majoritaire et de son évolution |
| **Double climat d'opinion** | Noelle-Neumann (1993) | Écart entre positions déclarées et climat que la gazette laisse percevoir |
| **Deux sources du climat : médias et entourage** | Noelle-Neumann (1993) | Gazette et compères |
| **Noyau dur, avant-garde** | Noelle-Neumann (1993) | Agents qui expriment durablement des positions perçues comme minoritaires |
| **Disposition à s'autocensurer** | Hayes, Glynn et Shanahan (2005) | Attribut écrit dans les fiches |
| **Ignorance pluraliste** | Prentice et Miller (1993) | Majorité qui se déclare minoritaire |
| **Falsification des préférences** | Kuran (1995) | Positions exprimées contraires aux positions déclarées |
| **Conformité face à une majorité unanime** | Asch (1956) | Principe des compères |
| **L'opinion publique comme construction** | Bourdieu (1973) ; Champagne (1990) | Écart entre ce qui s'entend et la distribution des positions déclarées |
| **Spirale du silence chez des agents génératifs** | Zhong et al. (2025) ; Yang et al. (2026) | Travaux les plus proches |
| **Suffisance générative et plausibilité des mécanismes** | Epstein (1999) ; Zhao, Pham et Vincent (2026) | Une spirale reproduite n'est pas une spirale expliquée |

---

## 3. Dispositif expérimental

### 3.0 Faire varier une instance à la fois

Le dispositif traduit la clef de lecture : chaque instance de l'agencement a ses conditions, pour que sa part puisse être estimée (cadre scientifique, section 6.4).

| Instance | Conditions qui la font varier | Section | Hypothèses |
|---|---|---|---|
| Modèle de langage et fournisseur | Narrateurs N1 à N3 ; test sans public (étape 0a) ; « tout Le Chonk » et auteur unique | 3.5, 5 | HT1, HT2, HT3, S5c |
| Modèle en interaction | Dyades contrôlées (étape 0b) | 3.9, 5 | HT4, S5b |
| Fiche du persona | Disposition attribuée continue ; condition sans autocensure ; permutations | 3.4, 3.9 | HT1, S4, S5a |
| Orchestrateur | Lecture intégrale ou annotée | 3.3 | HT3 |
| Ordonnanceur | O-ALÉ ou O-HOM | 3.5 | HT1, S7 |
| Cadres d'énonciation | Scène publique ou privée ; gazette G0, G+, G− ; compères | 3.6, 3.8 | HT1, S1, S2 |
| Source | S0, S1, S2, S3 | 3.2 | HT2, S1, S5c |
| Agencement social | Village contre chaînes linéaires | 3.10 | HT3, S8 |
| Concepteur | Carnet de conception ; paraphrases de consignes | Cadre 6.2 | Réflexivité |

### 3.1 Le village

Saint-Aubert-sur-Lys, les 40 habitants des expériences C1 à C3, construits selon le protocole anti-biais (attributs tirés par script, décorrélation, OCEAN, audits, permutations des prénoms et du genre). Société contemporaine transposée, **sans partis, élus ni personnalités réels**, **sans élection en cours**. Les habitants sont joués par le modèle ILaaS le mieux calibré à l'étape 1.

### 3.2 Les sources

| Code | Source | Rôle | Position sur le continuum de la communication scientifique (Jacobi, 1999) |
|---|---|---|---|
| **S0** | Un ouvrage d'historien **non moralement chargé**, de même format et de même diffusion (par exemple une histoire d'une technique ou d'un objet du quotidien) | **Ligne de base** : combien parle-t-on d'un livre quand rien n'est en jeu ? | Essai d'historien pour le grand public |
| **S1** | *Les irresponsables* | Le savoir savant étudié | Essai d'historien pour le grand public |
| **S2** | Un compte rendu journalistique de S1 | La médiation journalistique | Discours médiatique |
| **S3** | Un ouvrage d'historien proposant une autre lecture de la même période | Contrôle symétrique | Essai d'historien pour le grand public |

Critères préenregistrés : même période traitée pour S3, **genre comparable** pour S0, S1 et S3, diffusion grand public pour S2.

### 3.3 Le lecteur

Un habitant, joué par **Le Chonk**, a lu la source et en parle si la conversation s'y prête. Position centrale dans le réseau. Mode de lecture : **lecture annotée** (notes de lecture plus les 5 passages les plus pertinents retrouvés à chaque conversation). Les notes de lecture et la grille des propositions sont **validées par une seconde personne indépendante**, idéalement un ou une historienne. Cinq simulations en lecture intégrale servent de contrôle.

### 3.4 Les personas : attributs propres au C4

| Attribut | Construction | Statut |
|---|---|---|
| Sensibilité politique (positions et valeurs, jamais d'étiquette partisane) | Distribution inspirée d'enquêtes publiques (baromètre de la confiance politique du CEVIPOF, European Social Survey), pour garantir la **diversité** des agents, sans prétention de représentativité | Attribut écrit |
| **Disposition à s'autocensurer** | Score tiré indépendamment des autres attributs, exprimé en consignes de comportement, inspiré de l'échelle de Hayes et al. (2005) | Attribut écrit ; son effet sur le comportement est une hypothèse (S5a), non un acquis |
| Rapport à l'histoire et à la lecture | Tiré indépendamment | Attribut écrit |

### 3.5 Ordonnanceur et narrateur

Le meneur de jeu de la version précédente est scindé en deux :

| Composant | Nature | Rôle | Conditions |
|---|---|---|---|
| **Ordonnanceur** | Code (algorithme), pas un modèle de langage | Décide qui rencontre qui, où, quand ; insère les sollicitations standardisées ; fait respecter le pare-feu de la connaissance | **O-ALÉ** : rencontres tirées selon le réseau et les routines ; **O-HOM** : rencontres favorisant les agents de positions déclarées proches (chambre d'écho) |
| **Narrateur** | Modèle de langage | Écrit uniquement la description des scènes | **N1** : Le Chonk ; **N2** : `qwen-3.8-27b` ; **N3** : `gemma-4-31b` |

Cette séparation distingue l'organisation de l'exposition (le dispositif) de l'écriture des scènes (l'architexte).

### 3.6 Scènes publiques et scènes privées

L'ordonnanceur étiquette chaque rencontre :
- **scène publique** : café, marché, réunion, au moins trois agents dont des non-proches ;
- **scène privée** : tête-à-tête avec un proche.

Chaque agent connaît les deux types de scènes en proportions équilibrées.

### 3.7 Sollicitations standardisées

Pour mesurer le silence sans ambiguïté, l'ordonnanceur insère à heures fixes une **sollicitation ouverte**, identique dans toutes les conditions, portée par un habitant tiré au hasard : par exemple « Quelqu'un a lu quelque chose d'intéressant ces temps-ci ? », puis, si le livre est évoqué par quelqu'un, « Et vous, vous en pensez quoi ? ».

Chaque agent reçoit au moins 5 sollicitations en scène publique et 5 en scène privée sur 15 journées. Le **taux de silence** se calcule sur ces sollicitations, pour les seuls agents informés de l'existence du livre (d'après l'enquête du soir).

### 3.8 Les deux sources du climat d'opinion

**La gazette (médias)** paraît aux jours 2, 5, 8 et 11.

| Code | Gazette |
|---|---|
| **G0** | Pas de gazette |
| **G+** | Gazette consonante favorable au livre |
| **G−** | Gazette consonante critique |

Les textes sont **rédigés par le pilote**, **appariés** (même longueur, même structure, même intensité), et vérifiés par deux évaluateurs indépendants. Ils ne sont jamais publiés comme de vraies critiques.

**Les compères (entourage)**, bloc exploratoire : quatre habitants programmés expriment une position fixe en scène publique, sur le principe des expériences d'Asch (1956). Conditions **K+** (compères favorables) et **K−** (compères critiques). Leur adhésion à la position fixée est contrôlée ; ils sont exclus des analyses.

### 3.9 Trois parts de l'agencement et leurs tests (QR-C)

| Mécanisme | Signature attendue | Test | Où |
|---|---|---|---|
| **Fiche du persona** : mécanisme social simulé (disposition à s'autocensurer) | Silence croissant avec la disposition attribuée ; plus fort en public ; absent sans autocensure | Variation continue de la disposition ; **condition sans autocensure** (disposition minimale pour tous, aucune consigne évoquant le risque social) | Village |
| **Modèle en interaction** : complaisance | Position exprimée qui suit celle de l'interlocuteur | **Dyades contrôlées** : chaque persona, avec sa position déclarée, rencontre en tête-à-tête un interlocuteur favorable puis critique ; on mesure le déplacement | Étape préalable 0b |
| **Neutralité apprise** | Neutralisation sans public ni interlocuteur, plus forte pour les thèses controversées | **Test sans public** : chaque modèle, sans persona puis avec persona, répond seul à des questions sur S0, S1, S3 | Étape préalable 0a |

Les trois tests peuvent donner des résultats compatibles entre eux : plusieurs mécanismes peuvent coexister. L'analyse estime la contribution de chacun.

### 3.10 Chaîne de transmission préalable (QR-D, S8)

Avant le village, la thèse (S1) et le savoir témoin (S0) passent par des **chaînes linéaires de 10 agents**, selon le protocole de l'expérience C0 du cadre scientifique. On obtient ainsi les transformations dues à la seule transmission ; la comparaison avec le village montre ce qu'ajoute la structure sociale (réseau, scènes, climat).

---

## 4. Mesures

### 4.1 L'enquêteur du soir (hors mémoire des agents)

Cadre explicitement confidentiel : « Tes réponses ne seront connues de personne au village. »

1. As-tu entendu parler d'un livre d'histoire récemment ? (oui, non)
2. Raconte ce que tu en sais, avec tes mots. (texte libre)
3. De qui le tiens-tu ? (traçabilité)
4. **Position déclarée, formulation A** : à quel point es-tu d'accord avec ce que dit ce livre ? (0 à 100)
5. **Climat perçu** : selon toi, quelle part du village est d'accord avec ce livre ? (0 à 100 %)
6. **Tendance perçue** : cet avis gagne-t-il du terrain, reste-t-il stable, recule-t-il ?
7. **Test du train** (Noelle-Neumann) : pendant un long trajet en train, accepterais-tu d'en discuter avec un inconnu qui pense le contraire ? (oui, peut-être, non)
8. As-tu parlé du livre aujourd'hui ? Si oui, avec qui, et qu'as-tu dit ?
9. **Position déclarée, formulation B** (test de stabilité) : ce livre a-t-il raison, selon toi ? (0 = pas du tout, 100 = tout à fait)

Un écart de plus de 20 points entre les formulations A et B signale une position instable. La part d'agents instables est rapportée.

### 4.2 Codage des scènes

Chaque réponse à une sollicitation, et chaque réplique où le livre est évoqué, est codée par un **modèle juge différent des modèles qui ont généré la simulation**, validé par double codage humain :
- le livre est-il évoqué ? Une position est-elle exprimée ?
- laquelle (favorable, critique, neutre, ambiguë) ?
- forme éventuelle du silence (4.4) ;
- correspondance avec la position déclarée le soir précédent.

### 4.3 Indicateurs

| Indicateur | Définition | Hypothèses |
|---|---|---|
| **Taux de silence** | Part des sollicitations sans position exprimée, chez les agents informés, par type de scène, par source | S1, S5 |
| **Écart entre cadres d'énonciation** | Différence entre position déclarée en enquête et position exprimée en scène, pour un même agent | S1, S5, S6 |
| **Double climat** | Écart entre climat perçu moyen et distribution réelle des positions déclarées, selon la gazette | S2 |
| **Ignorance pluraliste** | Part des agents majoritaires (en positions déclarées) qui se déclarent minoritaires | S3 |
| **Noyau dur** | Agents exprimant en public une position perçue comme minoritaire sur au moins 3 journées | S4 |
| **Déplacement en dyade** | Écart de position exprimée entre interlocuteur favorable et interlocuteur critique | S5b |
| **Taux de neutralisation sans public** | Part des réponses neutralisées en test sans public, par source | S5c |
| **Falsification des préférences** | Part des positions exprimées contraires aux positions déclarées | S1, S5 |
| **Ce qui s'entend** | Distribution des positions exprimées en public, comparée à celle des positions déclarées | Toutes |
| **Transformations de la thèse** | Livre de codes unifié, appliqué séparément aux versions publiques, privées et aux chaînes linéaires | S6, S8 |
| **Polarisation** | Dispersion des positions déclarées et des positions exprimées | S7 |
| **Stabilité** | Part d'agents dont les formulations A et B divergent | Contrôle |

### 4.4 Les formes du silence

Un livre de codes spécifique décrit les **formes discursives du silence** :

| Code | Forme | Exemple de forme |
|---|---|---|
| EVI | Évitement | Changement de sujet quand le livre est évoqué |
| NEU | Neutralisation | « Chacun pense ce qu'il veut » |
| EUP | Euphémisation | Position atténuée jusqu'à l'insignifiance |
| DEL | Délégation | « Il faudrait demander à quelqu'un qui l'a lu » |
| ALI | Alignement apparent | Position exprimée contraire à la position déclarée |
| TAC | Silence pur | Aucune réponse au fond alors que la sollicitation est directe |

Les formes NEU et EUP sont précisément celles que la neutralité apprise peut produire : leur fréquence en test sans public (S5c) sert de référence pour les interpréter dans le village.

---

## 5. Étapes préalables

| Étape | Contenu | Durée |
|---|---|---|
| **Revue n° 2** | Revue croisée des documents par un autre modèle (consigne : réfuter) et par un ou une collègue de SIC, avant le préenregistrement | 1 semaine |
| **0a. Profil des modèles et test sans public** | Chaque modèle répond sans persona à des items d'enquête publics (CEVIPOF, ESS), 10 fois ; puis, sans persona et avec persona, seul, à des questions sur S0, S1, S3 | 1 semaine |
| **0b. Dyades contrôlées** | 40 personas × interlocuteur favorable puis critique × S1 et S0 × 3 répétitions (environ 480 courts dialogues) | En parallèle |
| **1. Cohérence des personas** | Les personas répondent aux items d'enquête et à l'échelle d'autocensure ; contrôle de cohérence avec les attributs (sans valeur de validation) | 1 semaine |
| **2. Grille des propositions et notes de lecture** | Extraction par Le Chonk ; validation par l'ingénieur pédagogique et par une seconde personne indépendante | 1 semaine |
| **3. Livres de codes** | Transformations, lectures, formes du silence ; test sur le mini-village ; regard extérieur ; figement et préenregistrement | 1 semaine |
| **4. Gazette** | Rédaction appariée de G+ et G−, vérification par deux évaluateurs | En parallèle |
| **5. Chaînes de transmission** | S1 et S0, chaînes de 10 agents, 10 chaînes par source | En parallèle |
| **6. Pilote et puissance** | 3 simulations pilotes ; estimation de la variance entre graines ; calcul du nombre de graines ; vérification de la saturation sur 15 journées | 1 semaine |

---

## 6. Plan d'expérience à priorités

Le nombre de graines est confirmé ou ajusté après le pilote (étape 6). Toutes les simulations utilisent l'ordonnanceur O-ALÉ et le narrateur N1, sauf mention contraire.

**Priorité 1 : questions centrales (garantie)**

| Bloc | Conditions | Simulations |
|---|---|---|
| Cœur | S1 × gazette G0, G+, G− × 5 graines | 15 |
| Ligne de base | S0 × G0 × 5 graines | 5 |
| Mécanismes | S1 × G0 × condition sans autocensure × 5 graines | 5 |
| **Sous-total** | | **25** |

**Priorité 2 : comparaisons (selon budget)**

| Bloc | Conditions | Simulations |
|---|---|---|
| Symétrie | S3 × G0 × 5 graines | 5 |
| Lecture intégrale | S1 × G0 × 5 graines | 5 |
| Médiation | S2 × G0 × 3 graines | 3 |
| Ordonnancement homophile | S1 × G0 × O-HOM × 3 graines | 3 |
| Narrateurs | S1 × G0 × N2, N3 × 3 graines | 6 |
| **Sous-total** | | **22** |

**Priorité 3 : exploratoire**

| Bloc | Conditions | Simulations |
|---|---|---|
| Compères | S1 × K+, K− × 3 graines | 6 |
| Durée longue | S1 × G0 × 30 journées × 3 graines | 3 |
| Auteur unique | Le Chonk écrit d'un seul tenant les 15 journées, S1, G0 | 3 |
| **Sous-total** | | **12** |

**Total : 59 simulations**, plus le pilote et les étapes préalables (peu coûteuses).

**Coût estimé** : 10 à 25 $ par simulation avec Le Chonk comme lecteur et narrateur, soit environ 250 à 625 $ pour la priorité 1 et 600 à 1 500 $ pour l'ensemble. À recalculer selon les conditions de la clé et la mise en cache. Les tokens et une estimation énergétique sont journalisés.

---

## 7. Analyse

1. **Quantitative** : modèles à effets mixtes (silence, écart entre cadres, climat perçu, positions exprimées) expliqués par la source, la gazette, la condition d'autocensure, le type de scène, l'ordonnanceur, le narrateur et l'écart entre position déclarée et climat perçu, avec effets aléatoires par simulation et par agent. Pour les indicateurs collectifs, l'unité est la simulation.
2. **Décomposition par instance (QR-C, HT1)** : c'est l'analyse principale. On estime la part de chaque instance dans le dire et le taire (fiche, modèle et fournisseur, modèle en interaction, cadres d'énonciation, ordonnanceur, source), en s'appuyant sur les conditions de la section 3.0 et en comparant systématiquement S1 à S0. Une part qui ne peut pas être isolée est déclarée comme telle.
3. **Étalonnage théorique (QR-E)** : les trajectoires du village sont confrontées aux familles de formalisations du projet sur la spirale du silence ; on compare la qualité d'ajustement de chaque famille. Un bon ajustement indique une ressemblance de forme, non une identité de mécanisme (suffisance générative).
4. **Structure sociale (S8)** : comparaison des transformations dans le village et dans les chaînes linéaires.
5. **Qualitative** : analyse de discours d'une sélection préenregistrée de chaînes de reformulation, publiques et privées, et des formes du silence.
6. **Interprétation critique** : confrontation aux résultats humains (comparaison qualitative, sauf pour les questions reprises à l'identique des études) et aux travaux sur agents génératifs. Les écarts sont traités comme des résultats sur l'architexte et le dispositif.

**Fiabilité** : double codage humain à l'aveugle de 15 % du corpus (kappa ≥ 0,7) ; modèle juge distinct des générateurs ; résultats retenus seulement s'ils sont stables entre graines ; tests de permutation des prénoms et du genre.

**Critères de réussite** : accord de codage atteint ; résultats de priorité 1 stables entre graines ; part de chaque instance estimée. Quel que soit le sens des résultats sur S1 à S8, une expérience qui satisfait ces critères est publiable.

---

## 8. Déroulé (10 semaines, après validation de C1 à C3)

| Semaine | Activité | Responsable |
|---|---|---|
| S1 | Revue n° 2 ; choix de S0, S2, S3 | Ingénieur pédagogique |
| S2 | Préenregistrement ; étapes 0a et 0b | Ingénieur pédagogique |
| S3 | Étape 1 ; étape 4 (gazette) ; ajout des attributs C4 | Ingénieur pédagogique |
| S4 | Étape 2 (grille et notes, validation indépendante) ; étape 5 (chaînes) | Ingénieur pédagogique, validateur externe |
| S5 | Étape 3 (livres de codes, regard extérieur) ; étape 6 (pilote, puissance) | Ingénieur pédagogique, relecteur extérieur |
| S6 | Priorité 1 | Ingénieur pédagogique |
| S7 | Priorités 2 et 3 selon budget | Ingénieur pédagogique |
| S8 | Codage automatique et humain, fiabilité | Ingénieur pédagogique, second codeur extérieur |
| S9 | Analyses quantitative, mécanismes, étalonnage, qualitative | Ingénieur pédagogique |
| S10 | Rédaction | Ingénieur pédagogique |

**Tableau de bord** (développé par le pilote avec OpenCode, dans le bureau des agents) : pour chaque journée, deux vues du village côte à côte, « ce qui est déclaré en enquête » et « ce qui s'entend en scène », avec l'arbre de circulation de la thèse et la position des sollicitations.

---

## 9. Précautions

| Point | Précaution |
|---|---|
| Circularité | Aucune lecture du présent injectée ; les analogies sont observées, jamais suggérées |
| Statut des énoncés | Vocabulaire des cadres d'énonciation ; aucune intériorité prêtée aux agents |
| Biais des modèles | Mesurés en amont (étape 0a), utilisés comme variable (narrateur), jamais présentés comme reflet de la société |
| Confidentialité simulée | Le cadre « confidentiel » de l'enquêteur est un cadre d'énonciation parmi d'autres, non un accès à une vérité de l'agent |
| Interprétation | On parle de « sociétés d'agents » ; aucun résultat n'est présenté comme une mesure de l'opinion française |
| Calendrier électoral | Aucune mesure de préférence partisane ni d'intention de vote ; publication cadrée comme méthodologique, hors période de campagne présidentielle |
| Personas | Protocole anti-biais complet ; sensibilités décrites par des valeurs, jamais par des étiquettes partisanes |
| **Auteurs vivants** | Les versions déformées des thèses de S1 et S3 sont toujours présentées comme des productions d'agents, jamais comme des propos des auteurs ; traitement symétrique de S1 et S3 ; prise de contact courtoise avec les auteurs avant publication |
| Ouvrages | Pas de journal brut publié s'il contient de longs extraits |
| Gazette et compères | Textes et personnages fictifs, jamais présentés comme réels |
| Contenus produits | Tout contenu discriminatoire ou outrancier est une donnée : analysé, contextualisé, jamais publié en verbatim brut |
| Sobriété | Tokens et estimation énergétique rapportés |

---

## 10. Livrables

1. Le tableau des profils des modèles et des taux de neutralisation sans public.
2. L'étude des dyades contrôlées (complaisance).
3. La grille des propositions et les livres de codes (transformations, lectures, formes du silence).
4. Le module C4 en code ouvert, avec ordonnanceur et sollicitations standardisées.
5. Le tableau de bord « ce qui est déclaré, ce qui s'entend ».
6. Un article de recherche en SIC : dire et taire un savoir savant dans une société d'agents génératifs.
7. Un billet de retour d'expérience.

---

## 11. Bibliographie

### Spirale du silence et opinion publique
- Asch, S. E. (1956). Studies of independence and conformity: I. A minority of one against a unanimous majority. *Psychological Monographs: General and Applied*, 70(9), 1-70.
- Bourdieu, P. (1973). L'opinion publique n'existe pas. *Les Temps modernes*, 318, 1292-1309.
- Champagne, P. (1990). *Faire l'opinion. Le nouveau jeu politique*. Paris : Minuit.
- Glynn, C. J., Hayes, A. F., & Shanahan, J. (1997). Perceived support for one's opinions and willingness to speak out: A meta-analysis of survey studies on the "spiral of silence". *Public Opinion Quarterly*, 61(3), 452-463.
- Hayes, A. F., Glynn, C. J., & Shanahan, J. (2005). Willingness to self-censor: A construct and measurement tool for public opinion research. *International Journal of Public Opinion Research*, 17(3), 298-323.
- Kuran, T. (1995). *Private Truths, Public Lies: The Social Consequences of Preference Falsification*. Cambridge, MA : Harvard University Press.
- Matthes, J., Knoll, J., & von Sikorski, C. (2018). The "spiral of silence" revisited: A meta-analysis on the relationship between perceptions of opinion support and political opinion expression. *Communication Research*, 45(1), 3-33.
- Noelle-Neumann, E. (1974). The spiral of silence: A theory of public opinion. *Journal of Communication*, 24(2), 43-51.
- Noelle-Neumann, E. (1993). *The Spiral of Silence: Public Opinion, Our Social Skin* (2e éd.). Chicago : University of Chicago Press.
- Prentice, D. A., & Miller, D. T. (1993). Pluralistic ignorance and alcohol use on campus: Some consequences of misperceiving the social norm. *Journal of Personality and Social Psychology*, 64(2), 243-256.
- Scheufele, D. A., & Moy, P. (2000). Twenty-five years of the spiral of silence: A conceptual review and empirical outlook. *International Journal of Public Opinion Research*, 12(1), 3-28.

### Circulation, trivialité, transmission, médiation des savoirs
- Acerbi, A., & Stubbersfield, J. M. (2023). Large language models show human-like content biases in transmission chain experiments. *Proceedings of the National Academy of Sciences*, 120(44), e2313790120.
- Allport, G. W., & Postman, L. (1947). *The Psychology of Rumor*. New York : Henry Holt.
- Authier-Revuz, J. (1982). La mise en scène de la communication dans des discours de vulgarisation scientifique. *Langue française*, 53, 34-47.
- Hall, S. (1973). *Encoding and Decoding in the Television Discourse*. Birmingham : CCCS.
- Jacobi, D. (1999). *La communication scientifique. Discours, figures, modèles*. Grenoble : PUG.
- Jeanneret, Y. (2008). *Penser la trivialité. Volume 1 : La vie triviale des êtres culturels*. Paris : Hermès-Lavoisier.
- Krieg-Planque, A. (2009). *La notion de « formule » en analyse du discours*. Besançon : Presses universitaires de Franche-Comté.
- Mesoudi, A., & Whiten, A. (2008). The multiple roles of cultural transmission experiments in understanding human cultural evolution. *Philosophical Transactions of the Royal Society B*, 363(1509), 3489-3501.
- Moirand, S. (2007). *Les discours de la presse quotidienne. Observer, analyser, comprendre*. Paris : PUF.
- Perez, J., Kovač, G., Léger, C., Colas, C., Molinaro, G., Derex, M., Oudeyer, P.-Y., & Moulin-Frier, C. (2025). When LLMs Play the Telephone Game: Cultural Attractors as Conceptual Tools to Evaluate LLMs in Multi-turn Settings. *Proceedings of ICLR 2025*.
- Souchier, E., Jeanneret, Y., & Le Marec, J. (dir.) (2003). *Lire, écrire, récrire. Objets, signes et pratiques des médias informatisés*. Paris : Bibliothèque publique d'information.

### Agents génératifs, modèles de langage, validation
- Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., & Wingate, D. (2023). Out of One, Many: Using Language Models to Simulate Human Samples. *Political Analysis*, 31(3), 337-351.
- Epstein, J. M. (1999). Agent-based computational models and generative social science. *Complexity*, 4(5), 41-60.
- Larooij, M., & Törnberg, P. (2025). Validation is the central challenge for generative social simulation: a critical review of LLMs in agent-based modeling. *Artificial Intelligence Review*. *arXiv:2504.03274*.
- OpenAI (2025). *Model Spec*. Spécification publique du comportement attendu des modèles.
- Panickssery, A., Bowman, S. R., & Feng, S. (2024). LLM Evaluators Recognize and Favor Their Own Generations. *Advances in Neural Information Processing Systems 37 (NeurIPS 2024)*.
- Park, J. S., O'Brien, J., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative Agents: Interactive Simulacra of Human Behavior. *Proceedings of UIST '23*.
- Sharma, M., Tong, M., Korbak, T., et al. (2024). Towards Understanding Sycophancy in Language Models. *Proceedings of ICLR 2024*.
- Wang, A., Morgenstern, J., & Dickerson, J. P. (2025). Large language models that replace human participants can harmfully misportray and flatten identity groups. *Nature Machine Intelligence*.
- Yang, K., Lee, S., Peng, T.-Q., & Liu, H. (2026). Think-Before-Speak: From Internal Evaluation to Public Expression in Multi-Agent Social Simulation. *arXiv:2606.03137*.
- Zhao, P., Pham, D. H., & Vincent, N. (2026). Mechanism Plausibility in Generative Agent-Based Modeling. *Proceedings of ACM FAccT '26*. *arXiv:2605.12824*.
- Zhong, M., Fang, M., Shi, Z., Huang, Y., Zheng, S., Du, Y., Chen, L., & Wang, J. (2025). Spiral of Silence in Large Language Model Agents. *Findings of the Association for Computational Linguistics: EMNLP 2025*. *arXiv:2510.02360*.

### Modèles computationnels de la spirale du silence
- Ross, B., Pilz, L., Cabrera, B., Brachten, F., Neubaum, G., & Stieglitz, S. (2019). Are social bots a real threat? An agent-based model of the spiral of silence to analyse the impact of manipulative actors in social networks. *European Journal of Information Systems*, 28(4), 394-412.
- Sohn, D. (2022). Spiral of silence in the social media era: A simulation approach to the interplay between social networks and mass media. *Communication Research*, 49(1), 139-166.

### Cadres de l'interaction, attracteurs culturels, agentivité distribuée
- Akrich, M., & Latour, B. (1992). A Summary of a Convenient Vocabulary for the Semiotics of Human and Nonhuman Assemblies. In W. E. Bijker & J. Law (dir.), *Shaping Technology/Building Society* (p. 259-264). Cambridge, MA : MIT Press.
- Callon, M. (1986). Éléments pour une sociologie de la traduction. *L'Année sociologique*, 36, 169-208.
- Goffman, E. (1974). *Frame Analysis: An Essay on the Organization of Experience*. New York : Harper & Row. Trad. fr. *Les cadres de l'expérience*, Paris : Minuit, 1991.
- Latour, B. (2006). *Changer de société, refaire de la sociologie*. Paris : La Découverte.
- Sperber, D. (1996). *La contagion des idées. Théorie naturaliste de la culture*. Paris : Odile Jacob.
- Suchman, L. (2007). *Human-Machine Reconfigurations: Plans and Situated Actions* (2e éd.). Cambridge : Cambridge University Press.

### Ouvrage étudié
- Chapoutot, J. (2025). *Les irresponsables. Qui a porté Hitler au pouvoir ?* Paris : Gallimard.

*Références à contrôler (pagination, éditions) avant toute publication. La référence au Model Spec d'OpenAI est à dater précisément selon la version consultée.*
