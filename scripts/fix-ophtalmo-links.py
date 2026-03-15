#!/usr/bin/env python3
"""
Front 2a — Corriger tous les liens internes vers /ophtalmologue-levallois
au lieu de /pages/ophtalmologie.html pour concentrer l'autorité SEO.
"""
import os, glob

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Pages à ne PAS toucher pour le href (les sous-pages ophtalmo utilisent des chemins relatifs)
EXCLUDE_FILES = set()

# Compteurs
total_files = 0
total_replacements = 0

# 1. Remplacer href="/pages/ophtalmologie.html" → href="/ophtalmologue-levallois"
#    dans TOUS les fichiers HTML (sauf landing pages)
for pattern in ["**/*.html"]:
    for fpath in glob.glob(os.path.join(BASE, pattern), recursive=True):
        # Skip landing pages
        if "/landing/" in fpath:
            continue
        
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        original = content
        
        # Remplacement des href (avec et sans slash initial)
        content = content.replace('href="/pages/ophtalmologie.html"', 'href="/ophtalmologue-levallois"')
        content = content.replace("href='/pages/ophtalmologie.html'", "href='/ophtalmologue-levallois'")
        content = content.replace('href="pages/ophtalmologie.html"', 'href="/ophtalmologue-levallois"')
        content = content.replace("href='pages/ophtalmologie.html'", "href='/ophtalmologue-levallois'")
        
        # Aussi les liens avec /url: format (pour les composants)
        content = content.replace('/url: /pages/ophtalmologie.html', '/url: /ophtalmologue-levallois')
        
        if content != original:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            rel = os.path.relpath(fpath, BASE)
            count = len(original.split('pages/ophtalmologie.html')) - len(content.split('pages/ophtalmologie.html'))
            # Count by checking how many replacements happened
            r = 0
            for old in ['href="/pages/ophtalmologie.html"', "href='/pages/ophtalmologie.html'",
                         'href="pages/ophtalmologie.html"', "href='pages/ophtalmologie.html'"]:
                r += original.count(old)
            total_replacements += r
            total_files += 1
            print(f"  ✓ {rel} ({r} lien(s))")

# 2. Mettre à jour canonical et og:url sur ophtalmologie.html
ophtalmo = os.path.join(BASE, "pages", "ophtalmologie.html")
if os.path.exists(ophtalmo):
    with open(ophtalmo, "r", encoding="utf-8") as f:
        content = f.read()
    original = content
    
    # Canonical
    content = content.replace(
        'href="https://centremedicalparislevallois.fr/pages/ophtalmologie.html"',
        'href="https://centremedicalparislevallois.fr/ophtalmologue-levallois"'
    )
    # og:url  
    content = content.replace(
        'content="https://centremedicalparislevallois.fr/pages/ophtalmologie.html"',
        'content="https://centremedicalparislevallois.fr/ophtalmologue-levallois"'
    )
    
    if content != original:
        with open(ophtalmo, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ pages/ophtalmologie.html (canonical + og:url)")

print(f"\n{'='*50}")
print(f"  {total_files} fichiers modifiés, {total_replacements}+ liens corrigés")
print(f"  Tous pointent maintenant vers /ophtalmologue-levallois")
print(f"{'='*50}")
