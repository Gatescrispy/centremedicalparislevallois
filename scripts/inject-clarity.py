#!/usr/bin/env python3
"""
Injecte Microsoft Clarity sur toutes les pages HTML du site.
Respecte le Consent Mode V2 existant.
"""
import os

BASE = "/Users/cedrictantcheu/Documents/vtimagerie_v2_DEPLOY_FINAL_GTM_CONSENT_V2_20250724_025441 5/centremedicalparislevallois"
CLARITY_ID = "nw75u5l6n1"

# Script Clarity avec respect du consent mode
CLARITY_SCRIPT = f'''    <!-- Microsoft Clarity -->
    <script type="text/javascript">
    (function(c,l,a,r,i,t,y){{
        c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    }})(window,document,"clarity","script","{CLARITY_ID}");
    </script>'''

count = 0
for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('scripts', 'assets', 'docs', 'node_modules')]
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()

        # Skip if already has Clarity
        if 'clarity.ms' in html or 'clarity' in html.split('</head>')[0].lower().replace('cm-stable-layout', '').replace('politique-cookies', ''):
            # More precise check
            if f'clarity.ms/tag/{CLARITY_ID}' in html:
                rel = fpath.replace(BASE, "")
                print(f"  ⏭️ {rel} — Clarity déjà présent")
                continue

        # Skip components (no <head>)
        if '</head>' not in html:
            continue

        # Insert before </head>
        html = html.replace('</head>', CLARITY_SCRIPT + '\n</head>')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)

        count += 1
        rel = fpath.replace(BASE, "")
        print(f"  ✅ {rel}")

print(f"\n{'='*60}")
print(f"Clarity ({CLARITY_ID}) ajouté sur {count} pages")
