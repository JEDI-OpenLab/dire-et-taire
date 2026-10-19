"""Assemble les pages du site à partir des fragments : en-tête, navigation, pied de page.
Produit site/*.html (documents complets, pour GitHub Pages), dont carte.html, copiée de docs/visualisations/. Avec --artefact, produit aussi
site-artefact/index.html (sans doctype, pour un aperçu en artefact). Usage : python3 build.py"""
import pathlib, sys, re, html, unicodedata, hashlib

SRC = pathlib.Path(__file__).parent
OUT = SRC.parent / "site"
ART = SRC.parent / "site-artefact"
GITHUB = "https://github.com/JEDI-OpenLab/dire-et-taire/blob/main/"

PAGES = [
    ("index.html", "Accueil", "Dire et taire"),
    ("cadre.html", "Cadre scientifique", "Cadre scientifique · Dire et taire"),
    ("scenario.html", "Le scénario", "Le scénario · Dire et taire"),
    ("technique.html", "Technique", "Technique · Dire et taire"),
    ("glossaire.html", "Glossaire", "Glossaire · Dire et taire"),
    ("feuille-de-route.html", "Feuille de route", "Feuille de route · Dire et taire"),
]

HEAD = """<title>{title}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="Dire et taire : un village de 40 agents génératifs pour étudier la circulation d'un savoir savant, le dire et le taire. Recherche en sciences de l'information et de la communication, JEDI-OpenLab, Centrale Lille.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,500;8..60,650&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@500&display=swap">
<link rel="stylesheet" href="assets/site.css?v={css_v}">
"""


GLOSSAIRE_MD = SRC.parent / "docs" / "glossaire.md"
CARTE = SRC.parent / "docs" / "visualisations" / "carte-concepts.html"
CARTE_TITRE = '<div class="eyebrow">Village simulé · scénario « Dire et taire »</div>'
CARTE_TITRE_SITE = '<div class="eyebrow">Village simulé · « Dire et taire » · <a href="cadre.html" style="color:inherit">retour au site</a></div>'

def slug(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    return t

def glossaire():
    """Transforme les tableaux de docs/glossaire.md en fiches, rubrique par rubrique."""
    lines = GLOSSAIRE_MD.read_text(encoding="utf-8").splitlines()
    secs, cur, head, seen = [], None, None, set()
    for l in lines:
        m = re.match(r"^## (\d+)\. (.+)", l)
        if m:
            if m.group(2).startswith("Références"): cur = None; continue
            cur = {"t": m.group(2), "rows": []}; secs.append(cur); head = None; continue
        if cur is None or not l.startswith("|") or l.startswith("|---"): continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if head is None: head = cells; continue
        cur["rows"].append(dict(zip(head, cells)))
    toc, body = [], []
    for sec in secs:
        sid = slug(sec["t"]); toc.append(f'<a href="#{sid}">{html.escape(sec["t"])}</a>')
        items = []
        for r in sec["rows"]:
            vals = list(r.values()); term = vals[0].strip("*")
            eid = slug(term)
            while eid in seen: eid += "-2"
            seen.add(eid)
            parts = [f'<dt id="{eid}"><a href="#{eid}">{inline(term)}</a></dt>', f'<dd class="def">{inline(vals[1])}</dd>']
            for k, v in list(r.items())[2:]:
                if v: parts.append(f'<dd class="meta"><span>{html.escape(k)}</span> {inline(v)}</dd>')
            items.append('<div class="glo-entry">' + "".join(parts) + "</div>")
        body.append(f'<section class="band glo-sec" id="{sid}"><div class="wrap"><h2>{html.escape(sec["t"])}</h2><dl class="glo">' + "".join(items) + "</dl></div></section>")
    out = "\n".join(body)
    # Le site ne présente qu'un scénario : les renvois « C4 » deviennent « scénario »
    out = re.sub(r'<div class="glo-entry"><dt id="experiences-c0-a-c5">.*?</div>', "", out)
    out = re.sub(r"\bdu C4\b", "du scénario", out)
    out = re.sub(r"\bC4\b", "scénario", out)
    return " · ".join(toc), out

def nav(current):
    cur = ' aria-current="page"'
    items = "".join(
        f'<li><a href="{f}"{cur if f == current else ""}>{label}</a></li>'
        for f, label, _ in PAGES)
    return f"""<nav class="site-nav" aria-label="Sections du site"><div class="in">
<a class="brand" href="index.html">Dire et taire <span>· village simulé</span></a>
<ul>{items}</ul></div></nav>
"""

FOOT = """<footer class="site-foot"><div class="in">
<span>JEDI-OpenLab, Centrale Lille. Projet de recherche en sciences de l'information et de la communication mené par Jean Debaecker.</span>
<span><a href="https://jediopenlab.hypotheses.org/">Carnet de recherche</a> · <a href="{gh}">Documents et code</a></span>
</div></footer>
""".format(gh=GITHUB.replace("blob/main/", ""))

def build():
    art = "--artefact" in sys.argv
    OUT.mkdir(exist_ok=True)
    if art: ART.mkdir(exist_ok=True)
    # Empreinte de la feuille de style dans son adresse : un navigateur ne garde pas l'ancienne après une mise à jour
    css_v = hashlib.sha256((OUT / "assets" / "site.css").read_bytes()).hexdigest()[:10]
    for f, label, title in PAGES:
        body = (SRC / f).read_text(encoding="utf-8").replace("{GH}", GITHUB)
        if "{GLOSSAIRE}" in body:
            toc, gl = glossaire()
            body = body.replace("{TOC}", toc).replace("{GLOSSAIRE}", gl)
        inner = HEAD.format(title=title, css_v=css_v) + nav(f) + body + FOOT
        full = '<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n' + inner.replace(nav(f), "</head>\n<body>\n" + nav(f), 1) + "</body>\n</html>\n"
        (OUT / f).write_text(full, encoding="utf-8")
        if art and f == "index.html":
            (ART / "index.html").write_text(inner, encoding="utf-8")
    # La carte des concepts est une page autonome : copiée depuis docs/, avec un lien de retour au site
    carte = CARTE.read_text(encoding="utf-8")
    if CARTE_TITRE not in carte:
        sys.exit("carte-concepts.html : en-tête attendu introuvable, lien de retour au site non posé")
    (OUT / "carte.html").write_text(carte.replace(CARTE_TITRE, CARTE_TITRE_SITE, 1), encoding="utf-8")
    print("pages :", ", ".join(p[0] for p in PAGES), "+ carte.html")

if __name__ == "__main__":
    build()
