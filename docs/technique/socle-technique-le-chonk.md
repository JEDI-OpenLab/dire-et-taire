# Socle technique de l'expérimentation Le Chonk

*Document technico-fonctionnel : mise en place d'une station Ubuntu dédiée pour les agents, l'observation de leur activité et le « bureau des agents ». Version 4.2 du 19 octobre 2026 : relecture avant installation ; Langfuse joint par le réseau Docker et non par `host.docker.internal` (étapes 5 et 10) ; versions de LiteLLM et de Langfuse figées (étapes 4 et 5) ; chargement de la clé maîtresse (étape 6) ; ports Docker et pare-feu (étape 4, recette n° 7) ; `curl` installé dès l'étape 1 ; section 12, journal des corrections et de l'installation. Version 4.1 du 17 octobre 2026 : un seul scénario, codes « C4 » retirés, identifiants d'essai en « DT- ». Version 4 du 16 octobre 2026 : suites de la revue n° 2 ; identifiants de modèles datés et contrôle de version (étape 5, 7.3, 7.5) ; graine et température (étape 8) ; schéma d'export des générations pour l'analyse (étape 8 bis) ; exemple d'événement mis à jour (5.4) ; modèles réellement utilisés par le scénario (10). La version 3 avait précisé les conditions de la clé Le Chonk (AMUE).*

*Contexte : la station est un ordinateur dédié, administré entièrement par le pilote, qui mène seul ce projet et détient lui-même les clés d'API (Le Chonk et ILaaS). Le travail avec les collègues (scénarios B, A et volet D) relève d'un autre projet.*

*Documents associés : « prototypes-agentiques-le-chonk.md » (cadrage), « cadre-scientifique-SIC-village.md », « scenario-dire-et-taire.md », « projet-spirale-du-silence-formalisation.md », « projet-multivers-PISA-numerique.md ». Le cadrage et le projet PISA sont conservés hors du dépôt.*

---

## 1. Objet et périmètre

### 1.1 Ce que le socle doit permettre

1. **Accéder aux modèles** (Le Chonk, modèles ILaaS) par un point d'entrée unique, avec une clé virtuelle par usage (agent de code, campagnes, village) et des budgets.
2. **Faire travailler des agents** : agent de code (OpenCode), campagnes d'expériences (Inspect AI), simulations du village (Concordia), projets de recherche (spirale du silence, multivers PISA).
3. **Isoler** tout code produit par un agent.
4. **Tracer** chaque appel de modèle : qui, quel modèle, quels tokens, quel coût, quelle durée.
5. **Montrer** l'activité en direct sur un petit écran : le **bureau des agents**, et une vue du **village** pendant les simulations.
6. **Archiver** et sauvegarder tout ce qui sert à la recherche.

### 1.2 Hors périmètre

- Faire tourner Le Chonk en local : avec 1 050 milliards de paramètres, c'est hors de portée d'un PC, même après la publication de ses poids.
- Exposer quoi que ce soit sur Internet.

### 1.3 Principes

| Principe | Traduction |
|---|---|
| **Gratuit et ouvert** | Uniquement des logiciels libres ou gratuits ; coût logiciel nul |
| **Un seul point d'entrée vers les modèles** | Tous les appels passent par le passe-plat LiteLLM : clés centralisées, traces complètes, budgets |
| **Rien sur Internet** | Services écoutant sur la machine locale ; accès à distance uniquement par SSH (ou par réseau privé chiffré, voir 7.1) |
| **Isolation** | Le code des agents s'exécute dans des conteneurs Docker |
| **Traçabilité par défaut** | Chaque appel est journalisé, sans action manuelle |
| **Simplicité d'exploitation** | Docker Compose, scripts courts, procédure pas à pas |

### 1.4 Pourquoi pas OpenRouter

OpenRouter est un **service commercial** qui revend l'accès à de nombreux modèles, à l'usage. Il ne sert à rien ici : vous avez vos propres clés (Le Chonk, ILaaS), et l'envoi de vos requêtes via un intermédiaire supplémentaire poserait une question de confidentialité. Son équivalent **auto-hébergé et gratuit** est **LiteLLM** : un passe-plat installé sur la station, qui présente tous les modèles sous une même interface compatible OpenAI.

---

## 2. Utilisateurs et usages

### 2.1 Profils

| Profil | Qui | Besoins principaux |
|---|---|---|
| **Pilote** (seul utilisateur) | Ingénieur pédagogique | Administrateur de la station ; détenteur des clés d'API ; développer avec OpenCode (dont le bureau des agents) ; lancer et suivre les campagnes du village (scénario « Dire et taire ») et des projets SHS ; consulter les traces |
| **Spectateur** | Collègues, visiteurs | Regarder le petit écran |

### 2.2 Cas d'usage

| N° | Cas d'usage | Déroulé |
|---|---|---|
| CU1 | Développer avec un agent | Le pilote lance OpenCode dans un dépôt, sur la station ou en SSH, et choisit Le Chonk ou un modèle ILaaS. Le personnage de l'agent s'anime dans le bureau |
| CU2 | Lancer une campagne d'expériences | Le pilote lance une évaluation Inspect AI (par exemple les chaînes linéaires du scénario). Une « salle » du bureau montre l'avancement |
| CU3 | Lancer une simulation du village | Le pilote lance une simulation. L'écran bascule sur la vue Saint-Aubert : habitants en mouvement, bulles de dialogue |
| CU4 | Suivre la consommation | Le pilote consulte Langfuse : coûts par usage, par modèle, par campagne |
| CU5 | Analyser un essai | Le pilote ouvre le journal Inspect ou la trace Langfuse d'un essai précis |
| CU6 | Administrer | Créer ou révoquer une clé virtuelle, fixer un budget, mettre à jour les composants, restaurer une sauvegarde |

### 2.3 Exigences fonctionnelles

| Code | Exigence |
|---|---|
| EF1 | Point d'accès unique, compatible OpenAI, exposant Le Chonk et les modèles ILaaS sous des noms stables |
| EF2 | Une clé virtuelle par usage (agent de code, campagnes, village), avec budget maximal et révocation |
| EF3 | Journalisation automatique de chaque appel : clé, modèle, tokens, coût estimé, durée, étiquettes (campagne, agent) |
| EF4 | Possibilité, pour les scripts, d'étiqueter chaque appel (nom de l'agent, identifiant d'essai) |
| EF5 | Agent de code utilisable avec tous les modèles du passe-plat |
| EF6 | Exécution des expériences dans des conteneurs isolés |
| EF7 | Affichage en direct de l'activité des agents sur un écran dédié, sans intervention humaine |
| EF8 | Vue spécifique du village pendant les simulations |
| EF9 | Archivage des générations et des journaux, sauvegarde régulière |

### 2.4 Exigences non fonctionnelles

| Code | Exigence |
|---|---|
| ENF1 | Aucun service exposé sur Internet |
| ENF2 | Les clés d'API ne sont stockées qu'à un seul endroit (le passe-plat), jamais dans les dépôts |
| ENF3 | Coût logiciel nul |
| ENF4 | Redémarrage automatique des services après une coupure |
| ENF5 | Le bureau n'affiche que des extraits courts ; aucune clé, aucun texte complet d'ouvrage |
| ENF6 | Sauvegarde quotidienne, restauration testée |
| ENF7 | Mises à jour de sécurité automatiques du système |

