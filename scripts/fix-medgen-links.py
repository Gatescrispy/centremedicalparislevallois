#!/usr/bin/env python3
"""
Corriger tous les liens internes vers /medecin-generaliste-levallois
au lieu de /pages/medecine-generale.html pour concentrer l'autorité SEO.
"""
import os, glob

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

total_files = 0
total_replacements = 0

for fpath in glob.glob(os.path.join(BASE, "**/*.html"), recursive=True):
    if "/landing/" in fpath:
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    
    # Remplacement des href
    content = content.replace('href="/pages/medecine-generale.html"', 'href="/medecin-generaliste-levallois"')
    content = content.replace("href='/pages/medecine-generale.html'", "href='/medecin-generaliste-levallois'")
    content = content.replace('href="pages/medecine-generale.html"', 'href="/medecin-generaliste-levallois"')
    content = content.replace("href='pages/medecine-generale.html'", "href='/medecin-generaliste-levallois'")
    # Liens relatifs dans les sous-pages (ex: href="medecine-generale.html" dans pages/)
    # Ne PAS toucher les liens relatifs dans les sous-pages medecine-generale/ car ils pointent vers le parent
    if "/pages/medecine-generale/" not in fpath:
        content = content.replace('href="medecine-generale.html"', 'href="/medecin-generaliste-levallois"')
        content = content.replace("href='medecine-generale.html'", "href='/medecin-generaliste-levallois'")
    
    if content != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        rel = os.path.relpath(fpath, BASE)
        r = 0
        for old in ['href="/pages/medecine-generale.html"', "href='/pages/medecine-generale.html'",
                     'href="pages/medecine-generale.html"', "href='pages/medecine-generale.html'",
                     'href="medecine-generale.html"', "href='medecine-generale.html'"]:
            r += original.count(old)
        total_replacements += r
        total_files += 1
        print(f"  ✓ {rel} ({r} lien(s))")

# Mettre à jour canonical et og:url sur medecine-generale.html
medgen = os.path.join(BASE, "pages", "medecine-generale.html")
if os.path.exists(medgen):
    with open(medgen, "r", encoding="utf-8") as f:
        content = f.read()
    original = content
    
    content = content.replace(
        'href="https://centremedicalparislevallois.fr/pages/medecine-generale.html"',
        'href="https://centremedicalparislevallois.fr/medecin-generaliste-levallois"'
    )
    content = content.replace(
        'content="https://centremedicalparislevallois.fr/pages/medecine-generale.html"',
        'content="https://centremedicalparislevallois.fr/medecin-generaliste-levallois"'
    )
    # Schema URLs
    content = content.replace(
        '"url":"https://centremedicalparislevallois.fr/pages/medecine-generale.html"',
        '"url":"https://centremedicalparislevallois.fr/medecin-generaliste-levallois"'
    )
    content = content.replace(
        '"item":"https://centremedicalparislevallois.fr/pages/medecine-generale.html"',
        '"item":"https://centremedicalparislevallois.fr/medecin-generaliste-levallois"'
    )
    
    if content != original:
        with open(medgen, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ pages/medecine-generale.html (canonical + og:url + schema)")

print(f"\n{'='*50}")
print(f"  {total_files} fichiers modifiés, {total_replacements}+ liens corrigés")
print(f"  Tous pointent maintenant vers /medecin-generaliste-levallois")
print(f"{'='*50}")
