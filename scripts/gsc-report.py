#!/usr/bin/env python3
"""Google Search Console — Rapport de performance organique"""
import google.auth
from googleapiclient.discovery import build

# Auth via Application Default Credentials (gcloud auth)
creds, project = google.auth.default(scopes=["https://www.googleapis.com/auth/webmasters.readonly"])
service = build("searchconsole", "v1", credentials=creds)

SITE = "sc-domain:centremedicalparislevallois.fr"

def query_gsc(dimensions, row_limit=25, start="2026-02-13", end="2026-03-14"):
    body = {
        "startDate": start,
        "endDate": end,
        "dimensions": dimensions,
        "rowLimit": row_limit,
        "dataState": "all"
    }
    return service.searchanalytics().query(siteUrl=SITE, body=body).execute()

def fmt_pos(v):
    return "{:.1f}".format(v)

def fmt_ctr(v):
    return "{:.1f}%".format(v * 100)

# ═══════════════════════════════════════════════════════
print("=" * 80)
print("  GOOGLE SEARCH CONSOLE — 30 derniers jours")
print("  Site: {}".format(SITE))
print("=" * 80)

# 1. Requêtes top
print("\n1. TOP REQUETES (par clics)")
print("-" * 80)
r = query_gsc(["query"])
hdr = "{:<50} {:>5} {:>8} {:>6} {:>6}".format("Requete", "Clics", "Impress", "CTR", "Pos")
print("  " + hdr)
print("  " + "-" * 75)
if "rows" in r:
    for row in r["rows"]:
        q = row["keys"][0][:49]
        c = row["clicks"]
        imp = row["impressions"]
        ctr = fmt_ctr(row["ctr"])
        pos = fmt_pos(row["position"])
        print("  {:<50} {:>5} {:>8} {:>6} {:>6}".format(q, c, imp, ctr, pos))
else:
    print("  (aucune donnée)")

# 2. Pages top
print("\n2. TOP PAGES (par clics)")
print("-" * 80)
r = query_gsc(["page"])
hdr = "{:<55} {:>5} {:>8} {:>6} {:>6}".format("Page", "Clics", "Impress", "CTR", "Pos")
print("  " + hdr)
print("  " + "-" * 80)
if "rows" in r:
    for row in r["rows"]:
        p = row["keys"][0].replace("https://centremedicalparislevallois.fr", "")[:54]
        c = row["clicks"]
        imp = row["impressions"]
        ctr = fmt_ctr(row["ctr"])
        pos = fmt_pos(row["position"])
        print("  {:<55} {:>5} {:>8} {:>6} {:>6}".format(p, c, imp, ctr, pos))
else:
    print("  (aucune donnée)")

# 3. Requêtes par page (croisé)
print("\n3. TOP REQUETES PAR PAGE (clics > 0)")
print("-" * 80)
r = query_gsc(["page", "query"], row_limit=50)
if "rows" in r:
    current_page = None
    for row in sorted(r["rows"], key=lambda x: (x["keys"][0], -x["clicks"])):
        page = row["keys"][0].replace("https://centremedicalparislevallois.fr", "")
        q = row["keys"][1]
        c = row["clicks"]
        imp = row["impressions"]
        pos = fmt_pos(row["position"])
        if c > 0:
            if page != current_page:
                print("\n  --- {} ---".format(page[:70]))
                current_page = page
            print("    {:<45} {:>3} clics {:>6} imp  pos {:>5}".format(q[:44], c, imp, pos))
else:
    print("  (aucune donnée)")

# 4. Appareils
print("\n\n4. APPAREILS")
print("-" * 50)
r = query_gsc(["device"])
if "rows" in r:
    hdr = "{:<15} {:>5} {:>8} {:>6} {:>6}".format("Appareil", "Clics", "Impress", "CTR", "Pos")
    print("  " + hdr)
    for row in r["rows"]:
        d = row["keys"][0]
        print("  {:<15} {:>5} {:>8} {:>6} {:>6}".format(d, row["clicks"], row["impressions"], fmt_ctr(row["ctr"]), fmt_pos(row["position"])))
else:
    print("  (aucune donnée)")

# 5. Pays
print("\n5. PAYS")
print("-" * 50)
r = query_gsc(["country"], row_limit=10)
if "rows" in r:
    for row in r["rows"]:
        print("  {} — {} clics, {} impressions".format(row["keys"][0], row["clicks"], row["impressions"]))
else:
    print("  (aucune donnée)")

# 6. Evolution par semaine
print("\n6. EVOLUTION HEBDOMADAIRE")
print("-" * 50)
r = query_gsc(["date"], row_limit=100, start="2026-01-13", end="2026-03-14")
if "rows" in r:
    # Group by week
    weeks = {}
    for row in sorted(r["rows"], key=lambda x: x["keys"][0]):
        date = row["keys"][0]
        # ISO week
        from datetime import datetime
        dt = datetime.strptime(date, "%Y-%m-%d")
        week = dt.strftime("%Y-W%V")
        if week not in weeks:
            weeks[week] = {"clicks": 0, "impressions": 0}
        weeks[week]["clicks"] += row["clicks"]
        weeks[week]["impressions"] += row["impressions"]
    
    hdr = "{:<12} {:>6} {:>10}".format("Semaine", "Clics", "Impressions")
    print("  " + hdr)
    print("  " + "-" * 28)
    for w in sorted(weeks.keys()):
        print("  {:<12} {:>6} {:>10}".format(w, weeks[w]["clicks"], weeks[w]["impressions"]))
else:
    print("  (aucune donnée)")

# 7. Opportunités : forte impression, faible CTR
print("\n7. OPPORTUNITES (forte impression, faible CTR — positions 5-20)")
print("-" * 80)
r = query_gsc(["query"], row_limit=100)
if "rows" in r:
    opps = [row for row in r["rows"] if 5 <= row["position"] <= 20 and row["impressions"] >= 5]
    opps.sort(key=lambda x: x["impressions"], reverse=True)
    hdr = "{:<50} {:>5} {:>8} {:>6} {:>6}".format("Requete", "Clics", "Impress", "CTR", "Pos")
    print("  " + hdr)
    print("  " + "-" * 75)
    for row in opps[:15]:
        q = row["keys"][0][:49]
        print("  {:<50} {:>5} {:>8} {:>6} {:>6}".format(q, row["clicks"], row["impressions"], fmt_ctr(row["ctr"]), fmt_pos(row["position"])))
    if not opps:
        print("  (aucune opportunité détectée)")
else:
    print("  (aucune donnée)")

print("\n" + "=" * 80)
print("  FIN RAPPORT GSC")
print("=" * 80)
