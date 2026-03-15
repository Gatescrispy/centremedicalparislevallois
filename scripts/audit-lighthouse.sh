#!/bin/bash
# Audit Lighthouse CLI — Centre Médical Paris-Levallois
OUTDIR="/tmp/lighthouse-audit"
mkdir -p "$OUTDIR"

PAGES=(
  "Accueil|https://centremedicalparislevallois.fr/"
  "Ophtalmologie|https://centremedicalparislevallois.fr/pages/ophtalmologie.html"
  "Kinesitherapie|https://centremedicalparislevallois.fr/pages/kinesitherapie.html"
  "Medecine-generale|https://centremedicalparislevallois.fr/pages/medecine-generale.html"
  "Soins-infirmiers|https://centremedicalparislevallois.fr/pages/soins-infirmiers.html"
  "Contact|https://centremedicalparislevallois.fr/pages/contact.html"
  "Tarifs|https://centremedicalparislevallois.fr/pages/tarifs.html"
  "FAQ|https://centremedicalparislevallois.fr/pages/faq.html"
)

echo "========================================"
echo "AUDIT LIGHTHOUSE — $(date)"
echo "========================================"

for entry in "${PAGES[@]}"; do
  IFS='|' read -r name url <<< "$entry"
  echo ""
  echo "--- $name ($url) ---"
  npx lighthouse "$url" \
    --chrome-flags="--headless --no-sandbox" \
    --output=json \
    --output-path="$OUTDIR/$name.json" \
    --only-categories=performance,accessibility,best-practices,seo \
    --form-factor=mobile \
    --quiet 2>/dev/null

  if [ -f "$OUTDIR/$name.json" ]; then
    python3 -c "
import json
with open('$OUTDIR/$name.json') as f:
    d = json.load(f)
cats = d.get('categories', {})
audits = d.get('audits', {})
perf = int(cats.get('performance',{}).get('score',0)*100)
a11y = int(cats.get('accessibility',{}).get('score',0)*100)
bp = int(cats.get('best-practices',{}).get('score',0)*100)
seo = int(cats.get('seo',{}).get('score',0)*100)
lcp = audits.get('largest-contentful-paint',{}).get('displayValue','?')
fcp = audits.get('first-contentful-paint',{}).get('displayValue','?')
tbt = audits.get('total-blocking-time',{}).get('displayValue','?')
cls_v = audits.get('cumulative-layout-shift',{}).get('displayValue','?')
si = audits.get('speed-index',{}).get('displayValue','?')
print(f'  Perf={perf} | A11y={a11y} | BP={bp} | SEO={seo}')
print(f'  LCP={lcp} | FCP={fcp} | TBT={tbt} | CLS={cls_v} | SI={si}')
opps = []
for k,v in audits.items():
    det = v.get('details',{})
    if det.get('type')=='opportunity' and v.get('score') is not None and v['score']<0.9:
        sav = det.get('overallSavingsMs',0)
        if sav > 0: opps.append((v['title'], int(sav)))
opps.sort(key=lambda x:x[1], reverse=True)
if opps:
    print('  Opportunites:')
    for t,s in opps[:5]:
        print(f'    - {t} (~{s}ms)')
"
  else
    echo "  ERREUR: pas de résultat"
  fi
done

echo ""
echo "========================================"
echo "SYNTHESE"
echo "========================================"
python3 -c "
import json, os, glob
files = sorted(glob.glob('$OUTDIR/*.json'))
print(f\"{'Page':<22} {'Perf':>5} {'A11y':>5} {'BP':>5} {'SEO':>5} {'LCP':>10} {'TBT':>10}\")
print('-'*65)
for f in files:
    name = os.path.basename(f).replace('.json','')
    with open(f) as fh:
        d = json.load(fh)
    cats = d.get('categories',{})
    audits = d.get('audits',{})
    perf = int(cats.get('performance',{}).get('score',0)*100)
    a11y = int(cats.get('accessibility',{}).get('score',0)*100)
    bp = int(cats.get('best-practices',{}).get('score',0)*100)
    seo = int(cats.get('seo',{}).get('score',0)*100)
    lcp = audits.get('largest-contentful-paint',{}).get('displayValue','?')
    tbt = audits.get('total-blocking-time',{}).get('displayValue','?')
    print(f'{name:<22} {perf:>5} {a11y:>5} {bp:>5} {seo:>5} {lcp:>10} {tbt:>10}')
"
echo ""
echo "Rapports JSON dans: $OUTDIR/"
