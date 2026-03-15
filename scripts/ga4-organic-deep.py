#!/usr/bin/env python3
"""Analyse approfondie du trafic organique — mots-clés, pages, comportement"""
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest, DateRange, Dimension, Metric, OrderBy,
    FilterExpression, Filter
)

client = BetaAnalyticsDataClient()
PROP = "properties/526394430"

ORG_FILTER = FilterExpression(filter=Filter(
    field_name="sessionDefaultChannelGroup",
    string_filter=Filter.StringFilter(value="Organic Search", match_type=1)
))

def report(dims, mets, limit=25, order_met=None, dim_filter=None):
    req = RunReportRequest(
        property=PROP,
        date_ranges=[DateRange(start_date="30daysAgo", end_date="yesterday")],
        dimensions=[Dimension(name=d) for d in dims],
        metrics=[Metric(name=m) for m in mets],
        limit=limit,
    )
    if order_met:
        req.order_bys = [OrderBy(metric=OrderBy.MetricOrderBy(metric_name=order_met), desc=True)]
    if dim_filter:
        req.dimension_filter = dim_filter
    return client.run_report(req)

def fmt_time(v):
    s = int(float(v))
    return "{}m{:02d}s".format(s // 60, s % 60)

def fmt_pct(v):
    return "{:.1f}%".format(float(v) * 100)

# ═══════════════════════════════════════════════════════════
print("=" * 75)
print("  ANALYSE TRAFIC ORGANIQUE — 30 derniers jours")
print("=" * 75)

# 1. Vue d'ensemble organique
print("\n1. VUE D'ENSEMBLE ORGANIQUE")
print("-" * 50)
r = report([], ["activeUsers", "sessions", "screenPageViews", "averageSessionDuration",
                "bounceRate", "engagementRate", "newUsers", "eventCount"], dim_filter=ORG_FILTER)
if r.rows:
    row = r.rows[0]
    vals = {r.metric_headers[i].name: row.metric_values[i].value for i in range(len(r.metric_headers))}
    print("  Utilisateurs:       {}".format(vals.get("activeUsers", "0")))
    print("  Nouveaux:           {}".format(vals.get("newUsers", "0")))
    print("  Sessions:           {}".format(vals.get("sessions", "0")))
    print("  Pages vues:         {}".format(vals.get("screenPageViews", "0")))
    print("  Duree moy:          {}".format(fmt_time(vals.get("averageSessionDuration", "0"))))
    print("  Taux rebond:        {}".format(fmt_pct(vals.get("bounceRate", "0"))))
    print("  Taux engagement:    {}".format(fmt_pct(vals.get("engagementRate", "0"))))

# 2. Landing pages organiques
print("\n2. PAGES D'ENTREE ORGANIQUES (par ou arrivent les visiteurs Google)")
print("-" * 75)
r = report(["landingPagePlusQueryString"],
           ["sessions", "activeUsers", "bounceRate", "averageSessionDuration", "engagementRate"],
           order_met="sessions", dim_filter=ORG_FILTER)
hdr = "{:<50} {:>5} {:>5} {:>7} {:>7} {:>7}".format("Page", "Sess", "User", "Rebond", "Engag", "Duree")
print("  " + hdr)
print("  " + "-" * 81)
for row in r.rows:
    lp = row.dimension_values[0].value[:49]
    v = [x.value for x in row.metric_values]
    print("  {:<50} {:>5} {:>5} {:>7} {:>7} {:>7}".format(
        lp, v[0], v[1], fmt_pct(v[2]), fmt_pct(v[4]), fmt_time(v[3])))

# 3. Pages vues depuis l'organique
print("\n3. PAGES LES PLUS CONSULTEES (organique)")
print("-" * 60)
r = report(["pagePath"],
           ["screenPageViews", "activeUsers", "averageSessionDuration"],
           order_met="screenPageViews", dim_filter=ORG_FILTER)
hdr = "{:<50} {:>6} {:>5} {:>7}".format("Page", "Vues", "User", "Duree")
print("  " + hdr)
print("  " + "-" * 68)
for row in r.rows:
    p = row.dimension_values[0].value[:49]
    v = [x.value for x in row.metric_values]
    print("  {:<50} {:>6} {:>5} {:>7}".format(p, v[0], v[1], fmt_time(v[2])))

# 4. Conversions organiques
print("\n4. CONVERSIONS DU TRAFIC ORGANIQUE")
print("-" * 50)
r = report(["eventName"],
           ["eventCount", "activeUsers"],
           order_met="eventCount", dim_filter=ORG_FILTER, limit=15)
hdr = "{:<35} {:>8} {:>6}".format("Evenement", "Count", "Users")
print("  " + hdr)
print("  " + "-" * 49)
for row in r.rows:
    ev = row.dimension_values[0].value
    v = [x.value for x in row.metric_values]
    print("  {:<35} {:>8} {:>6}".format(ev, v[0], v[1]))

# 5. Evolution organique jour par jour
print("\n5. TENDANCE ORGANIQUE (14 jours)")
print("-" * 40)
r = report(["date"], ["sessions", "activeUsers", "screenPageViews"],
           dim_filter=ORG_FILTER, limit=30)
rows = sorted(r.rows, key=lambda x: x.dimension_values[0].value)[-14:]
hdr = "{:<12} {:>6} {:>6} {:>6}".format("Date", "Sess", "Users", "Vues")
print("  " + hdr)
print("  " + "-" * 30)
for row in rows:
    d = row.dimension_values[0].value
    date_fmt = "{}/{}/{}".format(d[6:8], d[4:6], d[:4])
    v = [x.value for x in row.metric_values]
    print("  {:<12} {:>6} {:>6} {:>6}".format(date_fmt, v[0], v[1], v[2]))

# 6. Mots-clés organiques (si disponibles via searchTerm)
print("\n6. TERMES DE RECHERCHE GOOGLE (si disponibles)")
print("-" * 50)
try:
    r = report(["sessionGoogleAdsQuery"], ["sessions"],
               order_met="sessions", dim_filter=ORG_FILTER, limit=15)
    if r.rows:
        for row in r.rows:
            q = row.dimension_values[0].value
            s = row.metric_values[0].value
            print("  {} ({} sessions)".format(q, s))
    else:
        print("  (pas de donnees — les mots-cles organiques sont dans Search Console)")
except Exception as e:
    print("  (dimension non disponible — mots-cles dans Search Console uniquement)")

# 7. Villes - organique
print("\n7. TOP VILLES (organique)")
print("-" * 40)
r = report(["city"], ["activeUsers", "sessions", "engagementRate"],
           order_met="activeUsers", dim_filter=ORG_FILTER, limit=10)
hdr = "{:<25} {:>5} {:>5} {:>7}".format("Ville", "User", "Sess", "Engag")
print("  " + hdr)
print("  " + "-" * 42)
for row in r.rows:
    c = row.dimension_values[0].value[:24]
    v = [x.value for x in row.metric_values]
    print("  {:<25} {:>5} {:>5} {:>7}".format(c, v[0], v[1], fmt_pct(v[2])))

# 8. Appareils - organique
print("\n8. APPAREILS (organique)")
print("-" * 40)
r = report(["deviceCategory"], ["sessions", "bounceRate", "averageSessionDuration", "engagementRate"],
           order_met="sessions", dim_filter=ORG_FILTER)
hdr = "{:<15} {:>6} {:>7} {:>7} {:>7}".format("Appareil", "Sess", "Rebond", "Engag", "Duree")
print("  " + hdr)
print("  " + "-" * 42)
for row in r.rows:
    d = row.dimension_values[0].value
    v = [x.value for x in row.metric_values]
    print("  {:<15} {:>6} {:>7} {:>7} {:>7}".format(d, v[0], fmt_pct(v[1]), fmt_pct(v[3]), fmt_time(v[2])))

print("\n" + "=" * 75)
print("  FIN ANALYSE ORGANIQUE")
print("=" * 75)
