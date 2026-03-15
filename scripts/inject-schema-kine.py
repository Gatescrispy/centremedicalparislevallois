#!/usr/bin/env python3
"""
Ajoute un schema MedicalProcedure aux sous-pages kinésithérapie
qui n'ont que BreadcrumbList comme schema.
"""
import os
import re
import json

BASE = "/Users/cedrictantcheu/Documents/vtimagerie_v2_DEPLOY_FINAL_GTM_CONSENT_V2_20250724_025441 5/centremedicalparislevallois"

# Config pour chaque sous-page kiné: (filename, procedure_name, body_location, description)
KINE_PAGES = [
    ("premiere-consultation", "Première consultation de kinésithérapie", "Corps entier", "Bilan initial kinésithérapique : évaluation posturale, bilan articulaire et musculaire, définition du plan de traitement personnalisé."),
    ("consultation-suivi", "Consultation de suivi en kinésithérapie", "Corps entier", "Suivi régulier du traitement kinésithérapique : réévaluation des progrès, ajustement du protocole, exercices d'entretien."),
    ("reeducation-membres-superieurs", "Rééducation des membres supérieurs", "Épaule, coude, poignet, main", "Rééducation kinésithérapique des membres supérieurs : épaule gelée, tendinite, fracture, syndrome du canal carpien, prothèse."),
    ("reeducation-membres-inferieurs", "Rééducation des membres inférieurs", "Hanche, genou, cheville, pied", "Rééducation kinésithérapique des membres inférieurs : prothèse de hanche/genou, ligaments croisés, entorse, fracture."),
    ("reeducation-post-operatoire", "Rééducation post-opératoire", "Corps entier", "Rééducation après chirurgie orthopédique : prothèse articulaire, ligamentoplastie, ostéosynthèse. Récupération fonctionnelle."),
    ("rachis-cervical-dorsal-lombaire", "Rééducation du rachis", "Rachis cervical, dorsal, lombaire", "Kinésithérapie du rachis : cervicalgies, dorsalgies, lombalgies, hernies discales, sciatique. Renforcement et mobilisation."),
    ("rhumatologie", "Kinésithérapie en rhumatologie", "Articulations", "Prise en charge kinésithérapique des pathologies rhumatologiques : arthrose, polyarthrite, spondylarthrite, fibromyalgie."),
    ("scoliose-adolescent", "Kinésithérapie pour scoliose adolescent", "Rachis", "Rééducation de la scoliose chez l'adolescent : correction posturale, renforcement musculaire, méthode Schroth."),
    ("traumatisme-adulte", "Rééducation traumatologique adulte", "Corps entier", "Kinésithérapie après traumatisme chez l'adulte : fractures, entorses, luxations. Rééducation fonctionnelle et reprise d'activité."),
    ("traumatisme-adolescent", "Rééducation traumatologique adolescent", "Corps entier", "Kinésithérapie après traumatisme chez l'adolescent : fractures, entorses sportives. Prise en charge adaptée à la croissance."),
    ("drainage-lymphatique", "Drainage lymphatique manuel", "Membres supérieurs et inférieurs", "Drainage lymphatique manuel : lymphœdème, jambes lourdes, post-opératoire, post-cancer. Technique de Vodder."),
    ("femme-enceinte", "Kinésithérapie femme enceinte", "Dos, bassin, jambes", "Kinésithérapie prénatale : lombalgie, drainage des jambes lourdes, préparation à l'accouchement, rééducation périnéale."),
    ("electrotherapie", "Électrothérapie", "Zone ciblée", "Traitement par électrothérapie : TENS antalgique, électrostimulation musculaire, ultrasons. Complément aux soins manuels."),
    ("renforcement-abdominal", "Renforcement abdominal", "Abdomen, tronc", "Renforcement de la sangle abdominale : gainage, rééducation abdominale hypopressive, post-partum, prévention lombalgie."),
    ("seance-sans-ordonnance", "Séance de kinésithérapie sans ordonnance", "Corps entier", "Accès direct au kinésithérapeute sans ordonnance médicale : jusqu'à 8 séances. Bilan et traitement en autonomie."),
]

