# Plan Maître d'Implémentation SEO — Centre Médical Paris-Levallois

**Date de création** : 25 mars 2026  
**Workflow de référence** : `.windsurf/workflows/implementer-seo.md`  
**Sources** : 10 analyses Semrush (mars 2026)  
**Site** : centremedicalparislevallois.fr (~60 pages HTML)

---

## Vue d'ensemble

### Volume total captable identifié

| Catégorie | Volume mensuel | Source |
|---|---|---|
| Quick Wins (KD ≤ 25) | ~11 160 | Keyword Overview |
| Opportunités moyennes (KD 25-45) | ~3 200 | Keyword Overview |
| Long terme (KD > 45) | ~49 820 | Keyword Overview |
| **TOTAL potentiel** | **~64 180/mois** | Consolidé |

### État actuel du site

| Métrique | Valeur (mars 2026) |
|---|---|
| Authority Score | 0 |
| Backlinks | 1 (nofollow, .uk) |
| Mots clés positionnés | 32 uniques |
| Trafic organique | ~46 visites/mois |
| Pages indexées | ~15 (sur ~60) |
| Impressions GSC | 6 380/mois |
| Clics GSC | 159/mois |

### Objectifs à 6 mois

| KPI | Objectif M+3 | Objectif M+6 |
|---|---|---|
| Trafic organique | 500+ visites/mois | 2 000+ |
| Mots clés top 10 | 20+ | 50+ |
| Authority Score | 10+ | 20+ |
| Domaines référents | 30+ | 80+ |
| Pages indexées | 50+ | 63+ |

---

## Organisation du plan

Le plan est divisé en **5 phases** séquentielles. Chaque phase contient des **lots (batches)** de tâches thématiques. Chaque tâche est autonome et suit le workflow `/implementer-seo`.

**Légende** :
- 🔲 À faire
- 🔄 En cours  
- ✅ Terminé
- ⏭️ Reporté

---

## PHASE 1 — Fondations techniques (Semaine 1)

> **Objectif** : Corriger les problèmes techniques bloquants avant toute optimisation de contenu.  
> **Effort estimé** : 4-6h  
> **Sources** : Domain Overview, On-Page SEO, Backlinks, Keyword Gap

### Lot 1.1 — Structured Data & Méta-données index.html

| # | Tâche | Source analyse | Impact | Effort |
|---|---|---|---|---|
| ✅ 1.1.1 | Ajouter `Psychology`, `PhysicalTherapy`, `Dietetics` dans `medicalSpecialty` de index.html | Backlinks §9.C | Google connaît toutes nos spécialités | 15 min | *(déjà présent dans structured data)* |
| ✅ 1.1.2 | Ajouter Kinésithérapie et Diététique dans `availableService` de index.html | Backlinks §9.C | Services déclarés complets | 15 min | *(déjà présent dans structured data)* |
| ✅ 1.1.3 | Mettre à jour `og:description` et `twitter:description` dans index.html pour mentionner les 6 spécialités | Backlinks §9.C | Partages sociaux complets | 10 min | *(déjà présent : ophtalmo, méd gén, psy, kiné, diét, soins inf.)* |
| ✅ 1.1.4 | Vérifier et corriger la redirection www → non-www (canonical) | Domain Overview §4 | Résoudre cannibalisation www/non-www | 30 min | *(.htaccess L12-13 : 301 www→non-www + canonical sans www)* |

> **Note** : les corrections structured data `address` sur `equipe.html`, `tarifs.html`, `bilan-sanguin-ecbu.html`, `vaccination-pediatrique.html` ont été faites dans le commit `8c301c9` (audit Semrush). Les tâches 1.1.1-1.1.3 concernent spécifiquement `index.html`.

### Lot 1.2 — Indexation

| # | Tâche | Source analyse | Impact | Effort |
|---|---|---|---|---|
| ✅ 1.2.1 | Vérifier que le sitemap.xml inclut toutes les ~60 pages | Keyword Gap §6.2 | Pages indexables par Google | 30 min |
| ⏳ 1.2.2 | Soumettre sitemap dans GSC + demander indexation des pages récentes (psycho, diét, kiné) | Keyword Gap §6.2 | Passer de 15 à 60+ pages indexées | 30 min | *(ACTION MANUELLE — GSC)* |
| ✅ 1.2.3 | Vérifier robots.txt (pas de blocage involontaire) | Domain Overview | Aucun blocage | 10 min | *(vérifié OK : Allow /, sitemap déclaré, docs/ bloqué)* |

