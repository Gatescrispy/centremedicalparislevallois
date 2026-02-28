---
description: Optimiser les images du site pour améliorer les performances
---

# Workflow : Optimiser les images

## Objectifs

- Réduire la taille des fichiers images
- Améliorer le temps de chargement
- Maintenir une qualité visuelle acceptable

## Étapes

### 1. Identifier les images à optimiser

// turbo
```bash
# Lister les images et leurs tailles
find . -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" \) -exec ls -lh {} \; | sort -k5 -h -r
```

**Seuils recommandés** :
- Hero/bannières : < 500 KB
- Cards/vignettes : < 100 KB
- Icônes/logos : < 50 KB

### 2. Identifier les images trop grandes

Images probablement à optimiser si :
- Largeur > 1920px
- Poids > 500 KB
- Format non optimisé (BMP, TIFF)

### 3. Optimisation avec outils en ligne

**Outils recommandés** :
- [TinyPNG](https://tinypng.com/) - PNG et JPEG
- [Squoosh](https://squoosh.app/) - Tous formats, contrôle qualité
- [ImageOptim](https://imageoptim.com/) - macOS

**Paramètres recommandés** :
- JPEG : Qualité 80-85%
- PNG : Compression sans perte
- Redimensionner si > 1920px de large

### 4. Optimisation en ligne de commande (si disponible)

// turbo
```bash
# Avec ImageMagick (si installé)
# Redimensionner à 1920px max de large
mogrify -resize '1920>' *.jpg

# Avec jpegoptim (si installé)
jpegoptim --max=85 --strip-all *.jpg

# Avec optipng (si installé)
optipng -o2 *.png
```

### 5. Vérifier les attributs HTML

S'assurer que chaque image a :

```html
<img 
    src="/image.jpg" 
    alt="Description pertinente"
    loading="lazy"
    width="800"
    height="600"
>
```

**Note** : `loading="lazy"` ne doit PAS être sur les images above-the-fold (hero).

### 6. Considérer le format WebP

Pour les navigateurs modernes, envisager :

```html
<picture>
    <source srcset="/image.webp" type="image/webp">
    <img src="/image.jpg" alt="...">
</picture>
```

### 7. Mettre à jour le .gitignore

S'assurer que les originaux ne sont pas commités :

```
*-original.jpg
*-original.png
*.HEIC
```

## Rapport d'optimisation

Générer un rapport :

```markdown
## Rapport d'optimisation images

### Images optimisées
| Fichier | Avant | Après | Réduction |
|---------|-------|-------|-----------|
| hero.jpg | 2.1 MB | 450 KB | -78% |

### Actions effectuées
- ...

### Recommandations
- ...
```

## Bonnes pratiques

1. **Toujours garder les originaux** dans un dossier séparé (hors Git)
2. **Nommer les fichiers de manière descriptive** : `ophtalmologue-levallois.jpg`
3. **Utiliser des dimensions appropriées** au contexte d'affichage
4. **Tester visuellement** après compression
