# Cadre scientifique en sciences de l'information et de la communication

*Le village simulé comme objet de recherche en SIC. Version 6.4 du 21 octobre 2026 : volet réflexif sur la complexité et l'incertitude au sens d'Edgar Morin, pour l'ingénierie pédagogique (2.6, 4.2, 6.2, 7, 8, 9). Version 6.3 du 16 octobre 2026 : le projet ne compte plus qu'un scénario, « Dire et taire » ; les expériences C0 à C5 prévues au départ sont retirées, les chaînes linéaires (ancienne C0) restent le modèle nul du scénario, et la rumeur de la boulangerie (ancienne C1) devient un prolongement possible (section 7). Version 6.2 : suites de la revue n° 2 ; statut de la décomposition des parts par rapport à la théorie de l'acteur-réseau (1.3, 1.4) ; résumé de mémoire rattaché à l'instance modèle et mémoire d'entraînement (1.1, 4.3) ; fournisseur réel du village (4.3) ; contrastes à étendue justifiée et interactions entre instances (6.4) ; graine, température, intervalles et comparaisons multiples (6.6) ; règle des juges par réplique (6.3). Version 6 : inventaire canonique des instances en trois statuts (production, stimuli, instruments), contrastes de référence, règles de décision à trois issues. Version 6.1 : condition de référence « tout Le Chonk », et contraste de modèle entre deux villages entiers. La version 5 avait réécrit le cadre autour de la co-agentivité.*

*Documents associés : « scenario-dire-et-taire.md » (version 11.3), « projet-spirale-du-silence-formalisation.md », « ../revues/revue-adversariale-1-cadre-et-scenario.md », « ../revues/revue-adversariale-2-cadre-et-scenario.md ». Les termes, leur paternité et leurs références d'origine sont définis dans « ../glossaire.md ».*

---

## 1. La clef de lecture : la co-agentivité

### 1.1 Qui parle quand un agent parle ?

Le village de Saint-Aubert-sur-Lys est peuplé d'« agents ». Le mot est trompeur. Quand un habitant dit quelque chose au café, la phrase n'est pas l'acte d'un individu : elle est **co-produite** par un agencement d'instances, humaines et non humaines.