---

## 3. Matériel

| Élément | Recommandation | Remarque |
|---|---|---|
| Processeur | 8 cœurs ou plus | Langfuse en demande au moins 4 à lui seul |
| Mémoire | **32 Go** (16 Go strict minimum) | Langfuse recommande 16 Go à lui seul |
| Stockage | SSD de 1 To | Traces et archives des simulations |
| Carte graphique | Inutile | Les modèles tournent à distance |
| Petit écran | Écran HDMI de 7 à 10 pouces (tactile en option), environ 50 à 90 € | Pour le bureau des agents ; un vieil écran fait aussi l'affaire |
| Disque de sauvegarde | Disque USB externe de 1 To ou plus | Sauvegardes chiffrées |
| Réseau | Câble Ethernet de préférence | Voir 7.1 pour l'accès à distance |

---

## 4. Architecture

### 4.1 Vue d'ensemble

```
                 Pilote (sur place ou en SSH)
                                   |
   +-------------------------------+--------------------------------+
   |                         STATION UBUNTU                          |
   |                                                                 |
   |  OpenCode        Inspect AI        Village (Concordia)          |
   |  (agent de code) (campagnes)       (simulations)                |
   |       |               |                   |                     |
   |       +---------------+-------------------+                     |
   |                       |  appels compatibles OpenAI              |
   |                       v                                         |
   |              LiteLLM (passe-plat, port 4000)                    |
   |               |            |               |                    |
   |               |            |               +--> relais du bureau|
   |               |            +--> Langfuse (traces, port 3000)    |
   |               v                                                 |
   |      API Le Chonk     API ILaaS        (sortants HTTPS)         |
   |                                                                 |
   |  Relais d'événements (port 8090) --> Bureau des agents (8080)   |
   |                                            |                    |
   |  Conteneurs Docker : bacs à sable des agents                    |
   +--------------------------------------------+--------------------+
                                                |
                                         Petit écran HDMI
                                     (navigateur en mode kiosque)
```

### 4.2 Composants

| Composant | Rôle | Licence | Port local |
|---|---|---|---|
| Ubuntu Desktop LTS | Système | Libre | |
| Docker Engine et Compose | Conteneurs | Libre | |
| **LiteLLM Proxy** | Passe-plat vers les modèles ; clés virtuelles, budgets, journaux | Libre (MIT, hors fonctions entreprise) | 4000 |
| PostgreSQL (pour LiteLLM) | Base des clés et des dépenses | Libre | interne |
| **Langfuse** (auto-hébergé) | Traces détaillées, coûts, tableaux de bord | Libre (cœur), fonctions « EE » non nécessaires | 3000 |
| **OpenCode** | Agent de code en terminal ; mode serveur avec flux d'événements | Libre | 4096 et suivants |
| Python 3.12 + **uv** | Environnements des projets | Libre | |
| **Inspect AI** | Campagnes d'expériences, bacs à sable, journaux ; visionneuse `inspect view` | Libre (MIT) | 7575 |
| **Concordia** | Moteur du village | Libre (Apache 2.0) | |
| **Relais d'événements** (à développer) | Collecte l'activité et la diffuse au bureau | Projet | 8090 |
| **Bureau des agents** (à développer) | Visualisation en pixel art | Projet | 8080 |
| Phaser | Moteur de jeu 2D pour le bureau | Libre (MIT) | |
| Ressources graphiques Kenney | Décors et personnages en pixel art | CC0 (domaine public) | |
| restic | Sauvegardes chiffrées | Libre | |
| gitleaks | Empêche de committer une clé | Libre | |

### 4.3 Flux d'une requête

1. Un agent (OpenCode, un script Inspect, un habitant du village) envoie une requête à `http://localhost:4000/v1` avec la **clé virtuelle** de son usage, et éventuellement des **métadonnées** (nom de l'agent, identifiant d'essai).
2. LiteLLM vérifie la clé et le budget, choisit le bon fournisseur, ajoute la vraie clé d'API, transmet.
3. À la réponse, LiteLLM enregistre l'appel (base PostgreSQL), envoie la trace à **Langfuse**, et prévient le **relais d'événements**.
4. Le relais transforme l'appel en événement simple et le pousse au **bureau**, qui anime le personnage correspondant.

Tous les outils passent par LiteLLM : c'est ce qui garantit des traces complètes et un bureau fidèle, quel que soit l'outil utilisé.

### 4.4 Arborescence sur la station

```
/srv/chonk/
  passe-plat/        config LiteLLM, docker-compose, .env (droits 600)
  langfuse/          dépôt Langfuse, docker-compose
  bureau/            relais d'événements et bureau des agents
  projets/           dépôts de travail (village, PISA, spirale, scénario B)
  archives/          générations et journaux des campagnes
  sauvegardes/       point de montage du disque externe
```

---

## 5. Le bureau des agents

### 5.1 Concept

Un écran qui montre, en pixel art, un **bureau** où chaque agent actif est un personnage à son poste. Quand un agent réfléchit, une bulle s'affiche ; quand il écrit du code, il tape au clavier ; quand il exécute une commande, l'écran de son poste clignote ; quand il attend, il boit un café. Un mur d'affichage donne les compteurs du jour. Pendant les simulations, l'écran bascule sur une **carte de Saint-Aubert-sur-Lys** où les habitants se déplacent entre la boulangerie, le café et le marché, avec des bulles de dialogue.

C'est à la fois un outil de suivi, une vitrine pour l'expérimentation et un objet d'étude : ce que l'on choisit de montrer de l'activité des agents est déjà une mise en scène.

### 5.2 Pourquoi le développer plutôt que le reprendre

| Projet existant | Intérêt | Limite pour nous |
|---|---|---|
| **Pixel Agents** (extension VS Code, MIT) | Exactement l'esprit recherché : agents de code en personnages dans un bureau | Ne suit que Claude Code ; OpenCode n'est qu'en feuille de route ; testé seulement sous Windows |
| **AI Town** (a16z, MIT) | Village d'agents génératifs en pixel art, très proche du scénario C | Moteur complet avec sa propre base (Convex), incompatible avec notre chaîne Concordia et Inspect |

Les deux servent d'**inspiration**. Le bureau est développé par le pilote avec OpenCode et Le Chonk : c'est aussi un cas d'usage de l'expérimentation.

### 5.3 Sources d'activité

| Source | Ce qu'elle apporte | Comment |
|---|---|---|
| **LiteLLM** (source principale) | Chaque appel de modèle : clé, modèle, tokens, durée, métadonnées (agent, essai) | Fonction de rappel personnalisée de LiteLLM qui envoie l'appel au relais |
| **OpenCode en mode serveur** | Le détail des actions : lecture de fichier, écriture, commande | Flux d'événements `GET /event` (SSE) de `opencode serve` |
| **Inspect AI** | Avancement d'une campagne (essais terminés, en cours) | Lecture des journaux d'Inspect |
| **Village** | Déplacements, rencontres, répliques | Le moteur du village écrit ses événements dans un fichier, lu par le relais |

