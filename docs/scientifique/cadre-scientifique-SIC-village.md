# Cadre scientifique en sciences de l'information et de la communication

*Le village simulé (expériences C0 à C5) comme objet de recherche en SIC. Version 5 du 16 octobre 2026 : réécriture autour de la co-agentivité, clef de lecture de l'ensemble du projet. Documents associés : « scenario-C4-circulation-savoir-savant.md », « projet-spirale-du-silence-formalisation.md », « ../revues/revue-adversariale-1-cadre-et-C4.md ».*


*Les termes, leur paternité et leurs références d'origine sont définis dans « ../glossaire.md ».*
---

## 1. La clef de lecture : la co-agentivité

### 1.1 Qui parle quand un agent parle ?

Le village de Saint-Aubert-sur-Lys est peuplé d'« agents ». Le mot est trompeur. Quand un habitant dit quelque chose au café, la phrase n'est pas l'acte d'un individu : elle est **co-produite** par un agencement d'instances, humaines et non humaines.

| Instance | Ce qu'elle fait à l'énoncé | Ce qui la porte |
|---|---|---|
| **Le modèle de langage** | Il écrit la phrase, avec ses régularités, ses préférences et ses réglages (complaisance, neutralité apprise) | Ses données d'entraînement et, derrière lui, son **fournisseur** et les règles de conduite qu'il lui impose |
| **La fiche du persona** | Elle oriente le ton, les valeurs, les dispositions attribuées | Le concepteur, qui l'a écrite |
| **L'orchestrateur** | Il assemble la consigne et choisit les souvenirs qui y figurent, donc ce que l'agent « sait » | Le code, et le modèle qui résume les souvenirs |
| **L'ordonnanceur** | Il décide de la rencontre : qui parle à qui, où, dans quel type de scène | Le code, et les règles fixées par le concepteur |
| **Le concepteur** | Il a fixé tout ce qui précède : consignes, règles, cadres d'énonciation, sollicitations | Le chercheur lui-même |

L'énoncé est l'acte d'un **agencement**. On appelle **co-agentivité** cette production conjointe des énoncés par le modèle, le dispositif et le concepteur.

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

### 1.4 Ce que la clef de lecture change

| Sans la clef de lecture | Avec la clef de lecture |
|---|---|
| On demande si les agents « reproduisent » des comportements humains | On demande **quelle instance de l'agencement** produit ce que l'on observe |
| Un écart aux humains est un défaut du simulateur | Un écart aux humains révèle **la part d'une instance** (le modèle, le fournisseur, le dispositif) |
| Le concepteur est extérieur à l'expérience | Le concepteur est **une instance parmi d'autres**, dont la part est documentée |
| Les conditions expérimentales sont des variantes techniques | Chaque condition **fait varier une instance** pour estimer sa part |

**Garde-fou** : si tout est agencement, rien n'est expliqué. La co-agentivité n'est utile que si l'on peut **décomposer** les parts. C'est le rôle du plan expérimental (section 6.4).

---

## 2. Construire l'objet

### 2.1 De l'objet concret à l'objet de recherche

En reprenant la distinction de Davallon (2004) :

| Niveau | Dans ce projet |
|---|---|
| **Objet concret** | Un village simulé : modèles, fiches, orchestrateur, ordonnanceur, narrateur, consignes, traces |
| **Objet scientifique** | La **trivialité co-produite** : la manière dont des énoncés (rumeur, démenti, convention, savoir savant) circulent et se transforment quand chaque reprise est écrite par un agencement de modèles, de code et de consignes |
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

---

## 3. Problématique et questions de recherche

### 3.1 Problématique générale

> **Comment une simulation sociale générative fait-elle circuler et se transformer des énoncés, alors qu'aucune des voix qui la peuplent ne parle seule ?**

| Terme | Contenu | Pourquoi |
|---|---|---|
| **X** | Une simulation sociale générative fait circuler et se transformer des énoncés | C'est l'objet scientifique : une trivialité générée |
| **Y** | Aucune voix ne parle seule : chaque énoncé est co-produit par le modèle (et son fournisseur), la fiche, l'orchestrateur, l'ordonnanceur et le concepteur, et toutes les voix passent par un petit nombre d'architextes | La circulation suppose des locuteurs distincts qui se transmettent des énoncés. Si chaque locuteur est lui-même un agencement, et si les mêmes instances écrivent toutes les voix, qu'est-ce qui circule, et entre qui ? |

### 3.2 Questions de recherche

