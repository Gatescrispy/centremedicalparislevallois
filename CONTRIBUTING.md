# 🤝 Guide de Contribution - Centre Médical Paris-Levallois

> Conventions de code, bonnes pratiques et workflow de développement

---

## 📋 Table des matières

1. [Structure des fichiers](#structure-des-fichiers)
2. [Conventions HTML](#conventions-html)
3. [Conventions CSS](#conventions-css)
4. [Conventions JavaScript](#conventions-javascript)
5. [Images](#images)
6. [SEO](#seo)
7. [Git Workflow](#git-workflow)
8. [Checklist avant commit](#checklist-avant-commit)

---

## 📁 Structure des fichiers

### Où placer les fichiers

| Type | Emplacement | Exemple |
|------|-------------|---------|
| Pages principales | `/pages/` | `le-centre.html` |
| Pages spécialités | `/pages/specialites/` | `ophtalmologie.html` |
| Landing pages | `/pages/landing/` | `google-ads.html` |
| Composants | `/components/` | `header.html`, `footer.html` |
| Styles | `/assets/css/` | `tailwind.css` |
| Scripts | `/assets/js/` | `main.js` |
| Images | `/assets/images/` ou racine | `hero.jpg` |

### Nommage des fichiers
- **Minuscules uniquement** : `medecine-generale.html` ✅ pas `MedecineGenerale.html` ❌
- **Tirets pour séparer** : `soins-infirmiers.html` ✅ pas `soins_infirmiers.html` ❌
- **Pas d'espaces** : `le-centre.html` ✅ pas `le centre.html` ❌
- **Pas d'accents** : `medecine-generale.html` ✅ pas `médecine-générale.html` ❌

---

## 🏗️ Conventions HTML

### Structure de base d'une page

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <!-- 1. Stable Layout (éviter CLS) -->
    <style id="cm-stable-layout">
        #header-placeholder{min-height:80px;}
        i.fas, i.fa-solid{display:inline-block;width:1.25em;}
    </style>

    <!-- 2. Google Tag Manager -->
    <script><!-- GTM snippet --></script>
    
    <!-- 3. Google Analytics / Ads -->
    <script><!-- GA4 + conversions --></script>

    <!-- 4. Meta tags -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Titre | Centre Médical Paris-Levallois</title>
    <meta name="description" content="...">
    
    <!-- 5. Open Graph -->
    <meta property="og:title" content="...">
    
    <!-- 6. Schema.org -->
    <script type="application/ld+json">...</script>
    
    <!-- 7. CSS -->
    <link rel="stylesheet" href="/assets/css/tailwind.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    
    <!-- 8. Alpine.js -->
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
    
    <!-- 9. Styles inline spécifiques -->
    <style>/* ... */</style>
</head>
<body class="font-sans bg-white">
    <!-- GTM noscript -->
    <noscript>...</noscript>
    
    <!-- Header placeholder -->
    <div id="header-placeholder"><div style="height:80px"></div></div>
    
    <!-- Contenu de la page -->
    <main>
        <!-- Sections... -->
    </main>
    
    <!-- Footer placeholder -->
    <div id="footer-placeholder"></div>
    
    <!-- Scripts de chargement des composants -->
    <script>
        async function loadComponent(placeholderId, componentPath) { /* ... */ }
        document.addEventListener('DOMContentLoaded', async function() {
            await loadComponent('header-placeholder', '/components/header.html');
            await loadComponent('footer-placeholder', '/components/footer.html');
        });
    </script>
</body>
</html>
```

### Classes CSS prioritaires

Utiliser les classes Tailwind en priorité. Styles inline uniquement pour :
- Couleurs spécifiques (`style="color: #00a7de;"`)
- Overrides ponctuels

### Accessibilité

- Toujours mettre un `alt` sur les images
- Utiliser `aria-label` sur les liens avec icône seule
- Contraste suffisant (WCAG AA minimum)

---

## 🎨 Conventions CSS

### Palette de couleurs

**TOUJOURS utiliser ces couleurs** (issues du logo) :

```css
/* Bleu primaire - pour CTA, liens, accents */
color: #00a7de;
background-color: #00a7de;

/* Bleu hover */
color: #0090c0;

/* Bleu active/pressed */
color: #007ba3;

/* Bleu clair - backgrounds */
background-color: #e6f7fc;
background-color: rgba(0, 167, 222, 0.1); /* 10% */

/* Textes */
color: #252525; /* Principal */
color: #4a4a4a; /* Secondaire */
color: #6b6b6b; /* Muted */
```

### Classes utilitaires custom

```css
/* Définis dans le header.html et index.html */
.cm-primary { color: #00a7de; }
.cm-primary-bg { background-color: #00a7de; }
.btn-cta-primary { /* Bouton principal */ }
.btn-cta-secondary { /* Bouton secondaire */ }
.specialty-card { /* Carte de spécialité */ }
.faq-item { /* Item FAQ accordion */ }
```

### Responsive

- **Mobile first** avec Tailwind
- Breakpoints : `sm:` (640px), `md:` (768px), `lg:` (1024px), `xl:` (1280px)
- Barre sticky mobile : visible uniquement `< md`

---

## ⚡ Conventions JavaScript

### Chargement des composants

```javascript
async function loadComponent(placeholderId, componentPath) {
    try {
        const response = await fetch(componentPath);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const html = await response.text();
        document.getElementById(placeholderId).innerHTML = html;
    } catch (error) {
        console.error('Erreur chargement composant:', error);
    }
}
```

### DataLayer events

Pour tracker un événement :
```javascript
dataLayer.push({'event': 'nom_evenement'});
```

### Conversions Google Ads

```javascript
// RDV Doctolib
onclick="gtagSendEventDoctolib();"

// Appel téléphonique
onclick="gtagSendEventTelephone('tel:+33180883716');"
```

---

## 🖼️ Images

### Formats recommandés
- **Photos** : JPEG (qualité 80-85%)
- **Logos/icônes** : PNG ou SVG
- **Pas de** : HEIC, BMP, TIFF

### Optimisation
- Largeur max : 1920px pour hero, 800px pour cards
- Compression : TinyPNG, Squoosh, ou ImageOptim
- Lazy loading : `loading="lazy"` (sauf hero)

### Nommage
```
hero-centre-medical.jpg          # OK
hero-centre-medical-original.jpg # Version non compressée (gitignore)
Femme ophtalmologie.jpg          # OK (espaces tolérés si déjà existant)
```

### Attributs requis
```html
<img 
    src="/image.jpg" 
    alt="Description de l'image"
    loading="lazy"
    width="800"
    height="600"
>
```

---

## 🔍 SEO

### Checklist SEO par page

- [ ] `<title>` unique (50-60 caractères)
- [ ] `<meta name="description">` unique (150-160 caractères)
- [ ] `<link rel="canonical">` vers l'URL canonique
- [ ] `<h1>` unique contenant le mot-clé principal
- [ ] Hiérarchie des titres (H1 > H2 > H3)
- [ ] Alt text sur toutes les images
- [ ] Schema.org approprié (MedicalClinic, FAQPage, etc.)
- [ ] Open Graph tags
- [ ] Liens internes vers autres pages

### Mots-clés cibles
- centre médical Levallois-Perret
- ophtalmologue Levallois / 92300
- orthoptiste Levallois-Perret
- médecin généraliste Levallois
- centre de santé conventionné

---

## 🔄 Git Workflow

### Branches
- `main` : Production (déployé sur LWS)
- `develop` : Développement en cours
- `feature/xxx` : Nouvelles fonctionnalités
- `fix/xxx` : Corrections de bugs

### Commits

Format : `type: description courte`

Types :
- `feat:` nouvelle fonctionnalité
- `fix:` correction de bug
- `style:` changements CSS/design
- `content:` mise à jour de contenu
- `seo:` optimisations SEO
- `docs:` documentation
- `refactor:` refactoring code
- `chore:` maintenance (gitignore, config)

Exemples :
```
feat: ajouter page ophtalmologie
fix: corriger lien Doctolib mobile
style: améliorer spacing section FAQ
content: mettre à jour horaires samedi
seo: ajouter schema FAQPage
```

### Pull Requests
1. Créer une branche depuis `develop`
2. Faire les modifications
3. Tester en local
4. Créer une PR vers `develop`
5. Merger après review
6. Merger `develop` → `main` pour déploiement

---

## ✅ Checklist avant commit

### Technique
- [ ] Le site fonctionne en local
- [ ] Pas d'erreurs console
- [ ] Header et footer se chargent
- [ ] Responsive OK (mobile, tablet, desktop)
- [ ] Liens fonctionnels

### Contenu
- [ ] Pas de fautes d'orthographe
- [ ] Informations à jour (horaires, téléphone, etc.)
- [ ] Images optimisées

### SEO
- [ ] Title et description uniques
- [ ] Schema.org présent
- [ ] Alt text sur images

### Performance
- [ ] Images compressées
- [ ] Pas de ressources inutiles

### Git
- [ ] Fichiers sensibles non commités (.env, credentials)
- [ ] Message de commit descriptif
- [ ] CHANGELOG.md mis à jour si changement important

---

## 📚 Ressources utiles

- [TailwindCSS Docs](https://tailwindcss.com/docs)
- [Alpine.js Docs](https://alpinejs.dev/)
- [Font Awesome Icons](https://fontawesome.com/icons)
- [Schema.org MedicalClinic](https://schema.org/MedicalClinic)
- [Google Search Central](https://developers.google.com/search)
