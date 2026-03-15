#!/usr/bin/env python3
"""Audit contenu SEO — mots de contenu, titres, mots-clés par page"""
import os, re

BASE = "/Users/cedrictantcheu/Documents/vtimagerie_v2_DEPLOY_FINAL_GTM_CONSENT_V2_20250724_025441 5/centremedicalparislevallois"
PAGES = [
    "index.html",
    "pages/ophtalmologie.html",
    "pages/kinesitherapie.html",
    "pages/soins-infirmiers.html",
    "pages/medecine-generale.html",
    "pages/le-centre.html",
    "pages/urgences.html",
    "pages/tarifs.html",
    "pages/faq.html",
    "pages/contact.html",
]

KEYWORDS = ["levallois", "ophtalmologue", "kiné", "soins infirmiers", "médecin",
            "centre médical", "doctolib", "secteur 1", "rendez-vous", "paris"]

for page in PAGES:
    fpath = os.path.join(BASE, page)
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    # Title
    title_m = re.search(r"<title>(.*?)</title>", html, re.DOTALL)
    title = title_m.group(1).strip() if title_m else "(manquant)"

    # Meta desc
    desc_m = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', html, re.I)
    desc = desc_m.group(1) if desc_m else "(manquant)"

    # Clean text
    clean = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL)
    clean = re.sub(r"<style[^>]*>.*?</style>", "", clean, flags=re.DOTALL)
    clean = re.sub(r"<[^>]+>", " ", clean)
    clean = re.sub(r"\s+", " ", clean).strip()
    word_count = len(clean.split())

    # Headings
    h1s = [re.sub(r"<[^>]+>", "", h).strip() for h in re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.DOTALL)]
    h2s = [re.sub(r"<[^>]+>", "", h).strip() for h in re.findall(r"<h2[^>]*>(.*?)</h2>", html, re.DOTALL)]
    h3s = [re.sub(r"<[^>]+>", "", h).strip() for h in re.findall(r"<h3[^>]*>(.*?)</h3>", html, re.DOTALL)]

    # Keywords
    text_lower = clean.lower()
    kw_counts = {}
    for kw in KEYWORDS:
        kw_counts[kw] = text_lower.count(kw.lower())

    # Links
    internal_links = len(re.findall(r'href="[^"]*(?:pages/|index\.html|/)[^"]*"', html))
    doctolib_links = len(re.findall(r'doctolib\.fr', html))

    # Output
    print("=" * 70)
    print("  {}".format(page))
    print("=" * 70)
    print("  Title:      {} ({} car.)".format(title[:60], len(title)))
    print("  Meta desc:  {} ({} car.)".format(desc[:70] + "..." if len(desc) > 70 else desc, len(desc)))
    print("  Mots:       {}".format(word_count))
    verdict = "FAIBLE" if word_count < 300 else "OK" if word_count < 800 else "BON" if word_count < 1500 else "EXCELLENT"
    print("  Verdict:    {} ({} mots)".format(verdict, word_count))
    print("  H1 ({}):    {}".format(len(h1s), " | ".join(h1s[:2]) if h1s else "(aucun!)"))
    print("  H2 ({}):    {}".format(len(h2s), " | ".join(h[:40] for h in h2s[:4])))
    print("  H3 ({}):    {}".format(len(h3s), " | ".join(h[:35] for h in h3s[:4])))
    print("  Liens int.: {}  |  Doctolib: {}".format(internal_links, doctolib_links))
    kw_str = ", ".join("{}: {}".format(k, v) for k, v in kw_counts.items() if v > 0)
    missing = [k for k, v in kw_counts.items() if v == 0]
    print("  Mots-cles:  {}".format(kw_str or "(aucun!)"))
    if missing:
        print("  MANQUANTS:  {}".format(", ".join(missing)))
    print()