| Code | Question | Lien à X/Y | Expériences |
|---|---|---|---|
| **QR1. Les transformations** | Quelles transformations les énoncés subissent-ils en circulant, et en quoi diffèrent-elles de celles documentées chez les humains par des procédures équivalentes ? | X | C0, C1, C4 |
| **QR2. La part des instances** | Quelle part de ces transformations revient à chaque instance : modèle et fournisseur, fiche, orchestrateur, ordonnanceur, concepteur ? | Y, question centrale | C3, C4, C5 |
| **QR3. La communication inscrite** | Quelle conception de la communication l'agencement réalise-t-il : transport, interaction, médiation ? | X et Y | Toutes |
| **QR4. Le dire et le taire** | Comment un dispositif génératif met-il en scène le dire et le taire autour d'un savoir savant, alors que ses agents, conçus pour toujours répondre, n'ont rien à craindre de la parole ? (Problématique du C4.) | X et Y appliqués au C4 | C4 |

Les hypothèses de travail et les hypothèses opérationnelles sont propres à chaque expérience (voir le document du C4).

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
| **Médiation** | Jeanneret (2014) ; Davallon | Ce qui s'interpose et transforme dans toute communication | Gazette, démenti, compte rendu, narrateur | Les transformations attribuables à un intermédiaire |

### 4.2 Concepts opératoires empruntés, et conditions d'emprunt

| Concept | Références | Usage | Ce qui est adapté | Ce qui est perdu ou à discuter |
|---|---|---|---|---|
| **Reproduction en série : réduction, accentuation, assimilation** | Bartlett (1932) ; Allport et Postman (1947) | Décrire les transformations par relais | Catégories descriptives, sans jugement de perte | Protocole de laboratoire et mémoire humaine ; comparaison par réplication procédurale (C0) |
| **Chaînes de transmission, biais de contenu, attracteurs** | Mesoudi et Whiten (2008) ; Acerbi et Stubbersfield (2023) ; Perez et al. (2025) ; Sperber (1996) | Mesurer les convergences ; protocole de C0 | Protocole transposable | Cadre cognitiviste distinct de la trivialité (2.5) |
| **Rumeur** | Morin (1969) ; Kapferer (1987) ; Froissart (2002) | Rumeur de la boulangerie | Définition descriptive | Fonctions sociales (anxiété collective, identité) sans équivalent |
| **Rumeur et anxiété** | Rosnow (1991) | Lien entre stabilité émotionnelle attribuée et transmission | Disposition attribuée, non ressentie | Mécanisme affectif absent |
| **Correction et influence continue** | Lewandowsky et al. (2012) | Survie de la rumeur après démenti | Persistance mesurée | Mécanismes mnésiques sans équivalent direct |
| **Flux à deux étages** | Katz et Lazarsfeld (1955) | Rôle des habitants très connectés | Position dans le réseau | Leadership fondé sur la compétence reconnue : non modélisé |
| **Convention et masse critique** | Centola et al. (2018) | Expérience C2 | Jeu de dénomination | Incitations du protocole humain absentes |
| **Spirale du silence** | Noelle-Neumann (1974, 1993) | Expérience C4 | Questions d'enquête, formalisations comme étalons | La peur de l'isolement n'existe que comme disposition écrite |
| **Lectures conforme, négociée, oppositionnelle** | Hall (1973) | Coder les appropriations | Rapportées au sens proposé par la source | La position sociale n'existe que comme attribut écrit |
| **Formule** | Krieg-Planque (2009) | Expressions figées qui résument l'énoncé | Repérage direct | Suppose un espace public réel |
| **Mise en scène de la communication** | Authier-Revuz (1982) | Marqueurs de reprise | Repérage direct | Aucun |
| **Mémoire interdiscursive** | Moirand (2007) | Analogies spontanées | Repérage des discours convoqués | La mémoire convoquée est celle des données d'entraînement |
| **Vulgarisation, continuum de la communication scientifique** | Jacobi (1999) ; Jurdant (2009) | Situer les sources | Classement sur le continuum | Aucun |

### 4.3 Concepts critiques sur les modèles de langage et la simulation

| Concept | Références | Usage |
|---|---|---|
| **Simulacres** | Park et al. (2023) | Le terme choisi par les promoteurs des agents génératifs, à interroger |
| **Perroquets stochastiques** | Bender et al. (2021) | Les modèles produisent des formes plausibles sans référence au sens ni à la situation |
| **Échantillons de silicium** | Argyle et al. (2023) | Promesse de simuler des sous-groupes humains, et ses limites |
| **Aplatissement des identités** | Wang, Morgenstern et Dickerson (2025) | Les modèles écrasent la diversité des groupes |
| **Suffisance générative, plausibilité des mécanismes** | Epstein (1999) ; Zhao, Pham et Vincent (2026) | Reproduire une forme n'est pas en expliquer le mécanisme |
| **Validation des simulations génératives** | Larooij et Törnberg (2025) | Structure les critères de la section 7 |
| **Règles de conduite des fournisseurs** | OpenAI (2025) | Le fournisseur comme actant : neutralité exigée sur les sujets controversés |
| **Préférence des juges automatiques pour leurs propres textes** | Panickssery et al. (2024) | Justifie la séparation entre modèles générateurs et modèle juge |

