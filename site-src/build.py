"""Assemble les pages du site à partir des fragments : en-tête, navigation, pied de page.
Produit site/*.html (documents complets, pour GitHub Pages). Avec --artefact, produit aussi
site-artefact/index.html (sans doctype, pour un aperçu en artefact). Usage : python3 build.py"""
import pathlib, sys

SRC = pathlib.Path(__file__).parent
OUT = SRC.parent / "site"
ART = SRC.parent / "site-artefact"
GITHUB = "https://github.com/JEDI-OpenLab/dire-et-taire/blob/main/"

PAGES = [
    ("index.html", "Accueil", "Dire et taire"),
    ("cadre.html", "Cadre scientifique", "Cadre scientifique · Dire et taire"),
    ("scenario.html", "Le scénario C4", "Le scénario C4 · Dire et taire"),
    ("technique.html", "Technique", "Technique · Dire et taire"),
    ("feuille-de-route.html", "Feuille de route", "Feuille de route · Dire et taire"),
]

HEAD = """<title>{title}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="Dire et taire : un village de 40 agents génératifs pour étudier la circulation d'un savoir savant, le dire et le taire. Recherche en sciences de l'information et de la communication, JEDI-OpenLab, Centrale Lille.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,500;8..60,650&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@500&display=swap">
<link rel="stylesheet" href="assets/site.css">
"""

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
    for f, label, title in PAGES:
        body = (SRC / f).read_text(encoding="utf-8").replace("{GH}", GITHUB)
        inner = HEAD.format(title=title) + nav(f) + body + FOOT
        full = '<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n' + inner.replace(nav(f), "</head>\n<body>\n" + nav(f), 1) + "</body>\n</html>\n"
        (OUT / f).write_text(full, encoding="utf-8")
        if art and f == "index.html":
            (ART / "index.html").write_text(inner, encoding="utf-8")
    print("pages :", ", ".join(p[0] for p in PAGES))

if __name__ == "__main__":
    build()
