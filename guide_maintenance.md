# Guide de Maintenance du Site Chef DEGAS

## Table des matières

1. [Introduction](#introduction)
2. [Maintenance régulière](#maintenance-régulière)
3. [Mise à jour du contenu](#mise-à-jour-du-contenu)
4. [Gestion des fichiers](#gestion-des-fichiers)
5. [Optimisation des performances](#optimisation-des-performances)
6. [Sécurité](#sécurité)
7. [Sauvegarde et restauration](#sauvegarde-et-restauration)
8. [Résolution des problèmes courants](#résolution-des-problèmes-courants)

## Introduction

Ce guide de maintenance est destiné aux personnes chargées de l'entretien et de la mise à jour du site Chef DEGAS. Il fournit des instructions détaillées sur les tâches de maintenance régulières, la mise à jour du contenu, et la résolution des problèmes courants.

Le site Chef DEGAS est un site statique, ce qui signifie qu'il ne nécessite pas de base de données ou de serveur d'application complexe. Cela simplifie considérablement la maintenance, mais certaines tâches restent nécessaires pour assurer son bon fonctionnement et sa sécurité.

## Maintenance régulière

### Vérifications mensuelles

Effectuez ces vérifications une fois par mois pour assurer le bon fonctionnement du site :

1. **Test de navigation** :
   - Vérifiez que tous les liens fonctionnent correctement
   - Testez la navigation sur différents appareils (desktop, tablette, mobile)
   - Vérifiez que les formulaires fonctionnent correctement

2. **Vérification des performances** :
   - Testez le temps de chargement des pages principales
   - Vérifiez la taille des pages et des ressources
   - Identifiez les éventuels goulots d'étranglement

3. **Vérification de la compatibilité** :
   - Testez le site sur différents navigateurs (Chrome, Firefox, Safari, Edge)
   - Vérifiez l'affichage sur différentes tailles d'écran

### Vérifications trimestrielles

Effectuez ces vérifications tous les trois mois :

1. **Audit de contenu** :
   - Vérifiez que le contenu est à jour et pertinent
   - Identifiez les pages peu consultées ou obsolètes
   - Planifiez les mises à jour de contenu nécessaires

2. **Audit technique** :
   - Vérifiez les performances avec des outils comme Google PageSpeed Insights
   - Testez l'accessibilité avec des outils comme WAVE ou Lighthouse
   - Vérifiez le référencement avec des outils d'analyse SEO

3. **Mise à jour des bibliothèques** :
   - Vérifiez si des mises à jour sont disponibles pour les bibliothèques externes
   - Testez les nouvelles versions dans un environnement de développement avant de les déployer

## Mise à jour du contenu

### Ajout de nouvelles recettes

Pour ajouter de nouvelles recettes, consultez le [Guide d'ajout de recettes](guide_ajout_recettes.md) détaillé.

### Modification des pages existantes

1. **Localiser le fichier** :
   - Identifiez le fichier HTML correspondant à la page à modifier
   - Ouvrez-le dans un éditeur de texte ou HTML

2. **Effectuer les modifications** :
   - Modifiez le contenu HTML en respectant la structure existante
   - Évitez de modifier les classes CSS et les identifiants sauf si nécessaire
   - Préservez les balises sémantiques et les attributs d'accessibilité

3. **Tester les modifications** :
   - Vérifiez les modifications localement avant de les publier
   - Testez sur différents appareils et navigateurs si possible

### Mise à jour des informations générales

Pour mettre à jour les informations présentes sur plusieurs pages (pied de page, mentions légales, etc.) :

1. **Identifier tous les fichiers concernés** :
   - Utilisez la fonction de recherche de votre éditeur pour trouver toutes les occurrences
   - Créez une liste des fichiers à modifier

2. **Effectuer les modifications de manière cohérente** :
   - Assurez-vous que les modifications sont identiques sur toutes les pages
   - Vérifiez particulièrement les liens et les coordonnées

## Gestion des fichiers

### Organisation des dossiers

Maintenez l'organisation des dossiers comme suit :

```
chef-degas/
├── index.html et autres pages principales
├── catégories/ (dossiers pour chaque catégorie)
└── assets/
    ├── css/ (fichiers CSS)
    ├── js/ (fichiers JavaScript)
    └── images/ (images organisées par sous-dossiers)
```

### Nommage des fichiers

Suivez ces conventions de nommage :

- **Pages HTML** : noms descriptifs en minuscules, mots séparés par des tirets (ex: `tarte-aux-pommes.html`)
- **Images** : noms descriptifs en minuscules, préfixés par leur catégorie si nécessaire (ex: `recette-croissants.jpg`, `ingredient-farine.svg`)
- **Fichiers CSS/JS** : noms descriptifs de leur fonction (ex: `responsive.css`, `portions.js`)

### Gestion des images

1. **Optimisation** :
   - Compressez toutes les images avant de les ajouter au site
   - Utilisez des formats appropriés : JPEG pour les photos, PNG pour les images avec transparence, SVG pour les icônes
   - Dimensionnez les images à la taille maximale nécessaire

2. **Organisation** :
   - Placez les images dans les sous-dossiers appropriés selon leur usage
   - Utilisez des noms de fichiers descriptifs et cohérents

## Optimisation des performances

### Optimisation des images

1. **Compression** :
   - Utilisez des outils comme TinyPNG, ImageOptim ou Squoosh pour compresser les images
   - Visez un équilibre entre qualité visuelle et taille de fichier

2. **Dimensionnement** :
   - Redimensionnez les images à la taille maximale à laquelle elles seront affichées
   - Envisagez d'utiliser des images responsives avec l'attribut `srcset`

3. **Format moderne** :
   - Envisagez d'utiliser des formats modernes comme WebP avec fallback pour les navigateurs plus anciens

### Optimisation du code

1. **Minification** :
   - Minifiez les fichiers CSS et JavaScript pour la production
   - Utilisez des outils comme UglifyJS pour JavaScript et CleanCSS pour CSS

2. **Chargement différé** :
   - Utilisez l'attribut `loading="lazy"` pour les images
   - Chargez les scripts non essentiels de manière asynchrone ou différée

3. **Réduction des requêtes** :
   - Combinez les fichiers CSS et JavaScript lorsque c'est possible
   - Utilisez des sprites CSS pour les petites images et icônes récurrentes

## Sécurité

Bien que le site soit statique et présente moins de risques de sécurité qu'un site dynamique, certaines précautions restent nécessaires :

### Protection contre les attaques XSS

1. **Validation des entrées utilisateur** :
   - Si vous ajoutez des fonctionnalités qui acceptent des entrées utilisateur (comme des commentaires), assurez-vous de les échapper correctement
   - Utilisez des méthodes d'échappement HTML pour afficher le contenu généré par les utilisateurs

### Sécurité du serveur

1. **HTTPS** :
   - Assurez-vous que le site est servi en HTTPS
   - Configurez la redirection HTTP vers HTTPS

2. **En-têtes de sécurité** :
   - Configurez les en-têtes de sécurité appropriés sur votre serveur web :
     - Content-Security-Policy
     - X-Content-Type-Options
     - X-Frame-Options
     - Referrer-Policy

### Gestion des accès

1. **Accès FTP/SFTP** :
   - Utilisez des mots de passe forts pour les accès FTP/SFTP
   - Changez régulièrement les mots de passe
   - Limitez l'accès aux personnes qui en ont réellement besoin

## Sauvegarde et restauration

### Stratégie de sauvegarde

1. **Sauvegarde régulière** :
   - Effectuez une sauvegarde complète du site au moins une fois par mois
   - Sauvegardez également avant toute modification majeure

2. **Stockage des sauvegardes** :
   - Stockez les sauvegardes dans au moins deux endroits différents
   - Utilisez un service de stockage cloud sécurisé comme solution de sauvegarde secondaire

3. **Contenu à sauvegarder** :
   - Tous les fichiers HTML
   - Tous les assets (CSS, JavaScript, images)
   - Fichiers de configuration du serveur web si applicable

### Procédure de restauration

En cas de problème nécessitant une restauration :

1. **Évaluation** :
   - Identifiez l'étendue du problème
   - Déterminez la sauvegarde la plus récente et la plus appropriée à utiliser

2. **Restauration** :
   - Restaurez les fichiers nécessaires à partir de la sauvegarde
   - Vérifiez que tous les liens et ressources fonctionnent correctement après la restauration

3. **Vérification** :
   - Testez le site restauré sur différents appareils et navigateurs
   - Vérifiez que toutes les fonctionnalités sont opérationnelles

## Résolution des problèmes courants

### Images manquantes

**Symptôme** : Les images ne s'affichent pas, icône d'image brisée visible.

**Solutions** :
1. Vérifiez que le fichier image existe à l'emplacement spécifié
2. Vérifiez que le chemin dans le code HTML est correct (attention aux majuscules/minuscules)
3. Vérifiez les permissions du fichier sur le serveur
4. Vérifiez que le format de l'image est supporté par tous les navigateurs

### Problèmes d'affichage CSS

**Symptôme** : Mise en page cassée, styles non appliqués.

**Solutions** :
1. Vérifiez que les fichiers CSS sont correctement liés dans le HTML
2. Vérifiez la présence d'erreurs dans la console du navigateur
3. Testez sur différents navigateurs pour identifier si le problème est spécifique
4. Vérifiez les règles CSS pour les conflits ou les erreurs de syntaxe

### Fonctionnalités JavaScript non fonctionnelles

**Symptôme** : Les interactions comme l'ajustement des portions ou les favoris ne fonctionnent pas.

**Solutions** :
1. Vérifiez que les fichiers JavaScript sont correctement liés dans le HTML
2. Vérifiez la présence d'erreurs dans la console du navigateur
3. Vérifiez que jQuery ou d'autres dépendances sont chargées avant vos scripts
4. Testez les fonctionnalités dans un navigateur différent

### Problèmes de liens

**Symptôme** : Les liens renvoient vers des pages 404 ou ne fonctionnent pas.

**Solutions** :
1. Vérifiez que les fichiers cibles existent aux emplacements spécifiés
2. Vérifiez la syntaxe des liens (chemins relatifs vs absolus)
3. Vérifiez les redirections sur le serveur
4. Testez les liens dans différents contextes (navigation directe, clic, etc.)

### Problèmes de performance

**Symptôme** : Le site est lent à charger.

**Solutions** :
1. Optimisez les images (taille, compression)
2. Minifiez les fichiers CSS et JavaScript
3. Réduisez le nombre de requêtes HTTP
4. Activez la mise en cache du navigateur via les en-têtes HTTP
5. Utilisez un CDN pour les ressources statiques si le trafic est important

---

Document préparé par Manus AI - Juin 2025

