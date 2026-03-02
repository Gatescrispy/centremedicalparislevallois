# AUDIT SEA — Centre Médical Paris-Levallois

**Date** : 2 mars 2026  
**Landing page** : `pages/landing/google-ads.html`  
**Compte Google Ads actuel** : `AW-11456521545` (VT Imagerie)  
**GTM** : `GTM-MQ2KK9XS` | **GA4** : `G-XHP0ZF8ZSF`

---

## 1. ÉTAT ACTUEL DU TRACKING

### 1.1 Configuration gtag sur les 49 pages

| Élément | Présent | Pages |
|---------|---------|-------|
| GTM `GTM-MQ2KK9XS` | ✅ | 49/49 |
| GA4 `G-XHP0ZF8ZSF` | ✅ | 49/49 |
| Ads `AW-11456521545` | ✅ | 49/49 |
| `gtagSendEventDoctolib()` | ⚠️ | 3/49 (index, le-centre, google-ads) |
| `gtagSendEventTelephone()` | ⚠️ | 3/49 (index, le-centre, google-ads) |

### 1.2 Conversion IDs (VT Imagerie)

| Conversion | Label | send_to |
|------------|-------|---------|
| RDV Doctolib | `ypsQCO_RwuEbEMnK8tYq` | `AW-11456521545/ypsQCO_RwuEbEMnK8tYq` |
| Appel téléphone | `xTpdCNWFw-EbEMnK8tYq` | `AW-11456521545/xTpdCNWFw-EbEMnK8tYq` |

---

## 2. PROBLÈMES IDENTIFIÉS

### 🔴 CRITIQUES

#### 2.1 Consent Mode V2 ABSENT
- **Aucune page** n'implémente Google Consent Mode V2
- Le fichier `assets/js/gtm-consent-mode-v2.js` existe mais :
  - Est configuré pour VT Imagerie (`GTM-525BNW8J`, couleurs VT)
  - N'est inclus dans **aucune page** du site
- **Impact** : Depuis mars 2024, Google exige Consent Mode V2 dans l'EEE. Sans lui :
  - Les conversions ne seront pas modélisées correctement
  - Le remarketing est dégradé
  - Risque de non-conformité RGPD

#### 2.2 Conversions trackées sur 3 pages seulement
- Les fonctions `gtagSendEventDoctolib()` et `gtagSendEventTelephone()` n'existent que sur `index.html`, `le-centre.html` et `google-ads.html`
- Les 46 autres pages ont le `gtag('config', 'AW-...')` mais **aucun tracking de conversion**
- **Impact** : Si un visiteur navigue vers une page spécialité puis clique sur Doctolib ou le téléphone → conversion perdue

### 🟡 IMPORTANTS

#### 2.3 Landing page — Performance
- Utilise **Tailwind CDN** (`cdn.tailwindcss.com`) au lieu du CSS compilé (`assets/css/tailwind.css`)
  - Ralentit le First Contentful Paint (~500ms+)
  - Exécute du JS pour compiler les classes → render-blocking
  - **Impact sur Quality Score Google Ads**
- Font Awesome **6.4.0** au lieu de 6.5.1 (incohérent avec le reste du site)

#### 2.4 Landing page — Classe Tailwind cassée dans le popup
- Ligne 346 : `bg-gradient-to-t from-black/60 via-transparent to-transparent`
- Les classes `from-black/60` sont des classes arbitraires qui ne fonctionnent pas avec le CDN Tailwind standard

#### 2.5 Landing page — UX Popup
- Le `body.overflow` n'est **jamais** mis à `hidden` à l'ouverture → la page scroll derrière le popup
- Pas de fermeture au clic sur l'overlay (seulement via le bouton ×)
- Pas de fermeture via touche Escape

#### 2.6 Landing page — Images
- Chemin `/Femme ophtalmologie.jpg` contient un espace → risque 404 sur certains serveurs
- Pas d'attributs `width`/`height` sur les images → CLS (Cumulative Layout Shift)

