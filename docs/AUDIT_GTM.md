# Audit Google Tag Manager — Centre Médical Paris-Levallois

**Date** : 02/03/2026  
**Conteneur** : `GTM-MQ2KK9XS`  
**Compte** : Centre Médical Paris-Levallois  
**Email** : `djouma-livine@centremedicalparislevallois.fr`  

---

## 1. État actuel du conteneur

| Élément | Quantité |
|---------|----------|
| **Balises (Tags)** | 0 |
| **Déclencheurs (Triggers)** | 0 |
| **Variables custom** | 0 |
| **Variables intégrées** | 5 (Event, Page Hostname, Page Path, Page URL, Referrer) |
| **Versions publiées** | 1 ("Empty Container" — auto-générée) |

### Constat

**Le conteneur GTM est complètement vide.** Il a été créé et publié automatiquement le 28/02/2026, mais aucune balise n'a jamais été configurée.

### Alerte malware

Google affiche "Le système de détection de Google a signalé la présence d'un logiciel malveillant dans une balise de cette version." — C'est un **faux positif classique** sur les conteneurs vides ou nouvellement créés. Aucun risque réel.

---

## 2. Tracking actuel (sans GTM)

Tout le tracking est fait via **gtag.js en dur** dans le code HTML :

```
<head>
    <!-- GTM snippet (chargé mais ne fait RIEN) -->
    <script>(...GTM-MQ2KK9XS...)</script>

    <!-- Tracking réel via gtag.js -->
    <script async src="gtag/js?id=G-XHP0ZF8ZSF"></script>
    <script>
      gtag('config', 'G-XHP0ZF8ZSF');   // GA4
      gtag('config', 'AW-11456521545');  // Google Ads
    </script>
</head>
```

| Service | Méthode | Présence |
|---------|---------|----------|
| GA4 (`G-XHP0ZF8ZSF`) | gtag.js inline | 50/50 pages ✅ |
| Google Ads (`AW-11456521545`) | gtag.js inline | 49/50 pages ✅ |
| Conversions Ads (Doctolib + Tél) | `cm-ads-tracking.js` | 50/50 pages ✅ |
| Consent Mode V2 | `cm-consent-v2.js` | 50/50 pages ✅ |
| GTM snippet | inline | 50/50 pages (mais vide) |

---

## 3. Problèmes identifiés

### 🔴 Critique : Double chargement inutile

Le snippet GTM est chargé sur **toutes les pages** mais le conteneur est vide. Cela génère :
- 1 requête HTTP inutile vers `googletagmanager.com/gtm.js`
- ~80 Ko de JS téléchargé pour rien
- Aucune valeur ajoutée

### 🔴 Critique : Duplication GA4/Ads potentielle

Si des balises GA4 ou Ads sont ajoutées dans GTM à l'avenir **sans retirer le gtag.js inline**, chaque page enverra **des données en double** (une fois via gtag.js, une fois via GTM).

### 🟡 Absence de tracking avancé

GTM n'est pas utilisé pour les fonctionnalités avancées qu'il rend possible :
- Scroll tracking
- Outbound click tracking  
- Form submission tracking
- Video engagement tracking
- Custom event triggers

### 🟡 Consent Mode non lié à GTM

Le Consent Mode V2 est implémenté via `cm-consent-v2.js` directement avec gtag.js. GTM ne gère pas le consentement. C'est fonctionnel mais signifie que GTM ignorera les choix de consentement si des balises y sont ajoutées à l'avenir.

---

## 4. Deux options stratégiques

### Option A : Configurer GTM (recommandé)

Migrer tout le tracking de gtag.js inline vers GTM. C'est la best practice Google :

**Avantages :**
- Gestion centralisée de tous les tags
- Modifications sans toucher au code
- Consent Mode intégré nativement
- Tracking avancé (scroll, clics, vidéos)
- Debug mode intégré (Tag Assistant)
- Versioning et rollback

**Inconvénients :**
- Migration nécessaire
- Nécessite de retirer le gtag.js inline de toutes les pages

**Tags à créer dans GTM :**

| # | Tag | Type | Déclencheur |
|---|-----|------|-------------|
| 1 | GA4 Configuration | Google Analytics: GA4 Configuration | All Pages |
| 2 | Ads Configuration | Google Ads Remarketing | All Pages |
| 3 | Ads Conversion — Doctolib | Google Ads Conversion Tracking | Custom Event: clic_doctolib |
| 4 | Ads Conversion — Téléphone | Google Ads Conversion Tracking | Custom Event: clic_telephone |
| 5 | Consent Mode Defaults | Custom HTML | Consent Initialization |

### Option B : Retirer GTM

Supprimer le snippet GTM de toutes les pages et garder le tracking via gtag.js.

**Avantages :**
- Plus simple
- 1 requête HTTP en moins par page
- Pas de risque de double tracking

**Inconvénients :**
- Pas de gestion centralisée
- Modifications nécessitent de toucher au code
- Pas de debug mode
- Pas de versioning

---

## 5. Recommandation

**Je recommande l'Option A** (configurer GTM proprement).

Le site a déjà le snippet GTM sur toutes les pages. Il suffit de :
1. Créer les balises dans GTM
2. Retirer le gtag.js inline de toutes les pages
3. Publier le conteneur GTM

Cela permettra une gestion future beaucoup plus souple, surtout en vue de :
- La migration vers un compte Google Ads dédié
- L'ajout de tracking avancé (scroll, formulaires)
- La gestion du consentement directement dans GTM

---

## 6. Plan d'implémentation (si Option A choisie)

| Étape | Action |
|-------|--------|
| 1 | Créer les tags + triggers + variables dans GTM |
| 2 | Configurer Consent Mode dans GTM |
| 3 | Tester via GTM Preview mode |
| 4 | Retirer gtag.js inline + cm-ads-tracking.js de toutes les pages |
| 5 | Publier le conteneur GTM |
| 6 | Vérifier les conversions dans GA4 et Google Ads |

---

*Rapport généré le 02/03/2026 — Cascade*