### Lot 1.3 — Corrections NAP (Name, Address, Phone)

| # | Tâche | Source analyse | Impact | Effort |
|---|---|---|---|---|
| ✅ 1.3.1 | Vérifier que l'adresse "60 rue Victor Hugo" est cohérente partout (structured data, footer, contact, acces-horaires) | Keyword Gap §3 ("48 rue" apparaît en recherche) | Cohérence NAP pour Local SEO | 30 min | *(commit 8c301c9)* |
| ⏳ 1.3.2 | Vérifier les signaux NAP dans Google Business Profile | Keyword Gap §3 | Pas de confusion d'adresse | 15 min | *(ACTION MANUELLE — GBP)* |

---

## PHASE 2 — Optimisation SEO on-page des pages existantes (Semaines 1-3)

> **Objectif** : Optimiser les titles, H1, meta descriptions et contenu des pages existantes pour les KW à fort ROI.  
> **Effort estimé** : 15-20h  
> **Sources** : Keyword Overview, KMT, KSB, On-Page SEO, Position Tracking

### Lot 2.1 — Titles & H1 (Quick wins immédiats)

> **Principe** : Adopter le format `[Spécialité] Paris-Levallois (92300) | [Différenciant] | Centre Médical` pour capter les recherches "paris" ET "levallois".

| # | Page | Title actuel | Title optimisé proposé | KW cible (vol.) | Source |
|---|---|---|---|---|---|
| ✅ 2.1.1 | `ophtalmologie.html` | "Ophtalmologue Levallois-Perret (92300) \| Secteur 1" | "Ophtalmologue Paris-Levallois (92300) \| Secteur 1 \| Centre Médical" | ophtalmologue paris (8 100) | KMT §2 | *(commit 66dfb5f)* |
| ✅ 2.1.2 | `kinesitherapie.html` | ~~"Kinésithérapeute Levallois-Perret (92300) \| Secteur 1"~~ | "Kinésithérapeute Paris-Levallois (92300) \| Kiné D.E." | kinésithérapeute paris (1 600) | KMT §3 | *(commits 66dfb5f + fa62484 — tarifs retirés)* |
| ✅ 2.1.3 | `dieteticien.html` | "Diététicien à Levallois-Perret (92300) — Consultation Nutrition..." | "Diététicien Nutritionniste Paris-Levallois (92300) \| Centre Médical" | diététicienne nutritionniste (4 400) | KMT §5 | *(commit 66dfb5f)* |
| ✅ 2.1.4 | `psychologie.html` | OK (contient déjà "Paris-Levallois") | Title raccourci ≤65 chars | psychologue levallois (170) | KO §3.4 | *(commits 8c301c9 + a8f67a3)* |
| ✅ 2.1.5 | `soins-infirmiers.html` | Vérifier | Title optimisé "Paris-Levallois" | prise de sang levallois (70) | KO §3.6 | *(commit 66dfb5f)* |
| ✅ 2.1.6 | `medecine-generale.html` | "Médecin Généraliste Levallois-Perret (92300) \| Secteur 1" | Title optimisé "Paris-Levallois" | médecin généraliste levallois (210) | KO §3.2 | *(commit 66dfb5f)* |

### Lot 2.2 — Sous-pages ophtalmo (fort potentiel, KD bas)

