# 🚀 Guide de Déploiement - Centre Médical Paris-Levallois

> Instructions pour déployer le site sur l'hébergement LWS

---

## 📋 Informations d'hébergement

| Élément | Valeur |
|---------|--------|
| **Hébergeur** | LWS |
| **Type** | Serveur mutualisé |
| **Protocole** | FTP / SFTP |
| **Dossier racine** | `/www/` ou `/public_html/` |
| **URL production** | https://centremedicalparislevallois.fr/ |

---

## 🔐 Accès FTP

> ⚠️ **SÉCURITÉ** : Ne jamais commiter les identifiants FTP dans Git !

### Configuration FTP (à renseigner localement)

Créer un fichier `.ftpconfig` (gitignored) :
```json
{
    "host": "ftp.votredomaine.fr",
    "user": "votre_utilisateur",
    "password": "votre_mot_de_passe",
    "port": 21,
    "remote_path": "/www/"
}
```

### Clients FTP recommandés
- **FileZilla** (gratuit, multiplateforme)
- **Cyberduck** (macOS)
- **WinSCP** (Windows)

---

## 📦 Méthode 1 : Déploiement manuel FTP

### Étapes

1. **Connexion FTP**
   - Ouvrir FileZilla ou autre client FTP
   - Renseigner les identifiants LWS
   - Se connecter au serveur

2. **Navigation**
   - Aller dans `/www/` ou `/public_html/`
   - C'est la racine du site web

3. **Upload des fichiers**
   - Transférer les fichiers modifiés
   - Conserver la structure des dossiers

4. **Vérification**
   - Visiter https://centremedicalparislevallois.fr/
   - Vérifier les pages modifiées
   - Tester sur mobile

### Fichiers à NE PAS uploader
- `.git/`
- `.gitignore`
- `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`
- `PROJECT_CONTEXT.md`
- `.windsurf/`
- `docs/`
- `*-original.jpg` (images non compressées)
- `*.HEIC`
- `deploy-*.zip`

---

## 📦 Méthode 2 : Déploiement via ZIP

### Créer l'archive de déploiement

```bash
# Depuis le dossier du projet
zip -r deploy-centremedical-$(date +%Y%m%d).zip . \
    -x "*.git*" \
    -x "*.md" \
    -x ".windsurf/*" \
    -x "docs/*" \
    -x "*-original.jpg" \
    -x "*.HEIC" \
    -x "deploy-*.zip" \
    -x ".DS_Store"
```

### Upload via panneau LWS

1. Se connecter au panneau d'administration LWS
2. Aller dans "Gestionnaire de fichiers"
3. Naviguer vers `/www/`
4. Uploader le fichier ZIP
5. Extraire l'archive
6. Supprimer le ZIP après extraction

---

## 🔄 Méthode 3 : Déploiement automatisé (Git + FTP)

### Option A : GitHub Actions + FTP

Créer `.github/workflows/deploy.yml` :

```yaml
name: Deploy to LWS

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: FTP Deploy
        uses: SamKirkland/FTP-Deploy-Action@v4.3.4
        with:
          server: ${{ secrets.FTP_SERVER }}
          username: ${{ secrets.FTP_USERNAME }}
          password: ${{ secrets.FTP_PASSWORD }}
          server-dir: /www/
          exclude: |
            **/.git*
            **/.git*/**
            **/docs/**
            **/.windsurf/**
            **/*.md
            **/*-original.jpg
            **/*.HEIC
```

### Configuration des secrets GitHub

1. Aller dans Settings > Secrets and variables > Actions
2. Ajouter les secrets :
   - `FTP_SERVER` : l'adresse FTP LWS
   - `FTP_USERNAME` : l'utilisateur FTP
   - `FTP_PASSWORD` : le mot de passe FTP

---

## ✅ Checklist pré-déploiement

### Tests locaux
- [ ] Le site fonctionne en local
- [ ] Pas d'erreurs dans la console
- [ ] Header et footer se chargent
- [ ] Tous les liens fonctionnent
- [ ] Images s'affichent correctement
- [ ] Mobile responsive OK

### Contenu
- [ ] Informations à jour (horaires, téléphone)
- [ ] Pas de fautes d'orthographe
- [ ] Liens Doctolib fonctionnels

### Performance
- [ ] Images optimisées (< 500 KB chacune)
- [ ] Pas de fichiers inutiles

### Git
- [ ] Tous les changements commités
- [ ] CHANGELOG mis à jour
- [ ] Tag de version si release

---

## 🔍 Vérification post-déploiement

### Tests à effectuer

1. **Page d'accueil** : https://centremedicalparislevallois.fr/
2. **Navigation** : Tester tous les liens du menu
3. **Mobile** : Tester sur smartphone
4. **Formulaires** : Tester les liens Doctolib
5. **Analytics** : Vérifier dans GA4 que les visites sont trackées

### Outils de test

- [Google PageSpeed Insights](https://pagespeed.web.dev/)
- [Google Search Console](https://search.google.com/search-console)
- [GTMetrix](https://gtmetrix.com/)
- [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)

---

## 🚨 Rollback en cas de problème

### Procédure de rollback

1. **Via Git** :
   ```bash
   git log --oneline -10  # Trouver le commit précédent
   git checkout <commit_hash>
   # Re-déployer manuellement
   ```

2. **Via backup LWS** :
   - Accéder au panneau LWS
   - Utiliser la fonction "Restaurer une sauvegarde"

### Bonnes pratiques
- Toujours faire un backup avant un déploiement majeur
- Garder les 3 dernières versions en local
- Tester sur une URL de staging si possible

---

## 📞 Support LWS

- **Documentation** : https://aide.lws.fr/
- **Support** : Ticket depuis le panneau client
- **Téléphone** : 01 77 62 30 03
