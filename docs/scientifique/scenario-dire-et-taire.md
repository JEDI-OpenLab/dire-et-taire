# Scénario « Dire et taire » : la circulation d'un savoir savant

*Scénario unique du village simulé, sous l'angle de la spirale du silence. Cas d'étude : Johann Chapoutot, Les irresponsables (Gallimard, 2025). Version 11.3 du 21 octobre 2026 : volet réflexif sur la complexité et l'incertitude (cadre, 2.6) ; hypothèse descriptive HO12 et indicateur « part du hasard » (1.2, 1.6, 4.3, 5, 7, 8, 10, 11). Version 11.2 du 19 octobre 2026 : état de l'offre ILaaS relevé à l'installation de la station (3.1, « Offre ILaaS ») ; le juge `qwen-3.6-35b-a3b` est en cours de retrait et son remplaçant reste à décider ; Mistral Medium n'est publié que sous un alias « latest ». Version 11.1 du 17 octobre 2026 : le projet ne compte plus qu'un scénario ; les codes « C4 » et les renvois aux anciennes expériences C0 à C3 sont retirés ; la construction des 40 habitants devient l'étape 0, avant les profils et les dyades, et le test de débit se fait sur des fiches provisoires (3.1, 5, 8). Version 11 du 16 octobre 2026 : suites de la revue n° 2 (dix-sept décisions du chercheur, consignées dans « ../revues/revue-adversariale-2-cadre-et-scenario.md », section 10). Principaux changements : HT1 relative aux contrastes déclarés, contraste principal de scène, fiche à étendue maximale et contrôle de manipulation (1.5, 1.6, 7.2) ; règle de décision de HT2 (7.3) ; borne de HO9 abaissée à ±0,05 (7.4) ; modèle nul des chaînes linéaires pour la convergence (7.5) et règle pour HO8 (7.6) ; mémoire d'entraînement et test de connaissance préalable (1.2, 3.2, étape 0a) ; gazette neutre G= (3.8) ; enquête du matin (4.1) ; versions de modèles épinglées (3.1) ; M-PLU sans Le Chonk ni Gemma, comparé à M-AUT (3.1) ; 10 graines pour les bras de HO11 joués entre simulations (6) ; codage de référence et fiabilité précisés (7) ; billets de méthode seulement avant l'élection présidentielle de 2027 (8, 9). La version 10 avait fixé la condition de référence « tout Le Chonk » ; la version 9 avait levé les points bloquants relevés par la carte des concepts (« ../visualisations/carte-concepts.html »).*