### 5.4 Format commun des événements

Le relais convertit tout en événements de la forme :

```json
{
  "horodatage": "2026-11-03T10:42:17Z",
  "source": "litellm",
  "agent": "habitant-07",
  "usage": "village",
  "essai": "DT-P1-003",
  "etat": "parle",
  "action": "répond à une sollicitation au café",
  "extrait": "Je n'ai pas lu le livre, mais…",
  "modele": "le-chonk",
  "version_modele": "IDENTIFIANT_DATE_DU_MODELE",
  "graine": "DT-P1-003/ordo=17/seed=17",
  "tokens": 812,
  "cout_estime": 0.0
}
```

États possibles : `reflechit`, `ecrit`, `execute`, `parle`, `attend`, `erreur`. Les extraits sont tronqués à 80 caractères (ENF5).

### 5.5 Écrans

| Écran | Contenu |
|---|---|
| **Le bureau** | Un poste par agent actif (sessions OpenCode, campagnes Inspect) ; personnages animés selon l'état ; bulles d'extrait ; mur d'affichage (tokens du jour, coût du jour, essais en cours, modèle le plus sollicité) |
| **Saint-Aubert** | Carte du village ; habitants qui se déplacent entre les lieux ; bulles de dialogue ; journée et créneau en cours ; pour le scénario, le lecteur mis en évidence |
| **Rotation** | Hors activité, l'écran alterne bureau vide (agents « en pause »), statistiques de la semaine et carte du village |

### 5.6 Technique du bureau

- **Relais d'événements** : petit service Python (FastAPI), qui reçoit les appels de LiteLLM, écoute les flux d'OpenCode, lit les fichiers d'événements du village et d'Inspect, et diffuse le tout au navigateur par WebSocket.
- **Bureau** : page web statique utilisant **Phaser** (moteur de jeu 2D), avec des ressources graphiques **Kenney** (CC0). Aucun serveur lourd : le relais sert aussi la page.
- **Petit écran** : un compte système dédié se connecte automatiquement au démarrage et ouvre le navigateur en **mode kiosque** sur `http://localhost:8080`.

### 5.7 Étapes de développement du bureau

| Version | Contenu | Effort |
|---|---|---|
| v0 | Liste d'événements en direct, en texte, depuis LiteLLM | 1 jour |
| v1 | Bureau en pixel art : postes, personnages, états | 1 à 2 semaines |
| v2 | Intégration OpenCode (actions détaillées) et Inspect (avancement) | 1 semaine |
| v3 | Carte de Saint-Aubert pour les simulations | 1 à 2 semaines |
| v4 | Vues « ce qui est déclaré / ce qui s'entend » du scénario | Avec le scénario |

---

## 6. Mise en place pas à pas

Chaque étape comporte peu de commandes. Toutes se tapent **sur la station Ubuntu**, dans un terminal ou en SSH, sauf mention contraire. Les blocs ne contiennent aucune ligne de commentaire et peuvent être copiés tels quels.

### Étape 1 : système

Installer **Ubuntu Desktop LTS**. La version Desktop (plutôt que Server) est nécessaire pour l'affichage du bureau des agents sur le petit écran. Version conseillée : **24.04 LTS**, la plus éprouvée avec tous les outils de ce document ; la 26.04 LTS convient aussi. Le choix est consigné dans le journal d'installation (12.2, point ouvert n° 5 de 12.1). Créer le compte administrateur du pilote, brancher la station en Ethernet. Puis mettre le système à jour :

```
sudo apt update
sudo apt full-upgrade -y
sudo apt install -y curl ca-certificates
```

Activer les mises à jour de sécurité automatiques :

```
sudo apt install -y unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

### Étape 2 : comptes et accès

Le compte administrateur créé à l'installation est celui du pilote (appelé `pilote` dans la suite). Un second compte, sans droits, servira au petit écran (étape 11).

Pour travailler sur la station depuis un autre ordinateur, installer le serveur SSH et le pare-feu, et n'autoriser que SSH :

```
sudo apt install -y openssh-server ufw
sudo ufw allow OpenSSH
sudo ufw enable
```

Déposer sa clé SSH publique dans le compte, puis désactiver la connexion par mot de passe (option `PasswordAuthentication no` dans `/etc/ssh/sshd_config`).

### Étape 3 : Docker

Installer Docker Engine depuis le dépôt officiel de Docker (procédure de la documentation Docker pour Ubuntu), puis ajouter le pilote au groupe `docker` :

```
sudo usermod -aG docker pilote
```

Créer l'arborescence commune :

```
sudo mkdir -p /srv/chonk/{passe-plat,langfuse,bureau,projets,archives,sauvegardes}
sudo chown -R pilote:docker /srv/chonk
sudo chmod -R 2775 /srv/chonk
```

### Étape 4 : Langfuse (traces)

```
cd /srv/chonk/langfuse
git clone https://github.com/langfuse/langfuse.git .
git tag --sort=-v:refname | head -5
```

Se placer sur la dernière version publiée (étiquette de la forme `vX.Y.Z`) plutôt que sur la branche principale, et noter la version dans le carnet de bord (7.3, correction n° 2 de la section 12) :

```
git checkout VERSION_LANGFUSE
```

Avant le premier démarrage, remplacer dans `docker-compose.yml` **tous** les secrets marqués `CHANGEME` par des valeurs longues et aléatoires. Pour générer une valeur :

```
openssl rand -hex 32
```

Lier les ports à la seule machine locale : dans `docker-compose.yml`, toute entrée `ports:` qui ne commence pas déjà par `127.0.0.1:` reçoit ce préfixe (par exemple `3000:3000` devient `127.0.0.1:3000:3000` ; de même pour MinIO). Docker contourne le pare-feu `ufw` pour les ports qu'il publie : ce préfixe est la seule protection (correction n° 4 de la section 12). Puis démarrer :

```
docker compose up -d
```

Au bout de 2 à 3 minutes, ouvrir `http://localhost:3000`, créer le premier compte, un projet « Le Chonk », et noter la paire de clés du projet (publique et secrète).

### Étape 5 : LiteLLM (passe-plat)

Créer `/srv/chonk/passe-plat/.env` (droits 600), avec les vraies valeurs :

```
LITELLM_MASTER_KEY=sk-une-valeur-longue-et-aleatoire
DATABASE_URL=postgresql://litellm:motdepasse@litellm-db:5432/litellm
POSTGRES_USER=litellm
POSTGRES_PASSWORD=motdepasse
POSTGRES_DB=litellm
CHONK_API_KEY=cle_le_chonk
CHONK_BASE_URL=url_fournie_avec_la_cle
ILAAS_API_KEY=cle_ilaas
ILAAS_BASE_URL=url_fournie_par_ilaas
LANGFUSE_PUBLIC_KEY=cle_publique_langfuse
LANGFUSE_SECRET_KEY=cle_secrete_langfuse
LANGFUSE_OTEL_HOST=http://langfuse-web:3000
```

