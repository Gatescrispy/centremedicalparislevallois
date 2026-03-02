# Audit GA4 — Centre Médical Paris-Levallois

**Date** : 2 mars 2026  
**Propriété** : Centre Médical Paris-Levallois  
**ID Propriété** : 385911713 (p526394430)  
**ID Mesure** : G-XHP0ZF8ZSF  
**Flux Web** : 13683037585  
**Compte** : djouma-livine@centremedicalparislevallois.fr  

---

## 1. Résumé Exécutif

L'audit GA4 a révélé **plusieurs problèmes critiques** qui ont été **corrigés** pendant l'audit :

| Élément | Avant | Après | Statut |
|---------|-------|-------|--------|
| Conservation données événements | 2 mois | **14 mois** | ✅ Corrigé |
| Google Signals | Désactivé | **Activé (307 régions)** | ✅ Corrigé |
| Association Google Ads | Aucune | **397-970-4056 associé** | ✅ Créée |
| Association Search Console | Aucune | **centremedicalparislevallois.fr** | ✅ Créée |
| Événements clés métier | Aucun (purchase, qualify_lead...) | **clic_doctolib + clic_telephone** | ✅ Créés |

---

## 2. Configuration de la Propriété

### 2.1 Flux de données Web
- **Nom** : Centre Médical Paris-Levallois - Web
- **URL** : https://www.centremedicalparislevallois.fr
- **ID de mesure** : G-XHP0ZF8ZSF
- **ID du flux** : 13683037585
- **Collecte active** : ✅ Trafic reçu dans les dernières 48h
- **Mesures améliorées** : ✅ Activées (pages vues, défilements, clics sortants, recherche sur site, interactions vidéo, téléchargements de fichiers, engagement des formulaires)

### 2.2 Conservation des données
- **Données d'événement** : 14 mois ✅ (était 2 mois — corrigé)
- **Données utilisateur** : 14 mois ✅
- **Réinitialisation sur nouvelle activité** : Activé ✅

### 2.3 Collecte des données
- **Google Signals** : Activé ✅ (307 régions sur 307)
- **Données précises appareil/zone géo** : Activé ✅
- **Collecte données fournies par utilisateur** : Indisponible (catégorie sectorielle Santé — normal)

### 2.4 Paramètres de consentement
- **Statut global** : "Bon" — configuration correcte ✅
- **Signaux analytics** : Inactifs (normal — activés après déploiement GTM)
- **Signaux publicité** : Inactifs (normal — activés après déploiement GTM)

---

## 3. Associations de Produits

### 3.1 Google Ads ✅ CRÉÉE
- **Compte** : Compte Google Ads
- **ID** : 397-970-4056
- **Publicité personnalisée** : Activé
- **Accès fonctionnalités Analytics depuis Ads** : Activé
- **Date** : 2 mars 2026

### 3.2 Search Console ✅ CRÉÉE
- **Propriété** : centremedicalparislevallois.fr (Domaine)
- **Flux Web** : Centre Médical Paris-Levallois - Web
- **Date** : 2 mars 2026

---

## 4. Événements

### 4.1 Événements récents (6 actifs)
| Événement | Source | Type |
|-----------|--------|------|
| `page_view` | Mesure améliorée | Standard |
| `session_start` | Automatique | Standard |
| `first_visit` | Automatique | Standard |
| `user_engagement` | Automatique | Standard |
| `scroll` | Mesure améliorée | Standard |
| `click` | Mesure améliorée | Standard |

### 4.2 Événements clés (conversions)

#### Créés pendant l'audit ✅
| Événement | Devise | Valeur | Comptabilisation |
|-----------|--------|--------|-----------------|
| `clic_doctolib` | EUR (€) | 1 € | Une fois par événement |
| `clic_telephone` | EUR (€) | 1 € | Une fois par événement |

#### Événements clés par défaut (à nettoyer)
| Événement | Statut | Action recommandée |
|-----------|--------|-------------------|
| `close_convert_lead` | Aucune donnée | ⚠️ Désactiver — non pertinent |
| `purchase` | Aucune donnée | ⚠️ Désactiver — pas de e-commerce |
| `qualify_lead` | Aucune donnée | ⚠️ Désactiver — non pertinent |

---

## 5. Dimensions / Métriques personnalisées

Aucune dimension ou métrique personnalisée configurée. C'est normal pour ce stade du projet.

**Recommandation future** : Après le déploiement et la collecte de données, envisager :
- Dimension `centre` (event-scoped) — pour identifier quel centre génère la conversion
- Dimension `exam_type` (event-scoped) — pour identifier le type d'examen demandé
- Dimension `landing_page` (event-scoped) — pour distinguer conversions landing vs site

---

## 6. Actions Réalisées Pendant l'Audit

1. ✅ **Conservation données événements** : Passée de 2 à 14 mois
2. ✅ **Google Signals** : Activé dans 307 régions
3. ✅ **Association Google Ads** : Créée (397-970-4056)
4. ✅ **Association Search Console** : Créée (centremedicalparislevallois.fr)
5. ✅ **Événement clé `clic_doctolib`** : Créé (1€, par événement)
6. ✅ **Événement clé `clic_telephone`** : Créé (1€, par événement)

---

## 7. Recommandations Post-Déploiement

### Priorité haute
1. **Désactiver les événements clés inutiles** : `close_convert_lead`, `purchase`, `qualify_lead`
2. **Vérifier le trafic temps réel** après déploiement pour confirmer la collecte
3. **Résoudre l'alerte malware GTM** : Les tags GTM sont signalés comme potentiel malware (faux positif pour conteneurs récents)

### Priorité moyenne
4. **Configurer le taggage automatique** Google Ads pour des rapports plus détaillés
5. **Créer des audiences de remarketing** dans GA4 pour les campagnes Ads
6. **Ajouter des dimensions personnalisées** (`centre`, `exam_type`) une fois les données collectées

### Priorité basse
7. **Configurer des alertes personnalisées** pour détecter les baisses de trafic
8. **Exporter les conversions vers Google Ads** une fois validées
9. **Créer des rapports personnalisés** pour le suivi mensuel

---

## 8. Checklist Pré-Déploiement GA4

- [x] Flux de données Web configuré
- [x] Mesures améliorées activées
- [x] Conservation données 14 mois
- [x] Google Signals activé
- [x] Paramètres de consentement OK
- [x] Association Google Ads créée
- [x] Association Search Console créée
- [x] Événements clés métier configurés (clic_doctolib, clic_telephone)
- [ ] Désactiver événements clés par défaut inutiles
- [ ] Vérifier collecte temps réel post-déploiement
- [ ] Valider export conversions vers Google Ads

---

*Audit réalisé le 2 mars 2026*
