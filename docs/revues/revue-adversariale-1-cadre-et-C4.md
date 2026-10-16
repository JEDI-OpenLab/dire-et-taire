# Revue adversariale n° 1 : cadre scientifique SIC et scénario C4

*Revue des documents « cadre-scientifique-SIC-village.md » (version 2) et « scenario-C4-circulation-savoir-savant.md » (version 4). Version du 15 octobre 2026.*

---

## 1. Méthode de la revue

La revue adopte successivement cinq regards de relecteurs exigeants :

1. **un relecteur de SIC** (cohérence théorique, emprunts conceptuels) ;
2. **un méthodologue** (validité des mesures, confusions entre facteurs) ;
3. **un statisticien** (unités d'analyse, puissance) ;
4. **un spécialiste des modèles de langage** (ce que les agents font réellement) ;
5. **un relecteur éthique** (auteurs réels, publication, sobriété).

Chaque objection est classée :
- **bloquante** : elle ferait rejeter le projet en l'état ;
- **majeure** : elle affaiblit sérieusement une conclusion ;
- **mineure** : elle relève de la clarté ou du confort.

**Limite de cette revue** : c'est une auto-revue. Les documents ont été rédigés avec le même assistant. Il faut donc une **revue croisée** : faire relire les documents révisés par un autre modèle (par exemple `qwen-3.8-27b` via ILaaS, ou Le Chonk lui-même) avec la consigne de les réfuter, puis par un ou une collègue de SIC. C'est l'objet de la revue n° 2, et c'est aussi une matière intéressante pour le retour d'expérience.

---

## 2. Objections, décisions, modifications

### 2.1 Objections bloquantes

| N° | Objection | Pourquoi c'est grave | Décision et modification |
|---|---|---|---|
| **R1** | **Le statut des « opinions privées ».** Le C4 traite la réponse à l'enquêteur comme l'« opinion vraie » de l'agent et la réplique en scène comme son « expression publique ». Or un agent n'a pas d'intériorité : ce sont deux textes produits dans deux cadres d'énonciation différents. | Toute l'hypothèse S1 (écart public-privé) et la notion de silence reposent sur une ontologie psychologique que le cadre dit refuser. Contradiction interne. | Nouvelle section du cadre : **statut des énoncés générés**. On parle de **position déclarée en enquête confidentielle** et de **position exprimée en scène**. L'écart entre les deux devient un **écart entre cadres d'énonciation**, objet pleinement SIC. Ajout d'un **test de stabilité** (deux formulations de la même question) pour vérifier que la position déclarée est stable. |
| **R2** | **Le silence n'a pas de ligne de base.** Un agent qui ne parle pas du livre peut simplement parler d'autre chose : routines, sujets du jour. Sans mesurer combien on parle d'un livre quand rien n'est en jeu, impossible de dire qu'il y a « silence ». | Le résultat central du C4 serait ininterprétable. | Ajout d'une source témoin **S0** : un ouvrage savant **non moralement chargé**, de même format. Ajout de **sollicitations standardisées** : à heures fixes, dans des scènes publiques et privées, un habitant pose une question ouverte du type « Quelqu'un a lu quelque chose d'intéressant récemment ? ». Le taux de silence se calcule sur ces sollicitations, et non sur des « occasions » définies après coup. |
| **R3** | **Deux mécanismes concurrents seulement, alors qu'il y en a trois.** Le C4 oppose le mécanisme social simulé (autocensure attribuée) à la complaisance. Il oublie la **neutralité apprise** : les modèles sont réglés pour ne pas prendre parti sur les sujets controversés (« chacun pense ce qu'il veut »). Cette neutralité ressemble exactement à une forme du silence (NEU). | QR-C ne peut pas être tranchée ; la condition « sans autocensure » ne distingue pas complaisance et neutralité apprise. | QR-C reformulée autour de **trois mécanismes** : social simulé, complaisance envers l'interlocuteur, neutralité apprise. Trois tests distincts : condition sans autocensure ; variation de la position de l'interlocuteur en tête-à-tête ; test « sans public » (l'agent seul, sans scène, à l'étape 0) et comparaison S1 / S0. |
| **R4** | **Le meneur de jeu cumule trop de rôles.** Il décide des rencontres, décrit les scènes, et peut orienter les conversations. En M4, la chambre d'écho repose sur une simple consigne qu'il peut suivre plus ou moins. Le facteur « architecte » mélange organisation des rencontres et écriture des scènes. | Confusion entre facteurs : on ne saura pas ce qui produit l'effet. | Le meneur de jeu est **scindé** : un **ordonnanceur algorithmique** (du code, pas un modèle) organise les rencontres, au hasard ou de façon homophile ; un **narrateur** (modèle de langage) écrit seulement les scènes. La chambre d'écho devient une condition de l'ordonnanceur, parfaitement contrôlée. |
| **R5** | **La problématique générale du cadre n'est pas formulée en « Comment X alors que Y ».** Elle reste une double question descriptive. | Incohérence avec la méthode retenue pour le C4, et absence de tension qui guide l'ensemble. | Nouvelle problématique générale : *Comment une simulation sociale générative fait-elle circuler et se transformer des énoncés, alors que toutes les voix qui la peuplent sont écrites par un même architexte ?* La trivialité suppose des médiations hétérogènes ; ici, une seule machine écrit toutes les voix. |