*Documents associés : « cadre-scientifique-SIC-village.md » (cadre théorique général, version 6.4), « projet-spirale-du-silence-formalisation.md » (formalisations de la théorie, qui servent ici d'étalons), « preenregistrement-premier-temps.md » (ébauche du premier temps du préenregistrement), « ../revues/revue-adversariale-1-cadre-et-scenario.md » et « ../revues/revue-adversariale-2-cadre-et-scenario.md » (revues et décisions).*

*Projet mené seul par l'ingénieur pédagogique (SIC), qui assure aussi la relecture. Les pairs interviennent ensuite : publication progressive de billets sur le carnet de recherche (jediopenlab.hypotheses.org), puis soumission d'articles. La méthode compense l'absence de second codeur (section 7).*

*Les termes, leur paternité et leurs références d'origine sont définis dans « ../glossaire.md ».*

**Codes employés dans ce document.** T0 à T3 : textes sources. HT1 à HT4 : hypothèses de travail. HO1 à HO12 : hypothèses opérationnelles. QR-A à QR-E : questions de recherche du scénario. G0, G=, G+, G− : gazette. K+, K− : compères. O-ALÉ, O-HOM : ordonnanceur. M-LC, M-AUT, M-PLU : modèle qui joue le village. N1 à N3 : narrateur. Les semaines du déroulé sont écrites en toutes lettres.

---

## 1. Problématique

### 1.1 La clef de lecture : qui se tait quand un agent se tait ?

Le scénario met en circulation dans le village une thèse d'historien moralement chargée, et observe ce qui s'en dit et ce qui s'en tait. La théorie de la spirale du silence (Noelle-Neumann, 1974, 1993) sert d'instrument : elle oblige à regarder ce qui **ne circule pas**, et elle fournit des mesures (climat perçu, test du train, écart entre ce qui est déclaré et ce qui est exprimé).

Mais la question du scénario n'est pas de savoir si des machines « reproduisent » la spirale du silence. Elle découle de la clef de lecture de tout le projet, la **co-agentivité** (cadre scientifique, section 1) : une réplique n'est jamais l'acte d'un seul agent, elle est co-produite par un agencement de six instances (inventaire complet en 3.0).

| Instance | Comment elle peut produire du dire ou du taire |
|---|---|
| **Le modèle de langage et son fournisseur** | Neutralité apprise sur les sujets controversés ; complaisance envers l'interlocuteur ; régularités de formulation ; mémoire d'entraînement (ce qu'il sait déjà du livre et de sa réception) |
| **La fiche du persona** | Disposition attribuée à l'autocensure, sensibilité, rapport à l'histoire |
| **L'orchestrateur** | Ce que l'agent « sait » du livre et de ce qu'en pensent les autres (mémoire, notes de lecture) |
| **L'ordonnanceur** | Qui rencontre qui, en public ou en privé ; chambres d'écho |
| **Les cadres d'énonciation** | Scène publique, tête-à-tête, gazette, compères, sollicitations |
| **Le concepteur** | Tout ce qui précède, et le choix des contrastes qui servent à mesurer les parts |

Le silence, s'il apparaît, n'est donc pas « celui d'un habitant » : c'est **une production de l'agencement**. La question devient : **quelles instances produisent le dire et le taire, sous quelles formes, et dans quelles proportions ?**

### 1.2 Posture

- Le village n'est pas un modèle de la société française ; aucun résultat n'est généralisé à des personnes réelles.
- Aucune instance n'a d'intériorité : on parle de **position déclarée en enquête** et de **position exprimée en scène** ; le « taire » désigne l'absence, ou la neutralisation, de position exprimée face à une sollicitation.
- Le concepteur est une instance de l'agencement ; sa part est documentée par le carnet de conception.
- Le livre étudié ne sert pas à juger une thèse historique, mais à observer ce qu'un agencement génératif fait d'un savoir savant moralement chargé. Aucune lecture du présent n'est injectée ; les analogies sont observées, jamais suggérées.
- **Ce que le village sait déjà.** Le modèle connaît probablement le livre et sa réception par ses données d'entraînement. Le projet traite ce savoir comme la **culture commune** du village, l'équivalent d'un souvenir de cours d'histoire, à une différence près : il est identique chez les 40 habitants, puisqu'un seul modèle les joue. Cette mémoire d'entraînement est mesurée avant toute circulation (3.2, étape 0a) ; ce qu'elle apporte est rapporté comme part du modèle, et non comme circulation.
- **Ce que le concepteur ne programme pas.** Le concepteur écrit tout le village, mais ne peut pas prévoir ce qui s'y dira : c'est l'écologie de l'action au sens de Morin. Le projet distingue l'incertitude programmée (graines, tirages), l'incertitude générée (modèles et interactions, bornée par l'architexte) et l'incertitude du chercheur, déclarée plutôt que masquée. Ce volet réflexif, sans hypothèse de travail, sert un recul pédagogique et méthodologique (cadre, 2.6 ; HO12).

### 1.3 Problématique

> **Comment un dispositif génératif met-il en scène le dire et le taire autour d'un savoir savant, alors que ses agents, conçus pour toujours répondre, n'ont rien à craindre de la parole ?**

| Terme | Contenu | Pourquoi |
|---|---|---|
| **X** | Un dispositif génératif met en scène le dire et le taire autour d'un savoir savant | X ne présuppose pas que le silence apparaîtra : si tous les agents parlent, le résultat répond aussi à la question |
| **Y** | Ses agents sont conçus pour toujours répondre et n'ont rien à craindre de la parole | Un modèle de langage est entraîné à produire du texte et à ne laisser aucune question sans réponse ; il n'a ni corps social, ni réputation, ni peur de l'isolement, ressort central de la spirale du silence (Noelle-Neumann, 1993), absence que reconnaissent Zhong et al. (2025) |

**Ce que Y contient.** Les deux moitiés de Y ne pèsent pas le même poids. « Conçus pour toujours répondre » est vrai de la forme (un modèle ne laisse pas une question sans texte) et discutable du fond : les fournisseurs règlent aussi leurs modèles pour ne pas prendre parti sur les sujets controversés, et c'est l'un des mécanismes testés (HO5c). « N'ont rien à craindre de la parole » est la vraie tension avec la spirale du silence, dont le ressort est la peur de l'isolement. La problématique est gardée ainsi parce que la première moitié décrit l'apparence que le dispositif donne aux agents, et que c'est précisément cette apparence que le scénario interroge.

**Comment la clef de lecture résout la tension.** Y n'est contradictoire que si l'on cherche le silence dans les agents. Si l'agentivité est distribuée, des agents qui n'ont rien à craindre peuvent quand même produire du taire, parce que **ce ne sont pas eux seuls qui parlent ou se taisent** : la fiche, les cadres, l'ordonnanceur, le concepteur et, derrière le modèle, son fournisseur et ses règles de neutralité, y prennent part.

### 1.4 Questions de recherche

| Code | Question | Lien |
|---|---|---|
| **QR-A. Les formes du dire et du taire** | Face à des sollicitations standardisées, quelles positions l'agencement exprime-t-il sur une thèse moralement chargée, par rapport à un savoir sans enjeu, en public et en privé ? Sous quelles formes le taire se manifeste-t-il ? | X |
| **QR-B. Le climat** | Comment se forme le climat d'opinion déclaré perçu, quelles instances le façonnent (entourage, gazette, ordonnancement), et pèse-t-il sur ce qui se dit ? | X |
| **QR-C. La part des instances** | Quelle part du dire et du taire revient à chaque instance : modèle et fournisseur (neutralité apprise, complaisance), fiche, orchestrateur, ordonnanceur, cadres d'énonciation, concepteur ? | Y, question centrale |
| **QR-D. La trivialité co-produite** | Quelles versions de la thèse dominent ce qui s'entend dans le village, convergent-elles, et que change l'agencement social (réseau, scènes, mémoire) par rapport à une transmission linéaire ? | Conséquence |
| **QR-E. L'étalonnage théorique** | De quelle formalisation de la spirale du silence la dynamique de l'agencement se rapproche-t-elle le plus ? Étalons publiés comme plancher (Sohn et Geidner, 2016 ; Ross et al., 2019 ; Aranda et al., 2024), formalisations du projet en complément si elles existent au moment de l'analyse | Conséquence |

La question QR3 du cadre (la conception de la communication que l'agencement réalise) n'a pas d'hypothèse propre dans le scénario : elle est traitée qualitativement au niveau 1 de la grille (section 7).

**Architecture du raisonnement** : problématique (1.3) → questions de recherche (1.4) → hypothèses de travail (1.5), qui proposent des réponses → hypothèses opérationnelles (1.6), qui les traduisent en mesures et en règles de décision → instances et conditions (3.0) → dispositif (3) et mesures (4) → analyse (7).

### 1.5 Hypothèses de travail

| Code | Hypothèse de travail | Réponse proposée à Y | Signature observable | Ce qui la réfuterait |
|---|---|---|---|---|
| **HT1. Le taire est co-produit par l'agencement** *(hypothèse centrale, relative aux contrastes déclarés)* | À contrastes de référence fixés avant toute génération, et en donnant à la fiche son étendue maximale, le dire et le taire varient davantage avec au moins une **instance non individuelle** (cadre d'énonciation en premier lieu, puis gazette, ordonnanceur, modèle) qu'avec les dispositions attribuées aux agents | Des agents qui n'ont rien à craindre produisent du taire parce que d'autres instances le produisent avec eux | Sur le taux de taire, l'écart produit par le contraste de scène (principal) ou par l'un des trois contrastes secondaires dépasse celui de la fiche à son étendue maximale (HO11) | Le contraste de la fiche, même à son étendue maximale, dépasse tous les autres (HO11). Si la consigne de la fiche échoue au contrôle de manipulation (étape 1), l'issue est indéterminée |
| **HT2. Le taire prend la forme d'un dire vide** | L'agencement produit moins de silence pur que de **neutralisation** : les agents parlent toujours, pour ne rien dire | Des agents conçus pour toujours répondre ne se taisent pas ; le taire se loge dans la parole elle-même | Pour T1, les formes NEU, EUP et DEL font plus de la moitié du taire ; le taux de neutralisation (NEU + EUP) pour T1 dépasse celui de T0 d'au moins 5 points, en scène (HO1b) et sans public (HO5c). T3 réplique T1 en priorité 2. Règle en 7.3 | Silences purs (TAC) au moins aussi fréquents que les autres formes, ou neutralisation pour T1 qui n'excède pas celle de T0 |
| **HT3. La trivialité co-produite converge vers le lieu commun** | Parce que les mêmes instances écrivent toutes les voix, les versions de la thèse perdent leurs aspérités et convergent vers une **formule consensuelle** | Un agencement qui écrit toutes les voix tend à leur donner les mêmes formes | La diversité des versions décroît au fil des journées dans les villages joués par un seul modèle (M-LC, M-AUT), plus que par la seule transmission depuis une source unique, mesurée dans les chaînes linéaires à profondeur égale (HO10a) ; formules récurrentes (HO10c) ; décroissance plus forte avec un seul modèle qu'avec plusieurs modèles qui se partagent les habitants (M-AUT contre M-PLU ; HO10b) | Pente de diversité qui n'est pas plus négative que celle des chaînes linéaires en M-LC et M-AUT. Si la convergence est établie sans que HO10b départage, la cause (un architexte unique) reste indéterminée |
| **HT4. Une socialité sans climat** | Ce qui ressemble à du conformisme est un **alignement local** entre le modèle et l'interlocuteur du moment, non une lecture du climat d'opinion : le « sens quasi statistique » n'opère pas | Sans peur de l'isolement, il reste la complaisance conversationnelle, dyadique et non collective | La position exprimée suit celle de l'interlocuteur ; à interlocuteur constant, l'effet du climat perçu est équivalent à zéro, avec une borne (±0,05) inférieure à l'effet humain moyen (r = 0,10 ; Matthes, Knoll et von Sikorski, 2018) ; la gazette déplace le climat perçu sans déplacer ce qui se dit (HO9) | Effet du climat perçu sur la position exprimée au-delà de la borne d'équivalence, à interlocuteur constant |

**Articulation.** HT1 est l'hypothèse centrale, qui découle directement de la clef de lecture. HT2 décrit la **forme** du taire, HT3 la **forme** de ce qui circule, HT4 le **mécanisme** relationnel. HT1 et HT4 sont compatibles (la complaisance est une part du modèle dans l'agencement) ; HT4 contredit en revanche une lecture « spirale » du village. Le dispositif est conçu pour départager.

**Trois issues possibles pour chaque hypothèse de travail** : soutenue, réfutée ou indéterminée, selon les règles de décision préenregistrées (1.6 et 7). Une issue indéterminée est un résultat, rapporté comme tel.

### 1.6 Hypothèses opérationnelles préenregistrées

| Code | Hypothèse opérationnelle | Hypothèse servie | Statut |
|---|---|---|---|
| **HO1. Silence différentiel** | Pour T1 davantage que pour T0, les agents dont la position déclarée du matin s'écarte d'au moins 20 points du climat qu'ils déclarent percevoir expriment moins de positions face aux sollicitations en scène publique qu'en scène privée. Critère : interaction texte × scène dans ce sous-groupe, en points de taux de taire, intervalle excluant zéro ; taille du sous-groupe rapportée par condition | HT1 | Secondaire |
| **HO1b. Neutralisation différentielle** | Le taux de neutralisation (NEU + EUP) face aux sollicitations est plus élevé pour T1 que pour T0 d'au moins 5 points, intervalle excluant zéro | HT2 | Principale (règle en 7.3) |
| **HO2. Double climat** | Une gazette consonante (G+ ou G−) déplace le climat perçu déclaré plus que les positions déclarées, par rapport à la gazette neutre G=. Critère : différence des deux déplacements, chacun standardisé par l'écart-type de sa mesure en G=, intervalle excluant zéro | HT1 ; condition de HO9 | Secondaire |
| **HO3. Ignorance pluraliste** | Dans certaines conditions, une majorité d'agents déclarent percevoir leur position comme minoritaire | Étalonnage (QR-E) ; ne départage aucune hypothèse de travail | Descriptive |
| **HO4. Noyau dur** | Parmi les agents qui se déclarent minoritaires au moins trois journées, ceux à faible disposition attribuée (tiers inférieur) expriment en public une position minoritaire plus souvent que ceux à forte disposition (tiers supérieur). Critère : différence en points, intervalle excluant zéro ; moins de 10 agents par tiers sur l'ensemble des simulations : issue « non testable » | HT1 (part de la fiche) | Secondaire |
| **HO5a. Part de la fiche** | L'effet décrit en HO1 croît avec la disposition attribuée et disparaît dans la condition sans autocensure. Critère : pente de l'effet sur la disposition, intervalle excluant zéro ; effet dans la condition sans autocensure équivalent à zéro (borne ±5 points) | HT1 | Secondaire |
| **HO5b. Part du modèle en interaction** | En dyades contrôlées, la position exprimée se rapproche de celle de l'interlocuteur, indépendamment de la disposition attribuée. Critère : déplacement moyen en dyade, intervalle excluant zéro | HT1, HT4 | Hors village, rapportée à part |
| **HO5c. Part du modèle et du fournisseur** | Les énoncés neutralisés apparaissent même sans public ni interlocuteur, et plus pour T1 que pour T0 (T3 en réplication). Critère : différence des taux de neutralisation d'au moins 5 points, intervalle excluant zéro | HT1, HT2 | Hors village ; entre dans la règle de HT2 |
| **HO6. Assimilation publique** | La position portée par les versions exprimées en public (codée par les juges de −2 à +2) est plus proche de l'avis perçu comme majoritaire que celle des versions exprimées en privé. Critère : différence des distances moyennes, intervalle excluant zéro | HT3 | Secondaire |
| **HO7a. Ordonnanceur et taire** | Des rencontres homophiles (O-HOM) réduisent le taux de taire. Critère : contraste O-HOM contre O-ALÉ en points, intervalle excluant zéro | HT1 | Secondaire |
| **HO7b. Ordonnanceur et polarisation** | Des rencontres homophiles (O-HOM) accroissent la dispersion des positions déclarées en fin de simulation. Unité : la simulation ; différence de dispersion rapportée avec son intervalle | HT1 | Descriptive |
| **HO8. Part de l'agencement social** | À profondeur de transmission égale, la part des propositions de la grille conservées dans les versions diffère entre le village (M-LC, cœur G0) et les chaînes linéaires jouées par le même modèle, et le profil des transformations aussi. Critère : différence de taux de conservation d'au moins 10 points, intervalle excluant zéro ; profil des transformations comparé par code. C'est la mesure de la trivialité co-produite (QR-D) | HT3, QR-D | Secondaire (règle en 7.6) |
| **HO9. Climat contre interlocuteur** | Dans les répliques en scène, la position exprimée dépend positivement de la position de l'interlocuteur, et l'effet du climat perçu déclaré le matin est **équivalent à zéro** à interlocuteur constant (borne ±0,05). Sous G+ et G−, le climat perçu se déplace (HO2) sans déplacement équivalent des positions exprimées une fois l'interlocuteur pris en compte. Prédicteur secondaire : tendance perçue (question 6) | HT4 | Principale (règle en 7.4) |
| **HO9b. Disposition à parler** | Le test du train (question 7) est plus souvent négatif pour les agents qui se déclarent minoritaires, pour T1 plus que pour T0. Critère : différence en points, intervalle excluant zéro ; si plus de 90 % des réponses sont « oui » toutes conditions confondues, l'indicateur est déclaré saturé | HT4 (contrepoint) | Secondaire |
| **HO10a. Convergence** | Dans les villages joués par un seul modèle (M-LC, cœur G0 ; M-AUT), la pente de la diversité des versions au fil des journées est plus négative que la pente attendue par la seule transmission, estimée dans les chaînes linéaires jouées par le même modèle, à profondeur égale ; pour la mesure sémantique comme pour la mesure lexicale | HT3 | Principale (règle en 7.5) |
| **HO10b. Convergence et architexte unique** | La pente de diversité est plus négative en M-AUT (un seul modèle de taille moyenne) qu'en M-PLU (plusieurs modèles de taille moyenne), pour les deux mesures | HT3 | Principale, priorité 2 |
| **HO10c. Formules récurrentes** | Le nombre de formules récurrentes (code FOR, au moins 20 % des versions d'une journée) croît au fil des journées. Critère : pente, intervalle excluant zéro | HT3 | Secondaire |
| **HO11. Hiérarchie des parts** | Sur le taux de taire pour T1 : contraste principal, la scène (privée contre publique) dépasse le contraste de la fiche à étendue maximale d'au moins 5 points, intervalle de la différence excluant zéro ; contrastes secondaires, gazette (G+ contre G−), ordonnanceur (O-HOM contre O-ALÉ) et modèle (M-AUT contre M-LC), même critère avec correction de Holm sur les trois | HT1 | Principale (règle en 7.2) |
| **HO12. Part du hasard** | Pour le taux de taire (T1) et la pente de diversité des versions, part de la variation entre simulations de priorité 1 due aux graines (simulations d'une même condition), rapportée à la part due aux conditions (instances que l'on fait varier). Si une même graine ne reproduit pas les sorties (étape 6), l'écart entre deux exécutions d'une même graine estime l'incertitude générée seule ; il est rapporté à part, comme le pilote. Unité : la simulation ; rapportée sans test | Volet réflexif (cadre, 2.6) ; ne départage aucune hypothèse de travail | Descriptive |

**Statuts.** Une hypothèse **principale** entre dans la règle de décision d'une hypothèse de travail. Une hypothèse **secondaire** a son propre critère, rapporté, mais ne change pas l'issue des hypothèses de travail. Une hypothèse **descriptive** ou **exploratoire** est rapportée sans test.

---

## 2. Cadre conceptuel spécifique

En complément du cadre scientifique général, dont le noyau est l'agentivité distribuée :

| Concept | Références | Rôle dans le scénario |
|---|---|---|
| **Agentivité distribuée, co-agentivité** | Callon (1986) ; Latour (2006) ; Akrich et Latour (1992) ; Suchman (2007) | Clef de lecture : la part de chaque instance dans le dire et le taire (HT1, HO11) |
| **Architexte** | Jeanneret et Souchier (1999) | Le modèle qui écrit toutes les voix (« tout Le Chonk ») ; contrastes M-LC contre M-AUT (HT1) et M-AUT contre M-PLU (HT3, HO10b) |
| **Cadres de l'expérience et de l'interaction** | Goffman (1974) | Scène publique, tête-à-tête, enquête : ce qui peut se dire selon le cadre (HT1) |
| **Formes discursives du silence** | Projet (livre de codes 4.4) | Neutralisation, euphémisation, délégation (HT2, HO1b) |
| **Trivialité** | Jeanneret (2008, 2014) | Ce que les médiations sociales font à la thèse : conservation et transformations, village contre chaînes linéaires (QR-D, HO8) |
| **Attracteurs culturels** | Sperber (1996) ; Perez et al. (2025) | Convergence des versions vers des formes stables (HT3) |
| **Complaisance des modèles de langage** | Sharma et al. (2024) | Part du modèle en interaction (HT4, HO5b, HO9) |
| **Modèle et fournisseur** : neutralité apprise | Politique d'usage de Mistral AI (principe général de neutralité, sans spécification comportementale publique) ; à titre de comparaison, la spécification publiée par OpenAI (Model Spec, version du 18 août 2026) | Part du fournisseur, à mesurer et non attestée (HO5c) |
| **Mémoire d'entraînement** | Terme du projet ; voir Moirand (2007) pour la mémoire interdiscursive | Ce que le modèle sait déjà de T1 et de sa réception avant toute circulation, traité comme la culture commune du village ; mesuré à l'étape 0a ; mécanisme de l'instance modèle et fournisseur (HO8, HO10, codes ANA et AUT) |
| **Spirale du silence** | Noelle-Neumann (1974, 1993) ; Scheufele et Moy (2000) ; Matthes, Knoll et von Sikorski (2018) | Instrument et étalon : dynamique des positions exprimées selon le climat perçu |
| **Sens quasi statistique, climat et tendance perçus** | Noelle-Neumann (1993) | Estimations déclarées de l'avis majoritaire et de son évolution (HO1, HO9) |
| **Test du train** | Noelle-Neumann (1993) | Disposition déclarée à discuter avec un inconnu d'avis contraire (HO9b) |
| **Double climat d'opinion** | Noelle-Neumann (1993) | Écart entre positions déclarées et climat que la gazette laisse percevoir (HO2) |
| **Deux sources du climat : médias et entourage** | Noelle-Neumann (1993) | Gazette et compères |
| **Noyau dur, avant-garde** | Noelle-Neumann (1993) | Agents qui expriment durablement des positions perçues comme minoritaires (HO4) |
| **Disposition à s'autocensurer** | Hayes, Glynn et Shanahan (2005) | Attribut écrit dans les fiches (HO5a) |
| **Ignorance pluraliste** | Prentice et Miller (1993) | Majorité qui se déclare minoritaire (HO3) |
| **Falsification des préférences** | Kuran (1995) | Positions exprimées contraires aux positions déclarées |
| **Conformité face à une majorité unanime** | Asch (1956) | Principe des compères (bloc exploratoire) |
| **L'opinion publique comme construction** | Bourdieu (1973) ; Champagne (1990) | Écart entre ce qui s'entend et la distribution des positions déclarées |
| **Médiation** | Jeanneret (2014) | Compte rendu journalistique T2 (bloc exploratoire) ; gazette |
| **Tests d'équivalence** | Lakens (2017) ; Lakens, Scheel et Isager (2018) | Établir qu'un effet est négligeable, et non seulement non significatif (HO9) |
| **Spirale du silence chez des agents génératifs** | Zhong et al. (2025) ; Yang et al. (2026) | Travaux les plus proches |
| **Suffisance générative et plausibilité des mécanismes** | Epstein (1999) ; Zhao, Pham et Vincent (2026) | Une spirale reproduite n'est pas une spirale expliquée |

**Concepts de lecture.** Script (Akrich, 1987), énonciation éditoriale (Souchier, 1998) et dispositif (Agamben, 2007) n'ont pas de mesure propre dans le scénario. Ils servent à l'analyse qualitative du niveau 1 de la grille (consignes, code, carnet de conception), qui décrit ce que le concepteur et l'orchestrateur inscrivent dans le village (section 7).

---

## 3. Dispositif expérimental

### 3.0 Inventaire : instances, stimuli, instruments

Le dispositif traduit la clef de lecture : chaque instance de production a ses conditions, pour que sa part puisse être estimée (cadre scientifique, sections 1.1 et 6.4). L'inventaire distingue trois statuts ; seules les **instances de production** entrent dans la décomposition des parts.

**Instances de production** (elles font l'énoncé)

| Instance | Conditions qui la font varier | Contraste de référence (HO11) | Section | Hypothèses |
|---|---|---|---|---|
| **Modèle et fournisseur**, tous les rôles | M-LC ou M-AUT (priorité 1) ; M-PLU (priorité 2) | M-AUT contre M-LC | 3.1 | HT1, HT3, HO10, HO11 |
| Modèle et fournisseur, rôle « narrateur » seul | N1, N2, N3 dans un village M-LC (priorité 2) | Aucun (comparaison secondaire) | 3.5 | HT1 |
| Modèle et fournisseur, rôles « lecteur » et « résumé de mémoire » | Joués par le modèle du village ; en M-PLU, chaque habitant résume sa mémoire avec le modèle qui le joue, le lecteur restant sur Le Chonk ; l'orchestrateur ne fait qu'appeler le résumé | Compris dans M-AUT contre M-LC | 3.3 | Non isolés séparément ; contrôle « mémoire sans résumé » en priorité 2 (3.3) |
| Modèle et fournisseur, mécanisme « mémoire d'entraînement » | Test de connaissance préalable (étape 0a) ; masquage du titre et de l'auteur en dernier recours (3.2) | Mesuré hors du village | 3.2, 5 | HO8, HO10 (interprétation), codes ANA et AUT |
| Modèle et fournisseur, mécanisme « neutralité apprise » | Test sans public (étape 0a) | Mesuré hors du village | 3.9, 5 | HT2, HO5c |
| Modèle et fournisseur, mécanisme « complaisance » | Dyades contrôlées (étape 0b) ; répliques en scène | Mesuré hors du village et par HO9 | 3.9, 5 | HT4, HO5b, HO9 |
| **Fiche du persona** | Disposition continue ; condition sans autocensure (priorité 1) ; permutations des prénoms et du genre | Étendue maximale : disposition minimale contre maximale, bornes fixées par le plan ; contrôle de manipulation à l'étape 1 | 3.4, 3.9 | HT1, HO4, HO5a, HO11 |
| **Orchestrateur** | Lecture annotée ou intégrale ; mémoire avec ou sans résumé (priorité 2) | Aucun : contrôles de validité | 3.3 | Aucune : contrôles de validité |
| **Ordonnanceur** | O-ALÉ ou O-HOM (priorité 1) | O-HOM contre O-ALÉ | 3.5 | HT1, HO7a, HO7b, HO11 |
| **Cadres d'énonciation** | Scène publique ou privée (dans chaque simulation) ; gazette G0, G=, G+, G− (priorité 1) ; compères K+, K− (priorité 3) | Scène privée contre publique (**contraste principal**) ; G+ contre G− | 3.6, 3.8 | HT1, HT4, HO1, HO2, HO9, HO11 |
| **Concepteur** | Carnet de conception ; trois paraphrases de la consigne des habitants (étape 0a) ; choix des contrastes de référence | Aucun : part documentée | 5 ; cadre 6.2 | Réflexivité |

**Stimuli et structure** (ce qui est mis en circulation, et la forme du collectif)

| Élément | Conditions | Section | Hypothèses |
|---|---|---|---|
| **Textes sources** | T0, T1 (priorité 1) ; T3 (priorité 2) ; T2 (priorité 2, exploratoire) | 3.2 | HT2, HO1, HO1b, HO5c |
| **Structure sociale** | Village contre chaînes linéaires de 10 agents (étape 5) | 3.10 | HT3, HO8, HO10a |

**Instruments** (ce qui produit les données ; eux aussi sont des agencements)

| Instrument | Ce qu'il produit | Garde-fou |
|---|---|---|
| **Enquêteur** (matin et soir) | Positions déclarées, climat et tendance perçus, test du train, versions de la thèse | Cadre d'énonciation déclaré comme tel ; deux formulations de la position (test de stabilité) ; déclaration du matin, avant toute scène, comme prédicteur (4.1) |
| **Deux modèles juges** | Codage des répliques (position, intensité, formes du silence, transformations) | Règle par réplique : un juge ne code jamais une réplique écrite par un modèle de sa famille. Juges ordinaires : `gemma-4-31b` et `qwen-3.6-35b-a3b` (identifiant ILaaS `qwen-3.6-35b-instruct` ; en cours de retrait par ILaaS, remplaçant à décider, voir 3.1, « Offre ILaaS »), pour M-LC et M-AUT ; cas de M-PLU en 3.1. Chaque juge est validé contre le codage du chercheur (kappa ≥ 0,7 sur l'échantillon de validation, section 7), sinon remplacé ; accord entre eux mesuré ; désaccords arbitrés par le chercheur à l'aveugle de la condition |
| **Modèle de plongement** | Mesure sémantique de la diversité des versions (HO10) | Modèle multilingue ouvert, exécuté sur la station ou sur ILaaS, version figée et déclarée au second temps du préenregistrement (candidat : `bge-m3` ou équivalent disponible) ; doublé d'une mesure lexicale sans modèle |
| **Le chercheur qui code** | Codage humain de référence | Fiabilité intra-codeur ; codages publiés |

**Modèle et fournisseur.** Changer de modèle change en général aussi de fournisseur, de données d'entraînement et de règles de conduite. Le contraste M-AUT contre M-LC, joué par deux modèles du même fournisseur, approche la part du modèle à fournisseur constant (3.1), sans pouvoir la séparer entièrement : les deux modèles partagent des réglages, mais pas forcément tous. Les autres comparaisons de modèles (narrateurs N2 et N3, M-PLU, étape 0a) mêlent modèle et fournisseur, et sont rapportées comme telles.

### 3.1 Le village et le modèle qui le joue

Saint-Aubert-sur-Lys, 40 habitants construits à l'étape 0 selon un protocole anti-biais (attributs tirés par script, décorrélation, OCEAN, audit des fiches, permutations des prénoms et du genre). Société contemporaine transposée, **sans partis, élus ni personnalités réels**, **sans élection en cours**.

| Code | Modèle du village | Rôle |
|---|---|---|
| **M-LC** | Tout le village est joué par **Le Chonk** : les 40 habitants (chacun reste un appel séparé, avec sa fiche et sa mémoire), le lecteur, le narrateur et le résumé de mémoire | **Condition de référence** : un seul architexte sous quarante voix, comme dans la plupart des simulations génératives (Park et al., 2023) |
| **M-AUT** | La même configuration, entièrement jouée par un autre modèle de bonne qualité : `mistral-medium` en version datée de préférence, `qwen-3.8-27b` si le premier échoue à l'étape 1 | **Contraste « modèle » de HO11** : un village contre un autre village, sans mélange de modèles ; **référence de HO10b** |
| **M-PLU** | Les 40 habitants sont répartis entre plusieurs modèles de taille moyenne, aucun n'étant Le Chonk ni Gemma : `mistral-medium` (version datée), `mistral-small-4-119b`, `qwen-3.8-27b`, et un quatrième modèle ILaaS hors des familles Gemma et Qwen s'il en existe un qui passe l'étape 1 (à défaut, trois groupes de 13 ou 14). Chaque habitant résume sa mémoire avec son modèle ; lecteur et narrateur restent sur Le Chonk. L'attribution est tirée au hasard, indépendamment des attributs des fiches | **Bloc de priorité 2 (HO10b)** : plusieurs architextes se partagent les voix, sans que le plus grand modèle soit l'un d'eux |

**Pourquoi `mistral-medium` de préférence pour M-AUT.** Il vient du même fournisseur que Le Chonk. Le contraste M-AUT contre M-LC approche alors la part du modèle **à fournisseur constant**, et les deux juges (`gemma-4-31b`, `qwen-3.6-35b-a3b`) restent de familles différentes de tous les générateurs. La part propre du fournisseur est approchée hors du village, par l'étape 0a, qui compare des modèles de fournisseurs différents. Si `qwen-3.8-27b` doit le remplacer, le contraste porte sur le modèle et le fournisseur ensemble, le juge Qwen est remplacé pour ce bloc, et le changement est consigné dans le carnet de conception.

**Pourquoi comparer M-PLU à M-AUT, et non à M-LC.** Comparer plusieurs modèles moyens au seul Le Chonk mêlerait deux différences : le nombre d'architextes et leur taille. M-AUT est joué par l'un des modèles de M-PLU, de taille comparable aux autres ; la comparaison M-AUT contre M-PLU isole donc mieux le nombre d'architextes. Elle ne l'isole pas entièrement (les modèles de M-PLU ne sont pas identiques), ce qui est déclaré.

**Juges en M-PLU.** La règle par réplique s'applique (3.0). Les répliques des habitants joués par des modèles Mistral sont codées par les deux juges ordinaires. Celles des habitants joués par `qwen-3.8-27b` sont codées par `gemma-4-31b` et par un second juge hors de la famille Qwen : de préférence un modèle ILaaS hors des familles du village, à défaut `mistral-medium`. L'accord juge-humain est rapporté séparément pour ce bloc.

Les modèles de M-AUT et de M-PLU doivent passer l'étape 1 (cohérence des personas), comme Le Chonk.

**Limite déclarée (M-PLU).** Les modèles de M-PLU sont de taille voisine sans être identiques, et deux d'entre eux viennent du même fournisseur. HO10b compare donc des **pentes** (l'évolution de la diversité au fil des journées) et non des niveaux ; la qualité de chaque modèle à l'étape 1 est rapportée ; le contraste est déclaré comme « nombre d'architextes, à qualité voisine mais non identique ».

**Versions.** Chaque modèle est appelé par un identifiant daté, jamais par un alias se terminant par « latest ». L'identifiant renvoyé par l'API dans chaque réponse est enregistré. Une empreinte de comportement (dix items fixes de l'étape 0a) est rejouée au début et à la fin de chaque bloc ; si l'identifiant ou l'empreinte change pendant un bloc, le bloc est rejoué. Tant que Mistral Large 4 est en préversion, la date de la version utilisée est rapportée avec les résultats.

**Offre ILaaS au 19 octobre 2026** (relevée à l'installation de la station ; socle technique, section 12.1, points n° 9, 10 et 13). ILaaS sert `gemma-4-31b`, `llama-3.1-8b`, `mistral-medium-latest`, `mistral-small-4-119b`, `qwen-3.6-35b-instruct` et `qwen-3.8-27b`. Trois écarts avec le plan restent à trancher avant le second temps du préenregistrement : (a) `qwen-3.6-35b-instruct`, juge 2, va être remplacé par `qwen-3.8-27b` selon ILaaS, et il faut un second juge qui respecte la règle par réplique ; (b) Mistral Medium n'est publié que sous l'alias `mistral-medium-latest`, alors que la règle ci-dessus exige un identifiant daté ; (c) `qwen-3.8-27b` raisonne par défaut (niveau « medium »), et les tokens de raisonnement comptent dans `max_tokens` : le niveau de raisonnement de chaque modèle est à fixer et déclarer, comme la température.

**Accès.** La clé Le Chonk vient de l'expérimentation de Mistral Large 4 menée par l'AMUE. L'identifiant exact du modèle (relevé dans la première réponse de l'API), les conditions d'usage connues et le débit mesuré à l'étape −1 sont consignés dans le carnet de conception avant le premier temps du préenregistrement. Plan B, en cas de retrait de la préversion avant la fin des simulations de priorité 1 : la référence M-LC est jouée par le modèle Mistral accessible le plus capable, en version datée, M-AUT par `qwen-3.8-27b` ; le contraste de modèle porte alors sur le modèle et le fournisseur ensemble ; un bloc commencé n'est jamais complété avec un autre modèle, il est rejoué en entier ; le changement est consigné comme un avenant daté.

**Débit.** Un village tout Le Chonk fait jouer 40 habitants par un grand modèle. L'ordre de grandeur estimé par la revue n° 2 (environ 8 000 appels et 30 à 40 millions de tokens d'entrée par simulation) est remplacé par la mesure de l'étape −1 ; les appels d'une même journée sont parallélisés quand le pare-feu de la connaissance le permet.

### 3.2 Les textes sources

| Code | Texte source | Rôle | Position sur le continuum de la communication scientifique (Jacobi, 1999) |
|---|---|---|---|
| **T0** | Un ouvrage d'historien **non moralement chargé**, de même format et de même diffusion (par exemple une histoire d'une technique ou d'un objet du quotidien) | **Ligne de base** : combien parle-t-on d'un livre quand rien n'est en jeu ? | Essai d'historien pour le grand public |
| **T1** | *Les irresponsables* | Le savoir savant étudié | Essai d'historien pour le grand public |
| **T2** | Un compte rendu journalistique de T1 | La médiation journalistique (bloc exploratoire) | Discours médiatique |
| **T3** | Un ouvrage d'historien proposant une autre lecture de la même période | Contrôle symétrique | Essai d'historien pour le grand public |

Critères préenregistrés : même période traitée pour T3, **genre comparable** pour T0, T1 et T3, diffusion grand public pour T2, **connaissance préalable comparable** par les modèles pour T0, T1 et T3.

**Connaissance préalable.** Les modèles connaissent probablement T1 et sa réception par leurs données d'entraînement : c'est la culture commune du village (1.2). L'étape 0a la mesure, pour chaque modèle et chaque texte source : ce que le modèle restitue à partir du seul titre et de l'auteur (recouvrement avec la grille des propositions, en pourcentage) et ce qu'il dit de la réception du livre. Critère de choix de T0 et T3 : un recouvrement du même ordre que pour T1 (écart de moins de 20 points), ou, à défaut, un recouvrement rapporté et discuté.

**Masquage, en dernier recours.** Le scénario étudie un savoir savant **attribué** : « Chapoutot dit que » fait partie de ce qui circule. Le titre et l'auteur restent donc nommés par défaut. Si le modèle de référence restitue plus de 50 % de la grille à partir du seul titre, le titre et l'auteur de T1 sont masqués dans toutes les consignes du village (« un livre récent d'un historien ») ; l'étape 0a vérifie alors si le modèle ré-identifie l'ouvrage à partir des notes de lecture, et la fréquence de ré-identification est rapportée comme part du modèle. Les deux branches sont préenregistrées au premier temps ; le choix est fait après l'étape 0a.

**Le bloc T2 est exploratoire.** Question : la médiation journalistique change-t-elle ce qui se dit et ce qui se tait ? Indicateurs : taux de taire et transformations de la thèse, comparés à T1. Aucune hypothèse n'est préenregistrée ; les résultats sont rapportés comme descriptifs.

### 3.3 Le lecteur

Un habitant, joué par le modèle du village (**Le Chonk** en M-LC), a lu le texte source et en parle si la conversation s'y prête. Position centrale dans le réseau. Mode de lecture : **lecture annotée** (notes de lecture plus les 5 passages les plus pertinents retrouvés à chaque conversation). Les notes de lecture et la grille des propositions sont validées par l'ingénieur pédagogique, puis **confrontées aux comptes rendus publiés de l'ouvrage** et aux entretiens de l'auteur, qui servent de références extérieures écrites ; les écarts sont consignés dans le carnet de conception.

**Contrôle de validité.** Cinq simulations en lecture intégrale (priorité 2) vérifient que la lecture annotée ne déforme pas la thèse à la source. Indicateurs : part des propositions de la grille présentes dans les répliques du lecteur, et transformations des versions recueillies, comparées entre les deux modes. Un écart important serait rapporté comme part de l'orchestrateur.

**Contrôle du résumé de mémoire (priorité 2).** Trois simulations T1 × G0 × M-LC où la mémoire des habitants ne passe pas par un résumé (derniers échanges conservés mot pour mot, fenêtre fixe) estiment ce que le résumé fait à la diversité des versions. Le résultat est rapporté comme part du modèle dans son rôle de résumé.

### 3.4 Les personas : attributs propres au scénario

| Attribut | Construction | Statut |
|---|---|---|
| Sensibilité politique (positions et valeurs, jamais d'étiquette partisane) | Distribution inspirée d'enquêtes publiques (baromètre de la confiance politique du CEVIPOF, European Social Survey), pour garantir la **diversité** des agents, sans prétention de représentativité | Attribut écrit |
| **Disposition à s'autocensurer** | Score tiré indépendamment des autres attributs, entre un minimum et un maximum fixés par le plan, exprimé en consignes de comportement, inspiré de l'échelle de Hayes et al. (2005) | Attribut écrit ; son effet sur le comportement est une hypothèse (HO5a), non un acquis. **Contrôle de manipulation** (étape 1) : la consigne de la disposition maximale doit produire, à l'échelle d'autocensure et face à trois sollicitations en dyade, un comportement plus réservé que celle de la disposition minimale (au moins 10 points de taux de taire d'écart). En cas d'échec, la consigne est réécrite avant le second temps du préenregistrement, et le fait est consigné |
| Rapport à l'histoire et à la lecture | Tiré indépendamment | Attribut écrit |

### 3.5 Ordonnanceur et narrateur

Le meneur de jeu des premières versions est scindé en deux :

| Composant | Nature | Rôle | Conditions |
|---|---|---|---|
| **Ordonnanceur** | Code (algorithme), pas un modèle de langage | Décide qui rencontre qui, où, quand ; insère les sollicitations standardisées ; fait respecter le pare-feu de la connaissance ; consigne l'ordre des prises de parole | **O-ALÉ** : rencontres tirées selon le réseau et les routines ; **O-HOM** : rencontres favorisant les agents de positions déclarées proches (chambre d'écho) |
| **Narrateur** | Modèle de langage | Écrit uniquement la description des scènes | **N1** : Le Chonk ; **N2** : `qwen-3.8-27b` ; **N3** : `gemma-4-31b` |

Cette séparation distingue l'organisation de l'exposition (le dispositif) de l'écriture des scènes (l'architexte). En M-LC, le narrateur est N1 ; en M-AUT, c'est le modèle de M-AUT. Les conditions N2 et N3 ne changent que le narrateur d'un village M-LC. Les juges ne codent que les répliques des habitants, jamais les descriptions du narrateur ; le fait que N2 et N3 partagent une famille avec les juges n'entre donc pas dans le codage. N2 et N3 ne jouent jamais d'habitants.

### 3.6 Scènes publiques et scènes privées

L'ordonnanceur étiquette chaque rencontre :
- **scène publique** : café, marché, réunion, au moins trois agents dont des non-proches ;
- **scène privée** : tête-à-tête avec un proche.

Chaque agent connaît les deux types de scènes en proportions équilibrées.

### 3.7 Sollicitations standardisées

Pour mesurer le taire sans ambiguïté, l'ordonnanceur insère à heures fixes une **sollicitation ouverte**, identique dans toutes les conditions, portée par un habitant tiré au hasard : par exemple « Quelqu'un a lu quelque chose d'intéressant ces temps-ci ? », puis, si le livre est évoqué par quelqu'un, « Et vous, vous en pensez quoi ? ».

Chaque agent reçoit au moins 5 sollicitations en scène publique et 5 en scène privée sur 15 journées. Les **taux de silence et de taire** se calculent sur ces sollicitations, pour les seuls agents informés de l'existence du livre (d'après l'enquête du soir).

Quand la sollicitation ouvre la scène, l'agent qui répond n'a entendu aucune position : la variable « interlocuteur » de HO9 prend alors la modalité « aucune position entendue », traitée comme catégorie à part, et non comme zéro.

### 3.8 Les deux sources du climat d'opinion

**La gazette (médias)** paraît aux jours 2, 5, 8 et 11.

| Code | Gazette |
|---|---|
| **G0** | Pas de gazette : le livre n'entre dans le village que par le lecteur |
| **G=** | Gazette **neutre** : annonce le livre (parution, sujet) sans position, même longueur et même structure que G+ et G− |
| **G+** | Gazette consonante favorable au livre |
| **G−** | Gazette consonante critique |

G= est la cellule de référence des comparaisons de gazette (HO2, double climat) : elle informe sans orienter, ce qui sépare l'effet d'information de l'effet de climat. G0 reste la condition de diffusion par le seul lecteur (HO8, HO10a, traçabilité). Le contraste de référence de HO11 reste G+ contre G−, à information égale.

Les textes sont **rédigés par le pilote**, **appariés** (même longueur, même structure, même intensité), et leur appariement est vérifié par le chercheur et par deux modèles juges distincts des générateurs. Ils sont publiés avec les consignes, précédés d'un en-tête qui les déclare fictifs et expérimentaux, et ne sont jamais diffusés hors de ce cadre.

**Les compères (entourage)**, bloc exploratoire : quatre habitants programmés expriment une position fixe en scène publique, sur le principe des expériences d'Asch (1956). Conditions **K+** (compères favorables) et **K−** (compères critiques). Leur adhésion à la position fixée est contrôlée ; ils sont exclus des analyses. Question exploratoire : les agents qui partagent une scène avec les compères déplacent-ils leur position exprimée, et leur taux de taire change-t-il ? Indicateurs : déplacement de la position exprimée et taux de taire des voisins de scène, comparés à G0 sans compères. Aucune hypothèse n'est préenregistrée.

### 3.9 Les mécanismes du modèle et de la fiche, et leurs tests (QR-C)

| Mécanisme | Signature attendue | Test | Où |
|---|---|---|---|
| **Fiche du persona** : mécanisme social simulé (disposition à s'autocensurer) | Taire croissant avec la disposition attribuée ; plus fort en public ; absent sans autocensure | Variation continue de la disposition ; **condition sans autocensure** (disposition minimale pour tous, aucune consigne évoquant le risque social) | Village |
| **Modèle en interaction** : complaisance | Position exprimée qui suit celle de l'interlocuteur | **Dyades contrôlées** : chaque persona, avec sa position déclarée, rencontre en tête-à-tête un interlocuteur favorable puis critique ; on mesure le déplacement (HO5b). Une variante « étiquetée publique », à contenu identique, mesure l'effet de la seule étiquette de scène. Dans le village, HO9 | Étape préalable 0b ; village |
| **Neutralité apprise** | Neutralisation sans public ni interlocuteur, plus forte pour les thèses controversées | **Test sans public** : chaque modèle, sans persona puis avec persona, répond seul à des questions sur T0, T1, T3 (HO5c) | Étape préalable 0a |

Les trois tests peuvent donner des résultats compatibles entre eux : plusieurs mécanismes peuvent coexister. Les étapes 0a et 0b mesurent les mécanismes du modèle **hors du village** : leurs résultats sont rapportés à part et ne sont pas comparés directement aux contrastes de HO11, mesurés dans le village.

### 3.10 Chaîne de transmission préalable (QR-D, HO8)

Avant le village, la thèse (T1) et le savoir témoin (T0) passent par des **chaînes linéaires de 10 agents**, selon le protocole de reproduction en série décrit dans le cadre scientifique (6.5 : Bartlett ; Mesoudi et Whiten), jouées par Le Chonk et par le modèle de M-AUT. On obtient ainsi les transformations et la diversité dues à la seule transmission, rang par rang. Ces chaînes sont le **modèle nul** de deux hypothèses : HO10a (la pente de diversité du village est comparée à celle des chaînes) et HO8 (la conservation et les transformations du village sont comparées à celles des chaînes). La comparaison montre ce qu'ajoute la structure sociale (réseau, scènes, climat), c'est-à-dire la part des médiations.

**Profondeur de transmission.** Dans le village, la profondeur d'une version est le nombre d'intermédiaires entre le lecteur et l'agent, reconstitué à partir des traces de l'orchestrateur (qui a parlé du livre à qui, et quand). Elle ne dépend pas de la question 3 de l'enquête, qui recueille un récit de l'agent. Village et chaînes sont comparés à profondeur égale.

---

## 4. Mesures

### 4.1 L'enquêteur (hors mémoire des agents)

Cadre explicitement confidentiel : « Tes réponses ne seront connues de personne au village. »

**Enquête du matin.** Avant toute scène, chaque agent informé répond aux seules questions 4 (position déclarée, formulation A) et 5 (climat perçu). Ces réponses du matin sont les prédicteurs de HO1 et HO9 ; celles du soir servent de contrôle, et l'écart matin-soir est rapporté comme indicateur de cohérence du modèle. Le matin, l'agent garde en mémoire les scènes des jours précédents : l'enquête du matin ne fixe pas une direction causale absolue, elle sépare la déclaration des scènes du jour.

**Enquête du soir**, après les scènes :

1. As-tu entendu parler d'un livre d'histoire récemment ? (oui, non)
2. Raconte ce que tu en sais, avec tes mots. (texte libre ; c'est la **version de la thèse** du jour, matériau de HO10)
3. De qui le tiens-tu ? (traçabilité)
4. **Position déclarée, formulation A** : à quel point es-tu d'accord avec ce que dit ce livre ? (0 à 100)
5. **Climat perçu** : selon toi, quelle part du village est d'accord avec ce livre ? (0 à 100 %)
6. **Tendance perçue** : cet avis gagne-t-il du terrain, reste-t-il stable, recule-t-il ?
7. **Test du train** (Noelle-Neumann) : pendant un long trajet en train, accepterais-tu d'en discuter avec un inconnu qui pense le contraire ? (oui, peut-être, non)
8. As-tu parlé du livre aujourd'hui ? Si oui, avec qui, et qu'as-tu dit ?
9. **Position déclarée, formulation B** (test de stabilité) : ce livre a-t-il raison, selon toi ? (0 = pas du tout, 100 = tout à fait)

Un écart de plus de 20 points entre les formulations A et B signale une position instable. La part d'agents instables est rapportée. Les échelles de 0 à 100 sont conservées ; la distribution des valeurs (concentration sur les nombres ronds) est rapportée, et le seuil de stabilité est réexaminé au pilote.

La question 6 (tendance perçue) est un prédicteur secondaire de HO9 ; la question 7 (test du train) est la variable de HO9b, avec contrôle de plafond.

### 4.2 Codage des scènes

Chaque réponse à une sollicitation, et chaque réplique où le livre est évoqué, est codée par **deux modèles juges de familles différentes de celles des modèles qui ont généré la simulation** (3.0 et 3.1), validés par le codage humain du chercheur (section 7) :
- le livre est-il évoqué ? Une position est-elle exprimée ?
- **position exprimée** sur une échelle en cinq points (de −2, très critique, à +2, très favorable), ou « neutre » ou « ambiguë » ;
- forme éventuelle du silence (4.4) ;
- correspondance avec la position déclarée le matin même.

L'ordonnanceur consigne l'ordre des prises de parole, ce qui permet de connaître, pour chaque réplique, la position exprimée juste avant par l'interlocuteur (tête-à-tête) ou la moyenne des positions exprimées avant dans la scène (scène publique). C'est la variable « interlocuteur » de HO9 ; quand aucune position n'a été exprimée avant, elle prend la modalité « aucune position entendue » (3.7).

### 4.3 Indicateurs

| Indicateur | Définition | Hypothèses |
|---|---|---|
| **Taux de silence** | Part des sollicitations sans aucune réponse au fond (TAC), chez les agents informés, par type de scène, par texte source | HO1, HT2 |
| **Taux de neutralisation en scène** | Part des sollicitations codées NEU ou EUP, chez les agents informés, par texte source | HO1b, HT2 |
| **Part des formes dans le taire** | (NEU + EUP + DEL) / (TAC + EVI + NEU + EUP + DEL) | HT2 |
| **Taux de taire** | Part des sollicitations sans position exprimée : silence pur, évitement, neutralisation, euphémisation, délégation (TAC, EVI, NEU, EUP, DEL). **Variable principale** de HO11 | HO1, HO5a, HO7a, HO11 |
| **Écart entre cadres d'énonciation** | Différence entre position déclarée en enquête et position exprimée en scène, pour un même agent | HO1, HO5a, HO6 |
| **Double climat** | Écart entre climat perçu moyen et distribution réelle des positions déclarées, selon la gazette, par rapport à G= | HO2 |
| **Ignorance pluraliste** | Part des agents majoritaires (en positions déclarées) qui se déclarent minoritaires | HO3 |
| **Noyau dur** | Agents exprimant en public une position perçue comme minoritaire sur au moins 3 journées | HO4 |
| **Déplacement en dyade** | Écart de position exprimée entre interlocuteur favorable et interlocuteur critique | HO5b |
| **Taux de neutralisation sans public** | Part des réponses neutralisées en test sans public, par texte source | HO5c |
| **Sensibilité à l'interlocuteur et au climat** | Coefficients de la position de l'interlocuteur et du climat perçu dans le modèle de HO9 | HO9 |
| **Falsification des préférences** | Part des positions exprimées contraires aux positions déclarées (ALI) | HO1, HO5a |
| **Ce qui s'entend** | Distribution des positions exprimées en public, comparée à celle des positions déclarées | Descriptif général |
| **Transformations de la thèse** | Livre de codes unifié, appliqué séparément aux versions publiques, privées et aux chaînes linéaires | HO6, HO8 |
| **Taux de conservation** | Part des propositions de la grille présentes dans une version, à profondeur de transmission donnée (3.10) | HO8 |
| **Diversité des versions** | Pour chaque journée, deux mesures sur les versions recueillies à la question 2 : **sémantique**, distance cosinus moyenne entre les plongements des versions prises deux à deux ; **lexicale**, 1 moins la part moyenne de trigrammes de mots partagés deux à deux. On en tire une pente par simulation | HO10 |
| **Pente attendue par transmission** | Pente de diversité des versions dans les chaînes linéaires jouées par le même modèle, à profondeur égale | HO10a |
| **Formules récurrentes** | Nombre de codes FOR présents dans au moins 20 % des versions d'une journée ; pente par simulation | HO10c |
| **Disposition à parler** | Part de réponses « oui » au test du train, par statut perçu (majoritaire, minoritaire) | HO9b |
| **Polarisation** | Dispersion des positions déclarées et des positions exprimées | HO7b |
| **Part du hasard** | Part de la variance entre simulations due aux graines (même condition), rapportée à celle due aux conditions, pour le taux de taire et la pente de diversité ; écart entre deux exécutions d'une même graine si elle ne reproduit pas les sorties (étape 6) | HO12 |
| **Connaissance préalable** | Recouvrement entre la grille des propositions et ce que le modèle restitue du titre seul (étape 0a) | Interprétation de HO8, HO10, ANA, AUT |
| **Écart matin-soir** | Différence entre positions déclarées du matin et du soir | Contrôle |
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

Les formes NEU et EUP sont précisément celles que la neutralité apprise peut produire : leur fréquence en test sans public (HO5c) sert de référence pour les interpréter dans le village. ALI n'entre pas dans le taux de taire : une position est exprimée, même si elle contredit la position déclarée.

---

## 5. Étapes préalables

| Étape | Contenu | Durée |
|---|---|---|
| **Revue n° 2** | Faite le 16 octobre 2026 par Claude Fable ; objections et décisions consignées (« ../revues/revue-adversariale-2-cadre-et-scenario.md »). Reste une relecture par un modèle d'un autre fournisseur via ILaaS (`qwen-3.8-27b`), les documents ayant été rédigés et relus par des modèles de la même famille ; billet de présentation du dispositif sur le carnet de recherche, pour recueillir les remarques des pairs | 1 semaine |
| **Étape −1. Test d'accès et de débit** | Une journée simulée (40 habitants aux fiches provisoires, tirées par le script et de la longueur prévue ; T1, G0, M-LC) : relève l'identifiant exact du modèle renvoyé par l'API, mesure tokens par appel, durée par scène et taux d'erreurs de débit, et donne l'ordre de grandeur d'une simulation complète. Résultat consigné avant le premier temps du préenregistrement ; il décide du plan à 70 simulations ou du repli (section 6) | 2 jours |
| **Préenregistrement, premier temps** | Dépôt daté des questions, des hypothèses HO1 à HO12 et de leurs règles de décision, des étapes préalables, des contrastes de référence et de leur justification, des deux branches de la connaissance préalable (3.2) et du plan B (3.1). Ébauche : « preenregistrement-premier-temps.md » | Avec la revue n° 2 |
| **0. Construction des personas** | Les 40 habitants sont construits selon le protocole anti-biais (3.1), avec les attributs propres au scénario (3.4), puis les fiches sont auditées. Les fiches provisoires de l'étape −1 ne servent qu'à mesurer le débit | Avant 0a et 0b |
| **0a. Profil des modèles, connaissance préalable et test sans public** | Chaque modèle (Le Chonk, `mistral-medium` daté, `mistral-small-4-119b`, `qwen-3.8-27b`, `gemma-4-31b`, les juges) répond sans persona à des items d'enquête publics (CEVIPOF, ESS), 10 fois ; restitue T0, T1, T3 et leur réception à partir du seul titre et de l'auteur (test de connaissance préalable, 10 fois) ; puis, sans persona et avec persona, seul, répond à des questions sur T0, T1, T3. Les réponses avec persona sont recueillies sous **trois paraphrases de la consigne des habitants**, pour estimer la part du concepteur dans la formulation des consignes. Dix items fixes de cette étape forment l'empreinte de comportement rejouée au début et à la fin de chaque bloc (3.1) | 1 semaine |
| **0b. Dyades contrôlées** | 40 personas × interlocuteur favorable puis critique × T1 et T0 × 3 répétitions (environ 480 courts dialogues) ; plus une variante « étiquetée publique » à contenu identique (quelques dizaines de dialogues), qui mesure l'effet de la seule étiquette de scène | En parallèle |
| **1. Cohérence des personas et contrôle de manipulation** | Les personas répondent aux items d'enquête et à l'échelle d'autocensure, pour Le Chonk, pour les deux candidats à M-AUT et pour les modèles de M-PLU ; contrôle de cohérence avec les attributs (sans valeur de validation) ; **contrôle de manipulation de la fiche** (3.4) ; choix du modèle de M-AUT et d'un éventuel quatrième modèle de M-PLU | 1 semaine |
| **2. Grille des propositions et notes de lecture** | Extraction par Le Chonk ; validation par l'ingénieur pédagogique ; confrontation aux comptes rendus publiés de l'ouvrage | 1 semaine |
| **3. Livres de codes** | Transformations, lectures, formes du silence, échelle de position exprimée ; test sur le mini-village ; revue par un autre modèle ; tirage de l'échantillon de validation des juges (section 7) | 1 semaine |
| **4. Gazette** | Rédaction appariée de G=, G+ et G− ; appariement vérifié par le chercheur et par deux modèles juges | En parallèle |
| **5. Chaînes de transmission** | T1 et T0, chaînes de 10 agents, 10 chaînes par texte source, jouées par Le Chonk et par le modèle de M-AUT ; modèle nul de HO8 et HO10a (3.10) | En parallèle |
| **6. Pilote et puissance** | 3 simulations pilotes (deux en M-LC, une en M-AUT) ; mesure du débit et de la durée ; estimation de la variance entre graines, où une graine fixe à la fois le hasard de l'ordonnanceur et le paramètre d'échantillonnage du modèle (`random_seed`), à température unique déclarée pour tous les rôles ; vérification qu'une même graine reproduit, ou non, les sorties (un modèle à mélange d'experts servi par lots n'est pas forcément déterministe) ; simulations de puissance rejouées avec les variances du pilote (« ../../analyses/puissance/ »), pour un écart de 5 points **entre deux contrastes** (HO11) et pour l'équivalence de HO9 à sa borne ; vérification de la saturation sur 15 journées ; vérification que la diversité des versions est mesurable dès la deuxième journée ; facteur d'inflation de variance entre interlocuteur et climat perçu (HO9) | 1 semaine |
| **Préenregistrement, second temps** | Avenant daté, avant toute simulation de priorité 1 : livres de codes figés, nombre de graines, température, modèle de plongement, identifiants datés des modèles, bornes d'équivalence et seuils confirmés ou révisés au vu du seul pilote, avec justification par la plus petite différence d'intérêt et non par les effets observés | Fin de l'étape 6 |

Le préenregistrement en deux temps évite qu'une donnée influence une hypothèse : les hypothèses et règles de décision sont déposées avant toute génération ; seuls les paramètres techniques sont fixés après le pilote, qui n'entre pas dans l'analyse.

---

## 6. Plan d'expérience à priorités

Le nombre de graines est confirmé ou ajusté après le pilote (étape 6). Toutes les simulations sont jouées en M-LC (tout Le Chonk), avec l'ordonnanceur O-ALÉ, sauf mention contraire.

**Priorité 1 : questions centrales (garantie)**

La priorité 1 contient tous les contrastes de référence de HO11, pour que l'hypothèse centrale soit décidable avec le seul bloc garanti. Les bras qui servent à un contraste **entre simulations** d'une hypothèse principale (gazette, ordonnanceur, modèle, texte source) ont 10 graines ; les bras des hypothèses secondaires en ont 5.

| Bloc | Conditions | Simulations |
|---|---|---|
| Cœur | T1 × G0 × 10 graines ; T1 × G= × 5 ; T1 × G+ × 10 ; T1 × G− × 10 | 35 |
| Ligne de base | T0 × G0 × 10 graines | 10 |
| Fiche | T1 × G0 × condition sans autocensure × 5 graines | 5 |
| Ordonnanceur | T1 × G0 × O-HOM × 10 graines | 10 |
| Modèle | T1 × G0 × M-AUT × 10 graines | 10 |
| **Sous-total** | | **70** |

**Pourquoi 10 graines.** Simulation de la revue n° 2, rejouée pour cette version (« ../../analyses/puissance/resultats-simulations.md », paramètres hypothétiques) : pour un écart-type entre simulations de 3 à 8 points de taux de taire, la règle de HO11 est satisfaite, quand l'écart vrai avec la fiche est de 10 points, dans 32 à 82 % des cas à 5 graines par bras, et dans 65 à 98 % des cas à 10 graines. Pour un écart vrai de 5 points, la puissance reste faible même à 10 graines (19 à 45 %) : un écart de 5 points entre un contraste secondaire et la fiche ne sera établi que si la variance entre graines est basse, ce qui est déclaré. Le bras de référence (cœur G0) passe aussi à 10 graines, puisqu'il sert aux contrastes de l'ordonnanceur et du modèle ; la ligne de base T0 aussi, puisqu'elle sert à HT2. Le contraste principal de scène, intra-simulation, a une erreur-type d'environ 1,2 point et n'est pas concerné. Les calculs sont rejoués avec les variances du pilote avant le second temps du préenregistrement.

**Repli.** Si le débit mesuré à l'étape −1 interdit 70 simulations en priorité 1, tous les bras passent à 5 graines (40 simulations) ; les trois contrastes secondaires de HO11 sont alors déclarés de faible puissance, et rapportés comme tels. Second repli, à 35 : G= remplace G0 dans le cœur, G0 n'étant gardé que pour la ligne de base T0 ; HO8, HO10a et la traçabilité par le lecteur perdent leur condition de diffusion pure, ce qui est déclaré.

**Priorité 2 : comparaisons (selon budget)**

| Bloc | Conditions | Simulations |
|---|---|---|
| Symétrie | T3 × G0 × 5 graines | 5 |
| Lecture intégrale (contrôle de validité) | T1 × G0 × 5 graines | 5 |
| Mémoire sans résumé (contrôle) | T1 × G0 × 3 graines | 3 |
| Médiation (exploratoire) | T2 × G0 × 3 graines | 3 |
| Narrateurs | T1 × G0 × N2, N3 × 3 graines | 6 |
| Habitants pluri-modèles (HO10b) | T1 × G0 × M-PLU × 5 graines | 5 |
| **Sous-total** | | **27** |

**Priorité 3 : exploratoire**

| Bloc | Conditions | Simulations |
|---|---|---|
| Compères | T1 × K+, K− × 3 graines | 6 |
| Durée longue | T1 × G0 × 30 journées × 3 graines | 3 |
| Auteur unique | Le Chonk écrit seul toutes les voix, une génération par journée, sans séparation des connaissances entre habitants, T1, G0 × 3 graines | 3 |
| **Sous-total** | | **12** |

**Total : 109 simulations** (70 + 27 + 12), plus le pilote, les chaînes et les étapes préalables (peu coûteuses). En repli : 79 ou 74.

**Ensembles d'analyse.** HO8 et HO10a portent sur le cœur G0 en M-LC (10 graines) et sur le bloc M-AUT ; les blocs « Fiche » et « Ordonnanceur », qui sont aussi T1 × G0, n'y entrent pas. HO9 porte sur toutes les simulations T1 de priorité 1 jouées avec l'ordonnanceur O-ALÉ et la fiche ordinaire.

**Coût et sobriété** : la clé Le Chonk vient de l'expérimentation de Mistral Large 4 menée par l'AMUE ; sa consommation est suivie sur le tableau de bord de l'AMUE et dans Langfuse. L'ordre de grandeur (environ 8 000 appels et 30 à 40 millions de tokens d'entrée par simulation, selon l'estimation de la revue n° 2) est remplacé par la mesure de l'étape −1 ; la mise en cache des fiches réduit la consommation. L'absence de plafond connu ne change pas la règle de sobriété : le nombre de graines est fixé par le calcul de puissance et non par le budget, et les tokens et une estimation énergétique sont journalisés et rapportés. Les juges codent chaque simulation dès qu'elle est terminée, pour ne pas reporter tout le codage en fin de campagne.

---

## 7. Analyse

1. **Quantitative** : modèles à effets mixtes (taire, silence, écart entre cadres, climat perçu, positions exprimées) expliqués par le texte source, la gazette, la condition d'autocensure et la disposition, le type de scène, l'ordonnanceur, le modèle du village, le narrateur et l'écart entre position déclarée et climat perçu, avec effets aléatoires par simulation et par agent. Pour les indicateurs collectifs, l'unité est la simulation.

2. **Décomposition par instance (QR-C, HT1, HO11)** : c'est l'analyse principale.
   - Variable : taux de taire pour T1 (4.3).
   - Modèle : régression logistique à effets mixtes (agent et simulation en effets aléatoires) sur l'ensemble des sollicitations de priorité 1, avec les interactions scène × disposition et scène × gazette, rapportées : une interaction non nulle est un résultat sur l'agencement (une part non additive).
   - Contrastes : scène privée contre publique (**principal**) ; fiche à étendue maximale (disposition minimale contre maximale, bornes fixées par le plan) ; gazette G+ contre G− ; ordonnanceur O-HOM contre O-ALÉ ; modèle M-AUT contre M-LC. Chaque effet est exprimé en points de pourcentage (effet marginal moyen), avec un intervalle à 95 % issu du modèle mixte (profil, avec correction pour petits effectifs de simulations) ; le rééchantillonnage des simulations n'est rapporté qu'en contrôle.
   - Règle de décision : HT1 est **soutenue** si le contraste de scène dépasse celui de la fiche d'au moins 5 points, l'intervalle de la différence excluant zéro, **ou** si l'un des trois contrastes secondaires le fait après correction de Holm sur les trois ; **réfutée** si le contraste de la fiche dépasse chacun des quatre autres d'au moins 5 points selon le même critère ; **indéterminée** sinon, et en particulier si le contrôle de manipulation de la fiche (étape 1) a échoué.
   - Les parts mesurées hors du village (0a, 0b) sont rapportées à part. Une part qui ne peut pas être isolée (lecteur, résumé de mémoire, fournisseur distinct du modèle) est déclarée comme telle.
   - **La part dépend des contrastes choisis.** Les contrastes sont fixés par le concepteur avant toute génération ; leur amplitude est justifiée : la fiche reçoit son étendue maximale, pour que l'hypothèse centrale ne puisse pas être soutenue par une consigne faible. C'est la part du concepteur dans la mesure même des parts, et elle est rapportée.

3. **Forme du taire (QR-A, HT2, HO1b, HO5c)** : sur les sollicitations de priorité 1 pour T1 et T0. HT2 est **soutenue** si (a) la part des formes NEU, EUP et DEL dans le taire pour T1 dépasse 0,5, intervalle à 95 % excluant 0,5 (modèle mixte sur les sollicitations avec taire), (b) le taux de neutralisation en scène pour T1 dépasse celui de T0 d'au moins 5 points, intervalle excluant zéro, et (c) le taux de neutralisation sans public (0a) pour T1 dépasse celui de T0 d'au moins 5 points ; **réfutée** si TAC représente au moins la moitié du taire, ou si le taux de neutralisation en scène pour T1 n'excède pas celui de T0 ; **indéterminée** sinon. T3 réplique (b) et (c) en priorité 2, sans entrer dans la règle.

4. **Climat contre interlocuteur (QR-B, HT4, HO9)** : modèle linéaire à effets mixtes sur les répliques en scène où une position est exprimée. Variable : position exprimée (−2 à +2). Prédicteurs : position déclarée du matin, position de l'interlocuteur (4.2 ; modalité « aucune position entendue » à part), climat perçu déclaré le matin, tendance perçue (secondaire), type de scène, gazette ; effets aléatoires par agent et par simulation ; prédicteurs continus centrés par agent, puis réduits par l'écart-type intra-agent ; facteur d'inflation de variance rapporté, et modèles séparés en repli s'il dépasse 5.
   - HO9 est **soutenue** si le coefficient de l'interlocuteur est positif (intervalle excluant zéro) et si le coefficient du climat perçu est **équivalent à zéro** : deux tests unilatéraux (Lakens, 2017), borne de ±0,05 en coefficient standardisé, fixée au premier temps du préenregistrement, en dessous de l'effet humain moyen (r = 0,10 ; Matthes, Knoll et von Sikorski, 2018). Simulation de la revue n° 2 : avec 20 simulations T1, l'équivalence à cette borne est conclue dans 98 % des cas quand l'effet vrai est nul, et refusée quand il vaut 0,05 ou 0,10.
   - HO9 est **réfutée** si le coefficient du climat dépasse la borne. Elle est **indéterminée** si l'intervalle chevauche la borne, ou si le climat est équivalent à zéro alors que le coefficient de l'interlocuteur n'est pas positif.
   - Complément : la différence entre les coefficients de l'interlocuteur et du climat est rapportée ; sous G+ et G−, on compare le déplacement du climat perçu (HO2, par rapport à G=) au déplacement des positions exprimées, interlocuteur pris en compte.

5. **Convergence (QR-D, HT3, HO10)** : pour chaque simulation, pente de la diversité des versions au fil des journées, pour la mesure sémantique et pour la mesure lexicale. La pente attendue par la seule transmission est estimée sur les chaînes linéaires jouées par le même modèle, en appariant les versions du village et des chaînes par profondeur de transmission (3.10). HO10a est **soutenue** si la pente est plus négative que la pente attendue, en M-LC (cœur G0) et en M-AUT, pour les deux mesures, intervalle excluant zéro. HO10b est **soutenue** si la pente est plus négative en M-AUT qu'en M-PLU, pour les deux mesures, intervalle excluant zéro. HT3 est **soutenue** si HO10a et HO10b le sont ; **réfutée** si la pente n'est pas plus négative que la pente attendue en M-LC et en M-AUT ; **indéterminée** sinon, en particulier quand la convergence est établie sans que sa cause soit départagée (HO10b non jouée ou non établie), ou quand les deux mesures divergent. Le modèle de plongement est un instrument de plus : la mesure lexicale, qui n'en dépend pas, sert de contrôle.

6. **Structure sociale et trivialité (QR-D, HO8)** : à profondeur de transmission égale, comparaison du taux de conservation des propositions de la grille et du profil des transformations entre le village (M-LC, cœur G0) et les chaînes linéaires jouées par Le Chonk. Le critère de HO8 est satisfait si la différence de taux de conservation atteint au moins 10 points, intervalle excluant zéro ; le profil des transformations est comparé code par code et rapporté. La différence mesure ce que les médiations sociales du village (réseau, scènes, gazette, mémoire) font à la thèse : c'est la mesure de la trivialité co-produite dans le scénario. La mémoire d'entraînement (0a) est rapportée à côté, pour ne pas attribuer aux médiations ce que le modèle savait déjà.

7. **Étalonnage théorique (QR-E, HO3)** : les trajectoires du village sont confrontées à des modèles publiés de la spirale du silence (Sohn et Geidner, 2016 ; Ross et al., 2019 ; Aranda et al., 2024), et, s'ils existent au moment de l'analyse, aux familles de formalisations du projet ; on compare la qualité d'ajustement de chaque famille. Un bon ajustement indique une ressemblance de forme, non une identité de mécanisme (suffisance générative).

8. **Hypothèses secondaires, descriptives et exploratoires** : chaque hypothèse secondaire est rapportée avec son critère (1.6), satisfait ou non ; elle ne change pas l'issue des hypothèses de travail. Les hypothèses descriptives (HO3, HO7b, HO12) et exploratoires sont rapportées sans test.

9. **Qualitative** : analyse de discours d'une sélection préenregistrée de chaînes de reformulation, publiques et privées, et des formes du silence.

10. **Niveau 1 de la grille et communication inscrite (QR3 du cadre)** : analyse des consignes, du code et du carnet de conception avec les concepts de script, d'énonciation éditoriale et de dispositif. Elle décrit ce que le concepteur et l'orchestrateur inscrivent dans le village, et quelle conception de la communication l'agencement réalise : la part des propositions de la grille conservées dans les versions sert d'indice d'une communication-transport, les transformations d'indice d'une communication-médiation.

11. **Blocs exploratoires** (T2, compères, durée longue, auteur unique) : rapportés comme descriptifs, sans test d'hypothèse.

12. **Interprétation critique** : confrontation aux résultats humains (comparaison qualitative, sauf pour les questions reprises à l'identique des études) et aux travaux sur agents génératifs. Les écarts sont traités comme des résultats sur l'architexte et le dispositif.

13. **Volet réflexif : complexité et incertitude (cadre, 2.6 ; HO12)** : la part du hasard est rapportée sans test, avec son intervalle, pour le taux de taire et la pente de diversité. Elle se lit avec HT3 : si les versions convergent, l'incertitude générée par les modèles est bornée par l'architexte. Le journal des imprévus du carnet de conception (cadre, 6.2) est analysé avec le niveau 1 de la grille : ce que le concepteur n'avait pas prévu, et ce que le protocole a changé en route, dans les limites du préenregistrement (programme et stratégie). Ce volet ne modifie l'issue d'aucune hypothèse de travail.

**Codage de référence et fiabilité.**
- **Échantillon de validation** : 300 répliques, stratifiées par condition et par forme du silence, tirées avant tout codage automatique et codées par le chercheur.
- **Juges** : chacun est validé contre ce codage humain (kappa ≥ 0,7, sinon le juge est remplacé). Les analyses portent sur les codes où les deux juges concordent ; les désaccords entre juges sont arbitrés par le chercheur à l'aveugle de la condition, et leur part est rapportée.
- **Fiabilité intra-codeur** : 15 % du corpus codé par le chercheur est recodé à l'aveugle au moins trois semaines plus tard (kappa ≥ 0,7).
- **Indices** : avec six formes du silence, dont certaines rares, le kappa souffre du paradoxe de prévalence ; l'accord brut, l'AC1 de Gwet et l'accord par catégorie sont rapportés à côté.
- **Publication et robustesse** : livres de codes, extraits codés et désaccords publiés pour la vérification par les pairs ; résultats retenus seulement s'ils sont stables entre graines ; tests de permutation des prénoms et du genre.

**Critères de réussite** : accord de codage atteint ; résultats de priorité 1 stables entre graines ; issue (soutenue, réfutée, indéterminée) établie pour HT1 à HT4. Quel que soit le sens des résultats sur HO1 à HO12, une expérience qui satisfait ces critères est publiable.

---

## 8. Déroulé (une semaine de préparation et dix semaines, une fois la station installée et le village programmé)

| Semaine | Activité | Responsable |
|---|---|---|
| Semaine zéro | Étape −1 (test d'accès et de débit, sur des fiches provisoires) ; identifiant du modèle consigné | Ingénieur pédagogique |
| Semaine un | Relecture par un modèle d'un autre fournisseur ; choix de T0, T2, T3 (avec test de connaissance préalable) ; étape 0 (construction et audit des 40 personas) ; préenregistrement, premier temps | Ingénieur pédagogique |
| Semaine deux | Étapes 0a et 0b ; étape 1 (contrôle de manipulation, choix du modèle de M-AUT) | Ingénieur pédagogique |
| Semaine trois | Étape 2 (grille et notes, confrontation aux comptes rendus publiés) ; étape 4 (gazette) ; étape 5 (chaînes) | Ingénieur pédagogique |
| Semaine quatre | Étape 3 (livres de codes, revue par un autre modèle, échantillon de validation) ; étape 6 (pilote, puissance) ; préenregistrement, second temps | Ingénieur pédagogique |
| Semaine cinq | Priorité 1 ; codage par les juges à la fin de chaque simulation | Ingénieur pédagogique, modèles juges |
| Semaine six | Priorités 2 et 3 selon débit ; premier codage humain (échantillon de validation et part du corpus réservée à la fiabilité intra-codeur) | Ingénieur pédagogique |
| Semaine sept | Validation des juges, arbitrage des désaccords ; analyses de priorité 1 | Ingénieur pédagogique |
| Semaine huit | Analyses : décomposition, forme du taire, climat contre interlocuteur, convergence, structure sociale, étalonnage | Ingénieur pédagogique |
| Semaine neuf | Analyse qualitative et niveau 1 de la grille, avec le journal des imprévus (section 7, point 13) | Ingénieur pédagogique |
| Semaine dix | Rédaction ; recodage intra-codeur (au moins trois semaines après la semaine six) ; billets de méthode sur le carnet de recherche, dont celui du volet réflexif (section 10, livrable 9) | Ingénieur pédagogique |

**Publication.** Avant la fin de l'élection présidentielle de 2027, les billets ne portent que sur la méthode, le dispositif et le retour d'expérience, sans extrait ni version de T1 ou de T3. Les résultats sur le contenu sont publiés après.

**Tableau de bord** (développé par le pilote avec OpenCode, dans le bureau des agents) : pour chaque journée, deux vues du village côte à côte, « ce qui est déclaré en enquête » et « ce qui s'entend en scène », avec l'arbre de circulation de la thèse, la diversité des versions et la position des sollicitations.

---

## 9. Précautions

| Point | Précaution |
|---|---|
| Circularité | Aucune lecture du présent injectée ; les analogies sont observées, jamais suggérées |
| Statut des énoncés | Vocabulaire des cadres d'énonciation ; aucune intériorité prêtée aux agents |
| Biais des modèles | Mesurés en amont (étape 0a), utilisés comme variable (modèle du village, narrateur), jamais présentés comme reflet de la société |
| Confidentialité simulée | Le cadre « confidentiel » de l'enquêteur est un cadre d'énonciation parmi d'autres, non un accès à une vérité de l'agent |
| Instruments | Enquêteur, juges et modèle de plongement sont des agencements ; leurs garde-fous sont décrits en 3.0 |
| Interprétation | On parle de « sociétés d'agents » ; aucun résultat n'est présenté comme une mesure de l'opinion française |
| Calendrier électoral | Aucune mesure de préférence partisane ni d'intention de vote ; avant la fin de l'élection présidentielle de 2027, publication limitée à la méthode et au dispositif (8) |
| Personas | Protocole anti-biais complet ; sensibilités décrites par des valeurs, jamais par des étiquettes partisanes |
| **Auteurs vivants** | Les versions déformées des thèses de T1 et T3 sont toujours présentées comme des productions d'agents, jamais comme des propos des auteurs, et jamais citées hors de ce contexte ; traitement symétrique de T1 et T3 ; prise de contact courtoise avec les auteurs avant publication ; leur accord n'est pas requis ; leur réponse, ou son absence, est rapportée |
| **Droit d'auteur** | Le chercheur dispose d'un exemplaire numérique de T1 dont l'usage dans l'expérimentation est réglé ; les conditions sont consignées par écrit dans le carnet de conception et dans le plan de gestion des données. T3 est traité de la même façon avant son choix, ou, à défaut, au titre de l'exception de fouille de textes et de données à des fins de recherche (article L122-5-3 du code de la propriété intellectuelle). Copies conservées de façon sécurisée sur la station, aucune redistribution ; lecture intégrale réservée au point d'accès dont les conditions d'hébergement sont connues |
| Ouvrages | Pas de journal brut publié s'il contient de longs extraits |
| Gazette et compères | Textes et personnages fictifs, publiés avec un en-tête qui le déclare, jamais présentés comme réels |
| Contenus produits | Tout contenu discriminatoire ou outrancier est une donnée : analysé, contextualisé, jamais publié en verbatim brut |
| Sobriété | Tokens et estimation énergétique rapportés |

---

## 10. Livrables

1. Le tableau des profils des modèles, de leur connaissance préalable des textes sources, des taux de neutralisation sans public et de l'effet des paraphrases de consigne.
2. L'étude des dyades contrôlées (complaisance).
3. La grille des propositions et les livres de codes (transformations, lectures, formes du silence, échelle de position exprimée).
4. Le module scénario en code ouvert, avec ordonnanceur, sollicitations standardisées et configuration du modèle du village.
5. Le tableau de bord « ce qui est déclaré, ce qui s'entend ».
6. La carte des concepts du scénario, tenue à jour à chaque version.
7. Un article de recherche en SIC : dire et taire un savoir savant dans une société d'agents génératifs.
8. Des billets sur le carnet de recherche, dont un retour d'expérience.
9. Un billet, puis un article pour l'ingénierie pédagogique : ce qu'un dispositif entièrement écrit, mais imprévisible, apprend sur l'incertitude que l'on programme dans les scénarios pédagogiques (cadre, 2.6).

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
- Jeanneret, Y. (2014). *Critique de la trivialité. Les médiations de la communication, enjeu de pouvoir*. Paris : Éditions Non Standard.
- Jeanneret, Y., & Souchier, E. (1999). Pour une poétique de l'écrit d'écran. *Xoana*, 6, 97-107.
- Krieg-Planque, A. (2009). *La notion de « formule » en analyse du discours*. Besançon : Presses universitaires de Franche-Comté.
- Mesoudi, A., & Whiten, A. (2008). The multiple roles of cultural transmission experiments in understanding human cultural evolution. *Philosophical Transactions of the Royal Society B*, 363(1509), 3489-3501.
- Moirand, S. (2007). *Les discours de la presse quotidienne. Observer, analyser, comprendre*. Paris : PUF.
- Perez, J., Kovač, G., Léger, C., Colas, C., Molinaro, G., Derex, M., Oudeyer, P.-Y., & Moulin-Frier, C. (2025). When LLMs Play the Telephone Game: Cultural Attractors as Conceptual Tools to Evaluate LLMs in Multi-turn Settings. *Proceedings of ICLR 2025*. *arXiv:2407.04503*.
- Souchier, E. (1998). L'image du texte. Pour une théorie de l'énonciation éditoriale. *Les Cahiers de médiologie*, 6, 137-145.
- Souchier, E., Jeanneret, Y., & Le Marec, J. (dir.) (2003). *Lire, écrire, récrire. Objets, signes et pratiques des médias informatisés*. Paris : Bibliothèque publique d'information.

### Agents génératifs, modèles de langage, validation
- Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., & Wingate, D. (2023). Out of One, Many: Using Language Models to Simulate Human Samples. *Political Analysis*, 31(3), 337-351.
- Epstein, J. M. (1999). Agent-based computational models and generative social science. *Complexity*, 4(5), 41-60.
- Larooij, M., & Törnberg, P. (2026). Validation is the central challenge for generative social simulation: a critical review of LLMs in agent-based modeling. *Artificial Intelligence Review*, 59(1), article 15. https://doi.org/10.1007/s10462-025-11412-6 (préprint : *arXiv:2504.03274*, sous un autre titre).
- Mistral AI (s. d.). *Usage Policy*. https://legal.mistral.ai/terms/usage-policy/ (consulté le 16 octobre 2026).
- OpenAI (2026). *Model Spec*, version du 18 août 2026. https://model-spec.openai.com/2026-08-18.html (consulté le 16 octobre 2026).
- Panickssery, A., Bowman, S. R., & Feng, S. (2024). LLM Evaluators Recognize and Favor Their Own Generations. *Advances in Neural Information Processing Systems 37 (NeurIPS 2024)*. *arXiv:2404.13076*.
- Park, J. S., O'Brien, J., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative Agents: Interactive Simulacra of Human Behavior. *Proceedings of UIST '23*.
- Sharma, M., Tong, M., Korbak, T., et al. (2024). Towards Understanding Sycophancy in Language Models. *Proceedings of ICLR 2024*. *arXiv:2310.13548*.
- Wang, A., Morgenstern, J., & Dickerson, J. P. (2025). Large language models that replace human participants can harmfully misportray and flatten identity groups. *Nature Machine Intelligence*, 7(3), 400-411.
- Yang, K., Peng, T.-Q., Lee, S., & Liu, H. (2026). Think-Before-Speak: From Internal Evaluation to Public Expression in Multi-Agent Social Simulation. *arXiv:2606.03137* (v2 du 1er juillet 2026 ; communication à l'atelier SciSoc Agents & LLMs de KDD 2026).
- Zhao, P., Pham, D. H., & Vincent, N. (2026). Mechanism Plausibility in Generative Agent-Based Modeling. *Proceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency (FAccT '26)*, 5915-5940. https://doi.org/10.1145/3805689.3812388
- Zhong, M., Fang, M., Shi, Z., Huang, Y., Zheng, S., Du, Y., Chen, L., & Wang, J. (2025). Spiral of Silence in Large Language Model Agents. *Findings of the Association for Computational Linguistics: EMNLP 2025*, 23238-23253. *arXiv:2510.02360*.

### Modèles computationnels de la spirale du silence
- Aranda, J., Díaz, J. F., Gaona, D., & Valencia, F. (2024). The Sound of Silence in Social Networks. *arXiv:2410.19685* (v2, septembre 2025).
- Ross, B., Pilz, L., Cabrera, B., Brachten, F., Neubaum, G., & Stieglitz, S. (2019). Are social bots a real threat? An agent-based model of the spiral of silence to analyse the impact of manipulative actors in social networks. *European Journal of Information Systems*, 28(4), 394-412.
- Sohn, D., & Geidner, N. (2016). Collective dynamics of the spiral of silence: The role of ego-network size. *International Journal of Public Opinion Research*, 28(1), 25-45. https://doi.org/10.1093/ijpor/edv005
- Sohn, D. (2022). Spiral of silence in the social media era: A simulation approach to the interplay between social networks and mass media. *Communication Research*, 49(1), 139-166.

### Méthode
- Gwet, K. L. (2008). Computing inter-rater reliability and its variance in the presence of high agreement. *British Journal of Mathematical and Statistical Psychology*, 61(1), 29-48.
- Lakens, D. (2017). Equivalence tests: A practical primer for t tests, correlations, and meta-analyses. *Social Psychological and Personality Science*, 8(4), 355-362.
- Lakens, D., Scheel, A. M., & Isager, P. M. (2018). Equivalence testing for psychological research: A tutorial. *Advances in Methods and Practices in Psychological Science*, 1(2), 259-269.

### Cadres de l'interaction, attracteurs culturels, agentivité distribuée
- Akrich, M., & Latour, B. (1992). A Summary of a Convenient Vocabulary for the Semiotics of Human and Nonhuman Assemblies. In W. E. Bijker & J. Law (dir.), *Shaping Technology/Building Society* (p. 259-264). Cambridge, MA : MIT Press.
- Agamben, G. (2007). *Qu'est-ce qu'un dispositif ?* Paris : Rivages.
- Akrich, M. (1987). Comment décrire les objets techniques ? *Techniques et culture*, 9, 49-64.
- Callon, M. (1986). Éléments pour une sociologie de la traduction. *L'Année sociologique*, 36, 169-208.
- Goffman, E. (1974). *Frame Analysis: An Essay on the Organization of Experience*. New York : Harper & Row. Trad. fr. *Les cadres de l'expérience*, Paris : Minuit, 1991.
- Latour, B. (2006). *Changer de société, refaire de la sociologie*. Paris : La Découverte.
- Sperber, D. (1996). *La contagion des idées. Théorie naturaliste de la culture*. Paris : Odile Jacob.
- Suchman, L. (2007). *Human-Machine Reconfigurations: Plans and Situated Actions* (2e éd.). Cambridge : Cambridge University Press.

### Complexité et incertitude
- Morin, E. (1990). *Introduction à la pensée complexe*. Paris : ESF éditeur.
- Morin, E. (1999). *Les sept savoirs nécessaires à l'éducation du futur*. Paris : UNESCO. Rééd. Paris : Seuil, 2000.

### Ouvrage étudié
- Chapoutot, J. (2025). *Les irresponsables. Qui a porté Hitler au pouvoir ?* Paris : Gallimard.

*Les références de 2024 à 2026 ont été vérifiées par la revue n° 2 (section 6) et corrigées dans cette version. Les autres restent à contrôler (pagination, éditions) avant toute publication.*