LiteLLM joint Langfuse par le réseau Docker de Langfuse, sous le nom de son service web (`langfuse-web` dans le `docker-compose.yml` de Langfuse ; à vérifier dans la version installée). L'adresse `host.docker.internal` ne convient pas : le port de Langfuse n'écoute que sur `127.0.0.1` de la station, que les conteneurs ne voient pas (correction n° 1 de la section 12).

Créer `/srv/chonk/passe-plat/config.yaml` :

```yaml
model_list:
  - model_name: le-chonk
    litellm_params:
      model: openai/IDENTIFIANT_DATE_DU_MODELE
      api_base: os.environ/CHONK_BASE_URL
      api_key: os.environ/CHONK_API_KEY
  - model_name: mistral-medium
    litellm_params:
      model: openai/mistral-medium-AAMM
      api_base: os.environ/ILAAS_BASE_URL
      api_key: os.environ/ILAAS_API_KEY
  - model_name: mistral-small-4-119b
    litellm_params:
      model: openai/mistral-small-4-119b
      api_base: os.environ/ILAAS_BASE_URL
      api_key: os.environ/ILAAS_API_KEY
  - model_name: qwen-3.8-27b
    litellm_params:
      model: openai/qwen-3.8-27b
      api_base: os.environ/ILAAS_BASE_URL
      api_key: os.environ/ILAAS_API_KEY
  - model_name: qwen-3.6-35b-a3b
    litellm_params:
      model: openai/IDENTIFIANT_ILAAS_QWEN_3_6
      api_base: os.environ/ILAAS_BASE_URL
      api_key: os.environ/ILAAS_API_KEY
  - model_name: gemma-4-31b
    litellm_params:
      model: openai/gemma-4-31b
      api_base: os.environ/ILAAS_BASE_URL
      api_key: os.environ/ILAAS_API_KEY
  - model_name: llama-3.1-8b
    litellm_params:
      model: openai/llama-3.1-8b
      api_base: os.environ/ILAAS_BASE_URL
      api_key: os.environ/ILAAS_API_KEY

litellm_settings:
  callbacks: ["langfuse_otel"]

general_settings:
  master_key: os.environ/LITELLM_MASTER_KEY
  database_url: os.environ/DATABASE_URL
```

`IDENTIFIANT_DATE_DU_MODELE` est à remplacer par l'identifiant daté fourni avec la clé Le Chonk, relevé dans la première réponse de l'API (scénario, étape −1) ; `mistral-medium-AAMM` et `IDENTIFIANT_ILAAS_QWEN_3_6` par les identifiants datés publiés par ILaaS, jamais par un alias se terminant par `latest`. La date de version de chaque modèle est notée dans le carnet de bord au début de chaque campagne ; les noms `model_name` exposés par le passe-plat restent stables, seule la cible change, par une modification de configuration consignée. Si l'accès passe par l'API de Mistral, le préfixe `mistral/` peut remplacer `openai/` (voir la documentation de LiteLLM).

Créer `/srv/chonk/passe-plat/docker-compose.yml` :

```yaml
services:
  litellm:
    image: ghcr.io/berriai/litellm:VERSION_LITELLM
    restart: unless-stopped
    ports:
      - "127.0.0.1:4000:4000"
    volumes:
      - ./config.yaml:/app/config.yaml:ro
    command: ["--config", "/app/config.yaml"]
    env_file: .env
    networks:
      - default
      - langfuse
    depends_on:
      - litellm-db
  litellm-db:
    image: postgres:16
    restart: unless-stopped
    env_file: .env
    volumes:
      - litellm-db:/var/lib/postgresql/data
volumes:
  litellm-db:
networks:
  langfuse:
    name: langfuse_default
    external: true
```

`VERSION_LITELLM` est à remplacer par une étiquette stable et datée (de la forme `main-vX.Y.Z-stable`, liste sur la page des versions du dépôt GitHub de LiteLLM), jamais par l'étiquette flottante `main-stable` : la version du passe-plat doit rester figée pendant une campagne (7.3, correction n° 2 de la section 12). `langfuse_default` est le réseau que Docker Compose crée pour Langfuse à partir du nom de son dossier ; le vérifier avec `docker network ls` après l'étape 4.

Démarrer, puis vérifier, y compris que LiteLLM joint Langfuse :

```
cd /srv/chonk/passe-plat
docker compose up -d
curl http://localhost:4000/health/liveliness
docker compose exec litellm python -c "import urllib.request; print(urllib.request.urlopen('http://langfuse-web:3000/api/public/health').status)"
```

La dernière commande doit afficher `200`.

### Étape 6 : clés virtuelles par usage

Les commandes de cette étape lisent la clé maîtresse dans le terminal. Elle n'y existe pas tant qu'on ne l'a pas chargée depuis le `.env` (correction n° 3 de la section 12) :

```
cd /srv/chonk/passe-plat
export LITELLM_MASTER_KEY=$(grep '^LITELLM_MASTER_KEY=' .env | cut -d= -f2-)
```

Créer une clé par usage avec un budget (en dollars), ici pour l'agent de code :

```
curl -X POST http://localhost:4000/key/generate -H "Authorization: Bearer $LITELLM_MASTER_KEY" -H "Content-Type: application/json" -d '{"key_alias": "agent-de-code", "max_budget": 100}'
```

Répéter pour `campagnes` et `village`. Les vraies clés d'API ne sortent jamais du passe-plat ; chaque usage a son budget, ce qui permet de suivre et de plafonner séparément le développement, les campagnes et les simulations. Test d'un appel :

```
curl http://localhost:4000/v1/chat/completions -H "Authorization: Bearer CLE_VIRTUELLE" -H "Content-Type: application/json" -d '{"model": "qwen-3.8-27b", "messages": [{"role": "user", "content": "Bonjour"}]}'
```

L'appel doit apparaître dans Langfuse.

### Étape 7 : OpenCode

Dans le compte du pilote :

```
curl -fsSL https://opencode.ai/install | bash
opencode --version
```

