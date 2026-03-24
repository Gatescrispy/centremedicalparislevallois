---
description: Workflow qualité pour implémenter les optimisations SEO issues des analyses Semrush. À suivre pour CHAQUE tâche d'implémentation.
---

# Workflow : Implémenter une optimisation SEO

## Objectif

Garantir un niveau de qualité constant et maximal pour chaque implémentation SEO, du début à la fin du plan. Ce workflow est le **référentiel qualité** à consulter avant chaque tâche.

## Avant de commencer une tâche

### 1. Identifier la source

Lire le fichier d'analyse Semrush correspondant dans `docs/` :

| Fichier | Contenu |
|---|---|
| `PLAN_MASTER_IMPLEMENTATION_SEO.md` | **Plan maître** — liste ordonnée de toutes les tâches |
| `PLAN_IMPLEMENTATION_SEO_2026-03-22.md` | Quick wins Position Tracking |
| `AUDIT_SEMRUSH_DOMAIN_OVERVIEW_2026-03-22.md` | Métriques domaine, www/non-www, concurrence |
| `ANALYSE_ON_PAGE_SEO_2026-03-23.md` | 81 idées d'optimisation, comparaison top 10 |
| `ANALYSE_KEYWORD_OVERVIEW_2026-03-23.md` | 71 KW analysés, matrice Volume × KD |
| `ANALYSE_KEYWORD_STRATEGY_BUILDER_2026-03-23.md` | 10 topic clusters, pillar pages |
| `ANALYSE_KEYWORD_MAGIC_TOOL_2026-03-23.md` | 480K+ KW, seeds par spécialité |
| `ANALYSE_CONCURRENTIELLE_KEYWORD_GAP_2026-03-23.md` | 1632 KW gap, SWOT, backlink gap |
| `ANALYSE_TOPIC_RESEARCH_2026-03-23.md` | Benchmark concurrentiel ophtalmo |
| `ANALYSE_BACKLINKS_2026-03-23.md` | Audit backlinks, stratégie link building |
| `ANALYSE_LINK_BUILDING_2026-03-24.md` | Prospects, outreach, guest posting |

### 2. Analyser la tâche (5 min obligatoires)

Avant toute modification de code :

1. **Lire la page cible** — comprendre le contenu actuel, le title, H1, meta, structured data
2. **Lire les KW cibles** — vérifier volume, KD, intent dans les fichiers d'analyse
3. **Rechercher sur le web** — analyser les pages top 3 Google pour le KW cible :
   - Longueur de contenu
   - Structure des titres (H2/H3)
   - Questions couvertes (PAA)
   - Featured snippets existants
   - Structured data utilisé
4. **Vérifier les pages liées** — sous-pages, pages sœurs, maillage interne existant
5. **Identifier les contraintes** — ne pas casser le design, respecter la charte, vérifier les composants partagés

### 3. Planifier les modifications

Créer une mini-checklist mentale :
- [ ] Quels fichiers seront modifiés ?
- [ ] Y a-t-il un impact sur header.html / footer.html / index.html ?
- [ ] Faut-il modifier le structured data ?
- [ ] Le maillage interne doit-il être mis à jour ?
- [ ] Des images doivent-elles être ajoutées/optimisées ?

## Pendant l'implémentation

### Règles de qualité