---

## 5. Grille de lecture

La grille articule cinq niveaux d'analyse. À chaque niveau, la question transversale est la même : **quelle instance de l'agencement produit ce que l'on observe ?**

| Niveau | Question | Corpus | Concepts | Méthode | Instances principalement interrogées |
|---|---|---|---|---|---|
| **1. Agencement** | Qu'est-ce qui est inscrit dans le village avant toute circulation, et par qui ? | Code, consignes, fiches, mécanisme de mémoire, carnet de conception | Co-agentivité, script, architexte, énonciation éditoriale, dispositif | Analyse sociotechnique et sémiotique | Concepteur, orchestrateur, ordonnanceur |
| **2. Circulation** | Par où passent les énoncés ? | Traces des rencontres, réseau, traçabilité des relais | Flux à deux étages, rumeur, masse critique | Analyse de réseau, courbes de diffusion | Ordonnanceur, réseau |
| **3. Énoncés** | Comment les énoncés se transforment-ils ? | Chaînes de reformulation | Trivialité, reproduction en série, attracteurs, formule | Analyse de discours, codage | Modèle et fournisseur, orchestrateur (mémoire) |
| **4. Positions** | Quelles positions l'agencement produit-il selon les cadres d'énonciation ? | Réponses en enquête, répliques en scène | Cadres, lectures selon Hall, mémoire interdiscursive | Codage, analyse qualitative | Fiche, cadres, modèle |
| **5. Parts et écarts** | Quelle est la part de chaque instance, et que révèlent les écarts aux phénomènes humains ? | Résultats des niveaux 2 à 4, C0, conditions comparées | Co-agentivité, suffisance générative, aplatissement | Décomposition des effets par instance, interprétation critique | Toutes |

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

### 6.3 Fiabilité du codage

