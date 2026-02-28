---
description: Reprendre le développement du projet après une pause (workflow d'onboarding pour nouvelles sessions Cascade)
---

# Workflow : Reprendre le projet

## Objectif

Ce workflow permet à une nouvelle session Cascade de comprendre rapidement le contexte du projet et de reprendre le travail efficacement.

## Étapes d'onboarding

### 1. Lire la documentation essentielle

Lire ces fichiers dans l'ordre :

1. **PROJECT_CONTEXT.md** - Vue d'ensemble complète du projet
   - Informations du centre médical
   - Stack technique
   - Structure des fichiers
   - Points d'attention

2. **README.md** - Introduction rapide

3. **CHANGELOG.md** - Historique des modifications récentes

4. **CONTRIBUTING.md** - Conventions de code (si modifications prévues)

### 2. Comprendre la structure

```
centremedicalparislevallois/
├── index.html                 # Page d'accueil principale
├── components/
│   ├── header.html            # Navigation
│   └── footer.html            # Pied de page
├── pages/
│   ├── le-centre.html         # Page "À propos"
│   ├── specialites/           # Pages par spécialité
│   └── landing/               # Landing pages
├── assets/
│   ├── css/tailwind.css       # Styles
│   ├── images/                # Images
│   └── js/                    # Scripts
└── docs/                      # Documentation
```

### 3. Identifier l'état actuel

Vérifier :
- [ ] Derniers commits dans Git
- [ ] Pages existantes vs pages à créer (voir PROJECT_CONTEXT.md)
- [ ] Issues ou TODOs en cours

### 4. Vérifier les pages manquantes

Pages référencées mais non créées :
- `/pages/specialites/ophtalmologie.html`
- `/pages/specialites/orthoptie.html`
- `/pages/specialites/medecine-generale.html`
- `/pages/specialites/soins-infirmiers.html`
- `/pages/tarifs.html`
- `/pages/contact.html`
- `/pages/mentions-legales.html`
- `/pages/politique-confidentialite.html`

### 5. Tester le site en local

// turbo
```bash
# Lancer un serveur local
python -m http.server 8000
# ou
npx serve .
```

Puis ouvrir http://localhost:8000

### 6. Demander les objectifs de la session

Questions à poser à l'utilisateur :
1. Quel est l'objectif de cette session ?
2. Y a-t-il des priorités ou deadlines ?
3. Des modifications spécifiques demandées ?

## Informations clés à retenir

### Couleurs du projet
- Bleu primaire : `#00a7de`
- Bleu hover : `#0090c0`
- Texte : `#252525`

### IDs Analytics
- GTM : `GTM-525BNW8J`
- GA4 : `G-MQ9CEHQVW3`
- Google Ads : `AW-11456521545`

### Contact du centre
- Téléphone : 01 80 88 37 16
- Adresse : 60 Rue Victor Hugo, 92300 Levallois-Perret
- Doctolib : https://www.doctolib.fr/centre-de-sante/levallois-perret/centre-medical-paris-levallois

### Hébergement
- Hébergeur : LWS
- Déploiement : FTP (voir docs/DEPLOYMENT.md)

## Workflows disponibles

- `/nouvelle-page` - Créer une nouvelle page
- `/deployer` - Déployer sur LWS
- `/ajouter-specialite` - Ajouter une page spécialité
- `/verifier-seo` - Audit SEO d'une page
- `/optimiser-images` - Optimiser les images
- `/modifier-horaires` - Mettre à jour les horaires
- `/ajouter-faq` - Ajouter une question FAQ

## Prêt à commencer !

Une fois le contexte compris, demander à l'utilisateur ce qu'il souhaite accomplir dans cette session.
