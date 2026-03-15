#!/bin/bash
BASE="/Users/cedrictantcheu/Documents/vtimagerie_v2_DEPLOY_FINAL_GTM_CONSENT_V2_20250724_025441 5/centremedicalparislevallois/pages"

sed -i '' 's|<link rel="preload" as="image" href="/Femme ophtalmologie.jpg" fetchpriority="high">|<link rel="preload" as="image" href="/Femme ophtalmologie.webp" type="image/webp" fetchpriority="high">|' "$BASE/ophtalmologie.html"

sed -i '' 's|<link rel="preload" as="image" href="/kine-hero.jpg" fetchpriority="high">|<link rel="preload" as="image" href="/kine-hero.webp" type="image/webp" fetchpriority="high">|' "$BASE/kinesitherapie.html"

sed -i '' 's|<link rel="preload" as="image" href="/angle-eleve-de-femme-medecin-ecrit-une-ordonnance-au-bureau.jpg" fetchpriority="high">|<link rel="preload" as="image" href="/angle-eleve-de-femme-medecin-ecrit-une-ordonnance-au-bureau.webp" type="image/webp" fetchpriority="high">|' "$BASE/medecine-generale.html"

sed -i '' 's|<link rel="preload" as="image" href="/Femme médecin vaccinant collègue.jpg" fetchpriority="high">|<link rel="preload" as="image" href="/Femme médecin vaccinant collègue.webp" type="image/webp" fetchpriority="high">|' "$BASE/soins-infirmiers.html"

echo "4 preloads updated to webp"