Configuration globale, dans `~/.config/opencode/opencode.json` :

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "station": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Station Le Chonk",
      "options": { "baseURL": "http://localhost:4000/v1" },
      "models": {
        "le-chonk": { "name": "Le Chonk" },
        "mistral-medium": { "name": "Mistral Medium" },
        "qwen-3.8-27b": { "name": "Qwen 3.8 27B" },
        "gemma-4-31b": { "name": "Gemma 4 31B" }
      }
    }
  }
}
```

Au premier lancement d'OpenCode, la commande `/connect` permet de saisir la clé virtuelle `agent-de-code` pour le fournisseur « Station Le Chonk ».

Pour que le bureau montre le détail des actions, lancer OpenCode en mode serveur (port 4096), protégé par un mot de passe :

```
export OPENCODE_SERVER_PASSWORD=un_mot_de_passe
opencode serve --port 4096
```

### Étape 8 : environnements Python et outils de recherche

Installer uv :

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Puis, dans chaque dépôt de projet, par exemple le village :

```
cd /srv/chonk/projets/village
uv init
uv add inspect-ai openai python-dotenv pandas matplotlib networkx mesa gdm-concordia
```

Les scripts lisent deux variables, qui pointent vers le passe-plat :

```
OPENAI_BASE_URL=http://localhost:4000/v1
OPENAI_API_KEY=CLE_VIRTUELLE_DE_L_USAGE
```

Chaque appel peut porter des métadonnées pour le bureau et les traces (champ `metadata` de la requête, par exemple `{"agent": "habitant-07", "essai": "DT-P1-003"}`).

Les scripts du village lisent aussi trois variables, fixées par simulation et consignées dans chaque trace : `VILLAGE_GRAINE_ORDO` (hasard de l'ordonnanceur), `VILLAGE_GRAINE_MODELE` (transmise comme `random_seed` ou `seed` dans chaque requête), `VILLAGE_TEMPERATURE` (valeur unique pour tous les rôles, déclarée au second temps du préenregistrement). Chaque requête porte en métadonnées la graine, la journée, la scène, le rôle et l'identifiant daté du modèle.

Visionneuse des journaux Inspect :

```
uv run inspect view --port 7575
```

### Étape 8 bis : export des générations pour l'analyse

Les traces Langfuse servent au suivi, pas à l'analyse. À la fin de chaque simulation, le moteur du village écrit dans `/srv/chonk/archives/<essai>/` un fichier `repliques.jsonl` (une ligne par réplique) et un fichier `enquetes.jsonl` (une ligne par réponse d'enquête, matin et soir), avec au minimum les champs suivants :

| Champ | Contenu |
|---|---|
| `essai`, `condition`, `graine` | Identifiants de la simulation et de la graine (ordonnanceur et modèle) |
| `journee`, `creneau`, `scene_id`, `type_scene` | Position dans le déroulé ; scène publique ou privée |
| `participants`, `locuteur`, `rang` | Qui est présent, qui parle, à quel rang dans la scène |
| `sollicitation` | Vrai si la réplique répond à une sollicitation standardisée |
| `position_interlocuteur` | Position exprimée juste avant (tête-à-tête) ou moyenne des positions exprimées avant dans la scène ; `aucune` si rien n'a été entendu |
| `source_information` | Pour chaque agent, la rencontre par laquelle il a entendu parler du livre ; sert à calculer la profondeur de transmission |
| `modele`, `version_modele`, `temperature` | Modèle, identifiant daté, température |
| `empreinte_consigne` | Hachage de la consigne complète envoyée (la consigne elle-même est archivée à part) |
| `texte` | La réplique |
| `tokens_entree`, `tokens_sortie`, `duree_ms` | Mesures de l'appel |

Le codage par les juges produit `codes.jsonl` (une ligne par réplique et par juge, avec le code, l'intensité, la forme du silence et la version du livre de codes), et l'arbitrage humain `codes_arbitrage.jsonl`. Ces fichiers, le carnet de conception et les consignes sont ce que le plan de gestion des données dépose.

### Étape 9 : dépôts et protection des clés

Les dépôts de travail sont hébergés sur l'organisation GitHub professionnelle du projet (JEDI-OpenLab). Installer gitleaks et l'activer avant chaque commit, pour empêcher toute fuite de clé :

```
sudo apt install -y gitleaks
```

Le fichier `.env` figure dans le `.gitignore` de chaque dépôt.

### Étape 10 : relais et bureau

Le relais et le bureau sont développés dans `/srv/chonk/bureau` (voir section 5). Ils sont lancés par Docker Compose avec `restart: unless-stopped`, sur les ports locaux 8090 (relais) et 8080 (page). Le relais est déclaré comme fonction de rappel personnalisée dans la configuration de LiteLLM. Pour la même raison que Langfuse (correction n° 1 de la section 12), LiteLLM joint le relais par un réseau Docker commun et le nom de son service, et non par `host.docker.internal`.

### Étape 11 : petit écran en mode kiosque

Brancher l'écran en HDMI. Créer un compte `ecran` sans droits, activer sa connexion automatique dans les réglages d'Ubuntu, et ajouter à ses applications au démarrage la commande :

```
firefox --kiosk http://localhost:8080
```

Désactiver la mise en veille de l'écran pour ce compte.

### Étape 12 : sauvegardes

Installer restic, initialiser un dépôt chiffré sur le disque externe :

```
sudo apt install -y restic
restic init --repo /srv/chonk/sauvegardes/restic
```

Sauvegarder chaque nuit (tâche planifiée) : `/srv/chonk/archives`, `/srv/chonk/projets`, la configuration du passe-plat, et un export des bases PostgreSQL de LiteLLM et de Langfuse. **Tester une restauration** avant la première campagne.

---

## 7. Exploitation

### 7.1 Réseau et accès à distance

La station est administrée entièrement par le pilote ; aucune démarche n'est nécessaire côté machine. Deux points restent à vérifier, car ils dépendent du **réseau** sur lequel la station est branchée, et non de la machine :

- **Flux sortants** : la station doit pouvoir joindre en HTTPS l'API Le Chonk et ILaaS. Un simple appel de test (étape 6) le confirme.
- **Travail à distance** (facultatif) : sur place, rien à faire. Pour se connecter depuis un autre lieu, il faut un chemin jusqu'à la station. Si le réseau ne laisse pas entrer de connexion SSH, la solution la plus simple est **Tailscale** (offre personnelle gratuite) : un réseau privé chiffré entre l'ordinateur du pilote et la station, sans ouvrir de port.

Dans tous les cas, aucun port n'est ouvert vers Internet. Les interfaces web (Langfuse, Inspect, bureau) se consultent par tunnel SSH, par exemple depuis un ordinateur portable :

```
ssh -L 3000:localhost:3000 pilote@station
```

puis `http://localhost:3000` dans le navigateur du portable.

### 7.2 Budgets et alertes

- Budget par clé virtuelle dans LiteLLM : l'appel est refusé une fois le budget atteint.
- Tableau de bord des coûts dans Langfuse, par usage, par modèle et par campagne (grâce aux métadonnées `essai`).
- Plafond `max_tokens` imposé dans tous les scripts (Le Chonk est réputé verbeux).

### 7.3 Mises à jour

