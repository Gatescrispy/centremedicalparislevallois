#!/usr/bin/env python3
"""
Injecte un bloc de liens internes statiques avant le footer-placeholder
sur toutes les pages HTML du site.
"""
import os
import re

BASE = "/Users/cedrictantcheu/Documents/vtimagerie_v2_DEPLOY_FINAL_GTM_CONSENT_V2_20250724_025441 5/centremedicalparislevallois"

# Spécialités
SPECIALITES = [
    ("/pages/ophtalmologie.html", "Ophtalmologie", "fa-eye"),
    ("/pages/medecine-generale.html", "Médecine générale", "fa-stethoscope"),
    ("/pages/kinesitherapie.html", "Kinésithérapie", "fa-hands"),
    ("/pages/soins-infirmiers.html", "Soins infirmiers", "fa-syringe"),
]

# Infos pratiques
INFOS = [
    ("/pages/tarifs.html", "Tarifs & remboursement"),
    ("/pages/acces-horaires.html", "Accès & Horaires"),
    ("/pages/le-centre.html", "Le centre"),
    ("/pages/contact.html", "Contact"),
    ("/pages/faq.html", "Questions fréquentes"),
]

# Sous-pages par spécialité
KINE_SUBPAGES = [
    ("/pages/kinesitherapie/premiere-consultation.html", "Première consultation"),
    ("/pages/kinesitherapie/consultation-suivi.html", "Consultation de suivi"),
    ("/pages/kinesitherapie/reeducation-membres-superieurs.html", "Rééducation membres supérieurs"),
    ("/pages/kinesitherapie/reeducation-membres-inferieurs.html", "Rééducation membres inférieurs"),
    ("/pages/kinesitherapie/reeducation-post-operatoire.html", "Rééducation post-opératoire"),
    ("/pages/kinesitherapie/rachis-cervical-dorsal-lombaire.html", "Rachis cervical, dorsal, lombaire"),
    ("/pages/kinesitherapie/rhumatologie.html", "Rhumatologie"),
    ("/pages/kinesitherapie/scoliose-adolescent.html", "Scoliose adolescent"),
    ("/pages/kinesitherapie/traumatisme-adulte.html", "Traumatisme adulte"),
    ("/pages/kinesitherapie/traumatisme-adolescent.html", "Traumatisme adolescent"),
    ("/pages/kinesitherapie/drainage-lymphatique.html", "Drainage lymphatique"),
    ("/pages/kinesitherapie/femme-enceinte.html", "Femme enceinte"),
    ("/pages/kinesitherapie/electrotherapie.html", "Électrothérapie"),
    ("/pages/kinesitherapie/renforcement-abdominal.html", "Renforcement abdominal"),
    ("/pages/kinesitherapie/seance-sans-ordonnance.html", "Séance sans ordonnance"),
]

OPHTALMO_SUBPAGES = [
    ("/pages/ophtalmologie/premiere-consultation.html", "Première consultation"),
    ("/pages/ophtalmologie/premiere-consultation-enfant.html", "Consultation enfant"),
    ("/pages/ophtalmologie/consultation-suivi.html", "Consultation de suivi"),
    ("/pages/ophtalmologie/renouvellement-lunettes-lentilles.html", "Lunettes & lentilles"),
    ("/pages/ophtalmologie/champ-visuel-humphrey.html", "Champ visuel Humphrey"),
    ("/pages/ophtalmologie/urgence.html", "Urgence ophtalmologique"),
]

SOINS_SUBPAGES = [
    ("/pages/soins-infirmiers/vaccination-adulte.html", "Vaccination adulte"),
    ("/pages/soins-infirmiers/vaccination-pediatrique.html", "Vaccination pédiatrique"),
    ("/pages/soins-infirmiers/bilan-sanguin-ecbu.html", "Bilan sanguin & ECBU"),
    ("/pages/soins-infirmiers/injection.html", "Injection"),
    ("/pages/soins-infirmiers/pansement-simple.html", "Pansement simple"),
    ("/pages/soins-infirmiers/pansement-post-chirurgical.html", "Pansement post-chirurgical"),
    ("/pages/soins-infirmiers/retrait-fils-agrafes.html", "Retrait fils & agrafes"),
    ("/pages/soins-infirmiers/surveillance-constantes.html", "Surveillance constantes"),
    ("/pages/soins-infirmiers/test-antigenique.html", "Test antigénique"),
    ("/pages/soins-infirmiers/bilan-prevention.html", "Bilan prévention"),
]

MEDGEN_SUBPAGES = [
    ("/pages/medecine-generale/consultation.html", "Consultation"),
    ("/pages/medecine-generale/urgence.html", "Urgence"),
]

def get_page_type(filepath):
    """Determine page type from filepath."""
    rel = filepath.replace(BASE, "").replace("\\", "/")
    if rel == "/index.html":
        return "home", rel
    if "/kinesitherapie/" in rel and rel != "/pages/kinesitherapie.html":
        return "kine_sub", rel
    if "/ophtalmologie/" in rel and rel != "/pages/ophtalmologie.html":
        return "ophtalmo_sub", rel
    if "/soins-infirmiers/" in rel and rel != "/pages/soins-infirmiers.html":
        return "soins_sub", rel
    if "/medecine-generale/" in rel and rel != "/pages/medecine-generale.html":
        return "medgen_sub", rel
    if "/landing/" in rel:
        return "landing", rel
    return "main", rel

