# Plan d'Implémentation SEO — Post-Audit Suivi de Position Semrush

**Date** : 22 mars 2026
**Domaine** : centremedicalparislevallois.fr
**Contexte** : Après changement des mots clés (521 → 497 actifs), audit des 5 sections du Suivi de Position

---

## Diagnostic résumé

### Pages qui rankent bien
| Page | Mots clés captés | Position moy. |
|---|---|---|
| Homepage (/) | 203 | 11.79 |
| le-centre.html | 111 | 31.20 |
| medecine-generale.html | 102 | 36.35 |
| medecine-generale/consultation.html | 78 | 31.72 |
| medecine-generale/urgence.html | 43 | 23.91 |
| ophtalmologue-levallois | 39 | 15.69 |
| ophtalmologie/premiere-consultation.html | 36 | 24.28 |
| soins-infirmiers.html | 21 | 22.67 |
| ophtalmologie.html | 10 | 8.40 |

### Pages qui ne rankent PAS
| Page | Mots clés configurés | Captés | Causes identifiées |
|---|---|---|---|
| **psychologie.html** | 56 | 0 | H1 trop générique ("Psychologie"), page récente |
| **dieteticien.html** | 93 | 0 | Page la plus fine (1472 mots), 1 seule FAQ, 7 mentions commerciales |
| **kinesitherapie.html** | 114 | 3 | H1 sans localisation, sous-pages ~600 mots + 0 FAQ |

### Données comparatives clés
- **Ophtalmologie** (ranke bien) : 2872 mots, 12 FAQ, sous-pages 1056-1782 mots avec 6-8 FAQ chacune
- **Diététique** (ne ranke pas) : 1472 mots, 1 FAQ, sous-pages 1527-1805 mots avec 1 FAQ chacune
- **Kinésithérapie** (ranke mal) : 1881 mots, 8 FAQ, sous-pages 598-706 mots avec 0 FAQ chacune

---

## Priorité 1 — Quick Wins immédiats

### 1.1 Corriger H1 psychologie.html
- **Fichier** : `pages/psychologie.html`
- **Action** : Changer `<h1>Psychologie</h1>` → `<h1>Psychologue à Levallois-Perret</h1>`
- **Raison** : H1 trop générique, ne contient pas la localisation cible
- **Effort** : 1 min | **Impact** : ⭐⭐⭐

### 1.2 Corriger H1 kinesitherapie.html
- **Fichier** : `pages/kinesitherapie.html`
- **Action** : Changer `<h1>Kinésithérapie</h1>` → `<h1>Kinésithérapeute à Levallois-Perret</h1>`
- **Raison** : H1 trop générique, ne contient pas la localisation cible
- **Effort** : 1 min | **Impact** : ⭐⭐⭐

### 1.3 Ajouter liens homepage vers kiné et diététique
- **Fichier** : `index.html`
- **Action** : Dans la section qui mentionne les spécialités (actuellement seuls ophtalmo et psy sont liés), ajouter des liens vers `/kinesitherapeute-levallois` et `/dieteticien-levallois`
- **Raison** : La homepage (PageRank le plus fort) ne distribue pas de jus de lien vers ces 2 spécialités
- **Effort** : 5 min | **Impact** : ⭐⭐⭐

### 1.4 Demander indexation GSC
- **Action** : Via Google Search Console, soumettre manuellement à l'indexation :
  - `https://centremedicalparislevallois.fr/pages/psychologie.html`
  - `https://centremedicalparislevallois.fr/pages/kinesitherapie.html`
  - `https://centremedicalparislevallois.fr/pages/dieteticien.html`
- **Raison** : Pages récemment modifiées, forcer le re-crawl
- **Effort** : 2 min | **Impact** : ⭐⭐⭐

---

## Priorité 2 — Enrichissement contenu (impact fort, effort modéré)

### 2.1 Enrichir FAQ dieteticien.html
- **Fichier** : `pages/dieteticien.html`
- **Action** : Passer de 1 à 10-12 questions FAQ (visible + JSON-LD schema FAQPage)
- **Questions suggérées** :
  1. Quelle est la différence entre un diététicien et un nutritionniste ?
  2. Comment se déroule une première consultation de diététique ?
  3. Le diététicien est-il remboursé par la sécurité sociale ?
  4. Combien coûte une consultation de diététique à Levallois-Perret ?
  5. Faut-il une ordonnance pour consulter un diététicien ?
  6. Quels problèmes de santé nécessitent un suivi diététique ?
  7. Comment prendre rendez-vous avec notre diététicien ?
  8. Le diététicien prend-il en charge les enfants ?
  9. Combien de séances de diététique sont nécessaires ?
  10. Quels sont les tarifs en secteur 1 pour la diététique ?
  11. Le tiers payant est-il accepté pour les consultations de diététique ?
  12. Comment se préparer à sa première consultation nutrition ?
- **Effort** : 30 min | **Impact** : ⭐⭐⭐