- Préenregistrement des questions, des hypothèses, des livres de codes et des critères de sélection qualitative.
- Codage humain par le chercheur seul : fiabilité intra-codeur (recodage à l'aveugle de 15 % du corpus après au moins trois semaines ; kappa de Cohen, seuil de 0,7) ; accord entre ce codage et deux modèles juges distincts ; livres de codes et extraits codés publiés, pour que la vérification par les pairs reste possible.
- **Le modèle juge est toujours différent des modèles qui ont généré la simulation codée** (Panickssery et al., 2024). Il est validé contre le codage humain.
- Plusieurs graines par condition ; résultats retenus seulement s'ils sont stables.

### 6.4 Décomposer l'agentivité : faire varier une instance à la fois

C'est la traduction méthodologique de la clef de lecture. Chaque instance a sa ou ses conditions expérimentales :

| Instance | Condition qui la fait varier | Expériences |
|---|---|---|
| **Modèle de langage et fournisseur** | Changer le modèle des habitants, du narrateur, ou de tous les rôles (Le Chonk, Qwen, Gemma) ; test sans public des modèles seuls | C3, C4, C5 |
| **Fiche du persona** | Faire varier les attributs (disposition à l'autocensure, sensibilité) ; permutations des prénoms et du genre ; condition sans autocensure | C3, C4 |
| **Orchestrateur** | Mode de lecture (intégral ou annoté) ; mécanisme de résumé de la mémoire | C4 |
| **Ordonnanceur** | Rencontres au hasard ou homophiles ; position du premier émetteur | C1, C4 |
| **Cadres d'énonciation** | Scène publique ou privée ; enquêteur ; gazette ; compères | C4 |
| **Mode d'écriture** | Polyphonie mixte, polyphonie homogène, autre modèle, auteur unique | C5 |
| **Concepteur** | Carnet de conception ; variations de consignes censées être neutres (paraphrases) | C3, tous |

Les **modes d'écriture** comparés (C5) :

| Mode | Fonctionnement | Ce qu'il isole |
|---|---|---|
| Polyphonie mixte | Habitants sur ILaaS ; narrateur et lecteur sur Le Chonk | Condition principale |
| Polyphonie homogène | Tous les rôles joués par Le Chonk, chaque habitant restant un appel séparé avec sa mémoire | Un architexte unique sous des voix multiples |
| Polyphonie d'un autre architexte | Tous les rôles joués par Qwen ou Gemma | L'effet du modèle à configuration égale |
| Auteur unique | Le Chonk écrit d'un seul tenant la vie du village, sans séparation des connaissances | Ce que change la distribution de l'écriture entre agents |

Dans tous les modes, les rencontres sont organisées par un **ordonnanceur algorithmique** (du code), séparé du **narrateur** (un modèle), pour distinguer l'organisation de l'exposition de l'écriture des scènes.

### 6.5 Réplication procédurale des références humaines

Pour chaque référence humaine mobilisée, on reproduit son protocole dans le dispositif, ou l'on déclare la comparaison qualitative.

| Référence humaine | Procédure reproduite | Expérience |
|---|---|---|
| Reproduction en série (Bartlett, 1932 ; Allport et Postman, 1947) ; chaînes de transmission (Mesoudi et Whiten, 2008) | Chaînes linéaires de 10 agents | **C0** |
| Biais de contenu (Acerbi et Stubbersfield, 2023) | Mêmes matériaux | **C0** |
| Masse critique d'une convention (Centola et al., 2018) | Jeu de dénomination | C2 |
| Influence continue (Lewandowsky et al., 2012) | Comparaison qualitative | C1 |
| Spirale du silence (méta-analyses ; test du train) | Questions d'enquête reprises des études ; formalisations comme étalons | C4 |

L'expérience **C0** donne aussi la ligne de base qui permet de mesurer ce que l'**agencement social** (réseau, scènes, mémoire) ajoute à une transmission linéaire.

### 6.6 Unités d'analyse et puissance

Pour les indicateurs collectifs, l'unité est la simulation ; pour les indicateurs individuels, l'agent emboîté dans la simulation (modèles à effets mixtes). Un pilote estime la variance entre graines ; le nombre de graines est fixé par calcul de puissance, au moins 5 pour les contrastes centraux. Plans d'expérience à priorités.

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
| Validité des comparaisons | Réplication procédurale ; expérience C0 |
| Distinction entre forme reproduite et mécanisme | Décomposition par instance ; prudence sur la suffisance générative |
| Réflexivité | Le concepteur traité comme une instance ; carnet de conception |
| Fiabilité | Préenregistrement, fiabilité intra-codeur, deux modèles juges indépendants, codages publiés, puissance, répétitions |
| Prudence interprétative | Aucune généralisation aux humains ; vocabulaire des cadres d'énonciation |
| Transparence | Code, consignes, livres de codes, fiches, archives publiés selon le plan de gestion des données |

**Limites assumées**
- **Le risque de dilution** : affirmer que tout est agencement n'explique rien. La co-agentivité n'a de valeur que par la décomposition expérimentale des parts ; une part qui ne peut être isolée est déclarée comme telle.
- **L'agentivité n'est pas l'intentionnalité** : dire qu'une instance « agit » signifie qu'elle fait une différence mesurable, non qu'elle veut quelque chose.
- Les références humaines viennent de dispositifs différents ; seules certaines sont reproductibles procéduralement.
- Les modèles évoluent : les résultats valent pour des versions datées.
- Le codage automatique ajoute une instance à l'analyse elle-même ; d'où la séparation des modèles et la validation humaine.

---

## 8. Valorisation envisageable

**Revues de SIC** : *Communication & langages*, *Questions de communication*, *Les Enjeux de l'information et de la communication*, *Hermès*, *Réseaux*, *tic&société*, *Revue française des sciences de l'information et de la communication*.

**Simulation et méthodes** : *Journal of Artificial Societies and Social Simulation*.

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
- Jeanneret, Y., & Souchier, E. (1999). Pour une poétique de l'écrit d'écran. *Xoana*, 6-7, 97-107.
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
- Noelle-Neumann, E. (1974). The spiral of silence: A theory of public opinion. *Journal of Communication*, 24(2), 43-51.
- Noelle-Neumann, E. (1993). *The Spiral of Silence: Public Opinion, Our Social Skin* (2e éd.). Chicago : University of Chicago Press.
- OpenAI (2025). *Model Spec*. Spécification publique du comportement attendu des modèles.
- Panickssery, A., Bowman, S. R., & Feng, S. (2024). LLM Evaluators Recognize and Favor Their Own Generations. *Advances in Neural Information Processing Systems 37 (NeurIPS 2024)*.
- Park, J. S., O'Brien, J., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative Agents: Interactive Simulacra of Human Behavior. *Proceedings of UIST '23*.
- Varenne, F. (2007). *Du modèle à la simulation informatique*. Paris : Vrin.
- Varenne, F. (2018). *From Models to Simulations*. Londres : Routledge.
- Vezhnevets, A. S., et al. (2023). Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia. *arXiv:2312.03664*.
- Wang, A., Morgenstern, J., & Dickerson, J. P. (2025). Large language models that replace human participants can harmfully misportray and flatten identity groups. *Nature Machine Intelligence*.
- Zhao, P., Pham, D. H., & Vincent, N. (2026). Mechanism Plausibility in Generative Agent-Based Modeling. *Proceedings of ACM FAccT '26*. *arXiv:2605.12824*.

*Références à vérifier une à une (pagination, éditions) avant toute publication. La version publiée de Larooij et Törnberg (2025) n'a pas pu être consultée ; référence établie d'après la version arXiv.*
