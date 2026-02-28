# 🏗️ Architecture du site - Centre Médical Paris-Levallois

> Objectif principal : **Maximiser les conversions vers Doctolib**

---

## 📊 Vue d'ensemble

```
centremedicalparislevallois.fr/
│
├── 🏠 PAGES PRINCIPALES
│   ├── index.html                          # Accueil - Toutes spécialités
│   ├── le-centre.html                      # Présentation du centre
│   ├── contact.html                        # Contact & accès
│   ├── equipe.html                         # Notre équipe médicale
│   ├── tarifs.html                         # Tarifs & remboursements
│   └── urgences.html                       # Informations urgences
│
├── 📋 PAGES SPÉCIALITÉS (index par spécialité)
│   ├── soins-infirmiers.html               # Liste tous les motifs IDE
│   ├── kinesitherapie.html                 # Liste tous les motifs kiné
│   ├── medecine-generale.html              # Liste tous les motifs MG
│   └── ophtalmologie.html                  # Liste tous les motifs ophtalmo
│
├── 💉 PAGES MOTIFS - SOINS INFIRMIERS (13 motifs → 10 pages)
│   ├── soins-infirmiers/vaccination-adulte.html
│   ├── soins-infirmiers/vaccination-pediatrique.html
│   ├── soins-infirmiers/bilan-sanguin-ecbu.html
│   ├── soins-infirmiers/injection.html
│   ├── soins-infirmiers/pansement-simple.html
│   ├── soins-infirmiers/pansement-post-chirurgical.html
│   ├── soins-infirmiers/retrait-fils-agrafes.html
│   ├── soins-infirmiers/surveillance-constantes.html
│   ├── soins-infirmiers/test-antigenique.html
│   └── soins-infirmiers/bilan-prevention.html          # Groupe 18-75 ans
│
├── 🏃 PAGES MOTIFS - KINÉSITHÉRAPIE (18 motifs → 15 pages)
│   ├── kinesitherapie/premiere-consultation.html
│   ├── kinesitherapie/consultation-suivi.html
│   ├── kinesitherapie/reeducation-membres-superieurs.html
│   ├── kinesitherapie/reeducation-membres-inferieurs.html
│   ├── kinesitherapie/reeducation-post-operatoire.html
│   ├── kinesitherapie/rachis-cervical-dorsal-lombaire.html
│   ├── kinesitherapie/rhumatologie.html
│   ├── kinesitherapie/scoliose-adolescent.html
│   ├── kinesitherapie/traumatisme-adulte.html
│   ├── kinesitherapie/traumatisme-adolescent.html
│   ├── kinesitherapie/drainage-lymphatique.html        # Groupe post-op + femme enceinte
│   ├── kinesitherapie/femme-enceinte.html
│   ├── kinesitherapie/electrotherapie.html             # Groupe 3 types
│   ├── kinesitherapie/renforcement-abdominal.html
│   └── kinesitherapie/seance-sans-ordonnance.html
│
├── 🩺 PAGES MOTIFS - MÉDECINE GÉNÉRALE (2 motifs → 2 pages)
│   ├── medecine-generale/consultation.html
│   └── medecine-generale/urgence.html
│
├── 👁️ PAGES MOTIFS - OPHTALMOLOGIE (7 motifs → 6 pages)
│   ├── ophtalmologie/premiere-consultation.html
│   ├── ophtalmologie/premiere-consultation-enfant.html
│   ├── ophtalmologie/consultation-suivi.html
│   ├── ophtalmologie/renouvellement-lunettes-lentilles.html  # Groupe ophtalmo + orthoptiste
│   ├── ophtalmologie/champ-visuel-humphrey.html
│   └── ophtalmologie/urgence.html
│
├── 📄 PAGES LÉGALES
│   ├── mentions-legales.html
│   ├── politique-confidentialite.html
│   └── politique-cookies.html
│
└── 📁 ASSETS & TECHNIQUE
    ├── components/header.html
    ├── components/footer.html
    ├── sitemap.xml
    └── robots.txt
```

---

## 📈 Statistiques