| # | Page | KW cible (vol. / KD) | Action | Source |
|---|---|---|---|---|
| ✅ 2.2.1 | `ophtalmologie/champ-visuel-humphrey.html` (1733 mots) | champ visuel humphrey (880 / KD 13) | Optimiser title/H1, viser featured snippet | KO §4 | *(commit 11283dd)* |
| ✅ 2.2.2 | `ophtalmologie/premiere-consultation-enfant.html` (1176 mots) | 1er rdv ophtalmo bébé (140 / KD 16) + ophtalmologue pédiatrique (2 400 / KD 23) | Enrichir contenu + optimiser title pour KW national | KMT §2, KO §4 | *(commit dfc7ed2)* |
| ✅ 2.2.3 | `ophtalmologie/urgence.html` (1058 mots) | urgence oeil (13 300 / KD 21) | Enrichir contenu, optimiser title, structured data | KSB §4.2, KMT §2 | *(commit 16db2d9)* |
| ✅ 2.2.4 | `ophtalmologie/renouvellement-lunettes-lentilles.html` | renouvellement lunettes orthoptiste (90 / KD 13) + durée validité ordonnance lunettes (1 000 / KD 25) | Enrichir avec FAQ ordonnance | KO §3.1 | *(commit b436770)* |
| ✅ 2.2.5 | `ophtalmologie.html` (pillar, 2872 mots) | Ajouter section tarifs/remboursement détaillée | consultation ophtalmo prix (1 000 / KD 29), prix ophtalmo (880 / KD 30) | Keyword Gap §4.2 | *(commit 8547479)* |

### Lot 2.3 — Page psychologie (plus gros potentiel volumétrique)

| # | Page | KW cible (vol. / KD) | Action | Source |
|---|---|---|---|---|
| ✅ 2.3.1 | `psychologie/mon-soutien-psy.html` | mon soutien psy (49 500 / KD 58), prise en charge psychologue (137 200 / KD 47), liste psychologue conventionné cpam (18 100 / KD 42), remboursement psychologue (8 100 / KD 37) | **PRIORITÉ #1** — Enrichir massivement : FAQ CPAM, 8 séances, remboursement, liste conditions. Viser featured snippet. | KSB §4.2, KMT §4, KO §3.4 | *(commit a96ea2c)* |
| ✅ 2.3.2 | `psychologie.html` section TCC | psychologue tcc (4 400 / KD 36), thérapie cognitivo-comportementaliste (28 300 / KD 38) | Développer la section TCC existante | KMT §4, KSB §4.2 | *(commit 822324f)* |
| ✅ 2.3.3 | `psychologie.html` section Psy vs Psychiatre | psychiatre ou psychologue (21 300 / KD 26-31) | Enrichir la section comparative existante | KSB §4.2, TR §4.2 | *(commit 822324f)* |
| ✅ 2.3.4 | `psychologie/psychotraumatologie.html` | EMDR psychologue (2 400 / KD 35) | Enrichir contenu EMDR, ajouter FAQ | KO §3.4 | *(commit dfbc3aa)* |

### Lot 2.4 — Page diététique

| # | Page | KW cible (vol. / KD) | Action | Source |
|---|---|---|---|---|
| ✅ 2.4.1 | `dieteticien.html` section "Différences" | différence diététicien nutritionniste (1 600 / KD 22), diététicienne ou nutritionniste (2 400 / KD 26) | Optimiser SEO on-page de la section existante | KMT §5, KO §3.5 | *(commit fdcae2d)* |
| ✅ 2.4.2 | `dieteticien.html` section remboursement | remboursement nutritionniste (8 600 / KD 22), prix consultation diététicien (90 / KD 19) | Enrichir section tarifs/remboursement | KSB §4.2 | *(commit fdcae2d)* |
| ✅ 2.4.3 | `dieteticien/femme-enceinte-nutrition.html` | aliments interdits grossesse (1 600 / KD 25) | Enrichir avec guide grossesse + aliments interdits | KO §3.5 | *(commit ab1b1a3)* |

### Lot 2.5 — Soins infirmiers (niche KD ultra-bas)

| # | Page | KW cible (vol. / KD) | Action | Source |
|---|---|---|---|---|
| ✅ 2.5.1 | `soins-infirmiers/pansement-post-chirurgical.html` (666 mots) | pansement post opératoire (210 / KD 11), pansement en chirurgie (260 / KD 19) | Enrichir à 1200+ mots | Keyword Gap §6.1 | *(commit 3192ff5 — 350→469 lignes)* |
| ✅ 2.5.2 | `soins-infirmiers/retrait-fils-agrafes.html` (2244 mots) | ablation fils de suture (90 / KD 24), retrait agrafes (90 / KD 18) | Optimiser title/H1/meta pour KW cibles | Keyword Gap §3 | *(commit 793fba4)* |
| ✅ 2.5.3 | `soins-infirmiers/bilan-sanguin-ecbu.html` | prise de sang levallois (70 / KD 19) | Optimiser title/H1 pour KW local | KO §3.6 | *(commit 793fba4)* |

