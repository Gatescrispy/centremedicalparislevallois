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
