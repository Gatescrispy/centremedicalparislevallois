---
description: Mettre à jour les horaires d'ouverture du centre médical sur toutes les pages
---

# Workflow : Modifier les horaires

## Contexte

Les horaires doivent être cohérents sur toutes les pages et dans les données structurées Schema.org.

## Horaires actuels

| Jour | Horaires | Notes |
|------|----------|-------|
| Lundi | 9h - 00h | Garde de nuit |
| Mardi | 9h - 19h | |
| Mercredi | 9h - 19h | |
| Jeudi | 9h - 00h | Garde de nuit |
| Vendredi | 9h - 19h | |
| Samedi | 9h - 14h | |
| Dimanche | Fermé | |

## Fichiers à modifier

### 1. Page d'accueil (`index.html`)

Rechercher et modifier :
- Section hero (chips d'info)
- Section horaires (tableau détaillé)
- Schema.org `openingHoursSpecification`

### 2. Composant footer (`components/footer.html`)

Modifier la ligne :
```html
<p class="text-white text-base"><i class="fas fa-clock mr-2"></i>Lun-Ven 9h-19h • Sam 9h-14h</p>
```

### 3. Page le-centre (`pages/le-centre.html`)

Rechercher et modifier :
- Section horaires
- Schema.org si présent

### 4. Schema.org (données structurées)

Format correct :
```json
"openingHoursSpecification": [
    {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "opens": "09:00",
        "closes": "19:00"
    },
    {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": "Saturday",
        "opens": "09:00",
        "closes": "14:00"
    }
]
```

## Étapes

### 1. Demander les nouveaux horaires

Questions à poser :
- Quels jours sont modifiés ?
- Nouvelles heures d'ouverture/fermeture ?
- Gardes de nuit modifiées ?

### 2. Rechercher toutes les occurrences

// turbo
```bash
grep -rn "9h-19h\|09:00\|19:00\|9h - 19h" --include="*.html" .
```

### 3. Modifier chaque fichier

Utiliser la fonction de recherche/remplacement.

### 4. Vérifier la cohérence

S'assurer que les horaires sont identiques partout :
- [ ] index.html (section hero)
- [ ] index.html (section horaires)
- [ ] index.html (Schema.org)
- [ ] components/footer.html
- [ ] pages/le-centre.html

### 5. Commit

```bash
git add .
git commit -m "content: mise à jour horaires [détails]"
```

## Notes importantes

- Les gardes de nuit (lundi et jeudi jusqu'à minuit) concernent uniquement la **médecine générale**
- Penser à mettre à jour la fiche Google Business Profile également
