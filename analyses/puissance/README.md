# Simulations de puissance des règles de décision du C4

*Scripts issus de la revue adversariale n° 2 (16 octobre 2026), conservés pour être rejoués avec les variances du pilote (C4, étape 6) avant le second temps du préenregistrement.*

| Fichier | Contenu |
|---|---|
| `simulations-puissance.py` | A : probabilité de satisfaire la règle de HO11 pour un contraste entre simulations, et couverture du rééchantillonnage à 5 unités ; B : puissance du test d'équivalence de HO9 ; C : modèle jouet de diffusion pour HO10a |
| `resultats-simulations.md` | Résultats avec des paramètres hypothétiques, dont l'ajout A1 bis (10 graines par bras) |

Exécution, sur la station :

```
uv run --with numpy --with scipy python simulations-puissance.py
```

Les paramètres (taux de base, écart-type entre simulations, nombre d'agents, bruit des positions) sont en tête de chaque fonction : les remplacer par les valeurs du pilote.
