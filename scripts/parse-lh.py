#!/usr/bin/env python3
import json, os, glob

for f in sorted(glob.glob('/tmp/lighthouse-audit/*.json')):
    name = os.path.basename(f).replace('.json', '')
    with open(f) as fh:
        d = json.load(fh)
    audits = d.get('audits', {})

    # LCP element
    lcp_el = audits.get('largest-contentful-paint-element', {})
    items = lcp_el.get('details', {}).get('items', [])
    el = items[0].get('node', {}).get('snippet', '?')[:120] if items else '?'

    # Render blocking
    rb = audits.get('render-blocking-resources', {})
    rb_items = rb.get('details', {}).get('items', [])
    rb_sav = rb.get('details', {}).get('overallSavingsMs', 0)

    # Unused JS
    uj = audits.get('unused-javascript', {})
    uj_items = uj.get('details', {}).get('items', [])

    # Unused CSS
    uc = audits.get('unused-css-rules', {})
    uc_items = uc.get('details', {}).get('items', [])

    # BP fails
    bp = []
    for k in ['errors-in-console', 'deprecations', 'image-aspect-ratio', 'image-size-responsive']:
        a = audits.get(k, {})
        if a.get('score') is not None and a['score'] < 1:
            bp.append(a.get('title', k))

    # A11y fails
    a11y = []
    cats = d.get('categories', {}).get('accessibility', {})
    for ref in cats.get('auditRefs', []):
        aid = ref.get('id', '')
        a = audits.get(aid, {})
        if a.get('score') is not None and a['score'] == 0:
            a11y.append(a.get('title', aid))

    print(f"=== {name} ===")
    print(f"  LCP element: {el}")
    print(f"  Render blocking: {len(rb_items)} ({rb_sav}ms)")
    for r in rb_items[:3]:
        url = r.get('url', '?')
        print(f"    - ...{url[-70:]}")
    print(f"  Unused JS: {len(uj_items)} fichiers")
    for u in uj_items[:3]:
        url = u.get('url', '?')
        kb = int(u.get('wastedBytes', 0) / 1024)
        print(f"    - ...{url[-70:]} ({kb}KB)")
    if uc_items:
        print(f"  Unused CSS: {len(uc_items)} fichiers")
        for u in uc_items[:2]:
            url = u.get('url', '?')
            kb = int(u.get('wastedBytes', 0) / 1024)
            print(f"    - ...{url[-70:]} ({kb}KB)")
    if bp:
        print(f"  BP fails: {', '.join(bp)}")
    if a11y:
        print(f"  A11y fails: {', '.join(a11y[:5])}")
    print()
