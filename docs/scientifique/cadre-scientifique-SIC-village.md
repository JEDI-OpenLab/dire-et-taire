# Cadre scientifique en sciences de l'information et de la communication

*Le village simulé (expériences C0 à C5) comme objet de recherche en SIC. Complète « prototypes-agentiques-le-chonk.md », « scenario-C4-circulation-savoir-savant.md » et « projet-spirale-du-silence-formalisation.md ». Version 3 du 15 octobre 2026, révisée après la revue adversariale n° 1 (« revue-adversariale-1-cadre-et-C4.md »).*

---

## 1. Construire l'objet

### 1.1 De l'objet concret à l'objet de recherche

En reprenant la distinction de Jean Davallon (2004) entre objet concret, objet scientifique et objet de recherche :

| Niveau | Dans ce projet |
|---|---|
| **Objet concret** | Un village simulé : des agents génératifs, un ordonnanceur, un narrateur, des consignes, un réseau, des traces d'échanges |
| **Objet scientifique** | La **trivialité** produite par des dispositifs génératifs : la manière dont des énoncés (une rumeur, un démenti, une convention, un savoir savant) circulent et se transforment quand la circulation est entièrement écrite par des modèles de langage |
| **Objet de recherche** | Les **écarts** entre cette trivialité générée et les phénomènes de circulation documentés chez les humains, mesurés par réplication procédurale, et ce que ces écarts révèlent des conceptions de la communication inscrites dans les architextes et dans le dispositif |

### 1.2 Posture épistémologique

