#!/bin/bash
BASE="/Users/cedrictantcheu/Documents/vtimagerie_v2_DEPLOY_FINAL_GTM_CONSENT_V2_20250724_025441 5/centremedicalparislevallois/pages"

sed -i '' 's|<img src="/Femme ophtalmologie.jpg" alt="Consultation ophtalmologique" class="rounded-2xl shadow-xl w-full object-cover" style="max-height: 350px;">|<picture><source srcset="/Femme ophtalmologie.webp" type="image/webp"><img src="/Femme ophtalmologie.jpg" alt="Consultation ophtalmologique" class="rounded-2xl shadow-xl w-full object-cover" style="max-height: 350px;" width="1200" height="800" loading="eager" fetchpriority="high"></picture>|' "$BASE/ophtalmologie.html"

sed -i '' 's|<img src="/kine-hero.jpg" alt="Séance de kinésithérapie" class="rounded-2xl shadow-xl w-full object-cover" style="max-height: 350px;">|<picture><source srcset="/kine-hero.webp" type="image/webp"><img src="/kine-hero.jpg" alt="Séance de kinésithérapie" class="rounded-2xl shadow-xl w-full object-cover" style="max-height: 350px;" width="3000" height="2000" loading="eager" fetchpriority="high"></picture>|' "$BASE/kinesitherapie.html"

sed -i '' 's|<img src="/angle-eleve-de-femme-medecin-ecrit-une-ordonnance-au-bureau.jpg" alt="Consultation médecine générale" class="rounded-2xl shadow-xl w-full object-cover" style="max-height: 350px;">|<picture><source srcset="/angle-eleve-de-femme-medecin-ecrit-une-ordonnance-au-bureau.webp" type="image/webp"><img src="/angle-eleve-de-femme-medecin-ecrit-une-ordonnance-au-bureau.jpg" alt="Consultation médecine générale" class="rounded-2xl shadow-xl w-full object-cover" style="max-height: 350px;" width="1200" height="800" loading="eager" fetchpriority="high"></picture>|' "$BASE/medecine-generale.html"

sed -i '' 's|<img src="/Femme médecin vaccinant collègue.jpg" alt="Soins infirmiers vaccination" class="rounded-2xl shadow-xl w-full object-cover" style="max-height: 350px;">|<picture><source srcset="/Femme médecin vaccinant collègue.webp" type="image/webp"><img src="/Femme médecin vaccinant collègue.jpg" alt="Soins infirmiers vaccination" class="rounded-2xl shadow-xl w-full object-cover" style="max-height: 350px;" width="1200" height="798" loading="eager" fetchpriority="high"></picture>|' "$BASE/soins-infirmiers.html"

echo "4 pages updated with picture/webp"
