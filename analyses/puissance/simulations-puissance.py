"""Simulations de puissance et de fiabilité pour les règles de décision du scénario.

Trois questions, posées par la revue adversariale n° 2 (R2-05, R2-07, R2-08) :

A. HO11. Avec 5 simulations par bras pour les contrastes entre simulations (gazette,
   ordonnanceur, modèle), quelle est la probabilité de satisfaire la règle « le
   contraste X dépasse celui de la fiche d'au moins 5 points, intervalle de la
   différence excluant zéro » ? Et l'intervalle par rééchantillonnage de 5
   simulations couvre-t-il ce qu'il prétend couvrir ?

B. HO9. Avec 20 simulations T1 en priorité 1, quelle est la puissance du test
   d'équivalence du coefficient du climat perçu, à la borne ±0,05 et à ±0,10 ?

C. HO10a. Dans un modèle jouet de diffusion depuis une source unique, la diversité
   des versions décroît-elle « mécaniquement » ? Réponse : cela dépend du caractère
   contractant de chaque reprise, ce que les chaînes linéaires mesurent.

Tous les paramètres sont des hypothèses à remplacer par les mesures du pilote.
Dépendances : numpy, scipy. Exécution : python simulations-puissance.py
"""

import numpy as np
from scipy import stats

rng = np.random.default_rng(2026)


# ----------------------------------------------------------------------------
# A. HO11 : contrastes entre simulations, 5 contre 5
# ----------------------------------------------------------------------------

def simuler_taux(n_sim, p_base, sd_sim_logit, delta_logit, agents=40, sollic=10,
                 sd_agent_logit=0.5):
    """Taux de taire observé par simulation (moyenne sur agents × sollicitations)."""
    taux = np.empty(n_sim)
    base = np.log(p_base / (1 - p_base))
    for s in range(n_sim):
        u_sim = rng.normal(0, sd_sim_logit)
        u_ag = rng.normal(0, sd_agent_logit, agents)
        p = 1 / (1 + np.exp(-(base + u_sim + delta_logit + u_ag)))
        y = rng.binomial(sollic, p)
        taux[s] = y.sum() / (agents * sollic)
    return taux


def regle_ho11(n_rep, sd_sim_pts, diff_vraie_pts, p_base=0.40, n_par_bras=5,
               se_fiche=0.01, contraste_fiche=0.10, seuil=0.05):
    """Probabilité que la règle de HO11 soit satisfaite pour un contraste entre simulations.

    sd_sim_pts : écart-type entre simulations du taux de taire (en proportion).
    diff_vraie_pts : (contraste X vrai) − (contraste fiche vrai), en proportion.
    Le contraste de la fiche est supposé estimé avec une erreur-type se_fiche
    (il est intra-simulation, donc précis).
    """
    pente = p_base * (1 - p_base)          # d p / d logit au point de base
    sd_logit = sd_sim_pts / pente
    contraste_x = contraste_fiche + diff_vraie_pts
    delta_logit = contraste_x / pente
    satisfait = 0
    largeurs = []
    for _ in range(n_rep):
        a = simuler_taux(n_par_bras, p_base, sd_logit, 0.0)
        b = simuler_taux(n_par_bras, p_base, sd_logit, delta_logit)
        est_x = b.mean() - a.mean()
        se_x = np.sqrt(a.var(ddof=1) / n_par_bras + b.var(ddof=1) / n_par_bras)
        est_fiche = contraste_fiche + rng.normal(0, se_fiche)
        d = est_x - est_fiche
        se_d = np.sqrt(se_x ** 2 + se_fiche ** 2)
        # intervalle t avec degrés de liberté de Welch sur les deux bras
        df = 2 * n_par_bras - 2
        t = stats.t.ppf(0.975, df)
        bas = d - t * se_d
        largeurs.append(2 * t * se_d)
        if d >= seuil and bas > 0:
            satisfait += 1
    return satisfait / n_rep, float(np.mean(largeurs))