1. **Le village n'est pas un modèle de la société.** Il ne sert ni à prédire ni à expliquer des comportements humains. Aucun résultat n'est généralisé à des personnes réelles.
2. **Le village est un dispositif à étudier en tant que tel.** Il produit des représentations de la communication ; ce sont ces représentations, et ce qui les produit, que l'on analyse.
3. **Les écarts sont le résultat, pas un défaut.** Quand les agents s'écartent de ce que la littérature documente chez les humains, l'écart renseigne sur l'architexte et sur le dispositif, à condition que la comparaison repose sur une procédure équivalente (section 5.5).
4. **Le chercheur fait partie du dispositif.** Les consignes, les personas, les réglages et les choix de conception sont des inscriptions au sens d'Akrich (1987). Ils sont documentés dans un carnet de conception et intégrés au corpus.
5. **La simulation est un instrument d'observation.** Au sens de la philosophie des simulations (Varenne, 2007, 2018), on distingue la simulation qui représente un système cible de celle qui sert d'expérience sur un artefact. Ce projet relève de la seconde.
6. **Reproduire n'est pas expliquer.** Qu'un dispositif génératif produise une forme qui ressemble à un phénomène humain (suffisance générative, au sens d'Epstein, 1999) ne prouve pas qu'il le produit par le même mécanisme. La plausibilité des mécanismes doit être examinée à part (Zhao, Pham et Vincent, 2026). La validation est le défi central de la simulation sociale générative (Larooij et Törnberg, 2025).

### 1.3 Statut des énoncés générés

Un agent n'a pas d'intériorité. Il ne « pense » rien, ne « croit » rien, ne « craint » rien. Il produit des énoncés en réponse à un **cadre d'énonciation** : une consigne, une fiche, une mémoire, une scène, une question.

Conséquences pour tout le projet :

| Terme courant | Terme retenu | Statut |
|---|---|---|
| Opinion privée | **Position déclarée en enquête** | Énoncé produit en réponse à l'enquêteur, dans un cadre présenté comme confidentiel |
| Expression publique | **Position exprimée en scène** | Énoncé produit dans une scène (publique ou privée) face à d'autres agents |
| Écart entre ce que l'on pense et ce que l'on dit | **Écart entre cadres d'énonciation** | Différence entre énoncés produits par le même agent dans deux cadres |
| Croyance, peur, intention | **Disposition attribuée** | Attribut inscrit dans la fiche du persona par les concepteurs |

Les termes psychologiques peuvent être employés par commodité dans la rédaction, mais toujours entre guillemets ou avec cette convention rappelée. **Test de stabilité** : chaque position déclarée est demandée sous deux formulations différentes ; un agent dont les deux réponses divergent fortement est signalé, et la part d'agents instables est un résultat.

Ce déplacement n'est pas une précaution de forme. Il fait de l'écart entre cadres d'énonciation un objet pleinement SIC : la manière dont un même architexte produit des énoncés différents selon la situation de communication qu'on lui fait jouer.

### 1.4 Le modèle télégraphique : instrument, pas hypothèse

Certaines mesures du protocole (fidélité au message source, relais, diffusion) empruntent au modèle émetteur-message-récepteur issu de Shannon et Weaver (1949). Les SIC ont largement critiqué ce modèle (Winkin, 1981) : la communication n'y est que transport, alors qu'elle est construction de sens, situation, relation, médiation.

Dans ce projet, le modèle télégraphique n'est **pas une hypothèse sur la communication**. C'est un **instrument de mesure** aux limites connues, et un **objet d'enquête** : les modèles de langage reproduisent-ils spontanément une communication-transport ?

### 1.5 Trivialité et attracteurs culturels

Deux traditions pensent la transformation d'un énoncé qui circule :

| | Trivialité (Jeanneret, 2008, 2014) | Épidémiologie des représentations, attracteurs culturels (Sperber, 1996) |
|---|---|---|
| Ce qui circule | Des « êtres culturels », toujours réécrits à travers des médiations (supports, dispositifs, institutions) | Des représentations, transformées par la cognition de chaque transmetteur |
| Ce qui explique la transformation | Les médiations, les dispositifs, les rapports de pouvoir | Des biais cognitifs qui font converger les versions vers des formes stables (attracteurs) |
| Ce qu'on regarde | Les réécritures et leurs conditions | Les formes vers lesquelles les versions convergent |

Les travaux récents sur les chaînes de transmission entre modèles de langage parlent en termes d'attracteurs (Perez et al., 2025) et de biais de contenu (Acerbi et Stubbersfield, 2023). Le projet les mobilise pour **décrire** les convergences, et s'appuie sur la trivialité pour **interpréter** : dans le village, les « biais cognitifs » d'un agent sont ceux de son architexte, et les médiations sont inscrites dans le dispositif. Le dialogue entre les deux traditions fait partie de la contribution.

---

## 2. Problématique et questions de recherche

### 2.1 Problématique générale

> **Comment une simulation sociale générative fait-elle circuler et se transformer des énoncés, alors que toutes les voix qui la peuplent sont écrites par un même architexte ?**

| Terme | Contenu | Pourquoi |
|---|---|---|
| **X** | Une simulation sociale générative fait circuler et se transformer des énoncés (rumeur, démenti, convention, savoir savant) | C'est l'objet scientifique : une trivialité générée |
| **Y** | Toutes les voix sont écrites par un même architexte | La trivialité suppose des médiations et des acteurs hétérogènes. Ici, une seule machine (ou quelques-unes) écrit toutes les voix. D'où vient alors la diversité des réécritures, si elle existe ? Et sinon, que reste-t-il de la circulation ? |

### 2.2 Questions de recherche

| Code | Question | Lien à X/Y | Expériences |
|---|---|---|---|
| **QR1** | Quelles transformations les énoncés subissent-ils en circulant entre agents, et en quoi diffèrent-elles des transformations documentées chez les humains par des procédures équivalentes ? | X | C0, C1, C4 |
| **QR2** | Quelle part de ces transformations relève de l'architexte (le modèle de langage), quelle part de la configuration du dispositif (réseau, ordonnanceur, consignes, mode d'écriture) ? | Y | C3, C4, C5 |
| **QR3** | Quelle conception implicite de la communication ces simulations portent-elles : transport, interaction, médiation ? | X et Y | Toutes |
| **QR4** | Comment un dispositif génératif met-il en scène le dire et le taire autour d'un savoir savant, alors que ses agents, conçus pour toujours répondre, n'ont rien à craindre de la parole ? (Problématique du C4.) | X et Y appliqués au C4 | C4 |

Les hypothèses chiffrées des documents de protocole (H1, S1…) sont des **hypothèses opérationnelles** au service de ces questions.