### 2.2 Objections majeures

| N° | Objection | Décision et modification |
|---|---|---|
| **R6** | **Contradiction entre trivialité et fidélité.** Jeanneret conçoit la trivialité contre l'idée d'une dégradation du message ; Jacobi critique la vulgarisation pensée comme déperdition. Or le livre de codes est normatif : « réduction » définie comme perte, « fabrication » comme faute. | Livre de codes réécrit en termes **descriptifs**. Ajout de codes de **transformation créatrice** : contextualisation, exemplification, recadrage. La fidélité devient **une lentille parmi d'autres**, explicitement distinguée de l'analyse de la trivialité. |
| **R7** | **Emprunts conceptuels non discutés.** Hall (codage-décodage) suppose des sujets situés socialement face à un code dominant ; Allport et Postman relèvent d'une psychologie expérimentale de la reproduction en série. Les appliquer à des agents demande une justification. | Les concepts sont hiérarchisés en **noyau théorique** (trivialité, architexte, dispositif, énonciation éditoriale) et **concepts opératoires empruntés**. Pour ces derniers, une colonne « conditions d'emprunt » dit ce qui est adapté et ce qui est perdu. |
| **R8** | **État de l'art incomplet sur la transmission culturelle.** Des travaux majeurs manquent : chaînes de transmission avec des modèles de langage (Acerbi et Stubbersfield, 2023 ; Perez et al., 2025), épidémiologie des représentations et attracteurs culturels (Sperber, 1996). Ce dernier cadre est un concurrent direct de la trivialité, et il faut se situer par rapport à lui. | Ajout de ces travaux. Le cadre discute explicitement **trivialité et attracteurs culturels** : deux façons de penser la transformation en circulation. |
| **R9** | **Les écarts aux références humaines ne sont pas mesurables tels quels.** Allport et Postman, Centola, Lewandowsky, les méta-analyses de la spirale : chacun a son protocole. Comparer nos indicateurs à leurs chiffres n'a pas de sens sans équivalence de procédure. Or les écarts sont l'objet de recherche. | Principe de **réplication procédurale** : pour chaque référence humaine mobilisée, on reproduit son protocole dans le dispositif. Ajout d'une **expérience C0** : chaînes de transmission linéaires, protocole des études humaines (Mesoudi et Whiten, 2008). Pour le C4, la thèse passe d'abord par des chaînes linéaires, sans village, ce qui permet de voir ce que la structure sociale ajoute. |
| **R10** | **Validité des emprunts psychométriques.** Vérifier qu'un agent répond à l'échelle d'autocensure conformément au score qu'on lui a donné ne prouve que l'obéissance à la consigne. | Le questionnaire est rétrogradé en **contrôle de cohérence**. La validation porte sur le **comportement en scène** : le score attribué prédit-il le silence face aux sollicitations standardisées ? |
| **R11** | **Puissance statistique insuffisante.** Pour les indicateurs collectifs (climat, polarisation), l'unité est la simulation : 3 graines par cellule, c'est très faible. | Une **simulation pilote** estime la variance entre graines ; le nombre de graines est fixé par calcul de puissance. Minimum de 5 graines pour les contrastes centraux. **Plan à priorités** : le bloc prioritaire (questions centrales) est garanti, les blocs secondaires sont exécutés selon le budget. |
| **R12** | **Le juge automatique peut favoriser ses propres textes.** Un modèle qui code des textes qu'il a lui-même écrits tend à les juger plus favorablement (Panickssery et al., 2024). | Le modèle juge est toujours **différent** des modèles qui ont généré la simulation codée. Validation contre le codage humain maintenue. |
| **R13** | **Circularité des références de fidélité.** Les notes de lecture du lecteur et la grille des propositions sont toutes deux validées par la même personne, qui a sa propre lecture de l'ouvrage. | Grille et notes validées par **une seconde personne indépendante**, idéalement un ou une historienne. La comparaison lecture intégrale / lecture annotée passe à 5 graines. |
| **R14** | **Le cadrage de la gazette.** Si un modèle écrit G+ et G−, il y imprime ses biais ; deux textes de longueur ou d'intensité différentes rendraient la comparaison invalide. | Textes rédigés par l'équipe, **appariés** (longueur, structure, intensité), vérifiés par deux évaluateurs indépendants. Ils ne sont jamais publiés comme de vraies critiques. |
| **R15** | **Le climat d'opinion n'a qu'une source manipulée.** Pour Noelle-Neumann, le climat se lit dans les médias **et** dans l'entourage. Seul le média (la gazette) est manipulé. | Ajout d'une manipulation de l'entourage : des **compères** (habitants programmés, comme dans les expériences d'Asch) expriment une position fixe en scène publique. Bloc exploratoire. |
| **R16** | **Auteurs vivants.** Le dispositif produit des versions déformées de la thèse d'un historien vivant, et d'un second (S3). Publier ces déformations pourrait lui attribuer des propos qu'il n'a pas tenus. | Précaution ajoutée : aucune déformation publiée sans être explicitement présentée comme production d'agents ; prise de contact courtoise avec les auteurs avant publication ; traitement symétrique de S1 et S3. |
| **R17** | **Reproductibilité mal définie.** Les modèles par API ne sont pas déterministes et changent de version. | Distinction entre **reproductibilité des analyses** (garantie : toutes les générations sont archivées) et **réplicabilité des générations** (limitée, documentée). Ajout d'un **plan de gestion des données**. |

### 2.3 Objections mineures

| N° | Objection | Décision |
|---|---|---|
| **R18** | La règle de triangulation (« un résultat quantitatif n'est retenu que s'il s'interprète dans l'analyse qualitative ») risque d'écarter les résultats contre-intuitifs. | Reformulée : convergences et divergences sont documentées ; une divergence est un résultat. |
| **R19** | Quinze journées peuvent être trop courtes pour qu'une dynamique d'opinion se forme. | Le pilote vérifie la saturation ; un sous-ensemble est rejoué sur 30 journées. |
| **R20** | Le genre des sources n'est pas caractérisé. Un essai d'historien pour le grand public n'est pas un article savant. | Les trois sources sont situées sur le continuum de la communication scientifique (Jacobi, 1999). La symétrie S1 / S3 exige un genre comparable. |
| **R21** | La mémoire des agents est résumée par un modèle : ce résumé est un architexte supplémentaire, non déclaré. | Le mécanisme de mémoire est documenté comme élément du dispositif (niveau 1 de la grille). |
| **R22** | Le coût environnemental n'est pas mesuré. | Journalisation des tokens et estimation énergétique par simulation, rapportées dans les résultats. |
| **R23** | La problématique du C4 dit les agents « conçus pour toujours répondre ». Or ils sont aussi réglés pour rester neutres sur les sujets controversés (voir R3). | La formulation retenue est **conservée**. Le tableau X/Y signale désormais que cette part de Y est discutable, et que la neutralité apprise est précisément l'un des mécanismes testés. **Point soumis à l'arbitrage de l'ingénieur pédagogique.** |

---

## 3. Synthèse des modifications

**Cadre scientifique (version 3)**
- Problématique générale en « Comment X alors que Y ».
- Nouvelle section : statut des énoncés générés (cadres d'énonciation, pas d'intériorité).
- Concepts hiérarchisés, conditions d'emprunt explicitées ; ajout de Sperber, des chaînes de transmission, de la suffisance générative et de la plausibilité des mécanismes.
- Livre de codes descriptif, avec des codes de transformation créatrice.
- Réplication procédurale des références humaines ; expérience C0 (chaînes de transmission).
- Juge différent des générateurs ; puissance ; reproductibilité ; plan de gestion des données ; regards extérieurs ; sobriété.

**Scénario C4 (version 5)**
- Positions « déclarée en enquête » et « exprimée en scène » ; test de stabilité.
- Source témoin S0 ; sollicitations standardisées.
- Trois mécanismes concurrents du silence et leurs tests.
- Ordonnanceur algorithmique et narrateur séparés.
- Compères (exploratoire) ; gazettes appariées et validées.
- Chaîne de transmission préalable ; validation indépendante de la grille et des notes.
- Plan à priorités avec 5 graines pour les contrastes centraux.
- Précautions sur les auteurs vivants.

---

## 4. Points ouverts pour la revue n° 2

1. Faire relire les versions révisées par un autre modèle, avec pour consigne de **réfuter** le dispositif.
2. Faire relire le cadre par un ou une collègue de SIC, en particulier la discussion trivialité / attracteurs culturels.
3. Trancher R23 (formulation de Y).
4. Identifier un ou une historienne pour la validation indépendante de la grille (R13).
5. Choisir S0 et S3.

---

## 5. Addendum : projet mené seul

Le projet est mené et relu par une seule personne ; les pairs interviennent ensuite, par les billets du carnet de recherche puis les articles. Deux décisions de cette revue sont donc révisées, sans effacer leur trace :

- **R13** : la validation par une seconde personne est remplacée par la confrontation des notes de lecture et de la grille aux comptes rendus publiés de l'ouvrage et aux entretiens de l'auteur, avec écarts consignés.
- **Fiabilité du codage** : le double codage par une personne extérieure est remplacé par la fiabilité intra-codeur (recodage à l'aveugle après trois semaines au moins), l'accord avec deux modèles juges distincts et la publication des livres de codes et des extraits codés.
- Points ouverts 2 et 4 : la relecture par un ou une collègue et la recherche d'un ou une historienne sont abandonnées ; un billet de présentation du dispositif, publié avant le préenregistrement, sollicite les remarques des pairs.

---

## 6. Addendum : levée des points bloquants (C4 v9, cadre v6)

La carte des concepts du C4 a fait apparaître quatre points bloquants, levés le 16 octobre 2026 :

- **HT1 n'était pas décidable** : contrastes de référence exprimés en points de pourcentage de taux de taire, et règle de décision à trois issues (HO11).
- **HT4 n'avait pas de test direct** : hypothèse HO9 (effet du climat perçu équivalent à zéro à interlocuteur constant, test d'équivalence) ; l'ignorance pluraliste (HO3) devient un résultat descriptif rattaché à l'étalonnage.
- **HT3 manquait d'une mesure et d'une condition** : diversité des versions (sémantique et lexicale) et bloc « habitants pluri-modèles » (M-PLU) en priorité 1 (HO10). Le même bloc fournit le contraste « modèle » de HO11.
- **L'inventaire des instances variait** : inventaire canonique en trois statuts (instances de production, stimuli et structure, instruments).

**Correspondance des codes.** Dans cette revue, les textes sources S0 à S3 correspondent aujourd'hui à T0 à T3, et les hypothèses opérationnelles S1 à S8 à HO1 à HO8.

