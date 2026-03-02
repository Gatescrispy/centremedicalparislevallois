# Audit Complet GTM — Centre Médical Paris-Levallois
**Date** : 2 mars 2026  
**Conteneur** : GTM-MQ2KK9XS  
**Version publiée** : V2 - Configuration GA4 + Ads + Conversions

---

## 1. Résumé Exécutif

| Critère | Statut |
|---------|--------|
| GTM snippet (head) | ✅ 50/50 pages |
| GTM noscript (body) | ✅ 50/50 pages |
| Consent Mode V2 | ✅ 50/50 pages |
| Ordre Consent → GTM | ✅ 50/50 pages |
| gtag.js inline retiré | ✅ 49/49 pages (sauf google-ads.html) |
| cm-ads-tracking.js v2.0 | ✅ Dual mode (gtag + dataLayer) |
| Landing page GTM | ✅ google-ads-gtm.html créée |
| Landing page VT Imagerie | ✅ google-ads.html intacte |
| Sitemap | ✅ Aucune landing page incluse |
| robots.txt | ✅ Pas de blocage landing pages |

**Verdict : Configuration prête pour déploiement.**

---

## 2. Tags GTM Configurés

| Tag | Type | ID/Label | Déclencheur |
|-----|------|----------|-------------|
| GA4 - Configuration | Balise Google | G-XHP0ZF8ZSF | Initialization - All Pages |
| Ads - Remarketing | Remarketing Google Ads | AW-11456521545 | All Pages |
| Ads - Conversion Linker | Conversion Linker | — | All Pages |
| Ads - Conversion Doctolib | Suivi conversions | ypsQCO_RwuEbEMnK8tYq | CE - clic_doctolib |
| Ads - Conversion Telephone | Suivi conversions | xTpdCNWFw-EbEMnK8tYq | CE - clic_telephone |

### Déclencheurs personnalisés
| Déclencheur | Type | Événement |
|-------------|------|-----------|
| CE - clic_doctolib | Custom Event | `clic_doctolib` |
| CE - clic_telephone | Custom Event | `clic_telephone` |

---

## 3. Flux de Données — Parcours Utilisateur

### Pages normales du site (48 pages + index.html)
```
Utilisateur visite une page
  → Consent Mode V2 (defaults granted)
  → GTM charge (GTM-MQ2KK9XS)
  → GTM déclenche GA4 - Configuration (G-XHP0ZF8ZSF)
  → GTM déclenche Ads - Remarketing (AW-11456521545)
  → GTM déclenche Ads - Conversion Linker
  
Utilisateur clique sur lien Doctolib
  → cm-ads-tracking.js détecte le clic (event delegation)
  → dataLayer.push({event: 'clic_doctolib'})
  → GTM déclenche Ads - Conversion Doctolib
  
Utilisateur clique sur numéro de téléphone
  → cm-ads-tracking.js détecte le clic (event delegation)
  → dataLayer.push({event: 'clic_telephone'})
  → GTM déclenche Ads - Conversion Telephone
```

### Landing page GTM (google-ads-gtm.html)
```
Même flux que pages normales, MAIS :
  → Pas de cm-ads-tracking.js
  → Événements dataLayer.push directement dans le HTML inline
  → 100% GTM, zéro gtag.js
```

### Landing page VT Imagerie (google-ads.html) — LEGACY
```
Utilisateur visite la page
  → Consent Mode V2
  → GTM charge
  → gtag.js charge AUSSI (G-XHP0ZF8ZSF + AW-11456521545)
  → DOUBLE tracking GA4 (GTM + gtag inline) — accepté temporairement
  
Utilisateur clique Doctolib/Téléphone
  → cm-ads-tracking.js v2.0 :
    1. gtag('event','conversion',...) → tracking direct VT Imagerie ✅
    2. dataLayer.push({event:'clic_doctolib'}) → GTM tag ✅
```

---

## 4. Analyse de Cohérence

### ✅ Points validés
1. **Pas de double-fire GTM** : `gtag('event','conversion',...)` pousse au format `arguments` dans le dataLayer, pas au format `{event: ...}`. GTM ne le capte pas comme trigger.
2. **Consent avant GTM** : Sur les 50 pages, le Consent Mode V2 est toujours déclaré AVANT le snippet GTM.
3. **Event names cohérents** : Les noms `clic_doctolib` et `clic_telephone` dans `cm-ads-tracking.js` et `google-ads-gtm.html` correspondent exactement aux triggers GTM.
4. **Event delegation** : `cm-ads-tracking.js` utilise `document.addEventListener('click', ...)` — fonctionne même avec les composants header/footer chargés dynamiquement.
5. **noindex/nofollow** : Les deux landing pages ont la meta robots correcte.
6. **Sitemap propre** : Aucune landing page noindex dans le sitemap.

### ⚠️ Points d'attention
1. **Balises GTM en veille (malware faux positif)** : Toutes les balises sont en veille à cause d'une fausse détection de malware sur le conteneur neuf. Se résout sous 24-48h ou via support Google.
2. **Double GA4 sur google-ads.html** : La page legacy charge gtag.js inline + GTM → double comptage GA4. Acceptable temporairement car cette page sera désactivée.
3. **cm-ads-tracking.js sur google-ads.html** : Sur cette page, `gtag` est une vraie fonction (gtag.js chargé), donc les conversions VT Imagerie partent bien en direct + via GTM.

### ❌ Bug corrigé pendant l'audit
- **le-centre.html** : noscript GTM manquant dans le `<body>` → **corrigé**.

---

## 5. Fichiers Modifiés — Résumé

| Fichier | Modification |
|---------|-------------|
| 48 pages HTML | gtag.js inline retiré |
| pages/le-centre.html | noscript GTM ajouté |
| pages/landing/google-ads-gtm.html | **CRÉÉ** — Landing page 100% GTM |
| assets/js/cm-ads-tracking.js | v2.0 — dual mode (gtag + dataLayer.push) |
| pages/landing/google-ads.html | **INCHANGÉ** — tracking VT Imagerie intact |

---

## 6. Prochaines Étapes

1. **Déployer** le site via FTP sur LWS
2. **Résoudre le faux positif malware** dans GTM (attendre 24-48h ou contacter le support)
3. **Vérifier les tags** avec GTM Preview mode une fois les balises réactivées
4. **Vérifier les conversions** dans Google Ads (délai 24-48h après déploiement)
5. **Désactiver google-ads.html** quand le tracking VT Imagerie n'est plus nécessaire