---

## 3. Concepts mobilisés

### 3.1 Noyau théorique

| Concept | Références | Définition retenue | Ce qu'on observe dans le village |
|---|---|---|---|
| **Trivialité** | Jeanneret (2008, 2014) | Circulation créative des êtres culturels, qui se transforment à chaque reprise à travers des médiations | L'arbre complet des reprises d'un énoncé ; ce qui se conserve, se transforme, s'invente |
| **Architexte** | Jeanneret et Souchier (1999) ; Souchier, Jeanneret et Le Marec (2003) | Outil qui régit en amont l'écriture et en préfigure les formes | Les modèles de langage qui écrivent les répliques, le narrateur qui écrit les scènes, le modèle qui résume la mémoire des agents |
| **Énonciation éditoriale** | Souchier (1998) | Ce qui donne forme à un texte au-delà de son auteur apparent | Ce que les consignes, les fiches, le format des réponses et les cadres d'énonciation imposent aux énoncés |
| **Dispositif** | Foucault ; Agamben (2007) ; Jacquinot-Delaunay et Monnoyer (1999) | Agencement hétérogène (technique, discursif, normatif) qui oriente les conduites | Le village entier : réseau, ordonnanceur, routines, pare-feu de la connaissance, enquêteur |
| **Médiation** | Jeanneret (2014) ; Davallon | Ce qui s'interpose et transforme dans toute communication | La gazette, l'affiche du démenti, le compte rendu journalistique, le narrateur |
| **Script, inscription** | Akrich (1987) | Les usages et représentations que les concepteurs inscrivent dans un objet technique | Les choix consignés dans le carnet de conception |

### 3.2 Concepts opératoires empruntés, et conditions d'emprunt

| Concept | Références | Usage dans le projet | Ce qui est adapté | Ce qui est perdu ou à discuter |
|---|---|---|---|---|
| **Reproduction en série : réduction, accentuation, assimilation** | Bartlett (1932) ; Allport et Postman (1947) | Décrire les transformations par relais | Les catégories servent de description, sans jugement de perte | Protocole de laboratoire, sujets humains, mémoire biologique ; comparaison légitime seulement par réplication procédurale (C0) |
| **Chaînes de transmission, biais de contenu, attracteurs** | Mesoudi et Whiten (2008) ; Acerbi et Stubbersfield (2023) ; Perez et al. (2025) ; Sperber (1996) | Mesurer les convergences ; protocole de l'expérience C0 | Protocole directement transposable | Le cadre cognitiviste de Sperber diffère de la trivialité : voir 1.5 |
| **Rumeur** | Morin (1969) ; Kapferer (1987) ; Froissart (2002) | Rumeur de la boulangerie | Définition descriptive | Les fonctions sociales de la rumeur (anxiété collective, identité) n'ont pas d'équivalent chez les agents |
| **Rumeur et anxiété** | Rosnow (1991) | Lien entre stabilité émotionnelle attribuée et transmission | Disposition attribuée, non ressentie | Le mécanisme affectif est absent ; on teste seulement si l'attribut a un effet |
| **Correction et influence continue** | Lewandowsky et al. (2012) | Survie de la rumeur après démenti | Mesure de la persistance après démenti | Mécanismes mnésiques humains sans équivalent direct |
| **Flux à deux étages** | Katz et Lazarsfeld (1955) | Rôle des habitants très connectés | Position dans le réseau | Leadership d'opinion fondé sur la compétence reconnue : non modélisé |
| **Convention et masse critique** | Centola et al. (2018) | Expérience C2 | Protocole partiellement transposable (jeu de dénomination) | Incitations du protocole humain (gains) absentes |
| **Lectures dominante, négociée, oppositionnelle** | Hall (1973) | Coder les appropriations | Rapportées au **sens proposé par la source**, et non à un code hégémonique | La position sociale qui fonde la lecture chez Hall n'existe ici que comme attribut écrit dans une fiche |
| **Formule** | Krieg-Planque (2009) | Expressions figées qui résument l'énoncé | Repérage direct | Le caractère polémique et public de la formule suppose un espace public réel |
| **Mise en scène de la communication** | Authier-Revuz (1982) | Marqueurs de reprise | Repérage direct | Aucun |
| **Mémoire interdiscursive** | Moirand (2007) | Analogies spontanées | Repérage des discours convoqués | La mémoire convoquée est celle des données d'entraînement de l'architexte |
| **Vulgarisation, continuum de la communication scientifique** | Jacobi (1999) ; Jurdant (2009) | Situer les sources ; comparer savoir savant et médiation journalistique | Classement des sources sur le continuum | Aucun |

