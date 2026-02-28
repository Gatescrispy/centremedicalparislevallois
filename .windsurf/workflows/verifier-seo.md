---
description: Vérifier et optimiser le SEO d'une page du site
---

# Workflow : Vérifier le SEO d'une page

## Utilisation

Ce workflow vérifie les éléments SEO essentiels d'une page.

Demander à l'utilisateur : **Quelle page vérifier ?** (chemin du fichier ou URL)

## Checklist SEO automatique

### 1. Balises meta essentielles

Vérifier la présence et la qualité de :

```html
<!-- OBLIGATOIRE -->
<title>...</title>                           <!-- 50-60 caractères -->
<meta name="description" content="...">     <!-- 150-160 caractères -->
<meta name="viewport" content="...">        <!-- Responsive -->
<link rel="canonical" href="...">           <!-- URL canonique -->

<!-- RECOMMANDÉ -->
<meta name="robots" content="index, follow">
<html lang="fr">
```

### 2. Open Graph (réseaux sociaux)

```html
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:image" content="...">
<meta property="og:url" content="...">
<meta property="og:type" content="website">
```

### 3. Structure des titres

Vérifier :
- [ ] Un seul `<h1>` par page
- [ ] Hiérarchie respectée (H1 > H2 > H3)
- [ ] H1 contient le mot-clé principal
- [ ] Pas de saut de niveau (H1 puis H3)

### 4. Images

Pour chaque `<img>` vérifier :
- [ ] Attribut `alt` présent et descriptif
- [ ] Attribut `loading="lazy"` (sauf hero)
- [ ] Dimensions `width` et `height` spécifiées
- [ ] Nom de fichier descriptif

### 5. Liens

- [ ] Liens internes présents (min. 3)
- [ ] Pas de liens cassés (404)
- [ ] Ancres descriptives (pas "cliquez ici")
- [ ] Liens externes avec `rel="noopener noreferrer"`

### 6. Schema.org

Vérifier la présence de :
```html
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "...",
    ...
}
</script>
```

Types recommandés selon la page :
- Page d'accueil : `MedicalClinic`
- Page spécialité : `MedicalWebPage`
- FAQ : `FAQPage`
- Contact : `ContactPage`

### 7. Performance

- [ ] Pas de ressources bloquantes
- [ ] Images optimisées (< 500 KB)
- [ ] CSS/JS minifiés

## Rapport SEO

Générer un rapport avec :

```markdown
## Rapport SEO - [Nom de la page]

### ✅ Points positifs
- ...

### ⚠️ Points à améliorer
- ...

### ❌ Problèmes critiques
- ...

### 📝 Recommandations
1. ...
2. ...
```

## Outils complémentaires

Suggérer à l'utilisateur de tester avec :
- [Google PageSpeed Insights](https://pagespeed.web.dev/)
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)

## Actions correctives

Si des problèmes sont détectés, proposer les corrections :

1. **Title manquant ou trop long** → Réécrire
2. **Description manquante** → Ajouter
3. **H1 manquant** → Ajouter
4. **Alt manquant** → Ajouter sur les images
5. **Schema manquant** → Ajouter le type approprié