| Instance | Ce qu'elle fait à l'énoncé | Ce qui la porte |
|---|---|---|
| **Le modèle de langage** | Il écrit la phrase, résume les souvenirs, joue le lecteur et le narrateur, avec ses régularités, ses réglages (complaisance, neutralité apprise) et ce qu'il sait déjà par ses données d'entraînement (mémoire d'entraînement) | Ses données d'entraînement et, derrière lui, son **fournisseur** et les règles de conduite qu'il lui impose |
| **La fiche du persona** | Elle oriente le ton, les valeurs, les dispositions attribuées | Le concepteur, qui l'a écrite |
| **L'orchestrateur** | Il assemble la consigne et choisit les souvenirs qui y figurent, donc ce que l'agent « sait » | Le code ; le résumé des souvenirs est un rôle du modèle, que l'orchestrateur appelle et dont il choisit les sorties à insérer |
| **L'ordonnanceur** | Il décide de la rencontre : qui parle à qui, où, dans quel type de scène | Le code, et les règles fixées par le concepteur |
| **Les cadres d'énonciation** | Ils définissent la situation de parole : scène publique ou privée, enquête, gazette, sollicitations | Le concepteur, qui les écrit, et l'ordonnanceur, qui les distribue |
| **Le concepteur** | Il a fixé tout ce qui précède : consignes, règles, cadres d'énonciation, sollicitations, et les contrastes qui servent à mesurer les parts | Le chercheur lui-même |

L'énoncé est l'acte d'un **agencement**. On appelle **co-agentivité** cette production conjointe des énoncés par le modèle, le dispositif et le concepteur.

**Inventaire canonique.** Tous les documents du projet renvoient à cet inventaire, qui distingue trois statuts. Seules les instances de production entrent dans la décomposition des parts.

| Statut | Éléments | Rôle dans l'analyse |
|---|---|---|
| **Instances de production** (elles font l'énoncé) | Les six instances ci-dessus. Le modèle et son fournisseur tiennent plusieurs rôles (habitants, narrateur, lecteur, résumé de mémoire) et portent plusieurs mécanismes (écriture, complaisance, neutralité apprise) | Leur part est estimée en les faisant varier une à une (section 6.4) |
| **Stimuli et structure** (ce qui circule, et la forme du collectif) | Les textes sources mis en circulation ; la structure sociale (village ou chaînes linéaires) | Conditions expérimentales qui ne sont pas des instances de l'agencement |
| **Instruments** (ce qui produit les données) | L'enquêteur, les modèles juges, les outils de mesure automatique, le chercheur qui code | Ils sont eux aussi des agencements ; chacun a ses garde-fous (section 6.3) |

### 1.2 Agent et agentivité : une distinction à tenir

- Un **agent** (sens informatique) est un programme qui produit des actions ou des énoncés : ici, un habitant du village.
- L'**agentivité** (sens des sciences sociales) est la capacité d'agir, de faire une différence dans le cours des choses.

Que le village soit peuplé d'agents ne dit rien de l'endroit où se loge l'agentivité. **C'est précisément la question de recherche.**

### 1.3 Ancrage théorique

Le projet adopte une conception **distribuée** de l'agentivité, issue de la sociologie des sciences et des techniques et largement reprise en SIC :
- l'action est le fait de réseaux d'**actants** humains et non humains, qui se traduisent les uns les autres (Callon, 1986 ; Latour, 2006) ;
- les objets techniques portent des **scripts** inscrits par leurs concepteurs, qui prescrivent des rôles à leurs utilisateurs (Akrich, 1987 ; Akrich et Latour, 1992) ;
- l'action humaine avec les machines est **située** et se reconfigure dans la relation (Suchman, 2007) ;
- en SIC, l'**architexte** désigne l'outil qui régit en amont l'écriture et en préfigure les formes (Jeanneret et Souchier, 1999 ; Souchier, Jeanneret et Le Marec, 2003), et l'**énonciation éditoriale** tout ce qui donne forme à un texte au-delà de son auteur apparent (Souchier, 1998).

Ces notions convergent : un texte n'a jamais un seul auteur. Le village pousse cette idée à sa limite, puisque **chaque réplique est écrite par une machine, à partir d'une consigne écrite par un humain, dans une situation organisée par du code**.

**Ce que le projet prend à l'acteur-réseau, et ce qu'il ne lui prend pas.** Il lui prend le vocabulaire (actants humains et non humains, symétrie, agentivité sans intentionnalité) et le refus d'attribuer l'énoncé à un auteur unique. Il ne lui prend pas la méthode : l'acteur-réseau suit les associations sans fixer d'avance la liste des actants ni additionner leurs contributions, alors que le village fixe six instances avant toute observation, les fait varier une à une et exprime leurs parts dans une unité commune. Cette décomposition relève des plans d'expériences et de la sociologie expérimentale, et le projet l'assume : l'inventaire des six instances est un **découpage du concepteur**, rapporté comme tel. Deux garde-fous rendent la décomposition compatible avec l'idée d'agencement : les interactions entre contrastes sont estimées et rapportées, une part non additive étant un résultat qui va dans le sens de l'agencement (6.4) ; et une part qui ne peut pas être isolée est déclarée comme telle (7).

### 1.4 Ce que la clef de lecture change

| Sans la clef de lecture | Avec la clef de lecture |
|---|---|
| On demande si les agents « reproduisent » des comportements humains | On demande **quelle instance de l'agencement** produit ce que l'on observe |
| Un écart aux humains est un défaut du simulateur | Un écart aux humains révèle **la part d'une instance** (le modèle, le fournisseur, le dispositif) |
| Le concepteur est extérieur à l'expérience | Le concepteur est **une instance parmi d'autres**, dont la part est documentée |
| Les conditions expérimentales sont des variantes techniques | Chaque condition **fait varier une instance** pour estimer sa part |
| Les parts des instances s'additionnent | Les parts sont mesurées relativement à des contrastes déclarés, et leurs **interactions** sont rapportées |

**Garde-fou** : si tout est agencement, rien n'est expliqué. La co-agentivité n'est utile que si l'on peut **décomposer** les parts. C'est le rôle du plan expérimental (section 6.4).

---

## 2. Construire l'objet

### 2.1 De l'objet concret à l'objet de recherche

En reprenant la distinction de Davallon (2004) :

| Niveau | Dans ce projet |
|---|---|
| **Objet concret** | Un village simulé : modèles, fiches, orchestrateur, ordonnanceur, narrateur, consignes, traces |
| **Objet scientifique** | La **trivialité co-produite** : la manière dont des énoncés, ici un savoir savant, circulent et se transforment quand chaque reprise est écrite par un agencement de modèles, de code et de consignes |
| **Objet de recherche** | La **répartition de l'agentivité** dans cette trivialité : quelle instance produit quelles transformations, quels dires et quels silences, et ce que les écarts aux phénomènes humains documentés révèlent de chacune |

### 2.2 Posture épistémologique

1. **Le village n'est pas un modèle de la société.** Il ne sert ni à prédire ni à expliquer des comportements humains. Aucun résultat n'est généralisé à des personnes réelles.
2. **Le village est un agencement à étudier en tant que tel.** Ce sont ses productions, et la part de chaque instance dans ces productions, que l'on analyse.
3. **Les écarts sont des résultats.** Quand l'agencement s'écarte de ce que la littérature documente chez les humains, l'écart renseigne sur l'instance qui le produit, à condition que la comparaison repose sur une procédure équivalente (section 6.5).
4. **Le chercheur est une instance de l'agencement.** Ses choix sont documentés dans un carnet de conception, intégré au corpus.
5. **La simulation est un instrument d'observation**, au sens où la philosophie des simulations distingue la simulation qui représente un système cible de celle qui sert d'expérience sur un artefact (Varenne, 2007, 2018). Ce projet relève de la seconde.
6. **Reproduire n'est pas expliquer.** Qu'un agencement produise une forme qui ressemble à un phénomène humain (suffisance générative, Epstein, 1999) ne dit pas par quelle instance ni par quel mécanisme (Zhao, Pham et Vincent, 2026). La validation est le défi central de la simulation sociale générative (Larooij et Törnberg, 2025).

### 2.3 Statut des énoncés générés

Aucune instance de l'agencement n'a d'intériorité. Les énoncés sont produits en réponse à des **cadres d'énonciation** : une consigne, une fiche, une mémoire, une scène, une question (Goffman, 1974, pour la notion de cadre).

| Terme courant | Terme retenu | Statut |
|---|---|---|
| Opinion privée | **Position déclarée en enquête** | Énoncé produit face à l'enquêteur, dans un cadre présenté comme confidentiel |
| Expression publique | **Position exprimée en scène** | Énoncé produit dans une scène face à d'autres agents |
| Écart entre ce qu'on pense et ce qu'on dit | **Écart entre cadres d'énonciation** | Différence entre énoncés produits par le même agencement dans deux cadres |
| Croyance, peur, intention | **Disposition attribuée** | Attribut écrit dans la fiche par le concepteur |

**Test de stabilité** : chaque position déclarée est demandée sous deux formulations ; la part d'agents instables est un résultat.

### 2.4 Le modèle télégraphique : instrument, pas hypothèse

Certaines mesures (fidélité au message source, relais, diffusion) empruntent au modèle émetteur-message-récepteur (Shannon et Weaver, 1949), que les SIC ont largement critiqué (Winkin, 1981). Il est ici un **instrument de mesure** aux limites connues, et un **objet d'enquête** : l'agencement génératif produit-il une communication-transport ?

### 2.5 Trivialité et attracteurs culturels

| | Trivialité (Jeanneret, 2008, 2014) | Attracteurs culturels (Sperber, 1996) |
|---|---|---|
| Ce qui circule | Des « êtres culturels », réécrits à travers des médiations | Des représentations, transformées par la cognition des transmetteurs |
| Ce qui explique la transformation | Les médiations, les dispositifs, les rapports de pouvoir | Des biais qui font converger les versions vers des formes stables |

Les travaux sur les chaînes de transmission entre modèles de langage parlent d'attracteurs (Perez et al., 2025) et de biais de contenu (Acerbi et Stubbersfield, 2023). Le projet les mobilise pour **décrire** les convergences, et la co-agentivité pour **interpréter** : les « biais » d'un agent sont ceux de son modèle et de son fournisseur, et les médiations sont inscrites dans le dispositif par le concepteur.

Dans le village, toutes les médiations (gazette, mémoire, scènes) sont écrites par le concepteur et jouées par un seul architexte : la trivialité n'y a pas l'hétérogénéité des mondes sociaux que décrit Jeanneret. Elle reçoit donc une mesure circonscrite : la différence entre ce que deviennent les versions dans le village et dans des chaînes linéaires jouées par le même modèle, à profondeur de transmission égale (scénario, HO8). Cette différence est la trace des médiations sociales du dispositif ; le reste de la trivialité sert de lentille d'interprétation.

### 2.6 Complexité et incertitude : un volet réflexif pour l'ingénierie pédagogique

Le projet se donne un second regard, réflexif, emprunté à la pensée complexe d'Edgar Morin (1977-2004 ; 1990 ; 1999). Il n'ajoute pas d'hypothèse de travail : il lit le dispositif et ses résultats pour en tirer un recul pédagogique et méthodologique.

**Le constat de départ.** En ingénierie pédagogique, on introduit de l'incertitude dans les scénarios : un événement imprévu dans une étude de cas, un tirage dans un jeu sérieux, des embranchements dans une simulation. Cette incertitude est écrite d'avance : le concepteur a prévu l'ensemble des possibles, et l'apprenant découvre seulement lequel se produit. Au sens de Morin, c'est du **compliqué** (beaucoup d'éléments, beaucoup de branches, que l'on peut énumérer), non du **complexe** (ce qui est « tissé ensemble » : des éléments en interactions et en rétroactions, dont le tout ne se déduit pas des parties). Le village pousse la situation à sa limite. Le concepteur écrit tout, fiches, ordonnanceur, consignes, graines, et ne peut pourtant pas prévoir ce qui sera dit.

**Trois notions de Morin, et leur traduction dans le village.**

| Notion | Chez Morin | Dans le village |
|---|---|---|
| **Écologie de l'action** | Dès qu'une action entre dans un milieu d'interactions, elle échappe aux intentions de son auteur | La co-agentivité vue depuis le concepteur : il est une instance parmi six, pas l'auteur du résultat (section 1) |
| **Boucle récursive** | Les produits et les effets d'un processus sont aussi causes de ce qui les produit | La spirale du silence : le climat perçu fait taire, le silence modifie le climat, qui fait taire davantage (scénario, HT4, HO9) |
| **Programme et stratégie** | Le programme déroule une séquence fixée d'avance ; la stratégie se modifie selon ce qui arrive en route | Le préenregistrement est un programme ; les règles à trois issues, les replis du plan, le prolongement conditionnel (section 7) et le journal des imprévus (6.2) en font une stratégie |

**Trois incertitudes dans le projet.**
- L'**incertitude programmée** : les graines, les tirages, l'ordonnanceur au hasard. Le concepteur en connaît tous les possibles.
- L'**incertitude générée** : ce que produisent les modèles et les interactions entre agents. Le concepteur ne peut pas l'énumérer, mais elle reste bornée par l'architexte. Si les versions convergent vers le lieu commun (scénario, HT3), l'IA générative donne une impression d'ouverture tout en réduisant la diversité.
- L'**incertitude du chercheur** : ce qu'il ne peut pas savoir, comme l'intériorité des agents ou les parts qui ne peuvent être isolées. Le projet la déclare au lieu de la masquer, ce que Morin appelle « affronter les incertitudes » (1999).

**Mesure.** Le volet a une prise empirique sans simulation supplémentaire. La **part du hasard** (scénario, HO12, descriptive) rapporte la variation due aux graines à celle due aux conditions ; si une même graine ne reproduit pas les sorties (scénario, étape 6), l'écart entre deux exécutions d'une même graine isole l'incertitude générée. Le journal des imprévus du carnet de conception (6.2) en donne la trace qualitative.

**Question réflexive.** Que montre un dispositif entièrement écrit, mais imprévisible dans ses énoncés, sur l'incertitude que l'on programme dans les scénarios pédagogiques, et sur ce qu'apporte, ou retire, une IA générative qui joue des personnages ?

**Précaution.** La part aléatoire d'un modèle n'est pas l'incertitude au sens de Morin, qui est épistémologique et anthropologique. Le projet ne pose pas d'équivalence entre les deux : il montre la distinction entre aléatoire et complexe, et c'est elle qui a un intérêt pédagogique.

---

## 3. Problématique et questions de recherche

### 3.1 Problématique générale

> **Comment une simulation sociale générative fait-elle circuler et se transformer des énoncés, alors qu'aucune des voix qui la peuplent ne parle seule ?**

| Terme | Contenu | Pourquoi |
|---|---|---|
| **X** | Une simulation sociale générative fait circuler et se transformer des énoncés | C'est l'objet scientifique : une trivialité générée |
| **Y** | Aucune voix ne parle seule : chaque énoncé est co-produit par le modèle (et son fournisseur), la fiche, l'orchestrateur, l'ordonnanceur, les cadres d'énonciation et le concepteur, et toutes les voix passent par un petit nombre d'architextes | La circulation suppose des locuteurs distincts qui se transmettent des énoncés. Si chaque locuteur est lui-même un agencement, et si les mêmes instances écrivent toutes les voix, qu'est-ce qui circule, et entre qui ? |

### 3.2 Questions de recherche

| Code | Question | Lien à X/Y |
|---|---|---|
| **QR1. Les transformations** | Quelles transformations les énoncés subissent-ils en circulant, et en quoi diffèrent-elles de celles documentées chez les humains par des procédures équivalentes ? | X |
| **QR2. La part des instances** | Quelle part de ces transformations revient à chaque instance : modèle et fournisseur, fiche, orchestrateur, ordonnanceur, cadres d'énonciation, concepteur ? | Y, question centrale |
| **QR3. La communication inscrite** | Quelle conception de la communication l'agencement réalise-t-il : transport, interaction, médiation ? | X et Y |
| **QR4. Le dire et le taire** | Comment un dispositif génératif met-il en scène le dire et le taire autour d'un savoir savant, alors que ses agents, conçus pour toujours répondre, n'ont rien à craindre de la parole ? (Problématique du scénario.) | X et Y appliqués au scénario |

Les hypothèses de travail (HT) et les hypothèses opérationnelles (HO) sont détaillées dans le document du scénario. Chaque hypothèse de travail est assortie d'une règle de décision préenregistrée à trois issues : soutenue, réfutée, indéterminée.

---

## 4. Concepts mobilisés

### 4.1 Noyau théorique : l'agencement et ses instances

| Concept | Références | Définition retenue | Instance concernée | Ce qu'on observe |
|---|---|---|---|---|
| **Agentivité distribuée, co-agentivité** | Callon (1986) ; Latour (2006) ; Akrich et Latour (1992) ; Suchman (2007) | L'action est le fait d'un agencement d'actants humains et non humains | Toutes | La part de chaque instance dans les énoncés |
| **Architexte** | Jeanneret et Souchier (1999) ; Souchier, Jeanneret et Le Marec (2003) | Outil qui régit en amont l'écriture et en préfigure les formes | Modèle de langage, narrateur, modèle qui résume la mémoire | Les régularités propres à chaque modèle |
| **Script, inscription** | Akrich (1987) | Les usages et rôles que les concepteurs inscrivent dans un objet technique | Fiche, consignes, concepteur | Les choix consignés dans le carnet de conception |
| **Énonciation éditoriale** | Souchier (1998) | Ce qui donne forme à un texte au-delà de son auteur apparent | Orchestrateur, format des consignes | Ce que la consigne et la mémoire imposent aux énoncés |
| **Cadres de l'expérience** | Goffman (1974) | Les schèmes qui organisent ce qui se passe et ce qui peut se dire dans une situation | Ordonnanceur, enquêteur, gazette | Les effets du type de scène sur les énoncés |
| **Dispositif** | Foucault ; Agamben (2007) ; Jacquinot-Delaunay et Monnoyer (1999) | Agencement hétérogène qui oriente les conduites | Le village entier | L'ensemble des règles, du réseau, des routines |
| **Trivialité** | Jeanneret (2008, 2014) | Circulation créative des êtres culturels, réécrits à travers des médiations | Ce qui résulte de l'agencement | L'arbre complet des reprises d'un énoncé |
| **Médiation** | Jeanneret (2014) ; Davallon | Ce qui s'interpose et transforme dans toute communication | Gazette, compte rendu, narrateur | Les transformations attribuables à un intermédiaire |

### 4.2 Concepts opératoires empruntés, et conditions d'emprunt

| Concept | Références | Usage | Ce qui est adapté | Ce qui est perdu ou à discuter |
|---|---|---|---|---|
| **Reproduction en série : réduction, accentuation, assimilation** | Bartlett (1932) ; Allport et Postman (1947) | Décrire les transformations par relais | Catégories descriptives, sans jugement de perte | Protocole de laboratoire et mémoire humaine ; comparaison par réplication procédurale (chaînes linéaires) |
| **Chaînes de transmission, biais de contenu, attracteurs** | Mesoudi et Whiten (2008) ; Acerbi et Stubbersfield (2023) ; Perez et al. (2025) ; Sperber (1996) | Mesurer les convergences ; protocole des chaînes linéaires (modèle nul) | Protocole transposable | Cadre cognitiviste distinct de la trivialité (2.5) |
| **Rumeur** | Morin (1969) ; Kapferer (1987) ; Froissart (2002) | Prolongement possible : rumeur de la boulangerie (section 7) | Définition descriptive | Fonctions sociales (anxiété collective, identité) sans équivalent |
| **Rumeur et anxiété** | Rosnow (1991) | Prolongement possible : lien entre stabilité émotionnelle attribuée et transmission de la rumeur (section 7) | Disposition attribuée, non ressentie | Mécanisme affectif absent |
| **Correction et influence continue** | Lewandowsky et al. (2012) | Prolongement possible : survie de la rumeur après démenti (section 7) | Persistance mesurée | Mécanismes mnésiques sans équivalent direct |
| **Flux à deux étages** | Katz et Lazarsfeld (1955) | Rôle des habitants très connectés | Position dans le réseau | Leadership fondé sur la compétence reconnue : non modélisé |
| **Spirale du silence** | Noelle-Neumann (1974, 1993) | Scénario « Dire et taire » | Questions d'enquête, formalisations comme étalons | La peur de l'isolement n'existe que comme disposition écrite |
| **Lectures conforme, négociée, oppositionnelle** | Hall (1973) | Coder les appropriations | Rapportées au sens proposé par la source | La position sociale n'existe que comme attribut écrit |
| **Formule** | Krieg-Planque (2009) | Expressions figées qui résument l'énoncé | Repérage direct | Suppose un espace public réel |
| **Mise en scène de la communication** | Authier-Revuz (1982) | Marqueurs de reprise | Repérage direct | Aucun |
| **Mémoire interdiscursive** | Moirand (2007) | Analogies spontanées | Repérage des discours convoqués | La mémoire convoquée est celle des données d'entraînement |
| **Vulgarisation, continuum de la communication scientifique** | Jacobi (1999) ; Jurdant (2009) | Situer les sources | Classement sur le continuum | Aucun |
| **Complexité, incertitude** | Morin (1977-2004 ; 1990 ; 1999) | Volet réflexif (2.6) : écologie de l'action, boucle récursive, programme et stratégie | Trois incertitudes distinguées : programmée, générée, du chercheur ; part du hasard (scénario, HO12) | La complexité d'un village joué par un seul architexte est bornée ; la part aléatoire d'un modèle n'est pas l'incertitude au sens de Morin |

### 4.3 Concepts critiques sur les modèles de langage et la simulation

| Concept | Références | Usage |
|---|---|---|
| **Simulacres** | Park et al. (2023) | Le terme choisi par les promoteurs des agents génératifs, à interroger |
| **Perroquets stochastiques** | Bender et al. (2021) | Les modèles produisent des formes plausibles sans référence au sens ni à la situation |
| **Échantillons de silicium** | Argyle et al. (2023) | Promesse de simuler des sous-groupes humains, et ses limites |
| **Aplatissement des identités** | Wang, Morgenstern et Dickerson (2025) | Les modèles écrasent la diversité des groupes |
| **Suffisance générative, plausibilité des mécanismes** | Epstein (1999) ; Zhao, Pham et Vincent (2026) | Reproduire une forme n'est pas en expliquer le mécanisme |
| **Validation des simulations génératives** | Larooij et Törnberg (2026) | Structure les critères de la section 7 |
| **Règles de conduite des fournisseurs** | Mistral AI (politique d'usage, s. d.) ; OpenAI (2026) | Le fournisseur comme actant. Le fournisseur du village est Mistral, dont la politique d'usage pose un principe général de neutralité sans spécification comportementale publique ; la spécification d'OpenAI sert d'exemple de ce qu'un fournisseur peut prescrire. La neutralité apprise est mesurée (scénario, étape 0a), non attestée |
| **Mémoire d'entraînement** | Terme du projet | Ce que le modèle sait déjà des textes sources et de leur réception, traité comme la culture commune du village, identique chez tous les habitants ; mesuré avant toute circulation (scénario, étape 0a) ; conditionne l'interprétation des transformations, des analogies avec le présent et de la convergence |
| **Préférence des juges automatiques pour leurs propres textes** | Panickssery et al. (2024) | Justifie la séparation entre modèles générateurs et modèles juges |

---

## 5. Grille de lecture

La grille articule cinq niveaux d'analyse. À chaque niveau, la question transversale est la même : **quelle instance de l'agencement produit ce que l'on observe ?**

| Niveau | Question | Corpus | Concepts | Méthode | Instances principalement interrogées |
|---|---|---|---|---|---|
| **1. Agencement** | Qu'est-ce qui est inscrit dans le village avant toute circulation, et par qui ? | Code, consignes, fiches, mécanisme de mémoire, carnet de conception | Co-agentivité, script, architexte, énonciation éditoriale, dispositif | Analyse sociotechnique et sémiotique | Concepteur, orchestrateur, ordonnanceur |
| **2. Circulation** | Par où passent les énoncés ? | Traces des rencontres, réseau, traçabilité des relais | Flux à deux étages, rencontres homophiles (chambres d'écho) | Analyse de réseau, courbes de diffusion | Ordonnanceur, réseau |
| **3. Énoncés** | Comment les énoncés se transforment-ils ? | Chaînes de reformulation | Trivialité, reproduction en série, attracteurs, formule | Analyse de discours, codage | Modèle et fournisseur, orchestrateur (mémoire) |
| **4. Positions** | Quelles positions l'agencement produit-il selon les cadres d'énonciation ? | Réponses en enquête, répliques en scène | Cadres, lectures selon Hall, mémoire interdiscursive | Codage, analyse qualitative | Fiche, cadres, modèle |
| **5. Parts et écarts** | Quelle est la part de chaque instance, et que révèlent les écarts aux phénomènes humains ? | Résultats des niveaux 2 à 4, chaînes linéaires, conditions comparées | Co-agentivité, suffisance générative, aplatissement | Décomposition des effets par instance, interprétation critique | Toutes |

### 5.1 Livre de codes unifié (niveaux 3 et 4)

Les codes sont **descriptifs** : ils nomment une transformation, ils ne jugent pas une perte.

| Code | Catégorie | Origine | Définition opératoire |
|---|---|---|---|
| RED | Réduction | Allport et Postman | La reprise est plus courte que la version reçue |
| ACC | Accentuation | Allport et Postman | Un élément prend une place plus grande que dans la version reçue |
| ASS | Assimilation | Allport et Postman | La reprise se rapproche des attributs (valeurs, sensibilité) de la fiche de l'agent |
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

Un même énoncé peut recevoir plusieurs codes. La **fidélité** à la source est calculée à part : c'est une lentille parmi d'autres. Le livre de codes est testé sur le mini-village, soumis à une revue adversariale par un autre modèle, révisé, puis figé et préenregistré ; il est publié avec le carnet de conception pour que les pairs puissent le discuter.

---

## 6. Méthodologie

### 6.1 Une démarche mixte

- **Quantitative** : diffusion, fidélité, fréquences des codes, décomposition des effets par instance.
- **Qualitative** : analyse de discours de chaînes de reformulation complètes, choisies selon des critères préenregistrés.
- **Réflexive** : analyse de la part du concepteur, à partir du carnet de conception.

Convergences et divergences entre volets sont documentées ; une divergence est un résultat.

### 6.2 Le carnet de conception

Document daté, tenu par le chercheur, qui consigne pour chaque choix : le choix, sa justification au moment où il est fait, les alternatives écartées, ses effets observés ensuite. C'est la **trace de la part d'agentivité du concepteur**, et il fait partie du corpus du niveau 1.

Il comporte un **journal des imprévus** : ce que le concepteur n'avait pas prévu (un comportement des agents, une panne, un résultat du pilote) et ce qu'il a changé en conséquence, avec la date et la règle du préenregistrement concernée. C'est la trace de l'écologie de l'action et du passage du programme à la stratégie (2.6).

### 6.3 Fiabilité du codage

- Préenregistrement en deux temps : questions, hypothèses, règles de décision et contrastes de référence avant toute génération ; livres de codes figés, nombre de graines et seuils techniques après le pilote, par un avenant daté. Le pilote n'entre pas dans l'analyse.
- Codage humain par le chercheur seul : fiabilité intra-codeur (recodage à l'aveugle de 15 % du corpus après au moins trois semaines ; kappa de Cohen, seuil de 0,7) ; accord entre ce codage et deux modèles juges distincts ; livres de codes et extraits codés publiés, pour que la vérification par les pairs reste possible.
- **Un juge ne code jamais un énoncé écrit par un modèle de sa famille** (Panickssery et al., 2024). Deux juges codent chaque énoncé ; leur accord est mesuré ; chacun est validé contre un échantillon codé par le chercheur, et remplacé s'il n'atteint pas le seuil ; les analyses portent sur les codes concordants, les désaccords étant arbitrés par le chercheur à l'aveugle de la condition.
- **Les autres instruments** (enquêteur, outils de mesure automatique comme un modèle de plongement) sont déclarés comme tels ; toute mesure qui dépend d'un modèle est doublée d'une mesure qui n'en dépend pas, quand c'est possible.
- Plusieurs graines par condition ; résultats retenus seulement s'ils sont stables.

### 6.4 Décomposer l'agentivité : faire varier une instance à la fois

C'est la traduction méthodologique de la clef de lecture. Chaque instance a sa ou ses conditions expérimentales :

| Instance | Condition qui la fait varier |
|---|---|
| **Modèle de langage et fournisseur** | Village entier joué par un autre modèle ; narrateur seul changé ; habitants répartis entre plusieurs modèles ; test sans public des modèles seuls |
| **Fiche du persona** | Faire varier les attributs (disposition à l'autocensure, sensibilité) ; permutations des prénoms et du genre ; condition sans autocensure |
| **Orchestrateur** | Mode de lecture (intégral ou annoté) ; mécanisme de résumé de la mémoire |
| **Ordonnanceur** | Rencontres au hasard ou homophiles |
| **Cadres d'énonciation** | Scène publique ou privée ; gazette ; compères ; sollicitations |
| **Modèle et fournisseur : mode d'écriture** | Polyphonie homogène (référence), autre architexte, habitants pluri-modèles, auteur unique |
| **Concepteur** | Carnet de conception ; variations de consignes censées être neutres (paraphrases) ; choix des contrastes de référence |

Les **modes d'écriture** comparés dans le scénario :

| Mode | Fonctionnement | Ce qu'il isole |
|---|---|---|
| Polyphonie homogène (« tout Le Chonk ») | Tous les rôles joués par Le Chonk, chaque habitant restant un appel séparé avec sa fiche et sa mémoire | **Condition de référence** : un architexte unique sous des voix multiples |
| Polyphonie d'un autre architexte | La même configuration, entièrement jouée par un autre modèle de bonne qualité (de préférence du même fournisseur) | L'effet du modèle à configuration égale, sans mélange de modèles |
| Habitants pluri-modèles | Les habitants sont répartis entre plusieurs modèles de taille moyenne, sans Le Chonk ; chacun résume sa mémoire avec son modèle ; lecteur et narrateur sur Le Chonk | Ce que change la pluralité des architextes parmi les voix, par comparaison avec un village joué par un seul modèle de taille comparable |
| Auteur unique | Le Chonk écrit seul toute la vie du village, une génération par journée, sans séparation des connaissances | Ce que change la distribution de l'écriture entre agents |

Dans tous les modes, les rencontres sont organisées par un **ordonnanceur algorithmique** (du code), séparé du **narrateur** (un modèle), pour distinguer l'organisation de l'exposition de l'écriture des scènes.

**Contrastes de référence.** Pour comparer des parts, il faut une unité commune. Chaque instance reçoit un contraste de référence fixé avant toute génération (par exemple disposition faible contre forte, scène privée contre publique, un modèle contre plusieurs), et l'effet de chaque contraste est exprimé dans la même unité (en points de pourcentage pour une proportion). La part ainsi mesurée dépend du contraste choisi : ce choix est la part du concepteur dans la mesure elle-même, et il est justifié dans le préenregistrement. L'amplitude d'un contraste est justifiée avant toute génération. Pour l'instance dont l'hypothèse centrale prédit la moindre part (la fiche, dans le scénario), le contraste reçoit son **étendue maximale**, afin que l'hypothèse ne puisse pas être soutenue par une manipulation faible ; un contrôle de manipulation vérifie que le contraste produit bien ce qu'il est censé produire. Les interactions entre contrastes sont estimées dans le même modèle et rapportées. Les parts mesurées hors du village (test d'un modèle seul, dyades) sont rapportées à part et ne sont pas comparées directement aux contrastes mesurés dans le village.

**Règles de décision.** Chaque hypothèse de travail a une issue préenregistrée parmi trois : soutenue, réfutée, indéterminée. Quand une hypothèse affirme l'absence d'un effet, l'absence est établie par un test d'équivalence (Lakens, 2017), et non par un simple résultat non significatif.

### 6.5 Réplication procédurale des références humaines

Pour chaque référence humaine mobilisée, on reproduit son protocole dans le dispositif, ou l'on déclare la comparaison qualitative.

| Référence humaine | Procédure reproduite |
|---|---|
| Reproduction en série (Bartlett, 1932 ; Allport et Postman, 1947) ; chaînes de transmission (Mesoudi et Whiten, 2008) | Chaînes linéaires de 10 agents (étape 5 du scénario) |
| Biais de contenu (Acerbi et Stubbersfield, 2023) | Comparaison qualitative des transformations dans les chaînes |
| Spirale du silence (méta-analyses ; test du train) | Questions d'enquête reprises des études ; formalisations comme étalons |

Les **chaînes linéaires** donnent aussi la ligne de base qui permet de mesurer ce que l'**agencement social** (réseau, scènes, mémoire) ajoute à une transmission linéaire.

### 6.6 Unités d'analyse et puissance

Pour les indicateurs collectifs, l'unité est la simulation ; pour les indicateurs individuels, l'agent emboîté dans la simulation (modèles à effets mixtes). Une **graine** fixe à la fois le hasard de l'ordonnanceur et le paramètre d'échantillonnage du modèle, à température unique et déclarée ; le pilote vérifie si une même graine reproduit les sorties. Un pilote estime la variance entre graines ; le nombre de graines est fixé par calcul de puissance pour l'écart entre contrastes que la règle de décision exige, au moins 5 par condition. Les intervalles des contrastes entre simulations sont issus des modèles mixtes (avec correction pour petits effectifs de simulations) ; le rééchantillonnage des simulations ne sert que de contrôle. Les comparaisons multiples qu'une règle de décision autorise sont corrigées (Holm). Plans d'expérience à priorités.

### 6.7 Reproductibilité, données, sobriété

- **Reproductibilité des analyses** garantie (toutes les générations archivées avec leurs métadonnées) ; **réplicabilité des générations** limitée et documentée.
- **Plan de gestion des données** (DMP OPIDoR) : formats ouverts, licences, dépôt, exclusions (extraits longs d'ouvrages protégés, contenus discriminatoires bruts).
- **Revues** : chaque révision importante des documents passe par une revue consignée (auto-revue, revue croisée par un autre modèle, relecture différée par le chercheur). Les pairs interviennent ensuite : billets sur le carnet de recherche (jediopenlab.hypotheses.org), puis articles soumis à évaluation.
- **Sobriété** : tokens et estimation énergétique journalisés et rapportés.

---

## 7. Critères de scientificité et limites

| Critère | Comment il est satisfait |
|---|---|
| Construction explicite de l'objet | Objet concret, scientifique, de recherche ; clef de lecture explicitée |
| Cohérence théorie, méthode, corpus | Noyau théorique centré sur l'agencement ; décomposition des instances ; livre de codes descriptif |
| Validité des comparaisons | Réplication procédurale ; chaînes linéaires comme modèle nul |
| Distinction entre forme reproduite et mécanisme | Décomposition par instance ; prudence sur la suffisance générative |
| Réflexivité | Le concepteur traité comme une instance ; carnet de conception et journal des imprévus ; volet réflexif sur la complexité et l'incertitude (2.6) |
| Fiabilité | Préenregistrement en deux temps, règles de décision à trois issues, fiabilité intra-codeur, deux modèles juges indépendants, codages publiés, puissance, répétitions |
| Prudence interprétative | Aucune généralisation aux humains ; vocabulaire des cadres d'énonciation |
| Transparence | Code, consignes, livres de codes, fiches, archives publiés selon le plan de gestion des données |

**Limites assumées**
- **Le risque de dilution** : affirmer que tout est agencement n'explique rien. La co-agentivité n'a de valeur que par la décomposition expérimentale des parts ; une part qui ne peut être isolée est déclarée comme telle.
- **La part dépend du contraste** : la part d'une instance est mesurée relativement au contraste de référence choisi ; un autre contraste donnerait une autre part. Les contrastes sont donc fixés et justifiés avant toute génération.
- **Modèle et fournisseur se séparent mal** : changer de modèle change en général aussi de fournisseur, de données d'entraînement et de règles de conduite, et leurs parts sont alors rapportées ensemble. Un contraste entre deux modèles du même fournisseur approche la part du modèle à fournisseur constant (scénario, section 3.1) ; la part du fournisseur n'est approchée qu'hors du village, en comparant des modèles de fournisseurs différents.
- **Les instruments sont des agencements** : enquêteur, juges et outils de mesure produisent eux aussi des énoncés ou des scores ; d'où leurs garde-fous (section 6.3).
- **L'agentivité n'est pas l'intentionnalité** : dire qu'une instance « agit » signifie qu'elle fait une différence mesurable, non qu'elle veut quelque chose.
- **Décomposer n'est pas suivre les associations** : la mesure des parts est un découpage du concepteur, compatible avec l'agencement par le rapport des interactions et des parts non isolables (1.3).
- **Les modèles savent déjà** : ce qu'un modèle sait des textes sources par ses données d'entraînement entre dans le village avant toute circulation ; cette mémoire d'entraînement est mesurée et rapportée comme part du modèle et du fournisseur.
- Les références humaines viennent de dispositifs différents ; seules certaines sont reproductibles procéduralement.
- Les modèles évoluent : les résultats valent pour des versions datées.
- **La complexité du village est bornée** : un seul architexte écrit toutes les voix, et les médiations sont écrites par le concepteur ; l'incertitude qui y apparaît n'est pas celle d'une société (2.6).
- Le codage automatique ajoute une instance à l'analyse elle-même ; d'où la séparation des modèles et la validation humaine.

### Prolongements possibles

Le projet ne compte qu'un scénario. Un second est gardé en réserve, sans protocole : **la rumeur de la boulangerie qui ferme, puis son démenti** (Morin, 1969 ; Kapferer, 1987 ; Froissart, 2002 ; Lewandowsky et al., 2012). C'est un énoncé banal, sans enjeu moral, à l'opposé d'une thèse d'historien. Il serait joué dans le même village, avec les mêmes juges et la même méthode de décomposition, seulement si les résultats de « Dire et taire » le rendent informatif :
- si le **dire vide** (HT2) est soutenu : la neutralisation disparaît-elle face à un énoncé banal, ou les agents neutralisent-ils tout ?
- si la **convergence** (HT3) est établie : une rumeur converge-t-elle aussi vite qu'une thèse savante ? Si oui, la convergence tient à l'architexte plutôt qu'à la charge morale ;
- si le **climat ne pèse pas** (HT4) : un village qui ne lit pas le climat corrige-t-il une rumeur démentie, ou la garde-t-il (effet d'influence continue) ?

Si les résultats sont indéterminés, ce prolongement n'est pas engagé.

---

## 8. Valorisation envisageable

**Revues de SIC** : *Communication & langages*, *Questions de communication*, *Les Enjeux de l'information et de la communication*, *Hermès*, *Réseaux*, *tic&société*, *Revue française des sciences de l'information et de la communication*.

**Simulation et méthodes** : *Journal of Artificial Societies and Social Simulation*.

**Ingénierie pédagogique et sciences de l'éducation** (volet réflexif, 2.6) : *Distances et médiations des savoirs*, *Revue internationale des technologies en pédagogie universitaire*, *STICEF* ; billet sur le carnet de recherche JEDI-OpenLab.

**Événements** : congrès de la SFSIC ; journées d'étude sur les écritures numériques et l'IA générative.

---

## 9. Bibliographie

### Communication, trivialité, dispositifs
- Agamben, G. (2007). *Qu'est-ce qu'un dispositif ?* Paris : Rivages.
- Akrich, M. (1987). Comment décrire les objets techniques ? *Techniques et culture*, 9, 49-64.
- Akrich, M., & Latour, B. (1992). A Summary of a Convenient Vocabulary for the Semiotics of Human and Nonhuman Assemblies. In W. E. Bijker & J. Law (dir.), *Shaping Technology/Building Society* (p. 259-264). Cambridge, MA : MIT Press.
- Callon, M. (1986). Éléments pour une sociologie de la traduction. La domestication des coquilles Saint-Jacques et des marins-pêcheurs dans la baie de Saint-Brieuc. *L'Année sociologique*, 36, 169-208.
- Davallon, J. (2004). Objet concret, objet scientifique, objet de recherche. *Hermès*, 38, 30-37.
- Goffman, E. (1974). *Frame Analysis: An Essay on the Organization of Experience*. New York : Harper & Row. Trad. fr. *Les cadres de l'expérience*, Paris : Minuit, 1991.
- Jacquinot-Delaunay, G., & Monnoyer, L. (dir.) (1999). Le dispositif. Entre usage et concept. *Hermès*, 25.
- Jeanneret, Y. (2008). *Penser la trivialité. Volume 1 : La vie triviale des êtres culturels*. Paris : Hermès-Lavoisier.
- Jeanneret, Y. (2014). *Critique de la trivialité. Les médiations de la communication, enjeu de pouvoir*. Paris : Éditions Non Standard.
- Jeanneret, Y., & Souchier, E. (1999). Pour une poétique de l'écrit d'écran. *Xoana*, 6, 97-107.
- Latour, B. (2006). *Changer de société, refaire de la sociologie*. Paris : La Découverte. (Éd. originale : *Reassembling the Social*, Oxford University Press, 2005.)
- Shannon, C. E., & Weaver, W. (1949). *The Mathematical Theory of Communication*. Urbana : University of Illinois Press.
- Souchier, E. (1998). L'image du texte. Pour une théorie de l'énonciation éditoriale. *Les Cahiers de médiologie*, 6, 137-145.
- Souchier, E., Jeanneret, Y., & Le Marec, J. (dir.) (2003). *Lire, écrire, récrire. Objets, signes et pratiques des médias informatisés*. Paris : Bibliothèque publique d'information.
- Suchman, L. (2007). *Human-Machine Reconfigurations: Plans and Situated Actions* (2e éd.). Cambridge : Cambridge University Press.
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
- Froissart, P. (2002). *La rumeur. Histoire et fantasmes*. Paris : Belin.
- Kapferer, J.-N. (1987). *Rumeurs. Le plus vieux média du monde*. Paris : Seuil.
- Lewandowsky, S., Ecker, U. K. H., Seifert, C. M., Schwarz, N., & Cook, J. (2012). Misinformation and Its Correction. *Psychological Science in the Public Interest*, 13(3), 106-131.
- Mesoudi, A., & Whiten, A. (2008). The multiple roles of cultural transmission experiments in understanding human cultural evolution. *Philosophical Transactions of the Royal Society B*, 363(1509), 3489-3501.
- Morin, E. (1969). *La rumeur d'Orléans*. Paris : Seuil.
- Perez, J., Kovač, G., Léger, C., Colas, C., Molinaro, G., Derex, M., Oudeyer, P.-Y., & Moulin-Frier, C. (2025). When LLMs Play the Telephone Game: Cultural Attractors as Conceptual Tools to Evaluate LLMs in Multi-turn Settings. *Proceedings of ICLR 2025*.
- Rosnow, R. L. (1991). Inside rumor: A personal journey. *American Psychologist*, 46(5), 484-496.
- Sperber, D. (1996). *La contagion des idées. Théorie naturaliste de la culture*. Paris : Odile Jacob.

### Complexité et incertitude
- Morin, E. (1977-2004). *La Méthode* (6 tomes). Paris : Seuil.
- Morin, E. (1990). *Introduction à la pensée complexe*. Paris : ESF éditeur.
- Morin, E. (1999). *Les sept savoirs nécessaires à l'éducation du futur*. Paris : UNESCO. Rééd. Paris : Seuil, 2000.

### Modèles de langage, simulation, validation
- Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., & Wingate, D. (2023). Out of One, Many: Using Language Models to Simulate Human Samples. *Political Analysis*, 31(3), 337-351.
- Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? *Proceedings of FAccT '21*.
- Epstein, J. M. (1999). Agent-based computational models and generative social science. *Complexity*, 4(5), 41-60.
- Gebru, T., et al. (2021). Datasheets for Datasets. *Communications of the ACM*, 64(12), 86-92.
- Lakens, D. (2017). Equivalence tests: A practical primer for t tests, correlations, and meta-analyses. *Social Psychological and Personality Science*, 8(4), 355-362.
- Larooij, M., & Törnberg, P. (2026). Validation is the central challenge for generative social simulation: a critical review of LLMs in agent-based modeling. *Artificial Intelligence Review*, 59(1), article 15. https://doi.org/10.1007/s10462-025-11412-6 (préprint : *arXiv:2504.03274*, sous un autre titre).
- Mistral AI (s. d.). *Usage Policy*. https://legal.mistral.ai/terms/usage-policy/ (consulté le 16 octobre 2026).
- Noelle-Neumann, E. (1974). The spiral of silence: A theory of public opinion. *Journal of Communication*, 24(2), 43-51.
- Noelle-Neumann, E. (1993). *The Spiral of Silence: Public Opinion, Our Social Skin* (2e éd.). Chicago : University of Chicago Press.
- OpenAI (2026). *Model Spec*, version du 18 août 2026. https://model-spec.openai.com/2026-08-18.html (consulté le 16 octobre 2026).
- Panickssery, A., Bowman, S. R., & Feng, S. (2024). LLM Evaluators Recognize and Favor Their Own Generations. *Advances in Neural Information Processing Systems 37 (NeurIPS 2024)*. *arXiv:2404.13076*.
- Park, J. S., O'Brien, J., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative Agents: Interactive Simulacra of Human Behavior. *Proceedings of UIST '23*.
- Varenne, F. (2007). *Du modèle à la simulation informatique*. Paris : Vrin.
- Varenne, F. (2018). *From Models to Simulations*. Londres : Routledge.
- Vezhnevets, A. S., et al. (2023). Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia. *arXiv:2312.03664*.
- Wang, A., Morgenstern, J., & Dickerson, J. P. (2025). Large language models that replace human participants can harmfully misportray and flatten identity groups. *Nature Machine Intelligence*, 7(3), 400-411.
- Zhao, P., Pham, D. H., & Vincent, N. (2026). Mechanism Plausibility in Generative Agent-Based Modeling. *Proceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency (FAccT '26)*, 5915-5940. https://doi.org/10.1145/3805689.3812388

*Les références de 2024 à 2026 ont été vérifiées par la revue n° 2 (section 6) et corrigées dans cette version. Les autres restent à vérifier une à une (pagination, éditions) avant toute publication.*