def bootstrap_vs_t(n_rep, sd_sim_pts, p_base=0.40, n_par_bras=5, B=2000):
    """Couverture d'un intervalle à 95 % pour une différence de moyennes nulle :
    percentile bootstrap sur 5 + 5 simulations contre intervalle t."""
    pente = p_base * (1 - p_base)
    sd_logit = sd_sim_pts / pente
    couv_boot = couv_t = 0
    larg_boot = larg_t = 0.0
    for _ in range(n_rep):
        a = simuler_taux(n_par_bras, p_base, sd_logit, 0.0)
        b = simuler_taux(n_par_bras, p_base, sd_logit, 0.0)
        diffs = np.empty(B)
        for k in range(B):
            diffs[k] = rng.choice(b, n_par_bras).mean() - rng.choice(a, n_par_bras).mean()
        lo, hi = np.percentile(diffs, [2.5, 97.5])
        couv_boot += (lo <= 0 <= hi)
        larg_boot += hi - lo
        d = b.mean() - a.mean()
        se = np.sqrt(a.var(ddof=1) / n_par_bras + b.var(ddof=1) / n_par_bras)
        t = stats.t.ppf(0.975, 2 * n_par_bras - 2)
        couv_t += (d - t * se <= 0 <= d + t * se)
        larg_t += 2 * t * se
    return couv_boot / n_rep, larg_boot / n_rep, couv_t / n_rep, larg_t / n_rep


def contraste_intra(n_rep, n_sim=20, p_base=0.40, sd_sim_pts=0.05, delta_pts=0.10):
    """Erreur-type du contraste de scène (intra-simulation), estimée par différence
    appariée des taux public et privé dans chaque simulation."""
    pente = p_base * (1 - p_base)
    ses = []
    for _ in range(n_rep):
        d = np.empty(n_sim)
        for s in range(n_sim):
            u = rng.normal(0, sd_sim_pts / pente)
            pub = simuler_taux(1, p_base, 0.0, u + delta_pts / pente, sollic=5)[0]
            priv = simuler_taux(1, p_base, 0.0, u, sollic=5)[0]
            d[s] = pub - priv
        ses.append(d.std(ddof=1) / np.sqrt(n_sim))
    return float(np.mean(ses))


# ----------------------------------------------------------------------------
# B. HO9 : équivalence du coefficient du climat perçu
# ----------------------------------------------------------------------------

def ho9_equivalence(n_rep, beta_vrai, borne, n_sim=20, agents=40, jours=15,
                    repliques_par_jour=2, sd_bruit=1.2, sd_pente_sim=0.03,
                    sd_pente_agent=0.05, b_interloc=0.30):
    """Probabilité de conclure à l'équivalence (TOST, intervalle à 90 % dans ±borne),
    avec estimation par simulation (coefficient intra-agent) puis moyenne entre
    simulations (erreur-type entre simulations, conservatrice).
    Retourne aussi la probabilité que la borne supérieure de l'intervalle à 90 %
    soit inférieure à 0,10 (option B de la revue)."""
    equiv = sous_010 = 0
    for _ in range(n_rep):
        betas = np.empty(n_sim)
        for s in range(n_sim):
            u_s = rng.normal(0, sd_pente_sim)
            num = den = 0.0
            for a in range(agents):
                u_a = rng.normal(0, sd_pente_agent)
                n = jours * repliques_par_jour
                climat = rng.normal(0, 1, n)          # centré réduit intra-agent
                interloc = rng.normal(0, 1, n)
                y = b_interloc * interloc + (beta_vrai + u_s + u_a) * climat \
                    + rng.normal(0, sd_bruit, n)
                # régression bivariée, prédicteurs indépendants : coefficient partiel
                c = climat - climat.mean()
                yy = y - y.mean()
                num += (c * yy).sum()
                den += (c * c).sum()
            betas[s] = num / den
        m = betas.mean()
        se = betas.std(ddof=1) / np.sqrt(n_sim)
        t90 = stats.t.ppf(0.95, n_sim - 1)
        lo, hi = m - t90 * se, m + t90 * se
        equiv += (lo > -borne and hi < borne)
        sous_010 += (hi < 0.10)
    return equiv / n_rep, sous_010 / n_rep


# ----------------------------------------------------------------------------
# C. HO10a : modèle jouet de diffusion depuis une source unique
# ----------------------------------------------------------------------------

def diversite(versions):
    v = versions / np.linalg.norm(versions, axis=1, keepdims=True)
    sim = v @ v.T
    n = len(v)
    iu = np.triu_indices(n, 1)
    return float(np.mean(1 - sim[iu]))


