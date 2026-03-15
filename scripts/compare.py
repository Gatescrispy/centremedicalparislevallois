#!/usr/bin/env python3
import json

def scores(path):
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
        'cls': audits.get('cumulative-layout-shift',{}).get('displayValue','?'),
    }

pre = scores('/tmp/lighthouse-audit/pre-deploy-accueil.json')
post = scores('/tmp/lighthouse-audit/post-accueil.json')

print("COMPARAISON PRE vs POST DEPLOY — Accueil (mobile)")
print("=" * 55)
print(f"{'Metrique':<25} {'PRE':>10} {'POST':>10} {'Delta':>10}")
print("-" * 55)
for k in ['perf','a11y','bp','seo','lcp','fcp','tbt','cls']:
    p = pre[k]
    o = post[k]
    if isinstance(p, int) and isinstance(o, int):
        delta = o - p
        sign = "+" if delta > 0 else ""
        print(f"{k:<25} {p:>10} {o:>10} {sign}{delta:>9}")
    else:
        print(f"{k:<25} {str(p):>10} {str(o):>10}")
