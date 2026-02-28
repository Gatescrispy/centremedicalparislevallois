---
description: Créer une page complète pour une nouvelle spécialité médicale
---

# Workflow : Ajouter une page spécialité

## Spécialités existantes

Vérifier dans `/pages/specialites/` :
- ophtalmologie.html
- orthoptie.html
- medecine-generale.html
- soins-infirmiers.html

## Informations requises

Demander à l'utilisateur :
1. **Nom de la spécialité**
2. **Description courte** (1-2 phrases)
3. **Services proposés** (liste)
4. **Public concerné** (adultes, enfants, tous âges)
5. **Lien Doctolib spécifique** (specialityId)
6. **Image représentative** (si disponible)

## Structure de la page spécialité

### Sections recommandées

1. **Hero** - Titre + description + CTA RDV
2. **Présentation** - Description détaillée de la spécialité
3. **Services** - Liste des actes/consultations
4. **Déroulement** - Comment se passe une consultation
5. **Tarifs** - Informations de prise en charge
6. **FAQ** - Questions fréquentes spécifiques
7. **CTA Final** - Incitation à prendre RDV

### Template de base

```html
<!-- Hero -->
<section class="relative py-20" style="background: linear-gradient(135deg, #007ba3, #003d52);">
    <div class="max-w-4xl mx-auto px-4 text-center text-white">
        <span class="inline-flex items-center px-4 py-2 bg-white/20 rounded-full mb-6">
            <i class="fas fa-[ICONE] mr-2"></i>
            [NOM SPÉCIALITÉ]
        </span>
        <h1 class="text-4xl md:text-5xl font-bold mb-6">[TITRE H1]</h1>
        <p class="text-xl text-white/90 mb-8">[DESCRIPTION]</p>
        <a href="[LIEN_DOCTOLIB]" class="inline-flex items-center px-8 py-4 bg-white text-[#00a7de] rounded-xl font-bold">
            <i class="fas fa-calendar-plus mr-3"></i>
            Prendre rendez-vous
        </a>
    </div>
</section>

<!-- Services -->
<section class="py-16 bg-white">
    <div class="max-w-6xl mx-auto px-4">
        <h2 class="text-3xl font-bold text-center mb-12">Nos consultations</h2>
        <div class="grid md:grid-cols-3 gap-6">
            <!-- Cards services -->
        </div>
    </div>
</section>

<!-- FAQ -->
<section class="py-16 bg-gray-50" x-data="{ open: null }">
    <div class="max-w-4xl mx-auto px-4">
        <h2 class="text-3xl font-bold text-center mb-12">Questions fréquentes</h2>
        <!-- FAQ items avec Alpine.js -->
    </div>
</section>
```

## Liens Doctolib par spécialité

| Spécialité | specialityId | Lien |
|------------|--------------|------|
| Ophtalmologie | 4 | `...booking/motives?specialityId=4&placeId=practice-714912` |
| Médecine générale | 2 | `...booking/motives?specialityId=2&placeId=practice-714912` |
| Soins infirmiers | 30 | `...booking/motives?specialityId=30&placeId=practice-714912` |

## Icônes recommandées

| Spécialité | Icône Font Awesome |
|------------|-------------------|
| Ophtalmologie | `fa-eye` |
| Orthoptie | `fa-glasses` |
| Médecine générale | `fa-stethoscope` |
| Soins infirmiers | `fa-syringe` |
| Vaccination | `fa-shield-virus` |
| Prise de sang | `fa-vial` |

## Schema.org pour page spécialité

```json
{
    "@context": "https://schema.org",
    "@type": "MedicalWebPage",
    "name": "[Spécialité] - Centre Médical Paris-Levallois",
    "specialty": "[Spécialité]",
    "mainEntity": {
        "@type": "MedicalProcedure",
        "name": "Consultation [spécialité]",
        "procedureType": "https://schema.org/NoninvasiveProcedure"
    }
}
```

## Checklist

- [ ] Fichier créé dans `/pages/specialites/`
- [ ] Title et meta description optimisés
- [ ] Schema.org ajouté
- [ ] Lien Doctolib correct
- [ ] Page ajoutée dans header.html (mega-menu)
- [ ] Page ajoutée dans footer.html
- [ ] Liens internes vers autres spécialités
- [ ] Test mobile OK