### Lot 2.6 — Kinésithérapie

| # | Page | KW cible (vol. / KD) | Action | Source |
|---|---|---|---|---|
| ✅ 2.6.1 | `kinesitherapie.html` (pillar) | centre de kinésithérapeutes (1 300 / KD 21) | Ajouter KW dans contenu, H2, meta | KMT §3 | *(commit 5b1d9f2)* |
| ✅ 2.6.2 | `kinesitherapie/drainage-lymphatique.html` | drainage lymphatique levallois (90 / KD 14) | Optimiser title/H1 pour KW local | KO §3.3 | *(commit 5b1d9f2)* |

### Lot 2.7 — Pages transversales

| # | Page | KW cible (vol. / KD) | Action | Source |
|---|---|---|---|---|
| ✅ 2.7.1 | `tarifs.html` | remboursement consultation (8 100 / KD 25), tarif médecin généraliste secteur 1 (40) | Enrichir FAQ remboursement + maillage vers pages spécialités | KSB §4.2, KO §3.2 | *(commit 84b33b9)* |
| ✅ 2.7.2 | `le-centre.html` | Ajouter cartes Psychologie et Diététique manquantes dans "Nos spécialités" | Topic Research §10.E | Complétude du site | *(commit c00b47a)* |
| ✅ 2.7.3 | `le-centre.html` | Optimiser alt tags des 4 photos spécialités (alt trop génériques) | Topic Research §10.A | SEO images | *(4 alt tags enrichis avec lieu + spécialité)* |
| ✅ 2.7.4 | `urgences.html` (top-level, 2246 mots) | hopital levallois urgence (70 / KD 19), urgences levallois perret | Optimiser title/H1 pour KW locaux urgence | Keyword Gap §3 | *(commit c00b47a)* |

---

## PHASE 3 — Création de nouvelles pages (Semaines 3-6)

> **Objectif** : Créer les 3-5 pages manquantes identifiées dans les analyses, confirmées par vérification filesystem.  
> **Effort estimé** : 12-16h  
> **Workflow** : Utiliser `/nouvelle-page` + `/implementer-seo` pour chaque page  
> **Sources** : KSB, KMT, Keyword Gap

### Lot 3.1 — Nouvelles sous-pages confirmées manquantes

| # | Page à créer | KW cible (vol. / KD) | Justification | Source |
|---|---|---|---|---|
| ✅ 3.1.1 | `kinesitherapie/kine-sport.html` | kine sport (3 100 / KD 31), kinésithérapeute sport (720 / KD 29) | Cluster 691 KW non couvert, concurrent physiosportlevallois.fr | KSB + KMT | *(commit e27593b)* |
| ✅ 3.1.2 | `psychologie/enfant-adolescent.html` | psychologue enfant (4 400 / KD 36) | Mentionné en FAQ mais pas de page dédiée | KSB + KMT | *(commit d28d1d7)* |
| ✅ 3.1.3 | `dieteticien/nutrition-sport.html` | nutritionniste du sport (4 200 / KD 24) | Pas couvert, KD faible, fort volume | KSB | *(commit d12e4ec)* |

### Lot 3.2 — Articles informationnels à fort potentiel

> **Note** : Ces articles ciblent des KW informationnels à fort volume et faible KD, intégrés comme sous-pages de la spécialité correspondante (pas besoin de blog).

| # | Page à créer | KW cible (vol. / KD) | Type | Source |
|---|---|---|---|---|
| ✅ 3.2.1 | `ophtalmologie/fond-oeil.html` | fond d'oeil (5 400 / KD 20) | Article expert + viser featured snippet + Schema MedicalProcedure | KO §4, Keyword Gap §6.2 | *(commit bc622d2)* |
| ✅ 3.2.2 | `ophtalmologie/oct.html` | (à rechercher) | Article examen OCT, lié à ophtalmologie.html | Keyword Gap §6.2 | *(commit 7d6f41c)* |

