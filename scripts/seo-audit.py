#!/usr/bin/env python3
"""
Audit SEO expert — Centre Médical Paris-Levallois
Analyse: title, meta description, canonical, H1, schema, liens internes, images
"""
import urllib.request
import urllib.error
import re
import json
import time
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

DOMAIN = "https://centremedicalparislevallois.fr"

# Pages indexées GSC (from user data)
INDEXED = {
    "/pages/soins-infirmiers/retrait-fils-agrafes.html",
    "/pages/kinesitherapie/consultation-suivi.html",
    "/pages/kinesitherapie/premiere-consultation.html",
    "/pages/medecine-generale/urgence.html",
    "/pages/medecine-generale/consultation.html",
    "/pages/soins-infirmiers/vaccination-adulte.html",
    "/pages/soins-infirmiers/bilan-sanguin-ecbu.html",
    "/pages/soins-infirmiers/vaccination-pediatrique.html",
    "/pages/soins-infirmiers/pansement-post-chirurgical.html",
    "/pages/soins-infirmiers/surveillance-constantes.html",
    "/pages/soins-infirmiers/test-antigenique.html",
    "/pages/soins-infirmiers/bilan-prevention.html",
    "/pages/ophtalmologie.html",
    "/pages/ophtalmologie/renouvellement-lunettes-lentilles.html",
    "/pages/kinesitherapie.html",
    "/pages/soins-infirmiers.html",
    "/pages/medecine-generale.html",
    "/pages/ophtalmologie/champ-visuel-humphrey.html",
    "/pages/ophtalmologie/consultation-suivi.html",
    "/pages/ophtalmologie/premiere-consultation-enfant.html",
    "/pages/ophtalmologie/premiere-consultation.html",
    "/pages/ophtalmologie/urgence.html",
    "/pages/soins-infirmiers/pansement-simple.html",
    "/pages/soins-infirmiers/injection.html",
}

# www duplicates in GSC
WWW_DUPLICATES = [
    "https://www.centremedicalparislevallois.fr/pages/ophtalmologie/urgence.html",
    "https://www.centremedicalparislevallois.fr/pages/soins-infirmiers/pansement-simple.html",
    "https://www.centremedicalparislevallois.fr/pages/le-centre.html",
    "https://www.centremedicalparislevallois.fr/",
]

# Sitemap URLs (paths only)
SITEMAP_PATHS = [
    "/",
    "/pages/le-centre.html",
    "/pages/tarifs.html",
    "/pages/contact.html",
    "/pages/acces-horaires.html",
    "/pages/faq.html",
    "/pages/urgences.html",
    "/pages/equipe.html",
    "/pages/soins-infirmiers.html",
    "/pages/kinesitherapie.html",
    "/pages/medecine-generale.html",
    "/pages/ophtalmologie.html",
    "/pages/soins-infirmiers/vaccination-adulte.html",
    "/pages/soins-infirmiers/vaccination-pediatrique.html",
    "/pages/soins-infirmiers/bilan-sanguin-ecbu.html",
    "/pages/soins-infirmiers/injection.html",
    "/pages/soins-infirmiers/pansement-simple.html",
    "/pages/soins-infirmiers/pansement-post-chirurgical.html",
    "/pages/soins-infirmiers/retrait-fils-agrafes.html",
    "/pages/soins-infirmiers/surveillance-constantes.html",
    "/pages/soins-infirmiers/test-antigenique.html",
    "/pages/soins-infirmiers/bilan-prevention.html",
    "/pages/kinesitherapie/premiere-consultation.html",
    "/pages/kinesitherapie/consultation-suivi.html",
    "/pages/kinesitherapie/reeducation-membres-superieurs.html",
    "/pages/kinesitherapie/reeducation-membres-inferieurs.html",
    "/pages/kinesitherapie/reeducation-post-operatoire.html",
    "/pages/kinesitherapie/rachis-cervical-dorsal-lombaire.html",
    "/pages/kinesitherapie/rhumatologie.html",
    "/pages/kinesitherapie/scoliose-adolescent.html",
    "/pages/kinesitherapie/traumatisme-adulte.html",
    "/pages/kinesitherapie/traumatisme-adolescent.html",
    "/pages/kinesitherapie/drainage-lymphatique.html",
    "/pages/kinesitherapie/femme-enceinte.html",
    "/pages/kinesitherapie/electrotherapie.html",
    "/pages/kinesitherapie/renforcement-abdominal.html",
    "/pages/kinesitherapie/seance-sans-ordonnance.html",
    "/pages/medecine-generale/consultation.html",
    "/pages/medecine-generale/urgence.html",
    "/pages/ophtalmologie/premiere-consultation.html",
    "/pages/ophtalmologie/premiere-consultation-enfant.html",
    "/pages/ophtalmologie/consultation-suivi.html",
    "/pages/ophtalmologie/renouvellement-lunettes-lentilles.html",
    "/pages/ophtalmologie/champ-visuel-humphrey.html",
    "/pages/ophtalmologie/urgence.html",
    "/pages/mentions-legales.html",
    "/pages/politique-confidentialite.html",
    "/pages/politique-cookies.html",
]

def fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "SEO-Audit/1.0"})
        resp = urllib.request.urlopen(req, timeout=15)
        return resp.read().decode("utf-8", errors="replace"), resp.getcode()
    except urllib.error.HTTPError as e:
        return "", e.code
    except Exception as e:
        return "", str(e)

def extract_tag(html, pattern):
    m = re.search(pattern, html, re.IGNORECASE | re.DOTALL)
    return m.group(1).strip() if m else None

def analyze_page(path):
    url = DOMAIN + path
    html, status = fetch(url)
    if not html:
        return {"url": url, "status": status, "error": True}
    
    title = extract_tag(html, r'<title[^>]*>(.*?)</title>')
    meta_desc = extract_tag(html, r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']')
    if not meta_desc:
        meta_desc = extract_tag(html, r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']')
    canonical = extract_tag(html, r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']')
    h1 = extract_tag(html, r'<h1[^>]*>(.*?)</h1>')
    if h1:
        h1 = re.sub(r'<[^>]+>', ' ', h1).strip()
        h1 = re.sub(r'\s+', ' ', h1)
    
    # Count H2s
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.IGNORECASE | re.DOTALL)
    h2_texts = []
    for h in h2s:
        t = re.sub(r'<[^>]+>', '', h).strip()
        if t:
            h2_texts.append(t[:60])
    
    # Schema.org
    schemas = re.findall(r'"@type"\s*:\s*"(\w+)"', html)
    
    # Internal links
    links = re.findall(r'href=["\'](/[^"\']*?\.html)["\']', html)
    internal_links = list(set(links))
    
    # Images without alt
    imgs = re.findall(r'<img\s[^>]*?>', html, re.IGNORECASE)
    imgs_no_alt = [i for i in imgs if 'alt=' not in i.lower() or 'alt=""' in i.lower()]
    
    # Meta robots
    robots = extract_tag(html, r'<meta\s+name=["\']robots["\']\s+content=["\'](.*?)["\']')
    
    # OG tags
    og_title = extract_tag(html, r'<meta\s+property=["\']og:title["\']\s+content=["\'](.*?)["\']')
    og_desc = extract_tag(html, r'<meta\s+property=["\']og:description["\']\s+content=["\'](.*?)["\']')
    
    return {
        "url": url,
        "path": path,
        "status": status,
        "title": title,
        "title_len": len(title) if title else 0,
        "meta_desc": meta_desc,
        "meta_desc_len": len(meta_desc) if meta_desc else 0,
        "canonical": canonical,
        "h1": h1,
        "h2_count": len(h2_texts),
        "h2s": h2_texts[:5],
        "schemas": list(set(schemas)),
        "internal_links": len(internal_links),
        "imgs_no_alt": len(imgs_no_alt),
        "robots": robots,
        "og_title": og_title is not None,
        "og_desc": og_desc is not None,
        "indexed": path in INDEXED,
    }

# =============================================
# RUN AUDIT
# =============================================
print("=" * 80)
print("AUDIT SEO EXPERT — Centre Médical Paris-Levallois")
print("=" * 80)

