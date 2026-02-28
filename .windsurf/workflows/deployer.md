---
description: Déployer le site sur l'hébergement LWS via FTP
---

# Workflow : Déployer sur LWS

## Pré-requis

1. Identifiants FTP LWS (demander à l'utilisateur si non disponibles)
2. Accès au panneau d'administration LWS

## Étapes

### 1. Vérifications pré-déploiement

Vérifier que tout est prêt :

- [ ] Le site fonctionne en local
- [ ] Pas d'erreurs dans la console du navigateur
- [ ] Tous les liens fonctionnent
- [ ] Images optimisées
- [ ] CHANGELOG.md mis à jour

### 2. Créer l'archive de déploiement (si méthode ZIP)

// turbo
```bash
cd /chemin/vers/centremedicalparislevallois
zip -r deploy-centremedical-$(date +%Y%m%d).zip . \
    -x "*.git*" \
    -x "*.md" \
    -x ".windsurf/*" \
    -x "docs/*" \
    -x "*-original.jpg" \
    -x "*.HEIC" \
    -x "deploy-*.zip" \
    -x ".DS_Store" \
    -x "node_modules/*"
```

### 3. Connexion FTP

**Informations de connexion LWS** :
- Hôte : `ftp.centremedicalparislevallois.fr` (ou fourni par LWS)
- Port : 21 (FTP) ou 22 (SFTP)
- Dossier distant : `/www/` ou `/public_html/`

### 4. Upload des fichiers

**Option A - FileZilla** :
1. Ouvrir FileZilla
2. Connexion avec les identifiants
3. Naviguer vers `/www/`
4. Transférer les fichiers modifiés

**Option B - Via panneau LWS** :
1. Se connecter au panneau LWS
2. Gestionnaire de fichiers
3. Upload et extraction du ZIP

### 5. Vérification post-déploiement

Tester ces URLs :

- [ ] https://centremedicalparislevallois.fr/
- [ ] https://centremedicalparislevallois.fr/pages/le-centre.html
- [ ] Navigation mobile fonctionnelle
- [ ] Liens Doctolib fonctionnels

### 6. Commit et tag (si release)

```bash
git add .
git commit -m "chore: déploiement $(date +%Y-%m-%d)"
git tag v1.x.x
git push origin main --tags
```

## En cas de problème

1. **Page blanche** : Vérifier les chemins des fichiers CSS/JS
2. **404** : Vérifier que le fichier a bien été uploadé
3. **Styles cassés** : Vider le cache du navigateur

## Rollback

Si problème critique :
1. Restaurer depuis Git : `git checkout <commit_precedent>`
2. Re-déployer manuellement
3. Ou utiliser la restauration LWS depuis le panneau
