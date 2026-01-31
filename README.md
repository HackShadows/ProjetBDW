# Lost Seas - Version Web (Projet BDW)

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue.svg)
![Jinja2](https://img.shields.io/badge/Template-Jinja2-orange.svg)

Adaptation web du jeu de société **Lost Seas**, développée en Python selon une architecture **MVC (Modèle-Vue-Contrôleur)**.

Ce projet a été réalisé dans le cadre de l'unité d'enseignement "Base de Données et Programmation Web" (BDW) à l'Université Lyon 1.

## 📋 Fonctionnalités

* **Gestion de partie :** Création de parties, tours de jeu, gestion de la pioche et du plateau.
* **Base de données :** Persistance des joueurs, des parties et des scores via PostgreSQL.
* **Gameplay complet :** Implémentation des règles de placement, des contraintes de score et des bonus.
* **Statistiques :** Classements des meilleurs joueurs, historiques des parties.

## 🛠️ Architecture Technique

Le projet respecte une séparation stricte des responsabilités :
* **Modèle (`model_pg.py`) :** Interaction avec la base de données PostgreSQL (requêtes SQL paramétrées).
* **Vues (Templates Jinja2) :** Génération dynamique des pages HTML.
* **Contrôleurs :** Gestion de la logique métier et des routes.



[Image of Architecture MVC Schema]
 *(Tu peux insérer ici ton image Schéma_EA.png si pertinente)*

## 🚀 Installation et Lancement

### Prérequis
* Python 3.11+
* PostgreSQL

### Configuration
1.  Clonez le dépôt.
2.  Renommez `serveur/config-bd.toml.example` en `serveur/config-bd.toml` et renseignez vos identifiants PostgreSQL.
3.  Initialisez la base de données avec les scripts SQL présents dans `serveur/site/initialisation_bd/`.

### Lancement
```bash
# Installation des dépendances
pip install -r serveur/requirements.in

# Lancement du serveur
cd serveur
python serveur.py site
```

Rendez-vous sur http://localhost:4242 !

## 👥 Auteurs
* **Marius Ciserane**
* **Matthias Boullot**