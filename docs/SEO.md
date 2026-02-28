# 🔍 Guide SEO - Centre Médical Paris-Levallois

> Bonnes pratiques SEO pour le référencement local du centre médical

---

## 🎯 Objectifs SEO

### Mots-clés principaux
| Mot-clé | Volume estimé | Priorité |
|---------|--------------|----------|
| ophtalmologue Levallois-Perret | Moyen | ⭐⭐⭐ |
| centre médical Levallois | Moyen | ⭐⭐⭐ |
| médecin généraliste Levallois 92300 | Moyen | ⭐⭐⭐ |
| orthoptiste Levallois-Perret | Faible | ⭐⭐ |
| centre de santé 92300 | Moyen | ⭐⭐ |
| soins infirmiers Levallois | Faible | ⭐ |

### Zones géographiques ciblées
- Levallois-Perret (92300)
- Clichy (92110)
- Neuilly-sur-Seine (92200)
- Paris 17ème
- Asnières-sur-Seine

---

## 📝 Structure des pages

### Title tag
- **Format** : `[Mot-clé principal] | Centre Médical Paris-Levallois (92300)`
- **Longueur** : 50-60 caractères
- **Exemples** :
  - `Ophtalmologue Levallois-Perret | Centre Médical Paris-Levallois`
  - `Médecin Généraliste 92300 | Centre Médical Paris-Levallois`

### Meta description
- **Longueur** : 150-160 caractères
- **Contenu** : Inclure CTA, localisation, spécialité
- **Exemple** :
  ```
  Consultez un ophtalmologue à Levallois-Perret (92300). RDV Doctolib, conventionné secteur 1. 60 rue Victor Hugo. ☎ 01 80 88 37 16
  ```

### Hiérarchie des titres
```html
<h1>Titre principal avec mot-clé</h1>
  <h2>Section importante</h2>
    <h3>Sous-section</h3>
  <h2>Autre section</h2>
```

---

## 🏗️ Schema.org

### Types à utiliser

#### MedicalClinic (page d'accueil)
```json
{
  "@context": "https://schema.org",
  "@type": "MedicalClinic",
  "name": "Centre Médical Paris-Levallois",
  "medicalSpecialty": ["Ophthalmology", "Orthoptics", "GeneralPractice"],
  "address": {...},
  "telephone": "+33180883716",
  "openingHoursSpecification": [...]
}
```

#### FAQPage (pages avec FAQ)
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Question ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Réponse..."
      }
    }
  ]
}
```

#### BreadcrumbList (fil d'Ariane)
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://..."},
    {"@type": "ListItem", "position": 2, "name": "Ophtalmologie", "item": "https://..."}
  ]
}
```

---

## 🔗 Maillage interne

### Structure recommandée

```
Page d'accueil
├── /pages/specialites/ophtalmologie.html
├── /pages/specialites/orthoptie.html
├── /pages/specialites/medecine-generale.html
├── /pages/specialites/soins-infirmiers.html
├── /pages/le-centre.html
├── /pages/tarifs.html
└── /pages/contact.html
```

### Bonnes pratiques
- Chaque page doit avoir au moins 3 liens internes
- Utiliser des ancres descriptives (pas "cliquez ici")
- Lier les pages spécialités entre elles

---

## 📍 SEO Local

### Google Business Profile
- Vérifier que la fiche est à jour
- Répondre aux avis
- Publier régulièrement des posts

### Balises géographiques
```html
<meta name="geo.region" content="FR-92">
<meta name="geo.placename" content="Levallois-Perret">
<meta name="geo.position" content="48.8942;2.2878">
<meta name="ICBM" content="48.8942, 2.2878">
```

### NAP (Name, Address, Phone)
**Toujours cohérent partout** :
```
Centre Médical Paris-Levallois
60 Rue Victor Hugo
92300 Levallois-Perret
01 80 88 37 16
```

---

## 🖼️ SEO Images

### Nommage
```
ophtalmologue-levallois-examen-vue.jpg  ✅
IMG_3257.jpg                            ❌
```

### Alt text
```html
<img src="..." alt="Consultation ophtalmologie au Centre Médical Paris-Levallois">
```

### Compression
- Utiliser TinyPNG ou Squoosh
- Format JPEG pour photos (qualité 80-85%)
- Poids max : 200-500 KB

---

## 📊 Outils de suivi

### Google Search Console
- Vérifier les erreurs d'indexation
- Suivre les positions sur les mots-clés
- Soumettre le sitemap

### Google Analytics 4
- Suivre le trafic organique
- Analyser les pages d'entrée
- Mesurer les conversions

### Outils tiers
- [Ubersuggest](https://neilpatel.com/ubersuggest/) - Recherche de mots-clés
- [Screaming Frog](https://www.screamingfrog.co.uk/) - Audit technique
- [PageSpeed Insights](https://pagespeed.web.dev/) - Performance

---

## ✅ Checklist SEO par page

- [ ] Title unique et optimisé (50-60 car.)
- [ ] Meta description unique (150-160 car.)
- [ ] H1 unique avec mot-clé principal
- [ ] Hiérarchie H1 > H2 > H3 respectée
- [ ] URL propre et descriptive
- [ ] Balise canonical
- [ ] Alt text sur toutes les images
- [ ] Schema.org approprié
- [ ] Liens internes (min. 3)
- [ ] Contenu de qualité (min. 300 mots)
- [ ] Mobile-friendly
- [ ] Temps de chargement < 3s