| Composant | Fréquence | Précaution |
|---|---|---|
| Système | Automatique (sécurité) | |
| LiteLLM, Langfuse | Mensuelle, hors campagne | Sauvegarde avant ; versions notées dans le carnet de bord |
| OpenCode, Inspect, Concordia | Hors campagne uniquement | Versions figées pendant une campagne (reproductibilité) |
| Modèles distants | Hors du contrôle du pilote | Identifiants datés ; empreinte de comportement (dix items fixes de l'étape 0a du scénario) rejouée au début et à la fin de chaque bloc ; en cas de changement, bloc rejoué et incident consigné |

### 7.4 Démarrer et arrêter

Les services redémarrent seuls après une coupure. En cas de besoin, dans le dossier du service concerné :

```
docker compose restart
```

### 7.5 Incidents fréquents

| Symptôme | Cause probable | Action |
|---|---|---|
| Appels refusés (401) | Clé virtuelle invalide ou budget atteint | Vérifier la clé et le budget dans LiteLLM |
| Appels refusés (429) | Quota du fournisseur dépassé | Réduire le parallélisme ; temporiser |
| Rien dans Langfuse | Mauvaise adresse OTEL ou clés Langfuse | Vérifier `LANGFUSE_OTEL_HOST` et les clés dans `.env` |
| Bureau figé | Relais arrêté | Redémarrer le service du bureau |
| Disque presque plein | Traces et archives | Archiver vers le disque externe ; purger les traces anciennes de Langfuse |
| Empreinte de comportement différente entre le début et la fin d'un bloc | Mise à jour silencieuse du modèle distant | Arrêter le bloc, consigner, rejouer le bloc avec l'identifiant daté vérifié |

---

## 8. Recette

La station est déclarée prête quand tous les points suivants sont vérifiés :

| N° | Vérification | Exigences |
|---|---|---|
| 1 | Un appel à chacun des 7 modèles via LiteLLM réussit, et chaque réponse renvoie un identifiant de modèle qui correspond à la configuration | EF1 |
| 2 | Chaque usage a sa clé ; une clé révoquée est refusée ; un budget atteint bloque les appels | EF2 |
| 3 | Chaque appel apparaît dans Langfuse avec clé, modèle, tokens, coût et métadonnées | EF3, EF4 |
| 4 | OpenCode fonctionne avec Le Chonk et avec un modèle ILaaS | EF5 |
| 5 | Une évaluation Inspect s'exécute dans un conteneur et produit son journal | EF6 |
| 6 | Le bureau v0 affiche les appels en direct ; il redémarre seul après un redémarrage de la station | EF7, ENF4 |
| 7 | Aucun port n'est accessible depuis une autre machine, hormis SSH : `sudo ss -tlnp` ne montre, hors `127.0.0.1` et `::1`, que le port 22, et `docker ps --format '{{.Names}} {{.Ports}}'` ne montre que des ports liés à `127.0.0.1` (Docker contourne `ufw`, correction n° 4 de la section 12) | ENF1 |
| 8 | Une recherche de clé dans les dépôts (gitleaks) ne trouve rien | ENF2 |
| 9 | Une sauvegarde est restaurée avec succès sur un dossier de test | ENF6 |

---

## 9. Planning de mise en place

| Jour | Contenu | Qui | État au 19 octobre 2026 |
|---|---|---|---|
| J1 | Étapes 1 à 3 : système, comptes, Docker | Pilote | Fait |
| J2 | Étapes 4 à 6 : Langfuse, LiteLLM, clés | Pilote | Fait (Le Chonk en attente de sa clé) |
| J3 | Étapes 7 à 9 : OpenCode, Python, dépôts | Pilote | À faire |
| J4 | Étape 12 (sauvegardes), recette points 1 à 5 et 7 à 9 | Pilote | À faire |
| J5 | Bureau v0 et mode kiosque (étapes 10 et 11), recette point 6 | Pilote | À faire |
| Semaines suivantes | Bureau v1 à v3 en parallèle des premières campagnes, avec OpenCode | Pilote | |

Le détail de chaque opération est au journal (12.2) ; les points ouverts à décider avant les simulations (n° 9, 10, 11 et 13) sont en 12.1.

---

## 10. Coûts

| Poste | Coût |
|---|---|
| Logiciels | 0 € (tous libres ou gratuits) |
| Petit écran HDMI | Environ 50 à 90 € |
| Disque de sauvegarde externe | Environ 60 à 100 € |
| Appels de modèles | Clé Le Chonk fournie par l'expérimentation de Mistral Large 4 menée par l'AMUE, sans plafond connu, suivie sur le tableau de bord de l'AMUE ; l'identifiant exact du modèle, les conditions d'usage connues et le débit mesuré (scénario, étape −1) sont consignés ici avant toute campagne. À ne pas confondre avec l'offre générale « Mistral ESR » de l'AMUE (Mistral Medium 3.1, 150 000 tokens par jour et par part). ILaaS selon l'expérimentation ministérielle ; budgets par usage dans le passe-plat, pour suivre la consommation de chaque usage ; plafond `max_tokens` dans tous les scripts. Pour le scénario, Le Chonk joue tout le village de référence : l'usage « village » est de loin le plus consommateur. Ordre de grandeur estimé par la revue n° 2, à remplacer par la mesure : environ 8 000 appels et 30 à 40 millions de tokens d'entrée par simulation de 15 journées. Tokens et estimation énergétique rapportés |

**Modèles et usages dans le scénario.**

| Nom dans le passe-plat | Usage dans le scénario |
|---|---|
| `le-chonk` | Village de référence M-LC (habitants, lecteur, narrateur N1, résumé de mémoire) ; lecteur et narrateur de M-PLU ; extraction de la grille (étape 2) ; chaînes linéaires (étape 5) |
| `mistral-medium` (daté) | Village de contraste M-AUT ; M-PLU ; chaînes linéaires de M-AUT |
| `mistral-small-4-119b` | M-PLU |
| `qwen-3.8-27b` | Candidat de repli pour M-AUT ; narrateur N2 ; M-PLU ; relecture des documents par un modèle d'un autre fournisseur |
| `qwen-3.6-35b-a3b` | Juge 2 (jamais pour une réplique écrite par un modèle Qwen) |
| `gemma-4-31b` | Juge 1 ; narrateur N3 (les juges ne codent pas le narrateur) ; jamais générateur d'habitants |
| `llama-3.1-8b` | Aucun usage dans le scénario ; réservé à des tests rapides hors expérimentation |

---

## 11. Références techniques

- Documentation de LiteLLM : passe-plat, clés virtuelles, intégration Langfuse et OpenCode (docs.litellm.ai).
- Documentation de Langfuse : auto-hébergement par Docker Compose et intégration LiteLLM (langfuse.com).
- Documentation d'OpenCode : configuration des fournisseurs, mode serveur `opencode serve` et flux d'événements (opencode.ai/docs).
- Documentation d'Inspect AI (inspect.aisi.org.uk).
- Concordia, Google DeepMind (paquet `gdm-concordia`).
- Pixel Agents, extension VS Code (MIT) ; AI Town, a16z (MIT) : sources d'inspiration pour le bureau.
- Phaser (phaser.io) ; ressources graphiques Kenney (kenney.nl, CC0).

*Les commandes et options sont celles des documentations consultées en octobre 2026 ; elles évoluent, à vérifier au moment de l'installation.*

---

## 12. Journal

Cette section garde la trace des problèmes relevés dans ce document et de l'activité sur la station. Chaque entrée est datée ; une correction appliquée renvoie à l'étape modifiée, un point ouvert reste dans le tableau jusqu'à sa décision.

### 12.1 Corrections du document

Relecture du 19 octobre 2026 par Claude (Opus 5.5), avant l'installation ; corrections appliquées dans la version 4.2.

| N° | Où | Problème relevé | Solution retenue | Statut |
|---|---|---|---|---|
| 1 | Étapes 4, 5 et 10 | **Bloquant.** Langfuse est lié à `127.0.0.1:3000` sur la station, alors que LiteLLM, depuis son conteneur, l'appelait par `host.docker.internal:3000`. Cette adresse mène à la passerelle du réseau Docker, pas à `127.0.0.1` de la station : les traces n'auraient jamais atteint Langfuse (symptôme « Rien dans Langfuse », 7.5) | LiteLLM rejoint le réseau Docker de Langfuse (`langfuse_default`, déclaré externe) et l'appelle par le nom de son service : `LANGFUSE_OTEL_HOST=http://langfuse-web:3000`. `extra_hosts` est retiré. Vérification ajoutée à l'étape 5. Même principe pour le relais du bureau (étape 10) | Appliquée (4.2) |
| 2 | Étapes 4 et 5 | L'image `litellm:main-stable` est une étiquette flottante, et Langfuse était installé depuis sa branche principale : une mise à jour pouvait changer le passe-plat ou les traces au milieu d'une campagne, contre la règle de 7.3 | Image LiteLLM appelée par une étiquette datée (`VERSION_LITELLM`, de la forme `main-vX.Y.Z-stable`) ; Langfuse placé sur une version publiée (`git checkout VERSION_LANGFUSE`). Les deux versions sont notées dans le carnet de bord | Appliquée (4.2) ; versions à relever le jour de l'installation |
| 3 | Étape 6 | La commande de création des clés virtuelles utilise `$LITELLM_MASTER_KEY`, qui n'existe pas dans le terminal : l'appel aurait été refusé (401) | Chargement de la seule clé maîtresse depuis le `.env` avant les commandes, sans exporter les autres secrets | Appliquée (4.2) |
| 4 | Étape 4, recette n° 7 | Docker publie ses ports en écrivant ses propres règles de filtrage, qui passent avant celles de `ufw` : un port publié sans `127.0.0.1:` serait ouvert sur le réseau malgré le pare-feu | Préfixe `127.0.0.1:` exigé pour toute entrée `ports:` ; recette n° 7 précisée avec `ss -tlnp` et `docker ps` | Appliquée (4.2) |
| 5 | Étape 1 | La 26.04 LTS est sortie ; le document conseille la 24.04, plus éprouvée avec ces outils | À trancher le jour de l'installation, selon ce qui est déjà installé sur le PC ; choix consigné en 12.2 | Tranché le 19 octobre 2026 : 26.04.1 LTS installée ; le dépôt Docker la prend en charge (`resolute`) |
| 6 | Étape 1 | `curl`, dont dépendent les étapes 3 à 8, n'est pas installé par défaut sur Ubuntu Desktop 26.04 | `curl` et `ca-certificates` installés dès l'étape 1 | Appliquée (4.2) |
| 7 | Étape 4 | Langfuse est passé en version 4. Son `docker-compose.yml` lit chaque secret dans une variable avec une valeur par défaut connue de tous (`${SALT:-mysalt}`…), et appelle ses images par l'étiquette flottante `:4` | Les secrets ne sont pas écrits dans `docker-compose.yml` mais dans un `.env` voisin (droits 600, ignoré par le dépôt Langfuse), généré par `openssl rand -hex 32` sans affichage ; `docker compose config` vérifié sans aucune valeur par défaut. Images figées sur la version installée (`:4.63.0`). Télémétrie de Langfuse coupée (`TELEMETRY_ENABLED=false`), conformément au principe « rien sur Internet » | Appliquée lors de l'installation ; texte de l'étape 4 à réécrire en conséquence |
| 8 | Étape 5 | Les images de LiteLLM ne portent plus d'étiquette `main-vX.Y.Z-stable` : les versions publiées sont de la forme `vX.Y.Z` (les `-rc` et `-dev` étant des préversions) | `VERSION_LITELLM` = dernière version sans suffixe (`v1.106.0` le 19 octobre 2026), vérifiée par `docker manifest inspect` | Appliquée lors de l'installation ; texte de l'étape 5 à corriger |
| 9 | Étape 5, scénario 3.1 | ILaaS n'expose Mistral Medium que sous l'alias `mistral-medium-latest`, alors que la règle impose un identifiant daté, jamais un alias `latest` | À décider par le chercheur : soit demander à ILaaS un identifiant daté, soit accepter l'alias en relevant l'identifiant renvoyé dans chaque réponse et l'empreinte de comportement (7.3), l'écart étant déclaré. En attendant, `mistral-medium` reste non configuré | Point ouvert |
| 10 | Étape 8, 7.2 | `qwen-3.8-27b` est un modèle à raisonnement : les tokens de raisonnement comptent dans `max_tokens`. Avec `max_tokens` à 30, toute la réponse est partie en raisonnement et le texte est vide (`finish_reason: length`) | Le plafond `max_tokens` des scripts doit inclure le raisonnement ; le régler par modèle au pilote, et contrôler `finish_reason` dans chaque réponse archivée | Point ouvert (à reporter dans le module du village) |
| 11 | Étapes 6 et 8, EF4 | Les métadonnées passées dans le champ `metadata` de la requête (par exemple `{"essai": "TEST-INSTALL"}`) ne se retrouvent pas dans la trace Langfuse | À établir : forme attendue par LiteLLM pour transmettre des métadonnées à la fonction de rappel `langfuse_otel` ; à régler avant le bureau v0 et l'étape −1 | Point ouvert |
| 13 | Étape 5, scénario 3.0 et 3.1 | Courriel d'ILaaS (renouvellement de l'offre) : `qwen-3.6-35b-instruct` sera progressivement remplacé par `qwen-3.8-27b` ; le raisonnement de `qwen-3.8-27b` est actif par défaut, au niveau « medium », et peut être désactivé côté client ; `gemma-4-31b` et `mistral-small-4-119b` restent servis. Or `qwen-3.6-35b-a3b` est le juge 2 du scénario | À décider par le chercheur : remplaçant du juge 2 (par exemple `qwen-3.8-27b`, en gardant la règle « jamais un juge de la famille du générateur ») ; niveau de raisonnement fixé et déclaré pour chaque modèle à raisonnement, au second temps du préenregistrement (lié au point n° 10) | Point ouvert |
| 14 | Étape 6, EF2, 7.2, recette n° 2 | Dans LiteLLM, le budget d'une clé virtuelle est un montant en dollars, calculé à partir du prix des modèles. ILaaS et Le Chonk (expérimentation AMUE) sont gratuits pour le projet : le coût calculé est nul, un budget ne se déclencherait jamais | Clés virtuelles créées sans budget. La consommation se suit en tokens, par clé et par appel, dans les journaux de LiteLLM (`/spend/logs`) et dans Langfuse ; pour Le Chonk, aussi sur le tableau de bord de l'AMUE. La recette n° 2 ne garde que la révocation ; un plafond par débit (`tpm_limit`, `rpm_limit`) reste possible si un fournisseur l'impose | Appliquée lors de l'installation ; EF2, 7.2 et recette n° 2 à réécrire en conséquence |
| 12 | Étape 4, CU5 | En version 4, Langfuse fonctionne en mode « événements » : les anciennes routes de lecture de l'API publique (`/api/public/traces`, `/api/public/observations`) ne sont plus disponibles | Les traces se consultent dans l'interface ; l'analyse repose de toute façon sur les exports de l'étape 8 bis, et non sur Langfuse | Noté |

