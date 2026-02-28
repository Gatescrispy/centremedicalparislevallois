# 🏥 Centre Médical Paris-Levallois

> Site web officiel du Centre Médical Paris-Levallois  
> **URL de production** : https://centremedicalparislevallois.fr/

---

## 📋 À propos

Centre de santé pluridisciplinaire situé au **60 Rue Victor Hugo, 92300 Levallois-Perret**.

### Spécialités proposées
- 👁️ **Ophtalmologie** - Examen de la vue, dépistage pathologies oculaires
- 👓 **Orthoptie** - Bilan orthoptique, rééducation visuelle
- 🩺 **Médecine générale** - Consultations, suivi médical, vaccinations
- 💉 **Soins infirmiers** - Prises de sang, injections, pansements

### Informations pratiques
- **Téléphone** : 01 80 88 37 16
- **Horaires** : Lun-Ven 9h-19h, Sam 9h-14h
- **Conventionné** : Secteur 1, Tiers payant, Carte Vitale

---

## 🛠️ Stack Technique

| Technologie | Usage |
|-------------|-------|
| HTML5 | Structure des pages |
| TailwindCSS | Styling (fichier compilé) |
| Alpine.js | Interactions (FAQ accordion) |
| Font Awesome 6 | Icônes |
| Google Tag Manager | Analytics & Tracking |
| Google Analytics 4 | Mesure d'audience |
| Google Ads | Tracking conversions |

---

## 📁 Structure du projet

```
centremedicalparislevallois/
├── index.html                 # Page d'accueil
├── components/
│   ├── header.html            # Navigation (chargé dynamiquement)
│   └── footer.html            # Pied de page
├── pages/
│   ├── le-centre.html         # Page "À propos"
│   ├── landing/               # Landing pages Google Ads
│   └── specialites/           # Pages par spécialité (à créer)
├── assets/
│   ├── css/tailwind.css       # Styles compilés
│   ├── images/                # Images optimisées
│   └── js/                    # Scripts
├── .windsurf/
│   └── workflows/             # Workflows Cascade
└── docs/                      # Documentation
```

---

## 🚀 Développement

### Prérequis
- Éditeur de code (VS Code / Windsurf recommandé)
- Git
- Serveur local (Live Server, Python http.server, etc.)

### Lancer en local
```bash
# Avec Python
python -m http.server 8000

# Avec Node.js (npx)
npx serve .

# Avec VS Code
# Installer l'extension "Live Server" et cliquer sur "Go Live"
```

### Conventions
Voir [CONTRIBUTING.md](./CONTRIBUTING.md) pour les conventions de code et bonnes pratiques.

---

## 📦 Déploiement

**Hébergement** : LWS (serveur mutualisé)

Voir [docs/DEPLOYMENT.md](./docs/DEPLOYMENT.md) pour les instructions de déploiement.

### Déploiement rapide (FTP)
1. Se connecter au FTP LWS
2. Naviguer vers `/www/` ou `/public_html/`
3. Uploader les fichiers modifiés
4. Vider le cache si nécessaire

---

## 📊 Analytics & Tracking

| Service | ID |
|---------|-----|
| GTM Container | GTM-525BNW8J |
| GA4 Property | G-MQ9CEHQVW3 |
| Google Ads | AW-11456521545 |

### Événements trackés
- `cta_footer_doctolib` - Clic RDV footer
- `cta_footer_call` - Clic appel footer
- `cta_sticky_doctolib` - Clic RDV barre mobile
- `cta_sticky_call` - Clic appel barre mobile

---

## 🎨 Palette de couleurs

```css
--primary-500: #00a7de;    /* Bleu logo principal */
--primary-600: #0090c0;    /* Bleu hover */
--primary-700: #007ba3;    /* Bleu active */
--primary-50:  #e6f7fc;    /* Bleu très clair (backgrounds) */
--text-dark:   #252525;    /* Texte principal */
--text-secondary: #4a4a4a; /* Texte secondaire */
```

---

## 📝 Changelog

Voir [CHANGELOG.md](./CHANGELOG.md) pour l'historique des modifications.

---

## 📚 Documentation

- [PROJECT_CONTEXT.md](./PROJECT_CONTEXT.md) - Contexte complet du projet
- [CONTRIBUTING.md](./CONTRIBUTING.md) - Guide de contribution
- [docs/DEPLOYMENT.md](./docs/DEPLOYMENT.md) - Instructions de déploiement
- [docs/SEO.md](./docs/SEO.md) - Guide SEO

---

## 🤖 Workflows Cascade

Des workflows sont disponibles dans `.windsurf/workflows/` pour faciliter le développement :

- `/nouvelle-page` - Créer une nouvelle page
- `/deployer` - Déployer sur LWS
- `/optimiser-images` - Optimiser les images
- `/ajouter-specialite` - Ajouter une page spécialité
- `/verifier-seo` - Vérifier le SEO d'une page

---

## 📞 Contact

- **Site** : https://centremedicalparislevallois.fr/
- **Doctolib** : [Prendre RDV](https://www.doctolib.fr/centre-de-sante/levallois-perret/centre-medical-paris-levallois)
- **Téléphone** : 01 80 88 37 16