---

## PHASE 4 — Maillage interne & Local SEO (Semaines 4-8)

> **Objectif** : Renforcer le maillage entre pages et optimiser la présence locale.  
> **Effort estimé** : 6-8h  
> **Sources** : On-Page SEO, Domain Overview, Topic Research

### Lot 4.1 — Maillage interne

| # | Tâche | Impact | Effort |
|---|---|---|---|
| ✅ 4.1.1 | Auditer et renforcer les liens internes entre pillar pages et sous-pages (ex: ophtalmologie.html → 6 sous-pages, chaque sous-page → pillar + sœurs) | Transmission du PageRank interne | 2h | *(13 sous-pages psy+diét modifiées — commit c42bb27)* |
| ✅ 4.1.2 | Ajouter des liens contextuels entre spécialités (ex: dieteticien/femme-enceinte → medecine-generale, psychologie → dieteticien/troubles-comportement-alimentaire) | Maillage transversal | 1h | *(6 liens cross-spécialités — commit c42bb27)* |
| ✅ 4.1.3 | Ajouter des liens homepage → pages spécialités dans le contenu (pas juste navigation) | Autorité transmise depuis la homepage | 30 min | *(hero badges + cards + présentation — commit 7e31a33)* |
| ✅ 4.1.4 | Vérifier que toutes les nouvelles pages (Phase 3) sont liées depuis leurs pillar pages et le sitemap | Indexation rapide | 30 min | *(vérifié OK — fait en Phase 3)* |

### Lot 4.2 — Google Business Profile & Local SEO

| # | Tâche | Impact | Effort |
|---|---|---|---|
| ⏳ 4.2.1 | Vérifier que GBP est complet : catégories primaires alignées avec les 6 spécialités, horaires, photos, lien site | Visibilité Maps + Local Pack | 1h | *(ACTION MANUELLE — voir recommandations ci-dessous)* |
| ⏳ 4.2.2 | Mettre en place une stratégie d'avis Google (email post-consultation, QR code cabinet) | "ophtalmologue levallois les mieux notés" (TR) | Recommandation | *(ACTION MANUELLE — voir recommandations ci-dessous)* |
| ✅ 4.2.3 | Ajouter `sameAs` dans structured data (index.html, le-centre.html) avec les profils sociaux une fois créés | Signal social pour Google | 15 min | *(Doctolib + Google Maps — commit 87e609c)* |

---

## PHASE 5 — Backlinks & Autorité (Semaines 4-12, continu)

> **Objectif** : Passer d'un AS de 0 à 15+ en construisant un profil de backlinks de qualité.  
> **Effort estimé** : 8-12h (actions manuelles hors site)  
> **Sources** : Backlinks, Link Building, Keyword Gap §8

### Lot 5.1 — Inscriptions annuaires (Quick wins gratuits)

> **Objectif** : 15-20 domaines référents en 2 semaines.

| # | Action | Cible | AS estimé | Effort |
|---|---|---|---|---|
| 🔲 5.1.1 | Vérifier backlink Google Business Profile (existant : 4.9/5, 127 avis) | google.com | 100 | 15 min |
| 🔲 5.1.2 | Vérifier backlink Doctolib (profil existant) | doctolib.fr | ~70 | 15 min |
| 🔲 5.1.3 | Inscription PagesJaunes / Mappy | pagesjaunes.fr | ~65 | 30 min |
| 🔲 5.1.4 | Inscription lemedecin.fr | lemedecin.fr | 43 | 15 min |
| 🔲 5.1.5 | Inscription webwiki.fr | webwiki.fr | 34 | 15 min |
| 🔲 5.1.6 | Inscription horairesdouverture24.fr | horairesdouverture24.fr | 28 | 10 min |
| 🔲 5.1.7 | Inscription hotfrog.fr | hotfrog.fr | 26 | 15 min |
| 🔲 5.1.8 | Inscription autour-de-moi.com | autour-de-moi.com | 23 | 10 min |
| 🔲 5.1.9 | Inscription acompio.fr | acompio.fr | 22 | 15 min |
| 🔲 5.1.10 | Inscription centre.contact | centre.contact | 21 | 15 min |
| 🔲 5.1.11 | Inscription ouvert-a-proximite.com | ouvert-a-proximite.com | 21 | 10 min |
| 🔲 5.1.12 | Inscription empreintesduweb.com | empreintesduweb.com | 21 | 15 min |
| 🔲 5.1.13 | Inscription allbiz.fr | allbiz.fr | 20 | 10 min |
| 🔲 5.1.14 | Inscription annuaire-sante-bien-etre.fr | annuaire-sante-bien-etre.fr | 17 | 15 min |
| 🔲 5.1.15 | Inscription medicum.fr | medicum.fr | 12 | 15 min |
| 🔲 5.1.16 | Inscription ophtalmologues.org | ophtalmologues.org | 6 | 15 min |