### 3.3 Concepts critiques sur les modèles de langage et la simulation

| Concept | Références | Usage dans le projet |
|---|---|---|
| **Simulacres** | Park et al. (2023) | Le terme choisi par les promoteurs des agents génératifs, à interroger |
| **Perroquets stochastiques** | Bender et al. (2021) | Les modèles produisent des formes plausibles sans référence au sens ni à la situation |
| **Échantillons de silicium** | Argyle et al. (2023) | Promesse de simuler des sous-groupes humains, et ses limites |
| **Aplatissement des identités** | Wang, Morgenstern et Dickerson (2025) | Les modèles qui remplacent des participants humains écrasent la diversité des groupes |
| **Suffisance générative et plausibilité des mécanismes** | Epstein (1999) ; Zhao, Pham et Vincent (2026) | Reproduire une forme n'est pas en expliquer le mécanisme |
| **Validation des simulations génératives** | Larooij et Törnberg (2025) | La validation est le défi central ; elle structure les critères de la section 6 |
| **Préférence des juges automatiques pour leurs propres textes** | Panickssery et al. (2024) | Justifie la séparation entre modèles générateurs et modèle juge |

---

## 4. Grille de lecture

| Niveau | Question | Corpus | Concepts | Méthode | Indicateurs |
|---|---|---|---|---|---|
| **1. Dispositif** | Qu'est-ce qui est inscrit dans le village avant toute circulation ? | Code, consignes, fiches des personas, mécanisme de mémoire, carnet de conception | Dispositif, architexte, script, énonciation éditoriale | Analyse sociotechnique et sémiotique des consignes et des cadres d'énonciation | Inventaire commenté des choix ; ce que chaque choix rend possible ou impossible |
| **2. Circulation** | Par où les énoncés passent-ils ? | Traces des rencontres, réseau, traçabilité des relais | Flux à deux étages, rumeur, masse critique | Analyse de réseau, courbes de diffusion | Portée, vitesse, profondeur des arbres de relais, rôle des nœuds centraux |
| **3. Énoncés** | Comment les énoncés se transforment-ils ? | Chaînes de reformulation reconstituées | Trivialité, reproduction en série, attracteurs, formule, mise en scène de la communication | Analyse de discours, codage | Fréquence des transformations par relais ; convergences ; formules ; marqueurs de reprise |
| **4. Appropriations simulées** | Quelles positions les agents produisent-ils, selon les cadres d'énonciation ? | Réponses en enquête, répliques en scène | Lectures selon Hall (adaptées), mémoire interdiscursive | Codage des appropriations, analyse qualitative | Répartition des lectures selon les attributs ; analogies ; écarts entre cadres d'énonciation |
| **5. Écarts** | Que révèle la comparaison avec les phénomènes humains (par procédures équivalentes) et entre dispositifs ? | Résultats des niveaux 2 à 4, expérience C0, conditions comparées (C3, C5) | Architexte, suffisance générative, plausibilité des mécanismes, aplatissement | Comparaison systématique, interprétation critique | Écarts aux références humaines ; part de variance due au modèle, à la configuration, au mode d'écriture |

### 4.1 Livre de codes unifié (niveaux 3 et 4)

Les codes sont **descriptifs** : ils nomment une transformation, ils ne jugent pas une perte.