count = 0
for slug, name, body_loc, desc in KINE_PAGES:
    filepath = os.path.join(BASE, "pages", "kinesitherapie", f"{slug}.html")
    if not os.path.exists(filepath):
        print(f"  ❌ {slug}.html — fichier non trouvé")
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Skip if already has MedicalProcedure
    if '"MedicalProcedure"' in html:
        print(f"  ⏭️ {slug}.html — MedicalProcedure déjà présent")
        continue

    url = f"https://centremedicalparislevallois.fr/pages/kinesitherapie/{slug}.html"

    schema = {
        "@context": "https://schema.org",
        "@type": "MedicalProcedure",
        "name": name,
        "description": desc,
        "bodyLocation": body_loc,
        "procedureType": "https://schema.org/TherapeuticProcedure",
        "howPerformed": "Séance de kinésithérapie en cabinet avec un kinésithérapeute diplômé d'État",
        "preparation": "Apportez votre ordonnance médicale (si disponible), votre carte Vitale et des vêtements confortables.",
        "status": "https://schema.org/EventScheduled",
        "url": url,
        "provider": {
            "@type": "MedicalClinic",
            "name": "Centre Médical Paris-Levallois",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "60 Rue Victor Hugo",
                "addressLocality": "Levallois-Perret",
                "postalCode": "92300",
                "addressCountry": "FR"
            },
            "telephone": "+33180883716"
        }
    }

    schema_tag = f'\n    <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>'

    # Insert after the BreadcrumbList schema
    breadcrumb_end = html.find('</script>', html.find('"BreadcrumbList"'))
    if breadcrumb_end == -1:
        print(f"  ❌ {slug}.html — BreadcrumbList non trouvé")
        continue

    insert_pos = breadcrumb_end + len('</script>')
    html = html[:insert_pos] + schema_tag + html[insert_pos:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    count += 1
    print(f"  ✅ {slug}.html — MedicalProcedure ajouté")

# Also do soins-infirmiers sub-pages that don't have MedicalProcedure
SOINS_PAGES = [
    ("injection", "Injection intramusculaire et sous-cutanée", "Bras, cuisse, fesse", "Injection à domicile ou en cabinet : intramusculaire, sous-cutanée, intradermique. Traitement prescrit par votre médecin."),
    ("pansement-simple", "Pansement simple", "Zone de plaie", "Réfection de pansement simple : nettoyage, désinfection, protection. Suivi de cicatrisation des plaies superficielles."),
    ("pansement-post-chirurgical", "Pansement post-chirurgical", "Zone opératoire", "Soins de pansement post-chirurgical : surveillance de la cicatrisation, ablation des drains, prévention des infections."),
    ("retrait-fils-agrafes", "Retrait de fils et agrafes", "Zone de suture", "Retrait de fils de suture et agrafes chirurgicales : geste technique réalisé par un(e) infirmier(e) diplômé(e)."),
    ("surveillance-constantes", "Surveillance des constantes vitales", "Corps entier", "Surveillance infirmière des constantes : tension artérielle, glycémie, température, saturation en oxygène, poids."),
    ("test-antigenique", "Test antigénique rapide", "Nez", "Test antigénique rapide (TAG) Covid-19 et grippe : résultat en 15 minutes, certificat délivré. Sans rendez-vous."),
    ("bilan-prevention", "Bilan de prévention (Mon Bilan Prévention)", "Corps entier", "Bilan de prévention gratuit (Mon Bilan Prévention) : évaluation de santé personnalisée, dépistage, conseils de prévention."),
]

for slug, name, body_loc, desc in SOINS_PAGES:
    filepath = os.path.join(BASE, "pages", "soins-infirmiers", f"{slug}.html")
    if not os.path.exists(filepath):
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    if '"MedicalProcedure"' in html:
        print(f"  ⏭️ soins/{slug}.html — déjà présent")
        continue

    url = f"https://centremedicalparislevallois.fr/pages/soins-infirmiers/{slug}.html"

    schema = {
        "@context": "https://schema.org",
        "@type": "MedicalProcedure",
        "name": name,
        "description": desc,
        "bodyLocation": body_loc,
        "procedureType": "https://schema.org/TherapeuticProcedure",
        "url": url,
        "provider": {
            "@type": "MedicalClinic",
            "name": "Centre Médical Paris-Levallois",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "60 Rue Victor Hugo",
                "addressLocality": "Levallois-Perret",
                "postalCode": "92300",
                "addressCountry": "FR"
            },
            "telephone": "+33180883716"
        }
    }

    schema_tag = f'\n    <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>'

    breadcrumb_end = html.find('</script>', html.find('"BreadcrumbList"'))
    if breadcrumb_end == -1:
        continue

    insert_pos = breadcrumb_end + len('</script>')
    html = html[:insert_pos] + schema_tag + html[insert_pos:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    count += 1
    print(f"  ✅ soins/{slug}.html — MedicalProcedure ajouté")

# Also do medecine-generale sub-pages
MEDGEN_PAGES = [
    ("consultation", "Consultation de médecine générale", "Corps entier", "Consultation de médecine générale à Levallois-Perret : diagnostic, prescription, suivi, certificats médicaux. Secteur 1, tiers payant."),
    ("urgence", "Consultation d'urgence médecine générale", "Corps entier", "Consultation médicale d'urgence sans rendez-vous à Levallois-Perret : fièvre, douleur aiguë, infection. Médecin généraliste disponible."),
]

for slug, name, body_loc, desc in MEDGEN_PAGES:
    filepath = os.path.join(BASE, "pages", "medecine-generale", f"{slug}.html")
    if not os.path.exists(filepath):
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    if '"MedicalProcedure"' in html:
        print(f"  ⏭️ medgen/{slug}.html — déjà présent")
        continue

    url = f"https://centremedicalparislevallois.fr/pages/medecine-generale/{slug}.html"

    schema = {
        "@context": "https://schema.org",
        "@type": "MedicalProcedure",
        "name": name,
        "description": desc,
        "bodyLocation": body_loc,
        "procedureType": "https://schema.org/TherapeuticProcedure",
        "url": url,
        "provider": {
            "@type": "MedicalClinic",
            "name": "Centre Médical Paris-Levallois",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "60 Rue Victor Hugo",
                "addressLocality": "Levallois-Perret",
                "postalCode": "92300",
                "addressCountry": "FR"
            },
            "telephone": "+33180883716"
        }
    }

    schema_tag = f'\n    <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>'

    breadcrumb_end = html.find('</script>', html.find('"BreadcrumbList"'))
    if breadcrumb_end == -1:
        continue

    insert_pos = breadcrumb_end + len('</script>')
    html = html[:insert_pos] + schema_tag + html[insert_pos:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    count += 1
    print(f"  ✅ medgen/{slug}.html — MedicalProcedure ajouté")

print(f"\n{'='*60}")
print(f"MedicalProcedure schema ajouté sur {count} pages")
