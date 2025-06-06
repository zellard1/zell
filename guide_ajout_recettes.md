# Guide d'utilisation pour l'ajout de nouvelles recettes

## Table des matières

1. [Introduction](#introduction)
2. [Préparation des contenus](#préparation-des-contenus)
3. [Création du fichier HTML](#création-du-fichier-html)
4. [Ajout à la page de catégorie](#ajout-à-la-page-de-catégorie)
5. [Test et publication](#test-et-publication)
6. [Conseils et bonnes pratiques](#conseils-et-bonnes-pratiques)

## Introduction

Ce guide vous explique comment ajouter de nouvelles recettes au site Chef DEGAS. Il est destiné aux personnes chargées de la maintenance et de la mise à jour du contenu du site. Aucune connaissance approfondie en programmation n'est nécessaire, mais une familiarité de base avec HTML est recommandée.

## Préparation des contenus

Avant de commencer l'ajout d'une recette, assurez-vous d'avoir préparé tous les éléments nécessaires :

### 1. Informations générales
- Titre de la recette
- Catégorie (Viennoiseries, Entremets, Tartes, etc.)
- Temps de préparation
- Temps de repos (si applicable)
- Temps de cuisson
- Niveau de difficulté (Facile, Moyen, Difficile)
- Coût (Économique, Moyen, Élevé)
- Nombre de portions de base

### 2. Images
- Image principale de la recette (format paysage, idéalement 1200×800 pixels)
- Images des étapes (optionnel)

### 3. Contenu de la recette
- Liste complète des ingrédients avec quantités précises
- Étapes de préparation détaillées
- Astuces du chef (conseils, variantes, etc.)

## Création du fichier HTML

### 1. Dupliquer un modèle existant

La façon la plus simple d'ajouter une nouvelle recette est de dupliquer un fichier de recette existant et de le modifier.

1. Choisissez une recette similaire comme modèle (par exemple, `viennoiseries/croissants.html`)
2. Copiez ce fichier dans le dossier de la catégorie appropriée
3. Renommez le fichier avec un nom simple et descriptif (ex: `pain-au-chocolat.html`)

### 2. Modifier les métadonnées

Ouvrez le fichier dans un éditeur de texte et modifiez les informations suivantes dans la section `<head>` :

```html
<meta name="description" content="Description de votre recette - 150-160 caractères maximum">
<title>Nom de la recette - Chef DEGAS</title>
```

### 3. Mettre à jour le contenu principal

#### Titre et informations générales

```html
<h1 class="recipe-title">Nom de la recette</h1>

<div class="recipe-info">
    <div class="recipe-info-item">
        <i class="far fa-clock"></i> Préparation : XXh
    </div>
    <div class="recipe-info-item">
        <i class="fas fa-hourglass-half"></i> Repos : XXh
    </div>
    <div class="recipe-info-item">
        <i class="fas fa-temperature-high"></i> Cuisson : XX-XX min
    </div>
    <div class="recipe-info-item">
        <i class="fas fa-signal"></i> Difficulté : Facile/Moyen/Difficile
    </div>
    <div class="recipe-info-item">
        <i class="fas fa-euro-sign"></i> Coût : Économique/Moyen/Élevé
    </div>
</div>
```

#### Boutons de partage et favoris

Mettez à jour les attributs `data-` du bouton favoris :

```html
<button class="favorite-button" 
        data-recipe-id="ID-unique-de-la-recette" 
        data-recipe-title="Nom de la recette" 
        data-recipe-image="../assets/images/recipes/nom-image.jpg" 
        data-recipe-url="nom-du-fichier.html">
    <i class="far fa-heart favorite-icon"></i>
    <span class="favorite-text">Ajouter aux favoris</span>
</button>
```

#### Image principale

```html
<div class="recipe-main-image">
    <img src="../assets/images/recipes/nom-image.jpg" alt="Description de l'image">
</div>
```

#### Ingrédients

Mettez à jour la liste des ingrédients :

```html
<div class="ingredients-title">
    <h2>Ingrédients</h2>
    <div class="portions-control">
        <button id="decrease-portions" aria-label="Diminuer le nombre de portions"><i class="fas fa-minus"></i></button>
        <span><span id="portions-value" data-base-portions="X">X</span> portions</span>
        <button id="increase-portions" aria-label="Augmenter le nombre de portions"><i class="fas fa-plus"></i></button>
    </div>
</div>

<ul class="ingredients-list">
    <li>
        <img src="../assets/images/ingredients/ingredient.svg" alt="" class="ingredient-icon">
        <span><span class="ingredient-quantity">XXX g</span> de farine</span>
    </li>
    <!-- Répéter pour chaque ingrédient -->
</ul>
```

#### Étapes de préparation

```html
<h2>Préparation</h2>

<ol class="steps-list">
    <li class="step-item">
        <p>Description détaillée de l'étape 1.</p>
    </li>
    <li class="step-item">
        <p>Description détaillée de l'étape 2.</p>
    </li>
    <!-- Répéter pour chaque étape -->
</ol>
```

#### Astuces du chef

```html
<div class="recipe-tips">
    <h3>Astuces du Chef</h3>
    <ul>
        <li>Première astuce</li>
        <li>Deuxième astuce</li>
        <!-- Ajouter autant d'astuces que nécessaire -->
    </ul>
</div>
```

### 4. Ajouter les images

1. Placez l'image principale de la recette dans le dossier `assets/images/recipes/`
2. Assurez-vous que le nom de fichier correspond à celui utilisé dans le HTML
3. Optimisez l'image pour le web (compression, dimensions appropriées)

## Ajout à la page de catégorie

Une fois le fichier de recette créé, vous devez l'ajouter à la page de catégorie correspondante.

### 1. Ouvrir la page de catégorie

Ouvrez le fichier `index.html` du dossier de catégorie approprié (ex: `viennoiseries/index.html`).

### 2. Ajouter la recette à la liste

Localisez la section `recipes-grid` et ajoutez votre recette :

```html
<div class="recipes-grid">
    <!-- Recette existante -->
    
    <!-- Nouvelle recette -->
    <div class="recipe-card">
        <div class="recipe-image">
            <img src="../assets/images/recipes/nom-image.jpg" alt="Nom de la recette">
        </div>
        <div class="recipe-content">
            <h3><a href="nom-du-fichier.html">Nom de la recette</a></h3>
            <p>Brève description de la recette (1-2 phrases).</p>
            <div class="recipe-meta">
                <span><i class="far fa-clock"></i> Xh</span>
                <span><i class="fas fa-signal"></i> Difficulté</span>
                <span><i class="far fa-star"></i> Note/5</span>
            </div>
            <button class="favorite-button" 
                    data-recipe-id="ID-unique-de-la-recette" 
                    data-recipe-title="Nom de la recette" 
                    data-recipe-image="../assets/images/recipes/nom-image.jpg" 
                    data-recipe-url="nom-du-fichier.html">
                <i class="far fa-heart favorite-icon"></i>
                <span class="favorite-text">Ajouter aux favoris</span>
            </button>
        </div>
    </div>
</div>
```

### 3. Supprimer le message "Aucune recette"

Si c'est la première recette de la catégorie, n'oubliez pas de supprimer ou commenter le message "Aucune recette pour le moment".

## Test et publication

### 1. Tester localement

Avant de publier, testez votre nouvelle recette :

1. Ouvrez la page de catégorie dans un navigateur
2. Vérifiez que le lien vers la nouvelle recette fonctionne
3. Testez toutes les fonctionnalités de la page de recette :
   - Ajustement des portions
   - Bouton favoris
   - Boutons de partage
   - Affichage correct sur mobile et desktop

### 2. Corriger les erreurs

Vérifiez attentivement :
- Les fautes d'orthographe et de grammaire
- Les liens brisés
- Les images manquantes
- La cohérence des informations

### 3. Publier

Une fois les tests terminés avec succès, publiez les modifications sur le serveur web :

1. Transférez le nouveau fichier HTML de recette
2. Transférez les nouvelles images
3. Transférez la page de catégorie mise à jour

## Conseils et bonnes pratiques

### Nommage des fichiers

- Utilisez des noms de fichiers courts et descriptifs
- Évitez les espaces, les accents et les caractères spéciaux
- Utilisez des tirets pour séparer les mots (ex: `tarte-aux-pommes.html`)

### Images

- Utilisez des images de haute qualité mais optimisées pour le web
- Respectez les proportions recommandées (paysage pour l'image principale)
- Assurez-vous que les images sont libres de droits ou que vous en possédez les droits

### Contenu

- Soyez précis dans les quantités et les instructions
- Utilisez un langage clair et accessible
- Incluez des astuces utiles pour aider les utilisateurs à réussir la recette

### Accessibilité

- Ajoutez des attributs `alt` descriptifs à toutes les images
- Assurez-vous que la structure HTML est sémantique et logique
- Testez la navigation au clavier

### Cohérence

- Respectez le style et le ton des autres recettes du site
- Utilisez le même format pour les temps, les quantités, etc.
- Suivez la même structure pour toutes les recettes

---

Document préparé par Manus AI - Juin 2025