#### 2.7 Conversion téléphone — bug potentiel
- `gtagSendEventTelephone(url)` fait `window.location = url` dans le callback
- Pour les liens `tel:+33...`, le navigateur gère nativement l'appel
- Le `window.location = url` après le callback peut interférer ou dupliquer l'action

#### 2.8 Pas de tracking des UTM / gclid
- Aucune capture des paramètres UTM dans le DataLayer
- Le `gclid` (auto-tagging Google Ads) n'est pas explicitement capturé
- Note : `gclid` est géré automatiquement par gtag si les cookies sont autorisés

### ℹ️ RECOMMANDATIONS

#### 2.9 DataLayer — Nommage d'événements
- Les événements `conversion_doctolib_ophtalmologie` et `conversion_phone_ophtalmologie` utilisent le préfixe `conversion_`
- Dans GA4, les événements commençant par `conversion` peuvent créer de la confusion avec les conversions réelles
- Recommandation : renommer en `clic_doctolib_ophtalmologie` et `clic_phone_ophtalmologie`

#### 2.10 Enhanced Conversions
- Non implémenté (données first-party comme email/phone pour améliorer l'attribution)
- Pas prioritaire pour un centre médical, mais utile si le volume de conversions augmente

---

## 3. PLAN DE MIGRATION DOUBLE TRACKING

### Architecture cible

```
┌─────────────────────────────────────────────────┐
│  TOUTES LES PAGES                                │
│                                                   │
│  gtag('config', 'AW-11456521545');  ← VT Imagerie│
│  gtag('config', 'AW-XXXXXXXXXX');   ← Nouveau     │
│                                                   │
│  gtagSendEventDoctolib() → fire les 2 comptes     │
│  gtagSendEventTelephone() → fire les 2 comptes    │
└─────────────────────────────────────────────────┘
```

### Étapes de migration

1. **Phase 1** (maintenant) : Préparer la structure double tracking
   - Ajouter le placeholder `AW-NEW_ACCOUNT_ID` commenté
   - Centraliser les fonctions de conversion en un seul endroit
   
2. **Phase 2** (quand le nouveau compte est créé) : Activer le double tracking
   - Remplacer `AW-NEW_ACCOUNT_ID` par le vrai ID
   - Créer les conversion actions dans le nouveau compte Google Ads
   - Ajouter les nouveaux `send_to` labels

3. **Phase 3** (après validation ~2 semaines) : Retirer VT Imagerie
   - Supprimer `AW-11456521545` de toutes les pages
   - Supprimer les `send_to` VT Imagerie

---

## 4. ACTIONS À IMPLÉMENTER

### Priorité 1 — Consent Mode V2
- [ ] Adapter `gtm-consent-mode-v2.js` pour Centre Médical (IDs, couleurs)
- [ ] Adapter `gtm-consent-banner-v2.css` (couleurs #00a7de)
- [ ] Intégrer sur les 49 pages AVANT le chargement GTM/gtag

### Priorité 2 — Conversions sur toutes les pages
- [ ] Ajouter les fonctions `gtagSendEventDoctolib()` / `gtagSendEventTelephone()` sur les 46 pages manquantes
- [ ] Ajouter les listeners Doctolib + téléphone sur toutes les pages

### Priorité 3 — Fix landing page
- [ ] Remplacer Tailwind CDN par le CSS compilé
- [ ] Fix classe Tailwind cassée dans le popup
- [ ] Fix UX popup (body overflow, fermeture overlay/Escape)
- [ ] Fix chemin image avec espaces
- [ ] Ajouter width/height sur les images

### Priorité 4 — Préparation double tracking
- [ ] Structurer le code pour accepter 2 Ads accounts en parallèle
- [ ] Ajouter placeholder commenté pour le futur compte

---

## 5. RÉSUMÉ

| Catégorie | Score |
|-----------|-------|
| Tracking conversions | 🟡 Partiel (3/49 pages) |
| Consent Mode V2 | 🔴 Absent |
| Landing page performance | 🟡 CDN Tailwind = lent |
| Landing page UX | 🟡 Popup améliorable |
| Préparation migration | 🔴 Non préparé |
| DataLayer / GA4 | 🟡 Nommage à améliorer |