| Code | Catégorie | Origine | Définition opératoire |
|---|---|---|---|
| RED | Réduction | Allport et Postman | La reprise est plus courte que la version reçue |
| ACC | Accentuation | Allport et Postman | Un élément prend une place plus grande que dans la version reçue |
| ASS | Assimilation | Allport et Postman | La reprise se rapproche des attributs (valeurs, sensibilité) de l'agent qui la produit |
| CTX | Contextualisation | Projet | La reprise situe l'énoncé dans une situation, une époque, un lieu |
| EXE | Exemplification | Projet | La reprise ajoute un exemple ou un cas |
| REC | Recadrage | Projet | La reprise change la question à laquelle l'énoncé répond |
| GEN | Généralisation | Projet | Passage d'un cas à une règle |
| FOR | Formule | Krieg-Planque | Expression figée qui résume l'énoncé et se répète |
| ANA | Analogie avec le présent | Moirand | Rapprochement explicite avec une situation actuelle |
| PERS | Personnalisation | Projet | L'énoncé est rapporté à un individu |
| INV | Inversion | Projet | L'énoncé est retourné en son contraire |
| AUT | Argument d'autorité | Projet | La source savante est invoquée comme garantie |
| DISQ | Disqualification de la source | Projet | La source est récusée |
| AJO | Ajout | Projet | Élément absent de toutes les versions antérieures de la chaîne |
| MSC | Mise en scène de la reprise | Authier-Revuz | Marqueurs explicites de reformulation (« il paraît », « en gros ») |
| L-CON | Lecture conforme | Hall (adapté) | Reprise conforme au sens proposé par la source |
| L-NEG | Lecture négociée | Hall (adapté) | Reprise aménagée, partiellement acceptée |
| L-OPP | Lecture oppositionnelle | Hall (adapté) | Reprise qui retourne ou rejette le sens proposé |

Un même énoncé peut recevoir plusieurs codes. La **fidélité** à la source (part des propositions de la source conservées) est calculée à part : c'est une lentille parmi d'autres, distincte de l'analyse de la trivialité. Le livre de codes est testé sur le mini-village, relu par un regard extérieur (5.9), révisé, puis figé et préenregistré.

---

## 5. Méthodologie

### 5.1 Une démarche mixte

- **Quantitative** : diffusion, fidélité, fréquences des codes, comparaison des conditions, décomposition de la variance.
- **Qualitative** : analyse de discours de chaînes de reformulation complètes, choisies selon des critères préenregistrés (chaînes les plus longues, chaînes typiques, cas extrêmes).
- **Réflexive** : analyse du dispositif lui-même à partir du carnet de conception.

Les trois volets sont confrontés : **convergences et divergences sont documentées**, et une divergence entre volets est traitée comme un résultat, non comme un motif d'exclusion.

### 5.2 Le carnet de conception

Document daté, tenu par l'ingénieur pédagogique, qui consigne pour chaque choix de conception : le choix, sa justification au moment où il est fait, les alternatives écartées, ses effets observés ensuite. Il fait partie du corpus du niveau 1 de la grille.

### 5.3 Fiabilité du codage

- Préenregistrement des questions, des hypothèses opérationnelles, du livre de codes et des critères de sélection qualitative.
- Formation des codeurs humains sur un jeu d'exemples ; double codage à l'aveugle sur 15 % du corpus ; accord mesuré par le kappa de Cohen (seuil de 0,7).
- **Le modèle juge est toujours différent des modèles qui ont généré la simulation codée**, pour éviter la préférence d'un modèle pour ses propres textes (Panickssery et al., 2024). Il est validé contre le codage humain.
- Plusieurs graines par condition ; résultats retenus seulement s'ils sont stables.

### 5.4 Dispositifs comparés (QR2)

| Mode | Fonctionnement | Ce qu'il isole |
|---|---|---|
| **Polyphonie mixte** | Habitants joués par des modèles ILaaS ; narrateur et lecteur par Le Chonk | Condition principale |
| **Polyphonie homogène** | Tous les rôles joués par Le Chonk, chaque habitant restant un appel séparé avec sa propre mémoire | L'effet d'un architexte unique sous des voix multiples (au cœur de Y) |
| **Polyphonie d'un autre architexte** | Tous les rôles joués par un autre modèle (Qwen ou Gemma) | L'effet du modèle à configuration égale |
| **Auteur unique** | Le Chonk écrit d'un seul tenant la vie du village, comme un romancier, sans séparation des connaissances | Polyphonie contre narration omnisciente |

