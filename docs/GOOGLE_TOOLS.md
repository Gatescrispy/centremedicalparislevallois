# 🔧 Outils Google - Centre Médical Paris-Levallois

> Configuration et accès à tous les outils Google connectés au site

---

## 📊 Tableau récapitulatif

| Outil | ID / Identifiant | Status | Accès |
|-------|------------------|--------|-------|
| **Google Tag Manager** | GTM-MQ2KK9XS | ✅ Actif | [tagmanager.google.com](https://tagmanager.google.com/) |
| **Google Analytics 4** | G-XHP0ZF8ZSF | ✅ Actif | [analytics.google.com](https://analytics.google.com/) |
| **Google Ads** | AW-11456521545 | ✅ Actif | [ads.google.com](https://ads.google.com/) |
| **Google Search Console** | centremedicalparislevallois.fr | ✅ Configuré | [search.google.com/search-console](https://search.google.com/search-console) |
| **Google Business Profile** | - | ⚠️ À vérifier | [business.google.com](https://business.google.com/) |

---

## 🏷️ Google Tag Manager (GTM)

### Informations
- **Container ID** : `GTM-MQ2KK9XS`
- **Accès** : https://tagmanager.google.com/

### Implémentation
Le snippet GTM est dans le `<head>` de chaque page :
```html
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-MQ2KK9XS');</script>
```

Et le noscript juste après `<body>` :
```html
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MQ2KK9XS"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
```

### Tags configurés dans GTM
- GA4 Configuration
- Google Ads Conversion Tracking
- Google Ads Remarketing
- Consent Mode v2

---

## 📈 Google Analytics 4 (GA4)

### Informations
- **Property ID** : `G-XHP0ZF8ZSF`
- **Accès** : https://analytics.google.com/

### Configuration
Chargé via gtag.js ET GTM (double tracking possible à vérifier) :
```javascript
gtag('config', 'G-XHP0ZF8ZSF');
```

### Événements personnalisés suivis
| Événement | Description | Déclencheur |
|-----------|-------------|-------------|
| `cta_footer_doctolib` | Clic RDV footer | Clic bouton Doctolib footer |
| `cta_footer_call` | Clic appel footer | Clic téléphone footer |
| `cta_sticky_doctolib` | Clic RDV barre mobile | Clic bouton RDV sticky |
| `cta_sticky_call` | Clic appel barre mobile | Clic bouton appel sticky |

---

## 💰 Google Ads

### Informations
- **Account ID** : `AW-11456521545`
- **Accès** : https://ads.google.com/

### Conversions configurées

#### 1. Conversion RDV Doctolib
```javascript
gtag('event', 'conversion', {
    'send_to': 'AW-11456521545/ypsQCO_RwuEbEMnK8tYq'
});
```

#### 2. Conversion Appel téléphonique
```javascript
gtag('event', 'conversion', {
    'send_to': 'AW-11456521545/xTpdCNWFw-EbEMnK8tYq'
});
```

### Fonctions JavaScript
```javascript
// Appelé sur clic Doctolib
gtagSendEventDoctolib();

// Appelé sur clic téléphone
gtagSendEventTelephone('tel:+33180883716');
```

---

## 🔍 Google Search Console (GSC)

### Configuration requise

1. **Accéder à GSC** : https://search.google.com/search-console
2. **Ajouter une propriété** : `https://www.centremedicalparislevallois.fr/`
3. **Méthode de vérification recommandée** : Balise HTML

#### Option 1 : Vérification par balise HTML
Ajouter dans le `<head>` de `index.html` :
```html
<meta name="google-site-verification" content="VOTRE_CODE_VERIFICATION">
```

#### Option 2 : Vérification par fichier HTML
Télécharger le fichier `google[code].html` et le placer à la racine.

#### Option 3 : Vérification via GA4/GTM
Si le compte GA4 est lié, la vérification peut être automatique.

### Après vérification
1. **Soumettre le sitemap** : `https://www.centremedicalparislevallois.fr/sitemap.xml`
2. **Demander l'indexation** des pages principales
3. **Vérifier la couverture** d'indexation

---

## 🏢 Google Business Profile

### Configuration
- **Accès** : https://business.google.com/
- **Nom de l'établissement** : Centre Médical Paris-Levallois

### Informations à vérifier
- [ ] Adresse : 60 Rue Victor Hugo, 92300 Levallois-Perret
- [ ] Téléphone : 01 80 88 37 16
- [ ] Horaires à jour
- [ ] Photos du centre
- [ ] Catégorie : Centre médical / Centre de santé
- [ ] Lien vers Doctolib

### Lien avec le site
Ajouter les balises Schema.org `LocalBusiness` (déjà présentes dans index.html).

---

## 🗺️ Sitemap & Robots.txt

### sitemap.xml
- **URL** : https://www.centremedicalparislevallois.fr/sitemap.xml
- **Soumis à GSC** : ⚠️ À faire après vérification propriété

### robots.txt
- **URL** : https://www.centremedicalparislevallois.fr/robots.txt
- **Contenu** : Autorise tous les robots, bloque docs et fichiers internes

---

## 🍪 Consent Mode v2

### Configuration
Le Consent Mode v2 est configuré via GTM pour respecter le RGPD.

Voir le guide détaillé : `GUIDE_GTM_CONSENT_MODE_V2.md` (dossier parent)

### États de consentement
- `ad_storage` : Cookies publicitaires
- `analytics_storage` : Cookies analytics
- `ad_user_data` : Données utilisateur pour publicité
- `ad_personalization` : Personnalisation des annonces

---

## 📋 Checklist de configuration

### Initial (fait une fois)
- [x] GTM installé sur toutes les pages
- [x] GA4 configuré
- [x] Google Ads conversions configurées
- [x] sitemap.xml créé
- [x] robots.txt créé
- [ ] Google Search Console vérifié
- [ ] Sitemap soumis à GSC
- [ ] Google Business Profile à jour

### Régulier
- [ ] Vérifier les erreurs dans GSC
- [ ] Analyser les performances dans GA4
- [ ] Suivre les conversions Google Ads
- [ ] Mettre à jour sitemap.xml (nouvelles pages)

---

## 🔗 Liens utiles

- [GTM Container](https://tagmanager.google.com/#/container/accounts/xxx/containers/xxx)
- [GA4 Reports](https://analytics.google.com/analytics/web/)
- [Google Ads](https://ads.google.com/)
- [Search Console](https://search.google.com/search-console)
- [Business Profile](https://business.google.com/)
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [Rich Results Test](https://search.google.com/test/rich-results)