| Type de page | Quantité |
|--------------|----------|
| Pages principales | 6 |
| Pages spécialités (index) | 4 |
| Pages motifs IDE | 10 |
| Pages motifs Kiné | 15 |
| Pages motifs MG | 2 |
| Pages motifs Ophtalmo | 6 |
| Pages légales | 3 |
| **TOTAL** | **46 pages** |

---

## 🎯 Stratégie SEO par page motif

### Structure type d'une page motif

```
┌─────────────────────────────────────────────┐
│  HERO                                       │
│  - Titre H1 : "[Motif] à Levallois-Perret" │
│  - Durée consultation                       │
│  - CTA : "Prendre RDV sur Doctolib" 🔵      │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│  DESCRIPTION (150-300 mots uniques)         │
│  - Qu'est-ce que c'est ?                    │
│  - Pour qui ?                               │
│  - Quand consulter ?                        │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│  DÉROULEMENT                                │
│  - Comment se passe la consultation         │
│  - Ce qu'il faut apporter                   │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│  TARIFS & REMBOURSEMENT                     │
│  - Prix                                     │
│  - Remboursement Sécu                       │
│  - Mutuelle / CMU                           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│  PRATICIEN                                  │
│  - Photo + nom                              │
│  - Spécialité                               │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│  FAQ (3-5 questions)                        │
│  - Questions spécifiques au motif           │
│  - Schema.org FAQPage                       │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│  CTA FINAL                                  │
│  - "Prenez rendez-vous maintenant" 🔵       │
│  - Lien direct vers motif Doctolib          │
└─────────────────────────────────────────────┘
```

---

## 🔗 Liens Doctolib par motif

### Soins Infirmiers
| Motif | URL Doctolib |
|-------|--------------|
| Vaccination adulte | `https://www.doctolib.fr/centre-de-sante/levallois-perret/centre-medical-paris-levallois/booking/motives?specialityId=30` |
| Vaccination pédiatrique | idem avec sélection motif |
| ... | ... |

### Kinésithérapie
| Motif | URL Doctolib |
|-------|--------------|
| Première consultation | `https://www.doctolib.fr/centre-de-sante/levallois-perret/centre-medical-paris-levallois/booking/motives?specialityId=9` |
| ... | ... |

### Médecine Générale
| Motif | URL Doctolib |
|-------|--------------|
| Consultation | `https://www.doctolib.fr/centre-de-sante/levallois-perret/centre-medical-paris-levallois/booking/motives?specialityId=2` |
| Urgence | idem |

### Ophtalmologie
| Motif | URL Doctolib |
|-------|--------------|
| Première consultation | `https://www.doctolib.fr/centre-de-sante/levallois-perret/centre-medical-paris-levallois/booking/motives?specialityId=4` |
| ... | ... |

---

## 🚀 Ordre de création recommandé

### Phase 1 : Pages principales (Priorité haute)
1. ✅ `index.html` (existe)
2. ✅ `le-centre.html` (existe)
3. ⬜ `contact.html`
4. ⬜ `equipe.html`
5. ⬜ `tarifs.html`

### Phase 2 : Pages spécialités index
1. ⬜ `soins-infirmiers.html`
2. ⬜ `kinesitherapie.html`
3. ⬜ `medecine-generale.html`
4. ⬜ `ophtalmologie.html`

### Phase 3 : Pages motifs à fort volume SEO
1. ⬜ `kinesitherapie/premiere-consultation.html`
2. ⬜ `ophtalmologie/premiere-consultation.html`
3. ⬜ `soins-infirmiers/vaccination-adulte.html`
4. ⬜ `medecine-generale/consultation.html`
5. ⬜ `kinesitherapie/reeducation-post-operatoire.html`

### Phase 4 : Toutes les autres pages motifs

### Phase 5 : Pages légales
1. ⬜ `mentions-legales.html`
2. ⬜ `politique-confidentialite.html`
3. ⬜ `politique-cookies.html`

---

## 📝 Notes importantes

1. **Chaque page motif** doit avoir un lien Doctolib direct vers le bon motif
2. **Contenu unique** : minimum 150 mots par page pour éviter le thin content
3. **Schema.org** : MedicalClinic + FAQPage sur chaque page
4. **Mobile-first** : CTA sticky en bas de page sur mobile
5. **Tracking** : Event GA4 pour chaque clic vers Doctolib
