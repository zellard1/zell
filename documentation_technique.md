# Documentation Technique - Site Web Chef DEGAS

## Table des matières

1. [Introduction](#introduction)
2. [Architecture du site](#architecture-du-site)
3. [Structure des fichiers](#structure-des-fichiers)
4. [Charte graphique](#charte-graphique)
5. [Fonctionnalités implémentées](#fonctionnalités-implémentées)
6. [Technologies utilisées](#technologies-utilisées)
7. [Guide de maintenance](#guide-de-maintenance)
8. [Recommandations pour l'évolution](#recommandations-pour-lévolution)

## Introduction

Cette documentation technique présente le site web "Chef DEGAS", une plateforme dédiée aux recettes de pâtisserie créées par Claude (Opus 4). Le site a été développé selon les spécifications du cahier des charges fourni, avec pour objectif de proposer une expérience utilisateur intuitive et agréable, tout en mettant en valeur les recettes de pâtisserie.

Le site est conçu comme un site statique, ce qui permet une grande rapidité de chargement et une maintenance simplifiée. Il intègre néanmoins des fonctionnalités interactives côté client pour améliorer l'expérience utilisateur.

## Architecture du site

Le site "Chef DEGAS" est structuré selon une architecture simple et efficace :

### Pages principales
- **Page d'accueil** (`index.html`) : Point d'entrée du site présentant les différentes catégories de recettes et une introduction au concept.
- **Pages de catégories** : Pages listant les recettes par type (viennoiseries, entremets, tartes).
- **Pages de recettes** : Pages détaillées pour chaque recette avec ingrédients, étapes de préparation et fonctionnalités interactives.
- **Page de compte utilisateur** (`compte.html`) : Gestion du profil utilisateur et des recettes favorites.
- **Page À propos** (`a-propos.html`) : Présentation de Claude et du concept du site.
- **Page de mentions légales** (`mentions-legales.html`) : Informations légales obligatoires.
- **Page 404** (`404.html`) : Page d'erreur personnalisée.

### Organisation des dossiers
- **Racine** : Fichiers HTML principaux
- **assets/** : Ressources du site
  - **css/** : Feuilles de style
  - **js/** : Scripts JavaScript
  - **images/** : Images du site (logo, recettes, etc.)
  - **fonts/** : Polices de caractères (si nécessaire)

## Structure des fichiers

```
chef-degas/
├── index.html                  # Page d'accueil
├── compte.html                 # Page de compte utilisateur
├── a-propos.html               # Page À propos
├── mentions-legales.html       # Mentions légales
├── 404.html                    # Page d'erreur 404
├── viennoiseries/              # Catégorie Viennoiseries
│   ├── index.html              # Liste des viennoiseries
│   └── croissants.html         # Exemple de recette
├── entremets/                  # Catégorie Entremets
│   └── index.html              # Liste des entremets
├── tartes/                     # Catégorie Tartes
│   └── index.html              # Liste des tartes
└── assets/                     # Ressources
    ├── css/
    │   ├── normalize.css       # Reset CSS
    │   ├── style.css           # Styles principaux
    │   └── responsive.css      # Styles responsives
    ├── js/
    │   ├── main.js             # Script principal
    │   ├── portions.js         # Ajustement des portions
    │   └── favorites.js        # Gestion des favoris
    └── images/
        ├── logo/               # Logo du site
        ├── recipes/            # Images des recettes
        ├── categories/         # Images des catégories
        ├── ingredients/        # Icônes des ingrédients
        └── icons/              # Icônes diverses
```

## Charte graphique

### Couleurs
- **Couleur principale** : Corail/orange doux (#FF7F50)
- **Couleur principale claire** : #FFD8CC
- **Couleur de fond** : Blanc cassé/ivoire (#FFFCF8)
- **Couleur de texte** : Gris foncé (#333333)
- **Couleur de texte secondaire** : Gris moyen (#666666)
- **Couleur de bordure** : Gris clair (#E5E5E5)

### Typographie
- **Police principale** : 'Open Sans', 'Roboto', sans-serif
- **Taille de base** : 16px
- **Hiérarchie des titres** :
  - H1 : 2rem (32px)
  - H2 : 1.5rem (24px)
  - H3 : 1.125rem (18px)

### Espacements
- **xs** : 0.25rem (4px)
- **sm** : 0.5rem (8px)
- **md** : 1rem (16px)
- **lg** : 1.5rem (24px)
- **xl** : 2rem (32px)
- **xxl** : 3rem (48px)

### Éléments d'interface
- **Bordures arrondies** :
  - Petites : 4px
  - Moyennes : 8px
  - Grandes : 16px
- **Ombres** : 0 2px 8px rgba(0, 0, 0, 0.1)
- **Transitions** : 0.2s à 0.3s ease

## Fonctionnalités implémentées

### 1. Navigation responsive
- Menu de navigation adaptatif (hamburger sur mobile)
- Fil d'Ariane pour la navigation secondaire
- Détection automatique de la page active

### 2. Présentation des recettes
- Affichage des informations clés (temps de préparation, difficulté, etc.)
- Liste des ingrédients avec icônes
- Étapes de préparation numérotées
- Astuces du chef

### 3. Fonctionnalités interactives
- **Ajustement des portions** : Recalcul automatique des quantités d'ingrédients
- **Système de favoris** : Sauvegarde des recettes préférées (localStorage)
- **Partage sur réseaux sociaux** : Boutons de partage pour chaque recette
- **Système de commentaires** : Préparé pour intégration avec un service externe
- **Système de notation** : Interface pour noter les recettes

### 4. Gestion des utilisateurs
- Interface de connexion/inscription
- Gestion des favoris
- Profil utilisateur (simulation)

### 5. Accessibilité
- Structure sémantique HTML5
- Attributs ARIA pour les composants interactifs
- Focus visible pour la navigation au clavier
- Textes alternatifs pour les images
- Contraste suffisant pour la lisibilité

### 6. Performance
- CSS et JavaScript minifiés
- Chargement différé des images (lazy loading)
- Optimisation pour les moteurs de recherche

## Technologies utilisées

### Langages
- **HTML5** : Structure sémantique du site
- **CSS3** : Mise en forme et animations
- **JavaScript** : Fonctionnalités interactives côté client

### Bibliothèques externes
- **Font Awesome** : Icônes vectorielles
- **Google Fonts** : Polices web (Open Sans)
- **Normalize.css** : Normalisation des styles entre navigateurs

### Outils de développement
- **Visual Studio Code** : Éditeur de code
- **Git** : Gestion de versions
- **Chrome DevTools** : Débogage et tests

## Guide de maintenance

### Ajout d'une nouvelle recette

1. **Créer le fichier HTML** :
   - Dupliquer un fichier de recette existant (ex: `croissants.html`)
   - Placer le fichier dans le dossier de catégorie approprié
   - Mettre à jour le contenu (titre, ingrédients, étapes, etc.)

2. **Ajouter les images** :
   - Placer l'image principale dans `assets/images/recipes/`
   - Optimiser l'image pour le web (format, taille, compression)

3. **Mettre à jour la page de catégorie** :
   - Ajouter la recette dans la liste de la catégorie correspondante
   - Créer la vignette avec image, titre et description courte

### Ajout d'une nouvelle catégorie

1. **Créer le dossier de catégorie** :
   - Créer un nouveau dossier à la racine du site (ex: `cakes/`)

2. **Créer la page d'index** :
   - Dupliquer une page de catégorie existante (ex: `viennoiseries/index.html`)
   - Adapter le contenu pour la nouvelle catégorie

3. **Mettre à jour la navigation** :
   - Ajouter la nouvelle catégorie dans le menu de navigation (tous les fichiers HTML)
   - Ajouter la nouvelle catégorie dans le pied de page (tous les fichiers HTML)

4. **Mettre à jour la page d'accueil** :
   - Ajouter la nouvelle catégorie dans la section des catégories

### Modification de la charte graphique

1. **Couleurs** :
   - Modifier les variables CSS dans `assets/css/style.css` (section `:root`)

2. **Typographie** :
   - Mettre à jour les polices dans `assets/css/style.css`
   - Mettre à jour les liens Google Fonts dans les en-têtes HTML

3. **Éléments d'interface** :
   - Modifier les styles des composants dans `assets/css/style.css`

## Recommandations pour l'évolution

### Améliorations techniques
1. **Backend** :
   - Développer une API pour gérer les recettes de manière dynamique
   - Mettre en place une base de données pour stocker les recettes, utilisateurs, commentaires, etc.

2. **Authentification** :
   - Implémenter un système d'authentification réel (OAuth, JWT, etc.)
   - Sécuriser les données utilisateur

3. **Optimisation** :
   - Mettre en place un système de cache
   - Optimiser davantage les images avec des formats modernes (WebP)
   - Implémenter un service worker pour le fonctionnement hors ligne

### Nouvelles fonctionnalités
1. **Recherche avancée** :
   - Filtrage par ingrédients, temps de préparation, difficulté, etc.
   - Recherche textuelle dans les recettes

2. **Communauté** :
   - Permettre aux utilisateurs de soumettre leurs propres recettes
   - Système de commentaires et de notation plus élaboré
   - Forum de discussion

3. **Contenu enrichi** :
   - Vidéos de démonstration pour les recettes
   - Galeries d'images des étapes de préparation
   - Variantes des recettes

4. **Fonctionnalités pratiques** :
   - Liste de courses générée à partir des recettes
   - Planificateur de menus
   - Mode d'affichage spécial pendant la préparation (grand texte, pas de mise en veille)

---

Document préparé par Manus AI - Juin 2025