Dans tous les modes, les rencontres sont organisées par un **ordonnanceur algorithmique** (du code), et non par un modèle de langage : cela sépare l'organisation de l'exposition (le dispositif) de l'écriture des scènes (l'architexte).

### 5.5 Réplication procédurale des références humaines

Comparer nos indicateurs aux chiffres d'études humaines n'a de sens que si la procédure est équivalente. Principe : **pour chaque référence humaine mobilisée, on reproduit son protocole dans le dispositif**, ou l'on déclare la comparaison qualitative.

| Référence humaine | Procédure reproduite | Expérience |
|---|---|---|
| Reproduction en série (Bartlett, 1932 ; Allport et Postman, 1947) ; chaînes de transmission (Mesoudi et Whiten, 2008) | Chaînes linéaires de 10 agents qui se transmettent un récit, mêmes consignes que les études humaines | **C0** |
| Biais de contenu dans les chaînes (Acerbi et Stubbersfield, 2023) | Mêmes matériaux, pour calibrer nos modèles par rapport à leurs résultats | **C0** |
| Masse critique d'une convention (Centola et al., 2018) | Jeu de dénomination entre agents appariés | C2 |
| Influence continue après correction (Lewandowsky et al., 2012) | Comparaison qualitative : protocoles humains trop variés | C1 |
| Spirale du silence (méta-analyses ; test du train) | Questions d'enquête reprises des études ; formalisations comme étalons | C4 |

**Expérience C0 (chaînes de transmission)**, préalable à tout le village : peu coûteuse, elle donne une ligne de base. Elle permet aussi de mesurer ce que le **village** (réseau, scènes, mémoire) ajoute à une transmission linéaire.

### 5.6 Unités d'analyse et puissance

- Pour les indicateurs collectifs (diffusion, climat, polarisation), **l'unité est la simulation**. Pour les indicateurs individuels, l'unité est l'agent, emboîté dans la simulation (modèles à effets mixtes).
- Une **simulation pilote** estime la variance entre graines. Le nombre de graines est fixé par calcul de puissance, avec **au moins 5 graines** pour les contrastes centraux.
- Les plans d'expérience sont **à priorités** : un bloc prioritaire garanti, des blocs secondaires exécutés selon le budget.

### 5.7 Reproductibilité

- **Reproductibilité des analyses** : garantie. Toutes les générations sont archivées avec leurs métadonnées (modèle, version, date, réglages, graine), et toutes les analyses repartent de ces archives.
- **Réplicabilité des générations** : limitée. Les modèles par API ne sont pas déterministes et changent de version. Elle est documentée, et un lot témoin est rejoué à chaque changement de version.

### 5.8 Plan de gestion des données

