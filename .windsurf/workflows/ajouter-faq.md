---
description: Ajouter une nouvelle question à la FAQ du site
---

# Workflow : Ajouter une question FAQ

## Structure de la FAQ

La FAQ utilise Alpine.js pour l'effet accordion.

## Informations requises

Demander à l'utilisateur :
1. **Question** (texte exact)
2. **Réponse** (texte avec mise en forme si nécessaire)
3. **Page concernée** (index.html, page spécialité, etc.)
4. **Position** (ordre dans la liste)

## Template HTML

```html
<!-- FAQ Item -->
<div class="faq-item">
    <button class="w-full px-6 py-4 text-left flex items-center justify-between hover:bg-gray-50 transition-colors"
            @click="open = open === [NUMERO] ? null : [NUMERO]">
        <span class="font-semibold text-gray-900">[QUESTION] ?</span>
        <i class="fas fa-chevron-down transition-transform duration-200" style="color: #00a7de;" :class="{ 'rotate-180': open === [NUMERO] }"></i>
    </button>
    <div x-show="open === [NUMERO]" x-collapse class="px-6 pb-4">
        <p class="text-gray-600">
            [RÉPONSE]
        </p>
    </div>
</div>
```

## Mise en forme de la réponse

### Texte simple
```html
<p class="text-gray-600">Réponse simple ici.</p>
```

### Avec lien
```html
<p class="text-gray-600">
    Vous pouvez <a href="[URL]" class="font-medium underline" style="color: #00a7de;">prendre RDV en ligne</a>.
</p>
```

### Avec liste
```html
<p class="text-gray-600">
    Les documents nécessaires :
</p>
<ul class="list-disc list-inside text-gray-600 mt-2">
    <li>Carte Vitale</li>
    <li>Attestation mutuelle</li>
</ul>
```

### Avec mise en gras
```html
<p class="text-gray-600">
    Le centre est <strong>conventionné secteur 1</strong>.
</p>
```

## Ajouter au Schema.org FAQPage

Dans le `<head>`, ajouter à la liste `mainEntity` :

```json
{
    "@type": "Question",
    "name": "[QUESTION] ?",
    "acceptedAnswer": {
        "@type": "Answer",
        "text": "[RÉPONSE TEXTE BRUT]"
    }
}
```

## Étapes

### 1. Identifier le fichier et la section FAQ

### 2. Trouver le dernier numéro utilisé
```bash
grep -o "open === [0-9]*" index.html | tail -1
```

### 3. Ajouter le nouvel item FAQ
Incrémenter le numéro pour le nouveau `@click="open === N"`.

### 4. Mettre à jour le Schema.org
Ajouter l'entrée dans `mainEntity`.

### 5. Vérifier le fonctionnement
- L'accordion s'ouvre/se ferme correctement
- Le style est cohérent

### 6. Commit
```bash
git commit -m "content: ajouter FAQ - [résumé question]"
```

## FAQ existantes (index.html)

1. Comment prendre rendez-vous ?
2. Quelle est l'adresse du centre ?
3. Quels sont les horaires d'ouverture ?
4. Le centre est-il conventionné ?
5. Carte Vitale et tiers payant : comment ça marche ?
6. Quels moyens de paiement sont acceptés ?
7. Acceptez-vous les nouveaux patients ?
8. Que faire en cas d'urgence médicale ?