1. **Contenu médical** — Toujours précis, professionnel, sans promesses thérapeutiques
2. **SEO naturel** — Intégrer les KW naturellement, jamais de keyword stuffing
3. **Mobile-first** — Tester le rendu responsive
4. **Accessibilité** — Alt tags, contrastes, hiérarchie des titres
5. **Performance** — Images optimisées (<500KB), lazy loading sauf hero
6. **Cohérence** — Respecter la palette (#00a7de, #0090c0, #252525), les conventions TailwindCSS existantes

### Checklist SEO on-page (pour chaque page modifiée)

```
- [ ] Title : 50-60 caractères, KW principal en début, format "[KW] [Ville] | Centre Médical Paris-Levallois"
- [ ] Meta description : 150-160 caractères, KW + CTA, unique
- [ ] H1 : unique, contient le KW principal, différent du title
- [ ] Canonical : URL correcte sans trailing slash
- [ ] OG tags : title, description, url, type, image
- [ ] Schema.org : MedicalWebPage/FAQPage selon contexte
- [ ] Liens internes : min 3, ancres descriptives
- [ ] Images : alt descriptif, lazy loading, dimensions
- [ ] Contenu : min 800 mots (sous-pages), min 1500 mots (pillar pages)
```

### Format de title recommandé par spécialité

```
Ophtalmologie : "Ophtalmologue Paris-Levallois (92300) | Secteur 1 | Centre Médical"
Psychologie   : "Psychologue Levallois-Perret | [Spécialité] | Centre Médical Paris-Levallois"
Kinésithérapie: "Kinésithérapeute Paris-Levallois (92300) | Secteur 1 | Centre Médical"
Diététique    : "Diététicien Levallois-Perret | Consultation Nutrition | Centre Médical Paris-Levallois"
Soins inf.    : "Soins Infirmiers Levallois-Perret | [Type soin] | Centre Médical Paris-Levallois"
Méd. générale : "Médecin Généraliste Levallois-Perret (92300) | Secteur 1 | Centre Médical"
```

## Après l'implémentation

### 1. Vérifier la qualité

Pour chaque page modifiée, exécuter `/verifier-seo` mentalement :
- Title, meta, H1, canonical, OG, Schema
- Hiérarchie H1 > H2 > H3
- Liens internes fonctionnels
- Images avec alt

### 2. Tester en local

// turbo
```bash
cd "/Users/cedrictantcheu/Documents/vtimagerie_v2_DEPLOY_FINAL_GTM_CONSENT_V2_20250724_025441 5/centremedicalparislevallois" && python3 -m http.server 8000
```

Vérifier visuellement sur http://localhost:8000 :
- Rendu desktop et mobile
- Navigation fonctionnelle
- Pas de contenu cassé

### 3. Mettre à jour le plan maître

Après chaque tâche terminée :
- Cocher la tâche dans `docs/PLAN_MASTER_IMPLEMENTATION_SEO.md`
- Noter les éventuels impacts découverts sur d'autres tâches

### 4. Commit

```bash
git add -A
git commit -m "seo: [description courte de l'optimisation]"
```

Convention de commit SEO :
- `seo: optimiser title/H1 page [spécialité]`
- `seo: enrichir contenu [page]`
- `seo: ajouter structured data [type]`
- `seo: corriger maillage interne [section]`
- `feat: créer page [nom-page]`

## Outils disponibles

| Outil | Usage |
|---|---|
| **Code Search** | Trouver du code dans le site (grep, read) |
| **Web Search** | Rechercher les pages top Google pour un KW |
| **Read URL** | Analyser le contenu d'une page concurrente |
| **Browser (Playwright)** | Tester le site en local, vérifier le rendu |
| **Google Analytics MCP** | Vérifier les données de trafic GA4 |
| **Workflows existants** | `/verifier-seo`, `/nouvelle-page`, `/ajouter-faq`, `/ajouter-specialite` |

## Rappels critiques

- **Ne JAMAIS modifier `google-ads.html`** (landing VT Imagerie, compte séparé)
- **Ne JAMAIS confondre les deux landing pages ophtalmo** (google-ads.html vs google-ads-gtm.html)
- **GTM du site** : `GTM-MQ2KK9XS` (compte dédié CDS)
- **Adresse du centre** : 60 Rue Victor Hugo, 92300 Levallois-Perret (PAS 48 rue)
- **Structured data** : vérifier que `medicalSpecialty` et `availableService` sont à jour dans index.html
- **www vs non-www** : canonical TOUJOURS sans www (centremedicalparislevallois.fr)
