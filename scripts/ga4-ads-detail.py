#!/usr/bin/env python3
"""Détail du trafic Google Ads — campagnes, landing pages, timeline"""
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest, DateRange, Dimension, Metric, OrderBy,
    FilterExpression, Filter
)

client = BetaAnalyticsDataClient()
PROP = "properties/526394430"

def report(dims, mets, limit=20, order_met=None, dim_filter=None):
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

# 1. Campagnes
print("=" * 80)
print("1. CAMPAGNES GOOGLE ADS (30 derniers jours)")
print("=" * 80)
r = report(
    ["sessionCampaignName", "sessionGoogleAdsAdGroupName"],
    ["sessions", "activeUsers", "engagementRate"],
    order_met="sessions",
    dim_filter=FilterExpression(filter=Filter(
        field_name="sessionDefaultChannelGroup",
        string_filter=Filter.StringFilter(value="Paid Search", match_type=1)
    ))
)
hdr = "{:<40} {:<25} {:>6} {:>6} {:>7}".format("Campagne", "Ad Group", "Sess", "Users", "Engag")
print(hdr)
print("-" * 84)
for row in r.rows:
    camp = row.dimension_values[0].value[:39]
    ag = row.dimension_values[1].value[:24]
    s, u, e = row.metric_values[0].value, row.metric_values[1].value, row.metric_values[2].value
    eng = "{:.1f}%".format(float(e) * 100)
    print("{:<40} {:<25} {:>6} {:>6} {:>7}".format(camp, ag, s, u, eng))

# 2. Landing pages du trafic Ads
print()
print("=" * 80)
print("2. LANDING PAGES DU TRAFIC ADS")
print("=" * 80)
r = report(
    ["landingPagePlusQueryString"],
    ["sessions", "activeUsers", "bounceRate", "averageSessionDuration"],
    order_met="sessions",
    dim_filter=FilterExpression(filter=Filter(
        field_name="sessionDefaultChannelGroup",
        string_filter=Filter.StringFilter(value="Paid Search", match_type=1)
    ))
)
hdr = "{:<55} {:>6} {:>6} {:>7} {:>7}".format("Landing page", "Sess", "Users", "Rebond", "Duree")
print(hdr)
print("-" * 81)
for row in r.rows:
    lp = row.dimension_values[0].value[:54]
    s = row.metric_values[0].value
    u = row.metric_values[1].value
    b = "{:.1f}%".format(float(row.metric_values[2].value) * 100)
    dur = int(float(row.metric_values[3].value))
    d = "{}m{:02d}s".format(dur // 60, dur % 60)
    print("{:<55} {:>6} {:>6} {:>7} {:>7}".format(lp, s, u, b, d))

# 3. Timeline par jour - Ads vs Organic
print()
print("=" * 80)
print("3. EVOLUTION QUOTIDIENNE — Ads vs Organic (14 derniers jours)")
print("=" * 80)
r = report(
    ["date", "sessionDefaultChannelGroup"],
    ["sessions"],
    limit=100,
)
# Build day->channel map
data = {}
for row in r.rows:
    d = row.dimension_values[0].value
    ch = row.dimension_values[1].value
    s = int(row.metric_values[0].value)
    if d not in data:
        data[d] = {}
    data[d][ch] = s

hdr = "{:<12} {:>8} {:>10} {:>8} {:>8}".format("Date", "Ads", "Organic", "Direct", "Total")
print(hdr)
print("-" * 50)
for d in sorted(data.keys())[-14:]:
    date_fmt = "{}/{}/{}".format(d[6:8], d[4:6], d[:4])
    ads = data[d].get("Paid Search", 0)
    org = data[d].get("Organic Search", 0)
    direct = data[d].get("Direct", 0)
    total = sum(data[d].values())
    print("{:<12} {:>8} {:>10} {:>8} {:>8}".format(date_fmt, ads, org, direct, total))

# 4. Événements conversion du trafic Ads
print()
print("=" * 80)
print("4. CONVERSIONS DU TRAFIC ADS")
print("=" * 80)
r = report(
    ["eventName"],
    ["eventCount", "activeUsers"],
    order_met="eventCount",
    dim_filter=FilterExpression(filter=Filter(
        field_name="sessionDefaultChannelGroup",
        string_filter=Filter.StringFilter(value="Paid Search", match_type=1)
    ))
)
hdr = "{:<40} {:>8} {:>6}".format("Evenement", "Count", "Users")
print(hdr)
print("-" * 54)
for row in r.rows[:15]:
    ev = row.dimension_values[0].value
    c = row.metric_values[0].value
    u = row.metric_values[1].value
    print("{:<40} {:>8} {:>6}".format(ev, c, u))
