# Audit Google Search Console — Centre Médical Paris-Levallois

**Date** : 02/03/2026  
**Propriété** : `sc-domain:centremedicalparislevallois.fr`  
**Compte** : `djouma-livine@centremedicalparislevallois.fr`  

---

## 1. Vue d'ensemble

| Métrique | Valeur |
|----------|--------|
| Type de propriété | Domaine (vérifié) ✅ |
| Actions manuelles | Aucune ✅ |
| Problèmes de sécurité | Aucun ✅ |
| HTTPS | 2 pages HTTPS, 0 non-HTTPS ✅ |

---

## 2. Performances (3 derniers mois)

| Métrique | Valeur |
|----------|--------|
| **Clics** | 3 |
| **Impressions** | 155 |
| **CTR moyen** | 1,9% |
| **Position moyenne** | 5,9 |
| **Requêtes totales** | 24 |
| **Pages avec impressions** | 2 seulement |

### Top requêtes

| Requête | Clics | Impressions |
|---------|-------|-------------|
| centre médical paris levallois | 1 | 2 |
| centre medical levallois | 0 | 12 |
| centre medical paris levallois | 0 | 11 |
| centre medical de levallois perret | 0 | 9 |
| medecin de garde levallois | 0 | 4 |
| centre médical paris-levallois avis | 0 | 3 |
| cabinet médical levallois perret | 0 | 2 |
| centre medical ouvert le dimanche paris | 0 | 2 |
| centre ophtalmo levallois | 0 | 2 |

### Pages avec impressions

| Page | Clics | Impressions |
|------|-------|-------------|
| `/` (accueil) | 3 | 141 |
| `/pages/le-centre.html` | 0 | 50 |

**⚠️ Constat** : Sur 49 pages du site, seules **2 pages** apparaissent dans les résultats Google. Les 47 autres ne sont pas encore indexées.

---

## 3. Indexation

**Statut** : "Traitement des données en cours" — Google est encore en train de crawler le site.

### 🔴 CRITIQUE : Sitemap inaccessible

Le sitemap soumis à GSC (`https://www.centremedicalparislevallois.fr/sitemap.xml`) retourne une **erreur 404**.

**Cause** : Le fichier `sitemap.xml` existe localement mais **n'a pas été déployé** sur le serveur LWS.

**Impact** : Google ne peut pas découvrir les 49 pages du site via le sitemap, ce qui explique pourquoi seulement 2 pages sont indexées (découvertes via des liens internes uniquement).

### ⚠️ Bug sitemap : Landing page noindex incluse

La page `pages/landing/google-ads.html` est dans le sitemap alors qu'elle a `<meta name="robots" content="noindex, nofollow">`. Envoyer une URL noindex dans le sitemap crée un signal contradictoire pour Google.

**Action** : Retirer cette URL du sitemap.

---

## 4. Données structurées (Rich Results)

| Type | Valides | Non valides |
|------|---------|-------------|
| Fils d'Ariane | 2 | 0 ✅ |
| FAQ | 1 | 0 ✅ |
| Extraits d'avis | 1 | 0 ✅ |

Les données structurées détectées sont toutes valides.

---

## 5. Core Web Vitals

**Statut** : "Pas assez de données d'utilisation ces 90 derniers jours" (mobile et ordinateur).

Normal pour un site récent avec peu de trafic. Les données CrUX apparaîtront quand le site aura suffisamment de visites.

**Recommandation** : Tester via PageSpeed Insights en attendant les données CrUX.

---

## 6. HTTPS

| Pages HTTPS | Pages non-HTTPS |
|-------------|-----------------|
| 2 | 0 ✅ |

Le site est entièrement en HTTPS.

---

## 7. Liens

Rapport en cours de traitement (données non encore disponibles).

---

## 8. Configuration serveur

### 🔴 Pas de .htaccess

Aucun fichier `.htaccess` n'a été trouvé dans le projet. Sur un hébergement LWS (Apache), un `.htaccess` est essentiel pour :

- **Redirections www ↔ non-www** (canonicalisation)
- **Forcer HTTPS**
- **Cache navigateur** (améliore les Core Web Vitals)
- **Compression gzip/brotli**
- **Headers de sécurité** (X-Content-Type-Options, X-Frame-Options, etc.)
- **Types MIME** corrects pour le sitemap XML

### 🟡 robots.txt

Le `robots.txt` est bien configuré :
- ✅ Sitemap référencé
- ✅ Dossiers techniques bloqués (docs/, .windsurf/, .github/)
- ⚠️ La règle `Disallow: /*.md$` utilise `$` qui n'est supporté que par Googlebot (pas standard)
- ⚠️ `Crawl-delay: 1` n'est pas respecté par Googlebot (uniquement Bing/Yandex)

---

## 9. Problèmes identifiés (par priorité)

### 🔴 Critiques

| # | Problème | Impact | Action |
|---|----------|--------|--------|
| 1 | **Sitemap retourne 404** | Google ne découvre pas 47/49 pages | Déployer sitemap.xml + robots.txt sur LWS |
| 2 | **Pas de .htaccess** | Pas de redirect www, pas de cache, pas de compression | Créer un .htaccess complet |

### 🟡 Importants

| # | Problème | Impact | Action |
|---|----------|--------|--------|
| 3 | Landing page noindex dans le sitemap | Signal contradictoire | Retirer du sitemap |
| 4 | Seulement 2/49 pages indexées | 96% du site invisible sur Google | Résoudre #1 puis demander indexation |
| 5 | 0 clic sur 10 requêtes top | Title/description pas assez attractifs | Optimiser les meta descriptions |

### 🟢 Positifs

- Propriété domaine vérifiée ✅
- Aucune action manuelle ✅
- Aucun problème de sécurité ✅
- HTTPS complet ✅
- Données structurées valides (Breadcrumbs, FAQ, Review) ✅

---

## 10. Plan d'action recommandé

| Priorité | Action | Détail |
|----------|--------|--------|
| **P1** | Créer `.htaccess` | Redirections, cache, compression, sécurité |
| **P2** | Corriger `sitemap.xml` | Retirer la landing page noindex |
| **P3** | Déployer | sitemap.xml, robots.txt, .htaccess sur LWS |
| **P4** | Re-soumettre sitemap dans GSC | Après déploiement |
| **P5** | Demander indexation des pages clés | Via "Inspection de l'URL" dans GSC |
| **P6** | Optimiser meta descriptions | Pour améliorer le CTR |

---

*Rapport généré le 02/03/2026 — Cascade*
