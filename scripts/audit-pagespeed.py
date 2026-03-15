#!/usr/bin/env python3
"""Audit PageSpeed Insights — Centre Médical Paris-Levallois"""
import urllib.request, json, sys, time

PAGES = [
    ("Accueil", "https://centremedicalparislevallois.fr/"),
    ("Ophtalmologie", "https://centremedicalparislevallois.fr/pages/ophtalmologie.html"),
    ("Kinésithérapie", "https://centremedicalparislevallois.fr/pages/kinesitherapie.html"),
    ("Médecine générale", "https://centremedicalparislevallois.fr/pages/medecine-generale.html"),
    ("Soins infirmiers", "https://centremedicalparislevallois.fr/pages/soins-infirmiers.html"),
    ("Contact", "https://centremedicalparislevallois.fr/pages/contact.html"),
    ("Tarifs", "https://centremedicalparislevallois.fr/pages/tarifs.html"),
    ("FAQ", "https://centremedicalparislevallois.fr/pages/faq.html"),
]

API = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

def audit(name, url, strategy="mobile"):
    params = f"?url={url}&strategy={strategy}&category=performance&category=accessibility&category=best-practices&category=seo"
    try:
        req = urllib.request.urlopen(API + params, timeout=120)
        d = json.loads(req.read())
    except Exception as e:
        print(f"  ERREUR: {e}")
        return None

    cats = d.get("lighthouseResult", {}).get("categories", {})
    audits = d.get("lighthouseResult", {}).get("audits", {})

    scores = {}
    for k, v in cats.items():
        scores[v["title"]] = int(v["score"] * 100)

    metrics = {}
    for m in ["largest-contentful-paint", "first-contentful-paint", "cumulative-layout-shift", "total-blocking-time", "speed-index", "interactive"]:
        a = audits.get(m, {})
        metrics[a.get("title", m)] = a.get("displayValue", "N/A")

    opps = []
    for k, v in audits.items():
        details = v.get("details", {})
        if details.get("type") == "opportunity" and v.get("score") is not None and v["score"] < 0.9:
            savings = details.get("overallSavingsMs", 0)
            if savings > 0:
                opps.append((v["title"], v.get("displayValue", ""), savings))

    return scores, metrics, opps

print("=" * 70)
print("AUDIT PAGESPEED INSIGHTS — Centre Médical Paris-Levallois")
print("=" * 70)

all_results = []
for name, url in PAGES:
    print(f"\n{'─' * 50}")
    print(f"📄 {name} ({strategy})" if False else f"Page: {name}")
    print(f"   {url}")
    print(f"{'─' * 50}")

    for strategy in ["mobile", "desktop"]:
        print(f"\n  [{strategy.upper()}]")
        result = audit(name, url, strategy)
        if not result:
            continue
        scores, metrics, opps = result
        all_results.append({"name": name, "url": url, "strategy": strategy, "scores": scores, "metrics": metrics, "opps": opps})

        for k, v in scores.items():
            emoji = "🟢" if v >= 90 else "🟠" if v >= 50 else "🔴"
            print(f"    {emoji} {k}: {v}")

        print("    Métriques:")
        for k, v in metrics.items():
            print(f"      {k}: {v}")

        if opps:
            opps.sort(key=lambda x: x[2], reverse=True)
            print("    Opportunités:")
            for title, display, savings in opps[:5]:
                print(f"      ⚡ {title}: {display} (gain ~{savings}ms)")

    time.sleep(2)

print(f"\n{'=' * 70}")
print("SYNTHÈSE")
print(f"{'=' * 70}")
print(f"\n{'Page':<25} {'Perf M':>7} {'Perf D':>7} {'A11y':>5} {'BP':>5} {'SEO':>5}")
print("-" * 60)
for i in range(0, len(all_results), 2):
    mob = all_results[i] if i < len(all_results) else None
    desk = all_results[i+1] if i+1 < len(all_results) else None
    if mob:
        name = mob["name"]
        pm = mob["scores"].get("Performance", "?")
        pd = desk["scores"].get("Performance", "?") if desk else "?"
        a11y = mob["scores"].get("Accessibility", "?")
        bp = mob["scores"].get("Best Practices", "?")
        seo = mob["scores"].get("SEO", "?")
        print(f"{name:<25} {pm:>7} {pd:>7} {a11y:>5} {bp:>5} {seo:>5}")

print("\nTerminé!")