# 1. Coverage analysis
print("\n" + "=" * 80)
print("1. COUVERTURE D'INDEXATION (Sitemap vs GSC)")
print("=" * 80)

not_indexed = [p for p in SITEMAP_PATHS if p not in INDEXED]
print(f"\nSitemap: {len(SITEMAP_PATHS)} URLs | GSC indexées: {len(INDEXED)} | Non indexées: {len(not_indexed)}")
print(f"Doublons www dans GSC: {len(WWW_DUPLICATES)}")

print(f"\n⚠️  PAGES NON INDEXÉES ({len(not_indexed)}):")
categories = {
    "Pages principales": [],
    "Kinésithérapie": [],
    "Pages légales": [],
}
for p in not_indexed:
    if "/kinesitherapie/" in p:
        categories["Kinésithérapie"].append(p)
    elif "mentions" in p or "politique" in p or "cookies" in p:
        categories["Pages légales"].append(p)
    else:
        categories["Pages principales"].append(p)

for cat, pages in categories.items():
    if pages:
        print(f"\n  {cat}:")
        for p in pages:
            print(f"    ❌ {p}")

print(f"\n⚠️  DOUBLONS www (à supprimer de l'index):")
for u in WWW_DUPLICATES:
    print(f"    🔄 {u}")

# 2. Page-by-page analysis
print("\n" + "=" * 80)
print("2. ANALYSE PAGE PAR PAGE")
print("=" * 80)

issues = {
    "no_title": [],
    "title_too_short": [],
    "title_too_long": [],
    "no_meta_desc": [],
    "meta_desc_too_short": [],
    "meta_desc_too_long": [],
    "no_h1": [],
    "no_canonical": [],
    "wrong_canonical": [],
    "no_schema": [],
    "no_og": [],
    "imgs_no_alt": [],
    "few_internal_links": [],
    "noindex": [],
    "duplicate_title": {},
    "duplicate_h1": {},
}

results = []
for i, path in enumerate(SITEMAP_PATHS):
    if i > 0 and i % 5 == 0:
        time.sleep(1)
    print(f"  [{i+1}/{len(SITEMAP_PATHS)}] {path}...", end=" ", flush=True)
    r = analyze_page(path)
    results.append(r)
    
    status_icon = "✅" if r["status"] == 200 else "❌"
    idx_icon = "📗" if r.get("indexed") else "📕"
    print(f"{status_icon} {idx_icon} title={r.get('title_len',0)}c meta={r.get('meta_desc_len',0)}c")
    
    if r.get("error"):
        continue
    
    # Check issues
    if not r["title"]:
        issues["no_title"].append(path)
    elif r["title_len"] < 30:
        issues["title_too_short"].append((path, r["title_len"]))
    elif r["title_len"] > 65:
        issues["title_too_long"].append((path, r["title_len"], r["title"][:70]))
    
    if not r["meta_desc"]:
        issues["no_meta_desc"].append(path)
    elif r["meta_desc_len"] < 70:
        issues["meta_desc_too_short"].append((path, r["meta_desc_len"]))
    elif r["meta_desc_len"] > 160:
        issues["meta_desc_too_long"].append((path, r["meta_desc_len"]))
    
    if not r["h1"]:
        issues["no_h1"].append(path)
    
    if not r["canonical"]:
        issues["no_canonical"].append(path)
    elif r["canonical"] != DOMAIN + path:
        issues["wrong_canonical"].append((path, r["canonical"]))
    
    if not r["schemas"]:
        issues["no_schema"].append(path)
    
    if not r["og_title"] or not r["og_desc"]:
        issues["no_og"].append(path)
    
    if r["imgs_no_alt"] > 0:
        issues["imgs_no_alt"].append((path, r["imgs_no_alt"]))
    
    if r["internal_links"] < 3:
        issues["few_internal_links"].append((path, r["internal_links"]))
    
    if r["robots"] and "noindex" in r["robots"].lower():
        issues["noindex"].append(path)
    
    # Track duplicates
    if r["title"]:
        issues["duplicate_title"].setdefault(r["title"], []).append(path)
    if r["h1"]:
        issues["duplicate_h1"].setdefault(r["h1"], []).append(path)