def get_sibling_links(page_type, current_path):
    """Get sibling links for sub-pages."""
    mapping = {
        "kine_sub": ("Soins de kinésithérapie", KINE_SUBPAGES),
        "ophtalmo_sub": ("Soins d'ophtalmologie", OPHTALMO_SUBPAGES),
        "soins_sub": ("Soins infirmiers", SOINS_SUBPAGES),
        "medgen_sub": ("Médecine générale", MEDGEN_SUBPAGES),
    }
    if page_type not in mapping:
        return None, []
    title, pages = mapping[page_type]
    # Exclude current page, limit to 8
    siblings = [(p, n) for p, n in pages if p != current_path][:8]
    return title, siblings

def build_links_block(page_type, current_path):
    """Build the internal links HTML block."""
    # Column 1: Spécialités
    spec_links = ""
    for href, name, icon in SPECIALITES:
        if href == current_path:
            spec_links += f'<li class="font-medium" style="color:#00a7de"><i class="fas {icon} mr-1"></i> {name}</li>\n'
        else:
            spec_links += f'<li><a href="{href}" style="color:#4a4a4a;text-decoration:none;" onmouseover="this.style.color=\'#00a7de\'" onmouseout="this.style.color=\'#4a4a4a\'"><i class="fas {icon} mr-1"></i> {name}</a></li>\n'

    # Column 2: Infos pratiques
    info_links = ""
    for href, name in INFOS:
        if href == current_path:
            info_links += f'<li class="font-medium" style="color:#00a7de">{name}</li>\n'
        else:
            info_links += f'<li><a href="{href}" style="color:#4a4a4a;text-decoration:none;" onmouseover="this.style.color=\'#00a7de\'" onmouseout="this.style.color=\'#4a4a4a\'">{name}</a></li>\n'

    # Column 3: Context-specific
    col3 = ""
    sib_title, siblings = get_sibling_links(page_type, current_path)
    if siblings:
        sib_links = ""
        for href, name in siblings:
            sib_links += f'<li><a href="{href}" style="color:#4a4a4a;text-decoration:none;" onmouseover="this.style.color=\'#00a7de\'" onmouseout="this.style.color=\'#4a4a4a\'">{name}</a></li>\n'
        col3 = f'''<div>
                <p class="font-bold mb-3" style="color:#252525">{sib_title}</p>
                <ul class="space-y-1">{sib_links}</ul>
            </div>'''
    else:
        # For main pages and home: link to urgences + equipe
        col3 = '''<div>
                <p class="font-bold mb-3" style="color:#252525">Aussi sur notre site</p>
                <ul class="space-y-1">
                    <li><a href="/pages/urgences.html" style="color:#4a4a4a;text-decoration:none;" onmouseover="this.style.color='#00a7de'" onmouseout="this.style.color='#4a4a4a'"><i class="fas fa-exclamation-triangle mr-1"></i> Urgences</a></li>
                    <li><a href="/pages/equipe.html" style="color:#4a4a4a;text-decoration:none;" onmouseover="this.style.color='#00a7de'" onmouseout="this.style.color='#4a4a4a'"><i class="fas fa-user-md mr-1"></i> Notre équipe</a></li>
                    <li><a href="/" style="color:#4a4a4a;text-decoration:none;" onmouseover="this.style.color='#00a7de'" onmouseout="this.style.color='#4a4a4a'"><i class="fas fa-home mr-1"></i> Accueil</a></li>
                </ul>
            </div>'''

    block = f'''
    <!-- SEO: Liens internes statiques -->
    <nav class="border-t" style="background-color:#f9fafb" aria-label="Navigation interne">
        <div class="max-w-6xl mx-auto px-4 py-8">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-sm">
            <div>
                <p class="font-bold mb-3" style="color:#252525">Nos spécialités</p>
                <ul class="space-y-1">{spec_links}</ul>
            </div>
            <div>
                <p class="font-bold mb-3" style="color:#252525">Informations pratiques</p>
                <ul class="space-y-1">{info_links}</ul>
            </div>
            {col3}
            </div>
        </div>
    </nav>'''
    return block

def process_file(filepath):
    """Inject internal links block into an HTML file."""
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Skip if already has internal links
    if "Navigation interne" in html:
        return False, "already has links"

    # Find insertion point: before footer-placeholder
    marker = '<div id="footer-placeholder">'
    if marker not in html:
        return False, "no footer placeholder"

    page_type, rel_path = get_page_type(filepath)
    
    # Skip landing pages
    if page_type == "landing":
        return False, "landing page (skip)"

    # Convert filepath-based path to URL path
    url_path = rel_path.replace("/index.html", "/")
    if not url_path.startswith("/"):
        url_path = "/" + url_path

    block = build_links_block(page_type, url_path)
    html = html.replace(marker, block + "\n    " + marker)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    return True, page_type

# Find all HTML files
count = 0
for root, dirs, files in os.walk(BASE):
    # Skip hidden dirs, scripts, assets, docs
    dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('scripts', 'assets', 'docs', 'node_modules')]
    for fname in files:
        if fname.endswith('.html'):
            fpath = os.path.join(root, fname)
            ok, info = process_file(fpath)
            status = "✅" if ok else "⏭️"
            rel = fpath.replace(BASE, "")
            if ok:
                count += 1
            print(f"  {status} {rel} ({info})")

print(f"\n{'='*60}")
print(f"Liens internes ajoutés sur {count} pages")
