---
description: Créer une nouvelle page HTML pour le site Centre Médical Paris-Levallois
---

# Workflow : Créer une nouvelle page

## Informations requises

Avant de commencer, récupérer auprès de l'utilisateur :
1. **Nom de la page** (ex: "ophtalmologie", "tarifs", "contact")
2. **Emplacement** (ex: `/pages/`, `/pages/specialites/`)
3. **Type de page** (spécialité, info, landing)

## Étapes

### 1. Lire le contexte du projet
```
Lire PROJECT_CONTEXT.md pour comprendre :
- La structure du projet
- La palette de couleurs (#00a7de, #0090c0, etc.)
- Les conventions de nommage
```

### 2. Créer le fichier HTML

Utiliser ce template de base :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <style id="cm-stable-layout">
        #header-placeholder{min-height:80px;}
        i.fas, i.fa-solid, i.far, i.fa-regular{display:inline-block;width:1.25em;}
        [id]{scroll-margin-top:100px;}
    </style>

    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-525BNW8J');</script>

    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MQ9CEHQVW3"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-MQ9CEHQVW3');
    gtag('config', 'AW-11456521545');
    </script>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- SEO - À PERSONNALISER -->
    <title>[TITRE] | Centre Médical Paris-Levallois</title>
    <meta name="description" content="[DESCRIPTION 150-160 caractères]">
    <link rel="canonical" href="https://www.centremedicalparislevallois.fr/[URL]">
    
    <!-- Open Graph -->
    <meta property="og:title" content="[TITRE]">
    <meta property="og:description" content="[DESCRIPTION]">
    <meta property="og:url" content="https://www.centremedicalparislevallois.fr/[URL]">
    <meta property="og:type" content="website">
    
    <link rel="icon" type="image/png" href="/assets/images/favicon.png">
    <link rel="stylesheet" href="/assets/css/tailwind.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
    
    <style>
        :root {
            --primary-500: #00a7de;
            --primary-600: #0090c0;
            --primary-700: #007ba3;
        }
    </style>
</head>
<body class="font-sans bg-white">
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-525BNW8J"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    
    <div id="header-placeholder"><div style="height:80px"></div></div>

    <!-- CONTENU DE LA PAGE -->
    <main>
        <!-- Sections à créer -->
    </main>

    <div id="footer-placeholder"></div>

    <script>
        async function loadComponent(placeholderId, componentPath) {
            try {
                const response = await fetch(componentPath);
                if (!response.ok) throw new Error(`HTTP ${response.status}`);
                document.getElementById(placeholderId).innerHTML = await response.text();
            } catch (error) {
                console.error('Erreur:', error);
            }
        }
        document.addEventListener('DOMContentLoaded', async function() {
            await loadComponent('header-placeholder', '/components/header.html');
            await loadComponent('footer-placeholder', '/components/footer.html');
        });
    </script>
</body>
</html>
```

### 3. Personnaliser la page

- Remplacer les placeholders `[TITRE]`, `[DESCRIPTION]`, `[URL]`
- Ajouter le contenu spécifique
- Ajouter le Schema.org approprié si nécessaire

### 4. Ajouter dans la navigation

Si la page doit apparaître dans le menu :
- Modifier `components/header.html`
- Modifier `components/footer.html` si nécessaire

### 5. Vérifications

- [ ] Title unique et optimisé
- [ ] Meta description unique
- [ ] Canonical URL correcte
- [ ] H1 présent et unique
- [ ] Liens internes ajoutés
- [ ] Test en local OK
- [ ] Mobile responsive OK

### 6. Commit

```bash
git add pages/[nom-page].html
git commit -m "feat: ajouter page [nom-page]"
```
