# 📝 Changelog - Centre Médical Paris-Levallois

Toutes les modifications notables du projet sont documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/).

---

## [1.0.0] - 2026-02-28

### 🎉 Release initiale

#### Ajouté
- **Page d'accueil** (`index.html`) complète avec :
  - Hero full-screen avec image de fond
  - Section RDV par spécialité (3 cartes)
  - Section présentation du centre
  - Section tarifs & remboursement
  - Section accès avec carte Google Maps
  - Section horaires détaillés
  - FAQ interactive (8 questions)
  - CTA final
  - Barre sticky mobile (Appeler / RDV)

- **Composants réutilisables** :
  - `components/header.html` - Navigation avec mega-menu
  - `components/footer.html` - Pied de page complet

- **Page le centre** (`pages/le-centre.html`)

- **Landing page Google Ads** (`pages/landing/google-ads.html`)

- **Analytics & Tracking** :
  - Google Tag Manager (GTM-525BNW8J)
  - Google Analytics 4 (G-MQ9CEHQVW3)
  - Conversions Google Ads configurées

- **SEO** :
  - Schema.org MedicalClinic, FAQPage
  - Balises meta optimisées
  - Open Graph et Twitter Cards

- **Documentation** :
  - README.md
  - PROJECT_CONTEXT.md
  - CONTRIBUTING.md
  - CHANGELOG.md

- **Workflows Cascade** (`.windsurf/workflows/`)

- **Configuration Git** :
  - .gitignore complet
  - Structure de branches

---

## [2.0.0] - 2026-03-02

### Ajouté
- **Pages examens** : arthroscanner, cone-beam, dentaire, doppler, échographie, IRM, mammographie, panoramique, radiologie, scanner (+ sous-pages détaillées)
- **Pages actualités** : système d'articles avec page listing et articles individuels
- **Pages landing** : 11 landing pages Google Ads pour différentes spécialités
- **Landing GTM** (`pages/landing/google-ads-gtm.html`) : version sans gtag inline, 100% GTM
- **Système FAQ** : workflow automatisé pour ajouter des questions

### Modifié
- **GTM** : Migration vers GTM-MQ2KK9XS (compte dédié centremedicalparislevallois.fr)
  - 5 tags configurés : GA4 Config, Ads Remarketing, Conversion Linker, Conversion Doctolib, Conversion Telephone
  - Consent Mode V2 intégré sur toutes les pages
  - Suppression gtag.js inline sur toutes les pages (sauf legacy google-ads.html)
- **GA4** : Migration vers G-XHP0ZF8ZSF (compte dédié)
  - Conservation données événements : 14 mois
  - Google Signals activé (307 régions)
  - Association Google Ads créée (397-970-4056)
  - Association Search Console créée (centremedicalparislevallois.fr)
  - Événements clés : `clic_doctolib` (1€) et `clic_telephone` (1€)
- **Tracking** : `cm-ads-tracking.js` supporte dual tracking (gtag direct + dataLayer.push GTM)
- **SEO** : Sitemap mis à jour, canonicals corrigés, breadcrumbs corrigés
- **.htaccess** : HTTPS, compression GZIP, cache, headers sécurité

### Corrigé
- GTM noscript manquant sur `pages/le-centre.html`
- Landing page noindex retirée du sitemap
- Doublons schema FAQ supprimés
- Placeholders JSON-LD corrigés

### Documentation
- `docs/AUDIT_GTM_FINAL.md` : Rapport audit GTM complet
- `docs/AUDIT_GA4.md` : Rapport audit GA4 complet

---

## [À venir]

### Planifié
- [ ] Pages spécialités (ophtalmologie, orthoptie, médecine générale, soins infirmiers)
- [ ] Page tarifs détaillés
- [ ] Page contact avec formulaire
- [ ] Page mentions légales
- [ ] Page politique de confidentialité
- [ ] Optimisation images (WebP, lazy loading avancé)
- [ ] PWA (manifest, service worker)

---

## Convention de versioning

- **MAJOR** (X.0.0) : Refonte majeure du site
- **MINOR** (0.X.0) : Nouvelles pages ou fonctionnalités
- **PATCH** (0.0.X) : Corrections de bugs, mises à jour de contenu

---

## Comment mettre à jour ce fichier

1. Ajouter une nouvelle section avec la date `## [X.X.X] - YYYY-MM-DD`
2. Catégoriser les changements :
   - `### Ajouté` - Nouvelles fonctionnalités
   - `### Modifié` - Changements dans le code existant
   - `### Corrigé` - Corrections de bugs
   - `### Supprimé` - Fonctionnalités retirées
   - `### Sécurité` - Correctifs de sécurité
3. Commiter avec `docs: mise à jour CHANGELOG`
