#!/usr/bin/env python3
import json, os

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
        'cls': audits.get('cumulative-layout-shift',{}).get('displayValue','?'),
    }

pre = get_scores('/tmp/lighthouse-audit/Accueil.json')
post = get_scores('/tmp/lighthouse-final/Accueil.json')

print("AVANT vs APRES optimisations — Accueil (mobile)")
print("=" * 55)
print(f"{'Metrique':<25} {'AVANT':>10} {'APRES':>10} {'Delta':>10}")
print("-" * 55)
for k in ['perf','a11y','bp','seo']:
    p, o = pre[k], post[k]
    delta = o - p
    sign = "+" if delta > 0 else ""
    print(f"{k:<25} {p:>10} {o:>10} {sign}{delta:>9}")
for k in ['lcp','fcp','tbt','cls']:
    print(f"{k:<25} {str(pre[k]):>10} {str(post[k]):>10}")