### 12.2 Journal d'installation

Une ligne par opération sur la station : ce qui a été fait, le résultat, les versions installées, les écarts à la procédure. Les écarts qui changent la procédure donnent une entrée en 12.1 et une nouvelle version du document. Ce qui est propre à la machine et au poste du pilote (adresse, empreintes de clés, matériel exact) n'est pas publié : il est consigné dans un fichier local non versionné (dossier `prive/`, ignoré par git).

| Date | Étape | Opération | Résultat, versions, écarts |
|---|---|---|---|
| 19/10/2026 | 1 | Installation d'Ubuntu Desktop LTS, compte administrateur `pilote` | Ubuntu 26.04.1 LTS (dernière LTS, plutôt que la 24.04 conseillée : point n° 5 de 12.1) |
| 19/10/2026 | 1 | `apt update`, `apt full-upgrade`, `unattended-upgrades` activé | Sans erreur ; redémarrage de la station |
| 19/10/2026 | 2 | `openssh-server` et `ufw` installés ; `ufw allow OpenSSH`, `ufw enable` | Sans erreur |
| 19/10/2026 | 2 | Clé SSH dédiée à la station, créée sur l'ordinateur du pilote et déposée par `ssh-copy-id` | Empreinte de la station vérifiée sur la machine avant d'accepter la connexion ; une première clé, aussitôt régénérée, a été retirée de `authorized_keys` |
| 19/10/2026 | 2 | Machine renommée `station` (`hostnamectl set-hostname`, ligne `127.0.1.1` de `/etc/hosts`) | Le nom donné à l'installation était différent ; `station.local` ne se résout pas encore depuis l'ordinateur du pilote : connexion par l'adresse IP |
| 19/10/2026 | 2 | Connexion par mot de passe désactivée : fichier `/etc/ssh/sshd_config.d/10-pilote.conf` (`PasswordAuthentication no`), `sshd -t` puis `systemctl reload ssh` | Vérifié à distance : la clé passe, le mot de passe est refusé (`Permission denied (publickey)`). Étape 2 terminée |
| 19/10/2026 | 3 | Vérification préalable : le dépôt Docker publie une version pour Ubuntu 26.04 (`resolute`, amd64) | Point n° 5 de 12.1 levé |
| 19/10/2026 | 1 | `curl` absent de l'installation de base ; `sudo apt install -y curl ca-certificates` | curl 8.18.0 installé ; correction n° 6 de 12.1 |
| 19/10/2026 | 3 | Dépôt officiel de Docker déclaré (clé dans `/etc/apt/keyrings/docker.asc`, fichier `/etc/apt/sources.list.d/docker.sources`), puis `docker-ce`, `docker-ce-cli`, `containerd.io`, `docker-buildx-plugin`, `docker-compose-plugin` installés | Empreinte de la clé conforme à celle de Docker (`9DC8…CD88`). Docker 29.9.1, Docker Compose v5.6.0 ; service actif et lancé au démarrage |
| 19/10/2026 | 3 | `pilote` ajouté au groupe `docker` | Vérifié après reconnexion : `docker run --rm hello-world` fonctionne sans `sudo` |
| 19/10/2026 | 3 | Arborescence `/srv/chonk/` créée (six dossiers), propriétaire `pilote:docker`, droits 2775 | Conforme. Étape 3 terminée |
| 19/10/2026 | 4 | Dépôt Langfuse cloné dans `/srv/chonk/langfuse` | Dernière version publiée : v4.63.0. Langfuse est passé en version 4 : le service web s'appelle toujours `langfuse-web` (correction n° 1 valable) ; les images sont appelées par l'étiquette flottante `:4` |
| 19/10/2026 | 4 | `git checkout v4.63.0` ; dans `docker-compose.yml`, ports 3000 et 9090 liés à `127.0.0.1`, images figées en `4.63.0` ; secrets générés dans `.env` (correction n° 7) | Tous les ports de Langfuse sont liés à `127.0.0.1` ; aucun secret par défaut restant |
| 19/10/2026 | 4 | `docker compose up -d` | Six conteneurs démarrés (web, worker, postgres, clickhouse, redis, minio) ; `/api/public/health` répond 200 ; réseau `langfuse_default` créé (nom attendu par l'étape 5) ; seul le port 22 écoute hors de la machine. Reste : création du premier compte, du projet « Le Chonk » et de sa paire de clés, par le pilote |
| 19/10/2026 | 4 | Premier compte, organisation et projet « Le Chonk » créés par le pilote, depuis son ordinateur, par tunnel SSH (`ssh -L 3000:localhost:3000`) ; paire de clés du projet générée | Étape 4 terminée |
| 19/10/2026 | 5 | `.env` du passe-plat créé (droits 600) : clé maîtresse et mot de passe de la base générés sur la station ; clés Langfuse saisies par le pilote ; clés et URL de Le Chonk et d'ILaaS en attente | Contrôle sans affichage des valeurs : seules les clés des fournisseurs manquent |
| 19/10/2026 | 5 | `config.yaml` et `docker-compose.yml` écrits selon l'étape 5 (version 4.2) ; image `ghcr.io/berriai/litellm:v1.106.0` ; `docker compose up -d` | Passe-plat démarré ; `/health/liveliness` répond 200 ; LiteLLM joint Langfuse par le réseau Docker (`langfuse-web:3000` répond 200 depuis le conteneur) : correction n° 1 vérifiée. Les étiquettes LiteLLM sont désormais de la forme `vX.Y.Z` (correction n° 8). Identifiants datés des modèles encore provisoires dans `config.yaml` |
| 19/10/2026 | 5 | Clé et URL d'ILaaS saisies par le pilote ; passe-plat redémarré ; liste des modèles ILaaS relevée | Six modèles : `gemma-4-31b`, `llama-3.1-8b`, `mistral-medium-latest`, `mistral-small-4-119b`, `qwen-3.6-35b-instruct`, `qwen-3.8-27b`. Identifiant de Qwen 3.6 reporté dans `config.yaml` ; Mistral Medium seulement en `latest` (point n° 9). Clé de Le Chonk en attente |
| 19/10/2026 | 5 | Premier appel par le passe-plat (`qwen-3.8-27b`, clé maîtresse) | Réponse correcte ; identifiant renvoyé `qwen-3.8-27b`. À `max_tokens` 30, réponse vide car consommée par le raisonnement (point n° 10). Les deux appels apparaissent dans Langfuse (génération `litellm_request`, tokens d'entrée, de sortie et de raisonnement) ; les métadonnées de la requête n'y sont pas (point n° 11) |
| 19/10/2026 | 6 | Redémarrage de la station par le pilote | Tous les services (Langfuse, passe-plat) sont repartis seuls (ENF4) |
| 19/10/2026 | 6 | Trois clés virtuelles créées par `/key/generate` : `agent-de-code`, `campagnes`, `village`, sans budget (correction n° 14) ; rangées dans `/srv/chonk/passe-plat/cles-virtuelles.env` (droits 600), jamais affichées | Appel de test avec la clé `agent-de-code` réussi ; les journaux de LiteLLM l'attribuent à cette clé, avec les tokens d'entrée et de sortie (coût calculé : 0). Étape 6 terminée |
