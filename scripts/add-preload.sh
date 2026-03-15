#!/bin/bash
BASE="/Users/cedrictantcheu/Documents/vtimagerie_v2_DEPLOY_FINAL_GTM_CONSENT_V2_20250724_025441 5/centremedicalparislevallois/pages"

# ophtalmologie → /Femme ophtalmologie.jpg
sed -i '' 's|<link rel="stylesheet" href="assets/css/tailwind.css">|<link rel="preload" as="image" href="/Femme ophtalmologie.jpg" fetchpriority="high">\
    <link rel="stylesheet" href="assets/css/tailwind.css">|' "$BASE/ophtalmologie.html"

# kinesitherapie → /kine-hero.jpg
sed -i '' 's|<link rel="stylesheet" href="assets/css/tailwind.css">|<link rel="preload" as="image" href="/kine-hero.jpg" fetchpriority="high">\
    <link rel="stylesheet" href="assets/css/tailwind.css">|' "$BASE/kinesitherapie.html"

# medecine-generale → /angle-eleve-de-femme-medecin-ecrit-une-ordonnance-au-bureau.jpg
sed -i '' 's|<link rel="stylesheet" href="assets/css/tailwind.css">|<link rel="preload" as="image" href="/angle-eleve-de-femme-medecin-ecrit-une-ordonnance-au-bureau.jpg" fetchpriority="high">\
    <link rel="stylesheet" href="assets/css/tailwind.css">|' "$BASE/medecine-generale.html"

# soins-infirmiers → /Femme médecin vaccinant collègue.jpg
sed -i '' 's|<link rel="stylesheet" href="assets/css/tailwind.css">|<link rel="preload" as="image" href="/Femme médecin vaccinant collègue.jpg" fetchpriority="high">\
    <link rel="stylesheet" href="assets/css/tailwind.css">|' "$BASE/soins-infirmiers.html"

echo "Preload ajouté sur 4 pages spécialités"