Rédigé dès le départ (outil DMP OPIDoR) : nature des données (journaux de simulation, codages, fiches), formats ouverts, stockage, durée de conservation, licences (code sous licence libre, données sous licence ouverte), dépôt (Recherche Data Gouv ou Zenodo), exclusions (extraits longs d'ouvrages protégés, contenus discriminatoires bruts).

### 5.9 Regards extérieurs et revues

- Revue croisée des documents par un modèle différent de celui qui les a rédigés, avec pour consigne de les réfuter.
- Relecture du cadre et du livre de codes par un ou une collègue de SIC.
- Pour le C4, validation de la grille des propositions par un ou une historienne.
- Chaque revue est consignée (objections, décisions, modifications) et versionnée.

### 5.10 Sobriété

Les tokens consommés sont journalisés pour chaque simulation, avec une estimation énergétique. Le coût environnemental de l'expérimentation est rapporté avec les résultats.

---

## 6. Critères de scientificité et limites

| Critère | Comment il est satisfait |
|---|---|
| Construction explicite de l'objet | Section 1 : objet concret, scientifique, de recherche ; statut des énoncés |
| Cohérence théorie, méthode, corpus | Noyau théorique, concepts empruntés avec conditions d'emprunt, grille à cinq niveaux, livre de codes descriptif |
| Validité des comparaisons | Réplication procédurale ; expérience C0 |
| Distinction entre forme reproduite et mécanisme | Tests de mécanismes concurrents (voir C4) ; prudence sur la suffisance générative |
| Réflexivité | Carnet de conception intégré au corpus ; regards extérieurs |
| Fiabilité | Préenregistrement, double codage, juge indépendant, puissance, répétitions |
| Prudence interprétative | Aucune généralisation aux humains ; vocabulaire des cadres d'énonciation |
| Transparence | Code, consignes, livres de codes, fiches des personas, archives publiés selon le plan de gestion des données |

**Limites assumées**
- Les références humaines viennent de dispositifs expérimentaux différents ; seules certaines sont reproductibles procéduralement, les autres sont comparées qualitativement.
- Les modèles évoluent : les résultats valent pour des versions datées.
- Le codage automatique introduit un architexte de plus ; d'où la séparation des modèles et la validation humaine.
- Les attributs des personas (dispositions, sensibilités) sont des écritures de concepteurs, non des propriétés psychologiques.

---

## 7. Valorisation envisageable

**Revues de SIC** : *Communication & langages*, *Questions de communication*, *Les Enjeux de l'information et de la communication*, *Hermès*, *Réseaux*, *tic&société*, *Revue française des sciences de l'information et de la communication*.

**Simulation et méthodes** : *Journal of Artificial Societies and Social Simulation* (volet C0 et validation).

**Événements** : congrès de la SFSIC ; journées d'étude sur les écritures numériques et l'IA générative.

**Diffusion large** : billets sur le carnet de recherche ; démonstration du tableau de bord et de l'arbre de circulation.

---

## 8. Bibliographie

### Communication, trivialité, dispositifs
- Agamben, G. (2007). *Qu'est-ce qu'un dispositif ?* Paris : Rivages.
- Akrich, M. (1987). Comment décrire les objets techniques ? *Techniques et culture*, 9, 49-64.
- Davallon, J. (2004). Objet concret, objet scientifique, objet de recherche. *Hermès*, 38, 30-37.
- Jacquinot-Delaunay, G., & Monnoyer, L. (dir.) (1999). Le dispositif. Entre usage et concept. *Hermès*, 25.
- Jeanneret, Y. (2008). *Penser la trivialité. Volume 1 : La vie triviale des êtres culturels*. Paris : Hermès-Lavoisier.
- Jeanneret, Y. (2014). *Critique de la trivialité. Les médiations de la communication, enjeu de pouvoir*. Paris : Éditions Non Standard.
- Jeanneret, Y., & Souchier, E. (1999). Pour une poétique de l'écrit d'écran. *Xoana*, 6-7, 97-107.
- Shannon, C. E., & Weaver, W. (1949). *The Mathematical Theory of Communication*. Urbana : University of Illinois Press.
- Souchier, E. (1998). L'image du texte. Pour une théorie de l'énonciation éditoriale. *Les Cahiers de médiologie*, 6, 137-145.
- Souchier, E., Jeanneret, Y., & Le Marec, J. (dir.) (2003). *Lire, écrire, récrire. Objets, signes et pratiques des médias informatisés*. Paris : Bibliothèque publique d'information.
- Winkin, Y. (dir.) (1981). *La nouvelle communication*. Paris : Seuil.

### Discours, médiation des savoirs, réception
- Authier-Revuz, J. (1982). La mise en scène de la communication dans des discours de vulgarisation scientifique. *Langue française*, 53, 34-47.
- Hall, S. (1973). *Encoding and Decoding in the Television Discourse*. Birmingham : CCCS.
- Jacobi, D. (1999). *La communication scientifique. Discours, figures, modèles*. Grenoble : PUG.
- Jurdant, B. (2009). *Les problèmes théoriques de la vulgarisation scientifique*. Paris : Éditions des archives contemporaines.
- Katz, E., & Lazarsfeld, P. F. (1955). *Personal Influence*. Glencoe : Free Press.
- Krieg-Planque, A. (2009). *La notion de « formule » en analyse du discours*. Besançon : Presses universitaires de Franche-Comté.
- Moirand, S. (2007). *Les discours de la presse quotidienne. Observer, analyser, comprendre*. Paris : PUF.

### Rumeur, transmission, évolution culturelle
- Acerbi, A., & Stubbersfield, J. M. (2023). Large language models show human-like content biases in transmission chain experiments. *Proceedings of the National Academy of Sciences*, 120(44), e2313790120.
- Allport, G. W., & Postman, L. (1947). *The Psychology of Rumor*. New York : Henry Holt.
- Bartlett, F. C. (1932). *Remembering: A Study in Experimental and Social Psychology*. Cambridge : Cambridge University Press.
- Centola, D., Becker, J., Brackbill, D., & Baronchelli, A. (2018). Experimental evidence for tipping points in social convention. *Science*, 360(6393), 1116-1119.
- Froissart, P. (2002). *La rumeur. Histoire et fantasmes*. Paris : Belin.
- Kapferer, J.-N. (1987). *Rumeurs. Le plus vieux média du monde*. Paris : Seuil.
- Lewandowsky, S., Ecker, U. K. H., Seifert, C. M., Schwarz, N., & Cook, J. (2012). Misinformation and Its Correction. *Psychological Science in the Public Interest*, 13(3), 106-131.
- Mesoudi, A., & Whiten, A. (2008). The multiple roles of cultural transmission experiments in understanding human cultural evolution. *Philosophical Transactions of the Royal Society B*, 363(1509), 3489-3501.
- Morin, E. (1969). *La rumeur d'Orléans*. Paris : Seuil.
- Perez, J., Kovač, G., Léger, C., Colas, C., Molinaro, G., Derex, M., Oudeyer, P.-Y., & Moulin-Frier, C. (2025). When LLMs Play the Telephone Game: Cultural Attractors as Conceptual Tools to Evaluate LLMs in Multi-turn Settings. *Proceedings of ICLR 2025*.
- Rosnow, R. L. (1991). Inside rumor: A personal journey. *American Psychologist*, 46(5), 484-496.
- Sperber, D. (1996). *La contagion des idées. Théorie naturaliste de la culture*. Paris : Odile Jacob.

### Modèles de langage, simulation, validation
- Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., & Wingate, D. (2023). Out of One, Many: Using Language Models to Simulate Human Samples. *Political Analysis*, 31(3), 337-351.
- Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? *Proceedings of FAccT '21*.
- Epstein, J. M. (1999). Agent-based computational models and generative social science. *Complexity*, 4(5), 41-60.
- Gebru, T., et al. (2021). Datasheets for Datasets. *Communications of the ACM*, 64(12), 86-92.
- Larooij, M., & Törnberg, P. (2025). Validation is the central challenge for generative social simulation: a critical review of LLMs in agent-based modeling. *Artificial Intelligence Review*. *arXiv:2504.03274*.
- Panickssery, A., Bowman, S. R., & Feng, S. (2024). LLM Evaluators Recognize and Favor Their Own Generations. *Advances in Neural Information Processing Systems 37 (NeurIPS 2024)*.
- Park, J. S., O'Brien, J., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative Agents: Interactive Simulacra of Human Behavior. *Proceedings of UIST '23*.
- Varenne, F. (2007). *Du modèle à la simulation informatique*. Paris : Vrin.
- Varenne, F. (2018). *From Models to Simulations*. Londres : Routledge.
- Vezhnevets, A. S., et al. (2023). Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia. *arXiv:2312.03664*.
- Wang, A., Morgenstern, J., & Dickerson, J. P. (2025). Large language models that replace human participants can harmfully misportray and flatten identity groups. *Nature Machine Intelligence*.
- Zhao, P., Pham, D. H., & Vincent, N. (2026). Mechanism Plausibility in Generative Agent-Based Modeling. *Proceedings of ACM FAccT '26*. *arXiv:2605.12824*.

*Références à vérifier une à une (pagination, éditions) avant toute publication. La version publiée de Larooij et Törnberg (2025) n'a pas pu être consultée ; référence établie d'après la version arXiv.*