# 3. Issues report
print("\n" + "=" * 80)
print("3. PROBLÈMES DÉTECTÉS")
print("=" * 80)

def print_issue(label, items, severity="⚠️"):
    if items:
        print(f"\n{severity} {label} ({len(items)}):")
        for item in items[:10]:
            if isinstance(item, tuple):
                print(f"    → {item[0]} ({item[1:]})")
            else:
                print(f"    → {item}")

print_issue("Pages sans <title>", issues["no_title"], "🔴")
print_issue("Title trop court (<30c)", issues["title_too_short"], "🟡")
print_issue("Title trop long (>65c)", issues["title_too_long"], "🟡")
print_issue("Pages sans meta description", issues["no_meta_desc"], "🔴")
print_issue("Meta desc trop courte (<70c)", issues["meta_desc_too_short"], "🟡")
print_issue("Meta desc trop longue (>160c)", issues["meta_desc_too_long"], "🟡")
print_issue("Pages sans H1", issues["no_h1"], "🔴")
print_issue("Pages sans canonical", issues["no_canonical"], "🔴")
print_issue("Canonical incorrecte", issues["wrong_canonical"], "🟡")
print_issue("Pages sans Schema.org", issues["no_schema"], "🟡")
print_issue("Pages sans OG tags", issues["no_og"], "🟡")
print_issue("Images sans alt", issues["imgs_no_alt"], "🟡")
print_issue("Peu de liens internes (<3)", issues["few_internal_links"], "🟡")
print_issue("Pages avec noindex", issues["noindex"], "🔴")

# Duplicate titles
dup_titles = {t: ps for t, ps in issues["duplicate_title"].items() if len(ps) > 1}
if dup_titles:
    print(f"\n🔴 Titles dupliqués ({len(dup_titles)}):")
    for t, ps in dup_titles.items():
        print(f"    → \"{t[:60]}...\" sur {len(ps)} pages:")
        for p in ps:
            print(f"      - {p}")

# Duplicate H1s
dup_h1s = {h: ps for h, ps in issues["duplicate_h1"].items() if len(ps) > 1}
if dup_h1s:
    print(f"\n🔴 H1 dupliqués ({len(dup_h1s)}):")
    for h, ps in dup_h1s.items():
        print(f"    → \"{h[:60]}\" sur {len(ps)} pages:")
        for p in ps:
            print(f"      - {p}")

# 4. Summary scores
print("\n" + "=" * 80)
print("4. SCORES RÉCAPITULATIFS")
print("=" * 80)
total = len([r for r in results if not r.get("error")])
with_title = len([r for r in results if r.get("title") and 30 <= r["title_len"] <= 65])
with_meta = len([r for r in results if r.get("meta_desc") and 70 <= r["meta_desc_len"] <= 160])
with_h1 = len([r for r in results if r.get("h1")])
with_canonical = len([r for r in results if r.get("canonical") and r["canonical"] == DOMAIN + r.get("path","")])
with_schema = len([r for r in results if r.get("schemas")])
with_og = len([r for r in results if r.get("og_title") and r.get("og_desc")])

print(f"\n  Titles optimaux (30-65c):     {with_title}/{total} ({int(with_title/total*100)}%)")
print(f"  Meta desc optimales (70-160c): {with_meta}/{total} ({int(with_meta/total*100)}%)")
print(f"  H1 présent:                   {with_h1}/{total} ({int(with_h1/total*100)}%)")
print(f"  Canonical correcte:           {with_canonical}/{total} ({int(with_canonical/total*100)}%)")
print(f"  Schema.org:                   {with_schema}/{total} ({int(with_schema/total*100)}%)")
print(f"  OG tags complets:             {with_og}/{total} ({int(with_og/total*100)}%)")
print(f"  Indexation (GSC):             {len(INDEXED)}/{len(SITEMAP_PATHS)} ({int(len(INDEXED)/len(SITEMAP_PATHS)*100)}%)")

# Save detailed JSON
with open("/tmp/seo-audit-results.json", "w") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"\nRésultats détaillés: /tmp/seo-audit-results.json")
