# Nombre d'accidents par départements en France

## Introduction

Ce projet Python a été conçu dans le cadre d'un projet scolaire avec l'objectif de visualiser et d'analyser les données relatives aux accidents de la circulation en France. L'application utilise des données publiques fournies par [data.gouv.fr](https://www.data.gouv.fr) .

## Fonctionement

Ce projet offre une carte interactive centrée sur l'Île-de-France qui illustre le nombre d'accidents par département à l'aide d'indicateurs de couleur. Ces couleurs indiquent le niveau de gravité du nombre d'accidents.

## Installation

Pour installer ce projet et le faire fonctionner sur votre système local, suivez les étapes ci-dessous :

- **Prérequis**
  - [Python](https://www.python.org/downloads/) 
  - pip (généralement installé avec Python)
  - [Git](https://git-scm.com/downloads)

- **Clonage du Répertoire**

  1. Ouvrez votre terminal.
  2. Clonez le répertoire en utilisant la commande suivante :

      ```git clone https://github.com/1Cataclysm/Python-Dashboard.git```


- **Installation des Dépendances**

  1. Changez de répertoire pour accéder au projet cloné
  2. Installez les dépendances nécessaires en exécutant :
     
        ```pip install -r requirements.txt```
  4. Lancer l'application en exécutant :
     
        ```python main.py```
## Heading

### 1. User Guide

### Visualisation sur la Carte

- **Indicateurs de couleur :** Chaque département est représenté par une teinte différente en fonction de la gravité des accidents.
- **Détails au survol :** En passant votre curseur sur un département, vous pourrez voir le nombre d'accidents qui y ont été enregistrés.

### Interaction avec la Carte

- **Filtres :** Utilisez les options de filtre situées au-dessus de la carte pour personnaliser l'affichage selon vos besoins.
  - **Filtrer par nombre d'accidents :** Ajustez le filtre pour définir le seuil minimal d'accidents à afficher.

- **Histogramme :** En parallèle avec les filtres, l'histogramme affiché donne une vue d'ensemble du nombre d'incidents par type, ce qui permet une analyse statistique rapide et efficace.
### 2. Guide du Développeur

Cette section fournit un aperçu des fichiers de code source présents dans le projet et de leur rôle respectif.

- **Fichiers de Code :** Le projet contient quatre fichiers principaux :

  - **`main.py` :** C'est le point d'entrée du programme. Il génère et affiche la carte interactive, mettant en évidence les données relatives aux accidents de la circulation.

  - **`caracteristique.py` / `vehicule.py` :** Ces fichiers sont les principales sources de données utilisées par `main.py`. Ils récupèrent les données nécessaires via l'API du site [data.gouv.fr](https://www.data.gouv.fr).

  - **`get_data.py` :** Ce script gère les données statiques, telles que les codes des départements et la conversion des données retournées par l'API. En exécutant la commande `python get_data.py`, vous générerez deux fichiers Excel qui contiennent ces données statiques, qui sont essentielles pour l'interprétation et le traitement des informations fournies par `caracteristique.py` et `vehicule.py`.

### 3. Architecture du Code

#### Organisation des Fichiers
Le projet est structuré en plusieurs fichiers clés qui s'occupent de différentes parties de l'application :

- **main.py**: Le cœur de l'application Dash. Il initialise l'application, définit la mise en page, et contient les rappels nécessaires pour interactivité.

- **get_data.py**: Contient les fonctions pour récupérer les données statiques nécessaires à l'application, comme les codes des départements et la correspondance des données de l'API.

- **caracteristique.py**: S'occupe de récupérer et de traiter les données des caractéristiques des accidents depuis l'API de data.gouv.fr.

- **vehicule.py**: Similaire à `caracteristique.py`, ce fichier gère la récupération et le traitement des données des véhicules impliqués dans les accidents.

- **vehicule.py**: Similaire à `lieux.py`, ce fichier gère la récupération et le traitement des données des lieux impliqués dans les accidents.

#### Description Détaillée

**main.py**
- Initialise et configure l'application Dash.
- Créer une carte interactive avec Folium basée sur les données des accidents par département.
- Définit les rappels pour la mise à jour de la carte et la génération de l'histogramme des types d'accidents.
- Créer le diagramme en barre
- Créer l'histogramme
- Créer le graphique en aire avec son filtre

**get_data.py**
- Fournit des données statiques pour l'application, y compris les codes des départements.
- Exécuté séparément pour produire des fichiers Excel contenant les données nécessaires.

**caracteristique.py**
- Ce fichier est responsable de l'interaction avec l'API data.gouv.fr pour télécharger un fichier CSV détaillant les caractéristiques des accidents corporels de la circulation routière.
- Il utilise la bibliothèque `pandas` pour charger et traiter les données du CSV.
- Le script filtre les données pour les départements de la France métropolitaine (en excluant les départements d'outre-mer numérotés au-delà de 99, à l'exception de la Corse avec '2A' et '2B').
- Deux structures de données principales sont remplies :
  - `data_accident` : un dictionnaire qui associe chaque département à un ensemble d'accidents, avec l'adresse et les coordonnées géographiques de chaque accident.
  - `nb_acc_dp` : un dictionnaire qui compte le nombre total d'accidents par département.
- La fonction `get_data` peut renvoyer soit l'ensemble des caractéristiques des accidents (`data_accident`) si le `flag` est à 0, soit le nombre total d'accidents par département (`nb_acc_dp`) si le `flag` est à 1.
- Ce traitement permet de préparer les données pour une visualisation géographique des accidents sur la carte et pour des analyses statistiques complémentaires.

**vehicule.py**
- Ce script sert à récupérer des données concernant les véhicules impliqués dans les accidents corporels de la circulation, à partir de l'api mis à disposition sur la plateforme data.gouv.fr.
- Les données sont chargées et traitées à l'aide de la bibliothèque `pandas`.
- Avant d'accéder aux données, le script fait appel à une fonction `get_OBS` du module `get_data` pour obtenir un dictionnaire qui sert à décoder les codes d'observation (`OBS`) liés aux véhicules.
- Pour chaque enregistrement dans le CSV, le script vérifie la colonne `obs` (observation) et ne traite que les cas où cette valeur est différente de "0" (qui signifierait aucun observateur).
- Les données sont ensuite agrégées dans un dictionnaire `data_accident`, qui associe chaque type d'observation à son nombre d'occurrences.
- Le dictionnaire résultant résume le nombre d'accidents par type d'observation et est prêt à être utilisé pour des analyses ou des visualisations, telles que la création d'histogrammes qui reflètent la fréquence des différents types d'incidents impliquant des véhicules.

Ce fichier joue un rôle crucial dans l'analyse des types d'incidents véhiculaires, permettant aux utilisateurs de comprendre les tendances et les motifs communs dans les accidents de la route.

**lieux.py**
- Ce script sert à récupérer des données concernant les lieux impliqués dans les accidents corporels de la circulation, à partir de l'api mis à disposition sur la plateforme data.gouv.fr.
- Les données sont chargées et traitées à l'aide de la bibliothèque `pandas`.
- Le script convertit les "vma" récupérées en int
- Retourne la liste des datas avec les vma en int 

**style.css**
- Contient le style de tous les éléments de la page

### Utilisation des Données
- Les données récupérées par `caracteristique.py` et `vehicule.py` sont utilisées pour afficher les accidents sur la carte et pour fournir une analyse statistique dans le diagramme en barre.
- Les données récupérées par `lieux.py` sont utilisées pour afficher l'histogramme.
- `get_data.py` est utilisé pour préparer les données statiques, qui aident à interpréter et à afficher les données dynamiques correctement.


