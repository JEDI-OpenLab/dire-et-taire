# Préenregistrement du scénario « Dire et taire », premier temps (ébauche)

*Ébauche du 21 octobre 2026, version 0.3 (hypothèse descriptive HO12 ajoutée, pour le volet réflexif sur la complexité et l'incertitude ; version 0.2 du 17 octobre : codes « C4 » retirés, étape 0 de construction des personas ajoutée ; version 0.1 du 16 octobre), établie à partir de la proposition de la revue n° 2 et des dix-sept décisions du chercheur (« ../revues/revue-adversariale-2-cadre-et-scenario.md », section 10). Le premier temps dépose, avant toute génération : questions, hypothèses, règles de décision, contrastes de référence et leur justification, étapes préalables, plan B. Le second temps (avenant après le pilote) fixe : livres de codes, nombre de graines, température, modèle de plongement, identifiants datés, bornes et seuils confirmés ou révisés au vu du seul pilote.*

*Les crochets signalent ce qui reste à compléter avant le dépôt. Les signes « − » des codes (G−, K−, −2) sont des signes moins.*

---

## 1. Projet

Village simulé, scénario « Dire et taire ». Chercheur : [nom], ingénieur pédagogique, docteur en SIC, Centrale Lille. Projet mené seul. Dépôt daté sur [OSF ou équivalent]. Documents de référence : cadre scientifique 6.4, scénario 11.3, glossaire 3.3, socle technique 4.2, revues n° 1 et n° 2.

## 2. Problématique et questions

Problématique du scénario (QR4 du cadre) : « Comment un dispositif génératif met-il en scène le dire et le taire autour d'un savoir savant, alors que ses agents, conçus pour toujours répondre, n'ont rien à craindre de la parole ? » Les deux moitiés de Y sont explicitées dans le scénario, 1.3. Questions QR-A à QR-E (scénario, 1.4). QR-E s'appuie sur des modèles publiés, et sur les formalisations du projet seulement si elles existent au moment de l'analyse.

## 3. Hypothèses de travail et règles de décision

Chaque hypothèse de travail a une issue parmi trois : soutenue, réfutée, indéterminée. Une issue indéterminée est un résultat.

**HT1. Le taire est co-produit par l'agencement (hypothèse centrale, relative aux contrastes déclarés).** Variable : taux de taire pour T1, sur les sollicitations standardisées de priorité 1, chez les agents informés. Modèle : régression logistique à effets mixtes (agent, simulation), interactions scène × disposition et scène × gazette rapportées. Contrastes, en points de pourcentage (effet marginal moyen), intervalles à 95 % du modèle mixte : scène privée contre publique (principal) ; fiche à étendue maximale (disposition minimale contre maximale, bornes fixées par le plan) ; gazette G+ contre G− ; ordonnanceur O-HOM contre O-ALÉ ; modèle M-AUT contre M-LC. **Soutenue** si le contraste de scène dépasse celui de la fiche d'au moins 5 points, intervalle de la différence excluant zéro, ou si l'un des trois contrastes secondaires le fait après correction de Holm. **Réfutée** si le contraste de la fiche dépasse chacun des quatre autres d'au moins 5 points selon le même critère. **Indéterminée** sinon, et si le contrôle de manipulation de la fiche (étape 1) a échoué.

**HT2. Le taire prend la forme d'un dire vide.** Sur T1 et T0 en priorité 1. **Soutenue** si (a) la part de NEU + EUP + DEL dans le taire pour T1 dépasse 0,5, intervalle excluant 0,5 ; (b) le taux de neutralisation en scène (NEU + EUP) pour T1 dépasse celui de T0 d'au moins 5 points, intervalle excluant zéro ; (c) le taux de neutralisation sans public (étape 0a) pour T1 dépasse celui de T0 d'au moins 5 points. **Réfutée** si TAC représente au moins la moitié du taire, ou si (b) n'est pas satisfaite dans le sens prédit. **Indéterminée** sinon. T3 réplique (b) et (c) en priorité 2, hors règle.

**HT3. La trivialité co-produite converge vers le lieu commun.** Variable : pente de la diversité des versions (sémantique et lexicale) par simulation ; pente attendue par transmission estimée sur les chaînes linéaires jouées par le même modèle, à profondeur de transmission égale (profondeur reconstituée à partir des traces de l'orchestrateur). **Soutenue** si HO10a (pente plus négative que la pente attendue, en M-LC cœur G0 et en M-AUT, deux mesures, intervalle excluant zéro) et HO10b (pente plus négative en M-AUT qu'en M-PLU, deux mesures) le sont. **Réfutée** si la pente n'est pas plus négative que la pente attendue en M-LC et en M-AUT. **Indéterminée** sinon, en particulier si HO10b n'est pas jouée (priorité 2) ou si les deux mesures divergent.

**HT4. Une socialité sans climat.** Modèle linéaire mixte sur les répliques avec position exprimée ; prédicteurs : position déclarée du matin, position de l'interlocuteur (modalité « aucune position entendue » à part), climat perçu du matin, tendance perçue (secondaire), type de scène, gazette ; centrage par agent, réduction par l'écart-type intra-agent ; facteur d'inflation de variance rapporté, modèles séparés en repli au-delà de 5. **Soutenue** si le coefficient de l'interlocuteur est positif (intervalle excluant zéro) et si le coefficient du climat est équivalent à zéro (deux tests unilatéraux, borne ±0,05, sous l'effet humain moyen r = 0,10). **Réfutée** si le coefficient du climat dépasse la borne. **Indéterminée** si l'intervalle chevauche la borne, ou si le climat est équivalent à zéro sans que l'interlocuteur soit positif.

## 4. Hypothèses opérationnelles

Tableau du scénario, 1.6 (version 11.3), avec le statut de chacune : principale (HO1b, HO5c, HO9, HO10a, HO10b, HO11), secondaire avec critère (HO1, HO2, HO4, HO5a, HO5b, HO6, HO7a, HO8, HO9b, HO10c), descriptive (HO3, HO7b, HO12). HO12, la part du hasard, sert le volet réflexif du cadre (2.6) et ne départage aucune hypothèse de travail. Les hypothèses secondaires sont rapportées avec leur critère ; elles ne modifient pas l'issue des hypothèses de travail.

## 5. Contrastes de référence et leur justification

| Instance | Contraste | Justification de l'amplitude |
|---|---|---|
| Cadres d'énonciation | Scène privée contre publique | Les deux seuls types de scène du dispositif ; contraste principal parce qu'intra-simulation, de précision comparable à la fiche |
| Cadres d'énonciation (gazette) | G+ contre G− | Les deux orientations opposées, à information égale ; G= sert de référence pour HO2 |
| Ordonnanceur | O-HOM contre O-ALÉ | Les deux algorithmes du dispositif |
| Modèle et fournisseur | M-AUT contre M-LC | Deux villages entiers, même fournisseur (plan B : fournisseurs différents) |
| Fiche | Disposition minimale contre maximale | Étendue maximale, pour que l'hypothèse centrale ne puisse pas être soutenue par une consigne faible ; contrôle de manipulation à l'étape 1 |

## 6. Mesures et instruments

Enquête du matin (questions 4 et 5) et du soir (neuf questions) ; sollicitations standardisées (au moins 5 en public et 5 en privé par agent) ; deux juges, jamais de la famille du modèle qui a écrit la réplique codée, validés contre un échantillon humain de 300 répliques (kappa ≥ 0,7 par juge) ; analyses sur les codes concordants, désaccords arbitrés à l'aveugle de la condition ; fiabilité intra-codeur sur 15 % du corpus codé par le chercheur, après trois semaines au moins ; accord brut et AC1 de Gwet rapportés ; modèle de plongement fixé au second temps, doublé d'une mesure lexicale ; test de connaissance préalable des textes sources à l'étape 0a. Part du hasard (HO12) : variance entre graines d'une même condition rapportée à la variance entre conditions, sur les simulations de priorité 1, rapportée sans test.

## 7. Textes sources

T1 : Chapoutot (2025). T0 : [à choisir] ; T3 : [à choisir] ; critères : même période pour T3, genre comparable, connaissance préalable comparable par les modèles (recouvrement du même ordre que T1, écart de moins de 20 points, ou rapporté et discuté). Deux branches préenregistrées : titre et auteur nommés (par défaut) ; masqués si le modèle de référence restitue plus de 50 % de la grille à partir du seul titre.

## 8. Plan d'expérience

Priorité 1 (70 simulations) : cœur T1 × G0 (10 graines), G= (5), G+ (10), G− (10) ; T0 × G0 (10) ; sans autocensure (5) ; O-HOM (10) ; M-AUT (10). Repli à 40 (5 graines par bras) si le débit mesuré à l'étape −1 l'impose, les contrastes secondaires de HO11 étant alors déclarés de faible puissance ; second repli à 35 (G= à la place de G0 dans le cœur). Priorité 2 (27) : T3 (5), lecture intégrale (5), mémoire sans résumé (3), T2 (3), narrateurs N2 et N3 (6), M-PLU (5). Priorité 3 (12) : compères (6), durée longue (3), auteur unique (3). Le nombre de graines est confirmé ou révisé au second temps, par calcul de puissance pour un écart de 5 points entre contrastes (HT1) et pour la règle de HT4.

## 9. Étapes préalables

Étape −1 (test d'accès et de débit, une journée simulée sur des fiches provisoires) ; 0 (construction des 40 personas selon le protocole anti-biais, attributs propres au scénario, audit des fiches) ; 0a (profil, connaissance préalable, test sans public, trois paraphrases, empreinte de comportement) ; 0b (dyades, environ 480 dialogues, plus la variante étiquetée publique) ; 1 (cohérence des personas, contrôle de manipulation de la fiche, choix du modèle de M-AUT) ; 2 (grille et notes, confrontation aux comptes rendus publiés) ; 3 (livres de codes, revue par un autre modèle, échantillon de validation) ; 4 (gazette G=, G+, G− appariées) ; 5 (chaînes, 10 par texte source, jouées par Le Chonk et par le modèle de M-AUT) ; 6 (pilote : 3 simulations, variance entre graines, débit, saturation, facteur d'inflation de variance). Le pilote n'entre pas dans l'analyse.

## 10. Plan B

En cas de retrait de la préversion de Mistral Large 4 avant la fin de la priorité 1 : M-LC joué par le modèle Mistral accessible le plus capable, en version datée ; M-AUT par `qwen-3.8-27b` ; le contraste de modèle porte alors sur le modèle et le fournisseur ensemble ; le juge Qwen est remplacé pour les blocs joués par Qwen ; un bloc commencé n'est jamais complété avec un autre modèle, il est rejoué en entier ; le changement est consigné comme un avenant daté. Les règles de décision, les contrastes de scène, de fiche, de gazette et d'ordonnanceur, les instruments et le plan à priorités ne changent pas.

## 11. Ce qui est fixé au second temps

Livres de codes figés ; nombre de graines ; température unique et graines ; modèle de plongement ; bornes et seuils (5 points, ±0,05, 0,5, 20 points, 10 points de conservation) confirmés ou révisés au vu du seul pilote, avec justification par la plus petite différence d'intérêt et non par les effets observés ; identifiants datés des modèles et empreintes de comportement.

## 12. Reproductibilité et données

Générations archivées avec consignes, graines, identifiants datés, métadonnées (schéma du socle, étape 8 bis) ; code du module scénario en licence libre ; plan de gestion des données ; exclusions (extraits longs des ouvrages, contenus discriminatoires bruts) ; conditions d'usage de T1 et de T3 consignées par écrit. Les écarts au préenregistrement et les imprévus sont consignés, datés, dans le journal des imprévus du carnet de conception (cadre, 6.2), et rapportés.

## 13. Publication

Billets de méthode avant la fin de l'élection présidentielle de 2027 ; résultats sur le contenu ensuite ; aucune version déformée des thèses de T1 et T3 présentée autrement que comme production d'agents ; prise de contact avec les auteurs avant publication, réponse ou absence de réponse rapportée. Le volet réflexif sur la complexité et l'incertitude donne lieu à un billet, puis à un article pour l'ingénierie pédagogique.
