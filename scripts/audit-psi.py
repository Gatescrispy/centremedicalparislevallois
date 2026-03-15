#!/usr/bin/env python3
"""Audit PageSpeed Insights avec rate limiting"""
import urllib.request, json, time

PAGES = [
    ("Accueil", "https://centremedicalparislevallois.fr/"),
    ("Ophtalmologie", "https://centremedicalparislevallois.fr/pages/ophtalmologie.html"),
    ("Kinesitherapie", "https://centremedicalparislevallois.fr/pages/kinesitherapie.html"),
    ("Medecine generale", "https://centremedicalparislevallois.fr/pages/medecine-generale.html"),
    ("Soins infirmiers", "https://centremedicalparislevallois.fr/pages/soins-infirmiers.html"),
    ("Contact", "https://centremedicalparislevallois.fr/pages/contact.html"),
    ("Tarifs", "https://centremedicalparislevallois.fr/pages/tarifs.html"),
    ("FAQ", "https://centremedicalparislevallois.fr/pages/faq.html"),
]

API = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
results = []

for i, (name, url) in enumerate(PAGES):
    for strategy in ["mobile", "desktop"]:
        encoded = urllib.parse.quote(url, safe='')
        api_url = f"{API}?url={encoded}&strategy={strategy}&category=performance&category=accessibility&category=best-practices&category=seo"
        print(f"[{i*2 + (1 if strategy=='desktop' else 0) + 1}/{len(PAGES)*2}] {name} ({strategy})...", end=" ", flush=True)
        try:
            req = urllib.request.urlopen(api_url, timeout=120)
            d = json.loads(req.read())
            cats = d.get("lighthouseResult", {}).get("categories", {})
            audits = d.get("lighthouseResult", {}).get("audits", {})
            perf = int(cats.get("performance", {}).get("score", 0) * 100)
            a11y = int(cats.get("accessibility", {}).get("score", 0) * 100)
            bp = int(cats.get("best-practices", {}).get("score", 0) * 100)
            seo = int(cats.get("seo", {}).get("score", 0) * 100)
            lcp = audits.get("largest-contentful-paint", {}).get("displayValue", "?")
            fcp = audits.get("first-contentful-paint", {}).get("displayValue", "?")
            cls_val = audits.get("cumulative-layout-shift", {}).get("displayValue", "?")
            tbt = audits.get("total-blocking-time", {}).get("displayValue", "?")
            si = audits.get("speed-index", {}).get("displayValue", "?")
            tti = audits.get("interactive", {}).get("displayValue", "?")
            opps = []
            for k, v in audits.items():
                det = v.get("details", {})
                if det.get("type") == "opportunity" and v.get("score") is not None and v["score"] < 0.9:
                    sav = det.get("overallSavingsMs", 0)
                    if sav > 0:
                        opps.append((v["title"], v.get("displayValue", ""), int(sav)))
            opps.sort(key=lambda x: x[2], reverse=True)
            results.append({"name": name, "strategy": strategy, "perf": perf, "a11y": a11y, "bp": bp, "seo": seo, "lcp": lcp, "fcp": fcp, "cls": cls_val, "tbt": tbt, "si": si, "tti": tti, "opps": opps})
            print(f"Perf={perf} A11y={a11y} BP={bp} SEO={seo}")
        except Exception as e:
            print(f"ERREUR: {e}")
            results.append({"name": name, "strategy": strategy, "perf": "ERR", "a11y": "ERR", "bp": "ERR", "seo": "ERR", "opps": []})
        time.sleep(12)

print("\n" + "=" * 80)
print("SYNTHESE PAGESPEED INSIGHTS — Centre Medical Paris-Levallois")
print("=" * 80)
print(f"\n{'Page':<22} | {'Perf M':>6} {'Perf D':>6} | {'A11y':>5} {'BP':>5} {'SEO':>5} | {'LCP M':>8} {'FCP M':>8} {'TBT M':>8}")
print("-" * 95)
for i in range(0, len(results), 2):
    m = results[i]
    d = results[i+1] if i+1 < len(results) else {}
    print(f"{m['name']:<22} | {str(m.get('perf','')):>6} {str(d.get('perf','')):>6} | {str(m.get('a11y','')):>5} {str(m.get('bp','')):>5} {str(m.get('seo','')):>5} | {str(m.get('lcp','')):>8} {str(m.get('fcp','')):>8} {str(m.get('tbt','')):>8}")

print("\n" + "=" * 80)
print("TOP OPPORTUNITES D'AMELIORATION (mobile)")
print("=" * 80)
all_opps = {}
for r in results:
    if r["strategy"] == "mobile":
        for title, display, sav in r.get("opps", []):
            if title not in all_opps:
                all_opps[title] = {"count": 0, "total_ms": 0, "pages": []}
            all_opps[title]["count"] += 1
            all_opps[title]["total_ms"] += sav
            all_opps[title]["pages"].append(f"{r['name']} ({sav}ms)")

for title, data in sorted(all_opps.items(), key=lambda x: x[1]["total_ms"], reverse=True):
    print(f"\n  {title} (gain total: {data['total_ms']}ms sur {data['count']} pages)")
    for p in data["pages"]:
        print(f"    - {p}")

print("\nTermine!")
