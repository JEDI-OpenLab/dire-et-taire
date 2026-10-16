# Résultats (paramètres hypothétiques, à remplacer par ceux du pilote)

## A1. HO11 : probabilité de satisfaire la règle pour un contraste entre simulations (5 contre 5)

| Écart-type entre simulations (points) | Différence vraie contraste X moins fiche (points) | P(règle satisfaite) | Largeur moyenne de l'intervalle (points) |
|---|---|---|---|
| 3 | 0 | 0.01 | 12.7 |
| 3 | 5 | 0.27 | 12.5 |
| 3 | 10 | 0.83 | 12.6 |
| 3 | 15 | 1.00 | 12.3 |
| 5 | 0 | 0.03 | 16.8 |
| 5 | 5 | 0.20 | 16.4 |
| 5 | 10 | 0.59 | 16.1 |
| 5 | 15 | 0.94 | 16.1 |
| 8 | 0 | 0.02 | 23.6 |
| 8 | 5 | 0.11 | 23.0 |
| 8 | 10 | 0.34 | 22.8 |
| 8 | 15 | 0.64 | 23.1 |

## A2. Intervalle à 95 % pour une différence nulle : percentile bootstrap sur 5 + 5 contre intervalle t

| Écart-type entre simulations (points) | Couverture bootstrap | Largeur bootstrap (points) | Couverture t | Largeur t (points) |
|---|---|---|---|---|
| 3 | 0.88 | 8.8 | 0.95 | 11.6 |
| 5 | 0.86 | 11.8 | 0.94 | 15.6 |
| 8 | 0.92 | 17.4 | 0.97 | 23.1 |

## A3. Contraste de scène (intra-simulation, 20 simulations) : erreur-type ≈ 1.2 points

## B. HO9 : puissance du test d'équivalence (20 simulations T1, 40 agents, 15 journées, 2 répliques par jour)

| Coefficient vrai du climat | Borne | P(équivalence conclue) | P(borne supérieure de l'IC 90 % < 0,10) |
|---|---|---|---|
| 0.00 | ±0.05 | 0.98 | 1.00 |
| 0.00 | ±0.10 | 1.00 | 1.00 |
| 0.05 | ±0.05 | 0.05 | 1.00 |
| 0.05 | ±0.10 | 1.00 | 1.00 |
| 0.10 | ±0.05 | 0.00 | 0.07 |
| 0.10 | ±0.10 | 0.07 | 0.07 |

## C. HO10a : pente de la diversité dans un modèle jouet de diffusion depuis une source unique

| Facteur de contraction de chaque reprise (lam) | Pente moyenne de la diversité par jour | Part de répétitions à pente négative |
|---|---|---|
| 1.00 | +0.0160 | 0.00 |
| 0.95 | +0.0061 | 0.00 |
| 0.85 | +0.0004 | 0.33 |
| 0.70 | -0.0001 | 0.69 |

Lecture : à copie bruitée pure (lam = 1), la diversité augmente ; dès que la reprise est contractante, elle diminue. Le sens de l'effet de diffusion n'est donc pas connu a priori : il faut le mesurer sur les chaînes linéaires (modèle nul de HO10a).

## A1 bis. HO11 à 10 graines par bras (ajout du 16 octobre 2026, scénario version 11)

Même fonction `regle_ho11`, `n_par_bras=10`, 1 000 répétitions, mêmes paramètres hypothétiques.

| Écart-type entre simulations (points) | Différence vraie (points) | P(règle satisfaite), 5 graines | P(règle satisfaite), 10 graines | Largeur de l'intervalle à 10 graines (points) |
|---|---|---|---|---|
| 3 | 5 | 0.27 | 0.45 | 8.8 |
| 3 | 10 | 0.82 | 0.98 | 8.7 |
| 5 | 5 | 0.21 | 0.34 | 11.1 |
| 5 | 10 | 0.61 | 0.91 | 11.1 |
| 8 | 5 | 0.11 | 0.19 | 15.7 |
| 8 | 10 | 0.32 | 0.65 | 15.5 |

Lecture : à 10 graines par bras, un écart de 10 points entre un contraste secondaire et la fiche devient détectable dans la plupart des cas ; un écart de 5 points reste peu probable à établir, sauf si la variance entre graines est basse. D'où le choix du scénario version 11 (10 graines pour les bras des contrastes entre simulations, y compris le bras de référence cœur G0), et le rejeu de ces calculs avec les variances du pilote.