### Lot 5.2 — Profils sociaux (à créer)

| # | Action | Impact | Effort |
|---|---|---|---|
| 🔲 5.2.1 | Créer profil LinkedIn du centre médical | Backlink nofollow AS ~98 + canal de promotion | 1-2h |
| 🔲 5.2.2 | Créer page Facebook du centre avec lien site | Backlink nofollow AS ~100 + canal social | 1-2h |
| 🔲 5.2.3 | Mettre à jour `sameAs` structured data avec les nouveaux profils | Signal social Google | 15 min |

### Lot 5.3 — Partenariats locaux (Mois 2-3)

| # | Action | Cible | AS | Effort |
|---|---|---|---|---|
| 🔲 5.3.1 | Contacter defense-92.fr pour article/interview | defense-92.fr | 35 | Contact presse |
| 🔲 5.3.2 | Demander inscription annuaire Mairie Levallois | levallois.fr | ~40 | Demande admin |
| 🔲 5.3.3 | Adhésion + fiche CCI Hauts-de-Seine | cci-paris-idf.fr | ~55 | Adhésion |
| 🔲 5.3.4 | Inscription annuaire ARS Île-de-France | ars.sante.fr | ~70 | Demande officielle |
| 🔲 5.3.5 | Partenariat Helen Keller Europe (ophtalmo) | helenkellereurope.org | 26 | Don/partenariat |

### Lot 5.4 — Guest posting & contenu (Mois 3-6)

| # | Action | Domaine cible | Sujet proposé | Page backlink |
|---|---|---|---|---|
| 🔲 5.4.1 | Guest post medicalib.fr | medicalib.fr (AS 40) | "Ablation d'agrafes : protocole en centre médical" | `soins-infirmiers/retrait-fils-agrafes.html` |
| 🔲 5.4.2 | Contribution cof.fr | cof.fr (AS 40) | Contribution ophtalmo pédiatrique | `ophtalmologie.html` |
| 🔲 5.4.3 | Guest post psychologue.net | psychologue.net (AS 51) | "Mon Soutien Psy : comment en bénéficier à Levallois ?" | `psychologie/mon-soutien-psy.html` |
| 🔲 5.4.4 | Article handroit.com | handroit.com (AS 25) | Droits patients secteur 1 | `tarifs.html` |

---

## Matrice de priorisation consolidée

### Top 10 des tâches à plus fort impact

| Rang | Tâche | Vol. captable | KD | Phase |
|---|---|---|---|---|
| 1 | **Enrichir mon-soutien-psy.html** | 49 500 - 137 200 | 47-58 | 2.3.1 |
| 2 | **Créer fond-oeil.html** (featured snippet) | 5 400 | 20 | 3.2.1 |
| 3 | **Optimiser title ophtalmo "Paris-"** | 8 100 | 36 | 2.1.1 |
| 4 | **Enrichir section TCC psychologie** | 28 300 | 38 | 2.3.2 |
| 5 | **Enrichir urgence ophtalmo** | 13 300 | 21 | 2.2.3 |
| 6 | **Enrichir pansement-post-chirurgical** | 470 | 11 | 2.5.1 |
| 7 | **Enrichir section Psy vs Psychiatre** | 21 300 | 26-31 | 2.3.3 |
| 8 | **Créer kine-sport.html** | 3 100 | 31 | 3.1.1 |
| 9 | **Optimiser title diététicien "Nutritionniste"** | 4 400 | 29 | 2.1.3 |
| 10 | **Inscriptions annuaires (lot 5.1)** | — (AS 0→10) | — | 5.1 |

