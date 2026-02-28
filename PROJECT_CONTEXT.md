# 📋 PROJECT CONTEXT - Centre Médical Paris-Levallois

> **Document de référence pour toute session de développement**  
> Dernière mise à jour : Février 2026

---

## 🎯 OBJECTIF DU PROJET

Site web vitrine pour le **Centre Médical Paris-Levallois**, un centre de santé pluridisciplinaire.

**Objectifs principaux :**
1. **Conversion** - Inciter les visiteurs à prendre RDV via Doctolib ou appeler
2. **SEO Local** - Être bien positionné sur "ophtalmologue Levallois", "médecin généraliste 92300", etc.
3. **Information** - Fournir les infos pratiques (horaires, accès, tarifs, spécialités)
4. **Confiance** - Rassurer les patients (conventionné, tiers payant, accessibilité)

---

## 🏥 INFORMATIONS DU CENTRE

### Coordonnées
- **Nom** : Centre Médical Paris-Levallois
- **Adresse** : 60 Rue Victor Hugo, 92300 Levallois-Perret
- **Téléphone** : 01 80 88 37 16
- **Email** : contact@centremedicalparislevallois.fr

### Horaires
| Jour | Horaires | Notes |
|------|----------|-------|
| Lundi | 9h - 00h | Garde de nuit (médecine générale) |
| Mardi | 9h - 19h | |
| Mercredi | 9h - 19h | |
| Jeudi | 9h - 00h | Garde de nuit (médecine générale) |
| Vendredi | 9h - 19h | |
| Samedi | 9h - 14h | |
| Dimanche | Fermé | |

### Spécialités
1. **Ophtalmologie** - Examen de la vue, dépistage pathologies, prescription lunettes/lentilles (dès 5 ans)
2. **Orthoptie** - Bilan orthoptique, rééducation visuelle, champ visuel (tous âges)
3. **Médecine générale** - Consultations, suivi médical, vaccinations, certificats (dès la naissance)
4. **Soins infirmiers** - Prises de sang, injections, pansements, vaccinations

### Informations pratiques
- **Conventionnement** : Secteur 1 (tarifs Sécurité Sociale)
- **Tiers payant** : Oui (selon droits ouverts AM + mutuelle)
- **Carte Vitale** : Acceptée avec télétransmission
- **CSS/CMU** : Acceptée
- **Paiements** : CB, espèces, chèques
- **Accessibilité** : PMR (rez-de-chaussée, entrée accessible)

### Transports à proximité
- **Train L** : Gare de Clichy-Levallois (4 min à pied) ⭐
- **Tramway T3b** : Marguerite Long (8 min)
- **RER C** : Péreire-Levallois (12 min)
- **Métro 3** : Louise Michel (12 min)
- **Bus** : 94, 341 (arrêt Alsace, 1 min), 84, 20, 174, 165

---

## 🔗 LIENS IMPORTANTS

### Production
- **Site web** : https://centremedicalparislevallois.fr/
- **Doctolib** : https://www.doctolib.fr/centre-de-sante/levallois-perret/centre-medical-paris-levallois

### Liens Doctolib par spécialité
- **Ophtalmologie/Orthoptie** : `...booking/motives?specialityId=4&telehealth=false&placeId=practice-714912`
- **Médecine générale** : `...booking/motives?specialityId=2&telehealth=false&placeId=practice-714912`
- **Soins infirmiers** : `...booking/motives?specialityId=30&telehealth=false&placeId=practice-714912`

---

## 🛠️ STACK TECHNIQUE

### Frontend
| Technologie | Version | Usage |
|-------------|---------|-------|
| HTML5 | - | Structure |
| TailwindCSS | 3.x | Styling (fichier compilé) |
| Alpine.js | 3.x | Interactions légères (FAQ accordion) |
| Font Awesome | 6.5.1 | Icônes |

### Analytics & Tracking
| Service | ID | Usage |
|---------|-----|-------|
| Google Tag Manager | GTM-525BNW8J | Container de tags |
| Google Analytics 4 | G-MQ9CEHQVW3 | Analytics |
| Google Ads | AW-11456521545 | Conversions |

### Hébergement
- **Hébergeur** : LWS (serveur mutualisé)
- **Protocole** : FTP/SFTP
- **SSL** : Let's Encrypt (via LWS)

---

## 🎨 DESIGN SYSTEM

### Palette de couleurs (basée sur le logo)
```css
:root {
    --primary-500: #00a7de;    /* Bleu logo - CTA, liens */
    --primary-600: #0090c0;    /* Bleu foncé - hover */
    --primary-700: #007ba3;    /* Bleu très foncé - active */
    --primary-50:  #e6f7fc;    /* Bleu très clair - backgrounds */
    --text-dark:   #252525;    /* Noir - texte principal */
    --text-secondary: #4a4a4a; /* Gris foncé - texte secondaire */
    --text-muted:  #6b6b6b;    /* Gris - texte tertiaire */
}
```

### Typographie
- **Police** : System fonts (font-sans de Tailwind)
- **Titres H1** : 3xl-6xl, bold, text-dark
- **Titres H2** : 2xl-3xl, bold, text-dark
- **Corps** : base-lg, text-secondary

