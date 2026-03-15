#!/usr/bin/env python3
import json, os, glob

def get_scores(path):
    with open(path) as f:
        d = json.load(f)
    cats = d.get('categories', {})
    audits = d.get('audits', {})
    return {
        'perf': int(cats.get('performance',{}).get('score',0)*100),
        'a11y': int(cats.get('accessibility',{}).get('score',0)*100),
        'bp': int(cats.get('best-practices',{}).get('score',0)*100),
        'seo': int(cats.get('seo',{}).get('score',0)*100),
        'lcp': audits.get('largest-contentful-paint',{}).get('displayValue','?'),
        'fcp': audits.get('first-contentful-paint',{}).get('displayValue','?'),
        'tbt': audits.get('total-blocking-time',{}).get('displayValue','?'),
    }

pre_dir = '/tmp/lighthouse-audit'
post_dir = '/tmp/lighthouse-post'

pages = ['Accueil','Ophtalmologie','Kinesitherapie','Medecine-generale','Soins-infirmiers','Contact','Tarifs','FAQ']

print("=" * 90)
print("COMPARAISON PRE vs POST DEPLOY — Toutes pages (mobile)")
print("=" * 90)
print(f"\n{'Page':<20} | {'Perf':>8} | {'A11y':>8} | {'BP':>8} | {'SEO':>8} | {'LCP':>10}")
print(f"{'':20} | {'PRE>POST':>8} | {'PRE>POST':>8} | {'PRE>POST':>8} | {'PRE>POST':>8} | {'PRE>POST':>10}")
print("-" * 90)

totals_pre = {'perf':0,'a11y':0,'bp':0,'seo':0}
totals_post = {'perf':0,'a11y':0,'bp':0,'seo':0}
count = 0

for name in pages:
    pre_path = os.path.join(pre_dir, f"{name}.json")
    post_path = os.path.join(post_dir, f"{name}.json")
    if not os.path.exists(pre_path) or not os.path.exists(post_path):
        continue
    pre = get_scores(pre_path)
    post = get_scores(post_path)
    count += 1
    for k in totals_pre:
        totals_pre[k] += pre[k]
        totals_post[k] += post[k]

    def fmt(k):
        p, o = pre[k], post[k]
        delta = o - p
        arrow = "+" if delta > 0 else ""
        return f"{p}>{o}({arrow}{delta})"

    print(f"{name:<20} | {fmt('perf'):>8} | {fmt('a11y'):>8} | {fmt('bp'):>8} | {fmt('seo'):>8} | {pre['lcp']:>5}>{post['lcp']:>5}")

if count > 0:
    print("-" * 90)
    print(f"{'MOYENNE':<20} | ", end="")
    for k in ['perf','a11y','bp','seo']:
        avg_pre = totals_pre[k] // count
        avg_post = totals_post[k] // count
        delta = avg_post - avg_pre
        sign = "+" if delta > 0 else ""
        print(f"{avg_pre}>{avg_post}({sign}{delta}) | ", end="")
    print()