def diffusion_jouet(lam, sigma=0.15, d=20, agents=40, jours=15, nouveaux_par_jour=3,
                    n_rep=200):
    """Chaque jour, des agents non informés copient la version d'un informé tiré au
    hasard ; chaque informé réécrit aussi sa version (résumé). Une reprise est
    v' = lam * v + (1 − lam) * attracteur + bruit. lam = 1 : copie bruitée pure ;
    lam < 1 : reprise contractante vers une formule. Retourne la pente moyenne
    de la diversité (jours 2 à 15) et la part de répétitions à pente négative."""
    pentes = []
    for _ in range(n_rep):
        source = rng.normal(0, 1, d)
        attracteur = source + rng.normal(0, 1, d)   # la formule n'est pas la source
        versions = np.zeros((agents, d))
        informe = np.zeros(agents, bool)
        serie = []
        for jour in range(1, jours + 1):
            # réécriture quotidienne des versions existantes
            idx = np.where(informe)[0]
            for i in idx:
                versions[i] = lam * versions[i] + (1 - lam) * attracteur + rng.normal(0, sigma, d)
            # nouveaux informés
            candidats = np.where(~informe)[0]
            k = min(nouveaux_par_jour, len(candidats))
            for i in rng.choice(candidats, k, replace=False):
                src = source if not informe.any() else versions[rng.choice(np.where(informe)[0])]
                versions[i] = lam * src + (1 - lam) * attracteur + rng.normal(0, sigma, d)
                informe[i] = True
            if informe.sum() >= 2 and jour >= 2:
                serie.append((jour, diversite(versions[informe])))
        x = np.array([s[0] for s in serie], float)
        y = np.array([s[1] for s in serie], float)
        pentes.append(np.polyfit(x, y, 1)[0])
    pentes = np.array(pentes)
    return float(pentes.mean()), float((pentes < 0).mean())


# ----------------------------------------------------------------------------
if __name__ == "__main__":
    N = 400
    print("# Résultats (paramètres hypothétiques, à remplacer par ceux du pilote)\n")

    print("## A1. HO11 : probabilité de satisfaire la règle pour un contraste entre simulations (5 contre 5)\n")
    print("| Écart-type entre simulations (points) | Différence vraie contraste X moins fiche (points) | P(règle satisfaite) | Largeur moyenne de l'intervalle (points) |")
    print("|---|---|---|---|")
    for sd in (0.03, 0.05, 0.08):
        for diff in (0.0, 0.05, 0.10, 0.15):
            p, larg = regle_ho11(N, sd, diff)
            print(f"| {sd*100:.0f} | {diff*100:.0f} | {p:.2f} | {larg*100:.1f} |")

    print("\n## A2. Intervalle à 95 % pour une différence nulle : percentile bootstrap sur 5 + 5 contre intervalle t\n")
    print("| Écart-type entre simulations (points) | Couverture bootstrap | Largeur bootstrap (points) | Couverture t | Largeur t (points) |")
    print("|---|---|---|---|---|")
    for sd in (0.03, 0.05, 0.08):
        cb, lb, ct, lt = bootstrap_vs_t(200, sd)
        print(f"| {sd*100:.0f} | {cb:.2f} | {lb*100:.1f} | {ct:.2f} | {lt*100:.1f} |")

    se_scene = contraste_intra(100)
    print(f"\n## A3. Contraste de scène (intra-simulation, 20 simulations) : erreur-type ≈ {se_scene*100:.1f} points\n")

    print("## B. HO9 : puissance du test d'équivalence (20 simulations T1, 40 agents, 15 journées, 2 répliques par jour)\n")
    print("| Coefficient vrai du climat | Borne | P(équivalence conclue) | P(borne supérieure de l'IC 90 % < 0,10) |")
    print("|---|---|---|---|")
    for beta in (0.0, 0.05, 0.10):
        for borne in (0.05, 0.10):
            pe, p10 = ho9_equivalence(60, beta, borne)
            print(f"| {beta:.2f} | ±{borne:.2f} | {pe:.2f} | {p10:.2f} |")

    print("\n## C. HO10a : pente de la diversité dans un modèle jouet de diffusion depuis une source unique\n")
    print("| Facteur de contraction de chaque reprise (lam) | Pente moyenne de la diversité par jour | Part de répétitions à pente négative |")
    print("|---|---|---|")
    for lam in (1.0, 0.95, 0.85, 0.7):
        pm, pn = diffusion_jouet(lam)
        print(f"| {lam:.2f} | {pm:+.4f} | {pn:.2f} |")
    print("\nLecture : à copie bruitée pure (lam = 1), la diversité augmente ; dès que la reprise est contractante, elle diminue. Le sens de l'effet de diffusion n'est donc pas connu a priori : il faut le mesurer sur les chaînes linéaires (modèle nul de HO10a).")
