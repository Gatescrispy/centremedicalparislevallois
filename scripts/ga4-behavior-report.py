#!/usr/bin/env python3
"""
Rapport comportemental GA4 — Analyse détaillée du comportement utilisateur
sur centremedicalparislevallois.fr (30 derniers jours)
"""
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest, DateRange, Dimension, Metric, OrderBy, FilterExpression, Filter
)

PROPERTY_ID = "526394430"
client = BetaAnalyticsDataClient()

def run_report(dims, mets, order_by=None, limit=25, dim_filter=None):
    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        date_ranges=[DateRange(start_date="30daysAgo", end_date="yesterday")],
        dimensions=[Dimension(name=d) for d in dims],
        metrics=[Metric(name=m) for m in mets],
        limit=limit,
    )
    if order_by:
        request.order_bys = [order_by]
    if dim_filter:
        request.dimension_filter = dim_filter
    return client.run_report(request)

def fmt(val, is_pct=False, is_time=False):
    try:
        v = float(val)
        if is_pct:
            return f"{v*100:.1f}%"
        if is_time:
            m, s = divmod(int(v), 60)
            return f"{m}m{s:02d}s"
        if v == int(v):
            return str(int(v))
        return f"{v:.2f}"
    except:
        return val

# ═══════════════════════════════════════════════════════════
print("=" * 70)
print("  RAPPORT COMPORTEMENTAL GA4 — 30 derniers jours")
print("  centremedicalparislevallois.fr")
print("=" * 70)

# 1. Vue d'ensemble
print("\n📊 1. VUE D'ENSEMBLE")
print("-" * 50)
r = run_report([], ["activeUsers", "sessions", "screenPageViews", "averageSessionDuration", "bounceRate", "engagementRate", "newUsers", "eventCount"])
row = r.rows[0] if r.rows else None
if row:
    vals = {r.metric_headers[i].name: row.metric_values[i].value for i in range(len(r.metric_headers))}
    print(f"  Utilisateurs actifs:    {fmt(vals.get('activeUsers','0'))}")
    print(f"  Nouveaux utilisateurs:  {fmt(vals.get('newUsers','0'))}")
    print(f"  Sessions:               {fmt(vals.get('sessions','0'))}")
    print(f"  Pages vues:             {fmt(vals.get('screenPageViews','0'))}")
    print(f"  Durée moy. session:     {fmt(vals.get('averageSessionDuration','0'), is_time=True)}")
    print(f"  Taux de rebond:         {fmt(vals.get('bounceRate','0'), is_pct=True)}")
    print(f"  Taux d'engagement:      {fmt(vals.get('engagementRate','0'), is_pct=True)}")
    print(f"  Événements total:       {fmt(vals.get('eventCount','0'))}")

# 2. Top pages
print("\n📄 2. TOP PAGES (par vues)")
print("-" * 50)
r = run_report(
    ["pagePath"], 
    ["screenPageViews", "activeUsers", "averageSessionDuration", "bounceRate", "engagementRate"],
    order_by=OrderBy(metric=OrderBy.MetricOrderBy(metric_name="screenPageViews"), desc=True),
    limit=20
)
print(f"  {'Page':<55} {'Vues':>6} {'Users':>6} {'Durée':>7} {'Rebond':>7} {'Engag.':>7}")
for row in r.rows:
    path = row.dimension_values[0].value
    if len(path) > 54:
        path = path[:51] + "..."
    vals = [v.value for v in row.metric_values]
    print(f"  {path:<55} {fmt(vals[0]):>6} {fmt(vals[1]):>6} {fmt(vals[2], is_time=True):>7} {fmt(vals[3], is_pct=True):>7} {fmt(vals[4], is_pct=True):>7}")

# 3. Sources de trafic
print("\n🌐 3. SOURCES DE TRAFIC")
print("-" * 50)
r = run_report(
    ["sessionDefaultChannelGroup"],
    ["sessions", "activeUsers", "engagementRate", "averageSessionDuration"],
    order_by=OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True),
    limit=10
)
print(f"  {'Canal':<30} {'Sessions':>8} {'Users':>6} {'Engag.':>7} {'Durée':>7}")
for row in r.rows:
    ch = row.dimension_values[0].value
    vals = [v.value for v in row.metric_values]
    print(f"  {ch:<30} {fmt(vals[0]):>8} {fmt(vals[1]):>6} {fmt(vals[2], is_pct=True):>7} {fmt(vals[3], is_time=True):>7}")

# 4. Source / Medium détaillé
print("\n🔗 4. SOURCE / MEDIUM (top 10)")
print("-" * 50)
r = run_report(
    ["sessionSourceMedium"],
    ["sessions", "activeUsers", "engagementRate"],
    order_by=OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True),
    limit=10
)
print(f"  {'Source / Medium':<40} {'Sessions':>8} {'Users':>6} {'Engag.':>7}")
for row in r.rows:
    sm = row.dimension_values[0].value
    vals = [v.value for v in row.metric_values]
    print(f"  {sm:<40} {fmt(vals[0]):>8} {fmt(vals[1]):>6} {fmt(vals[2], is_pct=True):>7}")