### Composants réutilisables
- **btn-cta-primary** : Bouton principal bleu avec gradient
- **btn-cta-secondary** : Bouton secondaire blanc
- **specialty-card** : Carte de spécialité avec image et CTA
- **faq-item** : Accordion FAQ avec Alpine.js
- **info-chip** : Badge d'information (ex: "Carte Vitale acceptée")

---

## 📁 STRUCTURE DES FICHIERS

```
centremedicalparislevallois/
├── index.html                      # Page d'accueil (1259 lignes)
├── components/
│   ├── header.html                 # Navigation avec mega-menu
│   ├── header-new.html             # Version alternative (backup)
│   └── footer.html                 # Pied de page
├── pages/
│   ├── le-centre.html              # Page "À propos" (existante)
│   ├── landing/
│   │   └── google-ads.html         # Landing page Google Ads
│   └── specialites/                # À CRÉER
│       ├── ophtalmologie.html
│       ├── orthoptie.html
│       ├── medecine-generale.html
│       └── soins-infirmiers.html
├── assets/
│   ├── css/
│   │   └── tailwind.css            # Styles compilés (12 KB)
│   ├── images/                     # Images optimisées
│   └── js/                         # Scripts JS
├── .windsurf/
│   └── workflows/                  # Workflows Cascade
├── docs/                           # Documentation
└── [images à la racine]            # Images principales
```

---

## ⚠️ PAGES À CRÉER

Les pages suivantes sont référencées dans le header/footer mais n'existent pas encore :

### Priorité haute
- [ ] `/pages/specialites/ophtalmologie.html`
- [ ] `/pages/specialites/orthoptie.html`
- [ ] `/pages/specialites/medecine-generale.html`
- [ ] `/pages/specialites/soins-infirmiers.html`

### Priorité moyenne
- [ ] `/pages/tarifs.html`
- [ ] `/pages/contact.html`

### Priorité basse
- [ ] `/pages/urgences.html`
- [ ] `/pages/mentions-legales.html`
- [ ] `/pages/politique-confidentialite.html`

---

## 📊 SEO & SCHEMA.ORG

### Schema.org implémentés (index.html)
- **MedicalClinic** - Informations du centre
- **FAQPage** - Questions fréquentes
- **LocalBusiness** - SEO local

### Balises meta importantes
```html
<title>Centre Médical Paris-Levallois (92300) — RDV Ophtalmologie, Orthoptie, Médecine générale</title>
<meta name="description" content="Centre de santé au 60 Rue Victor Hugo, Levallois-Perret. RDV en ligne, horaires Lun-Sam, carte Vitale, tiers payant.">
<meta name="geo.region" content="FR-92">
<meta name="geo.placename" content="Levallois-Perret">
```

### Mots-clés cibles
- centre médical Levallois-Perret
- ophtalmologue Levallois / 92300
- orthoptiste Levallois-Perret
- médecin généraliste Levallois
- centre de santé conventionné secteur 1

---

## 🔄 CONVERSIONS GOOGLE ADS

### Événements de conversion configurés
```javascript
// RDV Doctolib
gtag('event', 'conversion', {
    'send_to': 'AW-11456521545/ypsQCO_RwuEbEMnK8tYq'
});

// Appel téléphonique
gtag('event', 'conversion', {
    'send_to': 'AW-11456521545/xTpdCNWFw-EbEMnK8tYq'
});
```

### DataLayer events
- `cta_footer_doctolib` - Clic RDV footer
- `cta_footer_call` - Clic appel footer
- `cta_sticky_doctolib` - Clic RDV barre sticky mobile
- `cta_sticky_call` - Clic appel barre sticky mobile

---

## 📝 NOTES DE DÉVELOPPEMENT

### Chargement des composants
Header et footer sont chargés dynamiquement via JavaScript :
```javascript
loadComponent('header-placeholder', './components/header.html');
loadComponent('footer-placeholder', './components/footer.html');
```

### Images
- Les images `-original.jpg` sont les versions haute résolution
- Les images sans suffixe sont optimisées pour le web
- Format recommandé : JPEG pour photos, PNG pour logos/icônes

### Mobile
- Barre sticky en bas sur mobile (< 768px) avec "Appeler" et "RDV"
- Safe area pour iPhone avec encoche (`env(safe-area-inset-bottom)`)
- Padding footer de 60px sur mobile pour la barre sticky

---

## 🚨 POINTS D'ATTENTION

1. **Doctolib** - Les liens de RDV utilisent des `specialityId` spécifiques, ne pas modifier
2. **GTM** - Ne pas supprimer le snippet GTM en haut du `<head>`
3. **Conversions** - Les fonctions `gtagSendEventDoctolib()` et `gtagSendEventTelephone()` sont essentielles
4. **Images** - Ne pas commiter les fichiers `.HEIC` ou `-original.jpg` (trop lourds)
5. **Header sticky** - Les ancres ont `scroll-margin-top: 100px` pour compenser le header

---

## 📞 SUPPORT

Pour toute question sur le projet, contacter le développeur ou consulter :
- Ce fichier `PROJECT_CONTEXT.md`
- Le fichier `CONTRIBUTING.md` pour les conventions
- Les workflows dans `.windsurf/workflows/`