### 2.2 Étoffer contenu dieteticien.html
- **Fichier** : `pages/dieteticien.html`
- **Action** : Ajouter ~1000 mots de contenu riche :
  - Description détaillée de chaque type de consultation
  - Présentation du praticien
  - Section "Pourquoi consulter un diététicien à Levallois-Perret"
  - Section tarifs/remboursement avec mentions commerciales (secteur 1, tiers payant, conventionné)
- **Cible** : Passer de 1472 → 2500+ mots
- **Effort** : 45 min | **Impact** : ⭐⭐⭐

### 2.3 Ajouter mentions commerciales dieteticien.html
- **Fichier** : `pages/dieteticien.html`
- **Action** : Intégrer naturellement dans le contenu : "secteur 1", "tiers payant", "conventionné", "sans dépassement d'honoraires", "remboursé"
- **Cible** : Passer de 7 → ~20 mentions
- **Effort** : 15 min | **Impact** : ⭐⭐

### 2.4 Ajouter FAQ JSON-LD sur toutes les sous-pages kiné
- **Fichiers** : 15 fichiers dans `pages/kinesitherapie/`
- **Action** : Ajouter 5-6 questions FAQ (visible + JSON-LD) sur chaque sous-page
- **Pages concernées** :
  - consultation-suivi.html (0 FAQ → 5-6)
  - drainage-lymphatique.html (0 FAQ → 5-6)
  - electrotherapie.html (0 FAQ → 5-6)
  - femme-enceinte.html (0 FAQ → 5-6)
  - premiere-consultation.html (0 FAQ → 5-6)
  - rachis-cervical-dorsal-lombaire.html (0 FAQ → 5-6)
  - reeducation-membres-inferieurs.html (0 FAQ → 5-6)
  - reeducation-membres-superieurs.html (0 FAQ → 5-6)
  - reeducation-post-operatoire.html (0 FAQ → 5-6)
  - renforcement-abdominal.html (0 FAQ → 5-6)
  - rhumatologie.html (0 FAQ → 5-6)
  - scoliose-adolescent.html (0 FAQ → 5-6)
  - seance-sans-ordonnance.html (0 FAQ → 5-6)
  - traumatisme-adolescent.html (0 FAQ → 5-6)
  - traumatisme-adulte.html (0 FAQ → 5-6)
- **Effort** : 2h | **Impact** : ⭐⭐⭐

### 2.5 Enrichir FAQ sous-pages diététique
- **Fichiers** : 10 fichiers dans `pages/dieteticien/`
- **Action** : Passer de 1 à 5-6 questions FAQ (visible + JSON-LD) sur chaque sous-page
- **Effort** : 1.5h | **Impact** : ⭐⭐⭐

---

## Priorité 3 — Expansion contenu sous-pages kiné (effort élevé)

### 3.1 Étoffer les 15 sous-pages kinésithérapie
- **Fichiers** : 15 fichiers dans `pages/kinesitherapie/`
- **Action** : Passer de ~600 mots → ~1100+ mots par page (aligner sur le standard ophtalmologie)
- **Contenu à ajouter** :
  - Description détaillée du soin/pathologie
  - Déroulement de la séance
  - Nombre de séances recommandées
  - Section praticien
  - Mentions commerciales (secteur 1, tiers payant)
- **Effort** : 4-6h | **Impact** : ⭐⭐⭐

### 3.2 Maillage interne croisé entre spécialités
- **Fichiers** : Toutes les pages spécialités
- **Action** : Ajouter des liens contextuels entre spécialités :
  - kiné → ophtalmo (post-opératoire)
  - psy → MG (burnout, stress)
  - diét → MG (diabète, obésité)
  - kiné → diét (chirurgie bariatrique)
  - soins inf → MG (bilans)
- **Effort** : 1h | **Impact** : ⭐⭐

---

## Priorité 4 — Monitoring (J+7 à J+14)

### 4.1 Re-vérifier les positions Semrush
- Vérifier si psycho/diét/kiné apparaissent dans le tracking
- Comparer les positions des mots clés existants

### 4.2 Vérifier l'indexation GSC
- Confirmer que les pages modifiées ont été re-crawlées
- Vérifier les nouvelles requêtes associées

### 4.3 Analyser les quick wins
- Identifier les mots clés passés de >100 à Top 100
- Identifier les mots clés en position 11-20 (proches du Top 10)

---

## Estimation totale

| Priorité | Effort | Impact |
|---|---|---|
| P1 — Quick Wins | ~10 min | Fort |
| P2 — Enrichissement | ~4-5h | Très fort |
| P3 — Expansion kiné | ~5-7h | Fort |
| P4 — Monitoring | ~30 min | Suivi |
| **Total** | **~10-13h** | — |

---

## Notes
- Les pages diététique ont été créées le 21-22 mars 2026 → Google n'a probablement pas encore crawlé
- La cannibalisation est à 23% (faible) → pas d'action urgente
- 0 extrait optimisé → objectif moyen terme quand les positions atteignent le Top 10
- Le header et footer lient déjà vers toutes les spécialités ✅