# 5. Appareils
print("\n📱 5. APPAREILS")
print("-" * 50)
r = run_report(
    ["deviceCategory"],
    ["sessions", "activeUsers", "bounceRate", "averageSessionDuration"],
    order_by=OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)
)
print(f"  {'Appareil':<20} {'Sessions':>8} {'Users':>6} {'Rebond':>7} {'Durée':>7}")
for row in r.rows:
    dev = row.dimension_values[0].value
    vals = [v.value for v in row.metric_values]
    print(f"  {dev:<20} {fmt(vals[0]):>8} {fmt(vals[1]):>6} {fmt(vals[2], is_pct=True):>7} {fmt(vals[3], is_time=True):>7}")

# 6. Événements clés (conversions)
print("\n🎯 6. ÉVÉNEMENTS CLÉS (conversions)")
print("-" * 50)
r = run_report(
    ["eventName"],
    ["eventCount", "activeUsers"],
    order_by=OrderBy(metric=OrderBy.MetricOrderBy(metric_name="eventCount"), desc=True),
    limit=15
)
print(f"  {'Événement':<35} {'Count':>8} {'Users':>6}")
for row in r.rows:
    ev = row.dimension_values[0].value
    vals = [v.value for v in row.metric_values]
    print(f"  {ev:<35} {fmt(vals[0]):>8} {fmt(vals[1]):>6}")

# 7. Pages de sortie (où les gens quittent)
print("\n🚪 7. OÙ LES VISITEURS QUITTENT (taux de rebond par page)")
print("-" * 50)
r = run_report(
    ["pagePath"],
    ["bounceRate", "sessions", "activeUsers"],
    order_by=OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True),
    limit=15
)
print(f"  {'Page':<55} {'Rebond':>7} {'Sess.':>6}")
for row in r.rows:
    path = row.dimension_values[0].value
    if len(path) > 54:
        path = path[:51] + "..."
    vals = [v.value for v in row.metric_values]
    bounce = fmt(vals[0], is_pct=True)
    icon = "🔴" if float(vals[0]) > 0.7 else "🟡" if float(vals[0]) > 0.5 else "🟢"
    print(f"  {icon} {path:<53} {bounce:>7} {fmt(vals[1]):>6}")

# 8. Évolution jour par jour
print("\n📈 8. TENDANCE (7 derniers jours)")
print("-" * 50)
r = run_report(
    ["date"],
    ["activeUsers", "sessions", "screenPageViews"],
    order_by=OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name="date"), desc=False),
    limit=7
)
# Only last 7 days
rows = list(r.rows)[-7:]
print(f"  {'Date':<12} {'Users':>6} {'Sess.':>6} {'Vues':>6}")
for row in rows:
    d = row.dimension_values[0].value
    date_fmt = f"{d[6:8]}/{d[4:6]}/{d[:4]}"
    vals = [v.value for v in row.metric_values]
    print(f"  {date_fmt:<12} {fmt(vals[0]):>6} {fmt(vals[1]):>6} {fmt(vals[2]):>6}")

# 9. Landing pages
print("\n🏠 9. PAGES D'ENTRÉE (landing pages)")
print("-" * 50)
r = run_report(
    ["landingPagePlusQueryString"],
    ["sessions", "activeUsers", "bounceRate", "averageSessionDuration"],
    order_by=OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True),
    limit=15
)
print(f"  {'Page entree':<55} {'Sess.':>6} {'Rebond':>7} {'Duree':>7}")
for row in r.rows:
    path = row.dimension_values[0].value
    if len(path) > 54:
        path = path[:51] + "..."
    vals = [v.value for v in row.metric_values]
    print(f"  {path:<55} {fmt(vals[0]):>6} {fmt(vals[1], is_pct=True):>7} {fmt(vals[2], is_time=True):>7}")

# 10. Villes
print("\n📍 10. TOP VILLES")
print("-" * 50)
r = run_report(
    ["city"],
    ["activeUsers", "sessions", "engagementRate"],
    order_by=OrderBy(metric=OrderBy.MetricOrderBy(metric_name="activeUsers"), desc=True),
    limit=10
)
print(f"  {'Ville':<30} {'Users':>6} {'Sess.':>6} {'Engag.':>7}")
for row in r.rows:
    city = row.dimension_values[0].value
    vals = [v.value for v in row.metric_values]
    print(f"  {city:<30} {fmt(vals[0]):>6} {fmt(vals[1]):>6} {fmt(vals[2], is_pct=True):>7}")

print("\n" + "=" * 70)
print("  FIN DU RAPPORT")
print("=" * 70)