### Ordre d'exécution recommandé

```
Semaine 1 :  Phase 1 (fondations) + Lot 2.1 (titles/H1) + Début lot 5.1 (annuaires)
Semaine 2 :  Lot 2.3.1 (mon-soutien-psy — PRIORITÉ #1) + Lot 2.2 (ophtalmo)
Semaine 3 :  Lot 2.3.2-2.3.4 (psychologie) + Lot 2.4 (diététique) + Lot 2.5 (soins inf.)
Semaine 4 :  Lot 2.6 (kiné) + Lot 2.7 (transversales) + Lot 3.2.1 (fond-oeil)
Semaine 5 :  Lot 3.1 (nouvelles pages kiné sport, psy enfant, nutrition sport)
Semaine 6 :  Phase 4 (maillage interne) + Lot 3.2.2 (OCT)
Semaines 4-12 : Phase 5 en parallèle (backlinks, annuaires, partenariats)
```

---

## Suivi des fichiers d'analyse traités

> Chaque fichier d'analyse doit être **entièrement exploité**. Cocher quand toutes les recommandations ont été implémentées ou explicitement reportées.

| # | Fichier | Tâches extraites | Statut |
|---|---|---|---|
| 🔲 1 | `PLAN_IMPLEMENTATION_SEO_2026-03-22.md` | Quick wins H1, FAQ, enrichissement contenu | — |
| 🔲 2 | `AUDIT_SEMRUSH_DOMAIN_OVERVIEW_2026-03-22.md` | www/non-www, backlinks, trafic diversification | — |
| 🔲 3 | `ANALYSE_ON_PAGE_SEO_2026-03-23.md` | 81 idées d'optimisation, comparaison top 10 | — |
| 🔲 4 | `ANALYSE_KEYWORD_OVERVIEW_2026-03-23.md` | 71 KW, matrice Volume × KD, plan d'action | — |
| 🔲 5 | `ANALYSE_KEYWORD_STRATEGY_BUILDER_2026-03-23.md` | 10 topic clusters, pillar pages, nouvelles pages | — |
| 🔲 6 | `ANALYSE_KEYWORD_MAGIC_TOOL_2026-03-23.md` | Seeds par spécialité, KW commerciaux, SERP features | — |
| 🔲 7 | `ANALYSE_CONCURRENTIELLE_KEYWORD_GAP_2026-03-23.md` | 1632 KW gap, SWOT, backlink gap, corrections NAP | — |
| 🔲 8 | `ANALYSE_TOPIC_RESEARCH_2026-03-23.md` | Benchmark concurrentiel, avis Google, trust signals | — |
| 🔲 9 | `ANALYSE_BACKLINKS_2026-03-23.md` | Stratégie link building 4 phases, annuaires | — |
| 🔲 10 | `ANALYSE_LINK_BUILDING_2026-03-24.md` | Prospects, outreach, guest posting | — |

---

## Notes

- **Toutes les tâches de Phase 2-3** impliquent des modifications de code HTML → suivre `/implementer-seo`
- **Les tâches de Phase 5** sont majoritairement hors-site (inscriptions, contacts) → le propriétaire du site (djouma-livine@centremedicalparislevallois.fr) devra effectuer certaines actions
- **Ne jamais modifier** les fichiers dans `pages/landing/` (landing pages Google Ads séparées)
- **Recherche web obligatoire** avant chaque enrichissement de contenu (analyser top 3 Google)
- **Volume KSB vs KO** : le KSB donne des volumes parfois beaucoup plus élevés (ex: "prise en charge psychologue" 137K vs "mon soutien psy" 49K) — utiliser les deux comme référence

---

*Plan créé le 25 mars 2026 — À mettre à jour après chaque tâche terminée*  
*Workflow qualité : `.windsurf/workflows/implementer-seo.md`*
