# 📊 Projet Business Intelligence - Ecommerce

## 📌 Description

Ce projet a été réalisé dans le cadre d’un projet de base de données et Business Intelligence.

L’objectif est de concevoir :

* une base de données relationnelle MySQL,
* des requêtes SQL avancées,
* un dashboard interactif en Python,
* une analyse des données commerciales.

Le projet exploite des données ecommerce :

* clients,
* produits,
* commandes,
* détails des commandes.

---

# 🛠️ Technologies utilisées

* MySQL
* Python
* Pandas
* Dash
* Plotly
* GitHub
* VS Code

---

# 📂 Structure du projet

```bash
projet-algo-bdd/
│
├── data/
│   ├── clients.csv
│   ├── produits.csv
│   ├── Commandes.csv
│   └── commande_produits.csv
│
├── sql/
│   ├── creation_bdd.sql
│   ├── requetes.sql
│   └── dashboard.py
│
├── requirements.txt
│
└── README.md
```

---

# 🗄️ Fonctionnalités SQL

Le projet contient plusieurs fonctionnalités SQL avancées :

## ✔️ Création de tables relationnelles

* clés primaires
* clés étrangères
* contraintes relationnelles

## ✔️ Requêtes SQL

* SELECT
* WHERE
* ORDER BY
* GROUP BY
* JOIN

## ✔️ VIEW SQL

Création d’une vue permettant d’afficher les informations clients et commandes.

## ✔️ Procédure stockée

Procédure permettant d’afficher automatiquement les clients.

## ✔️ Fonction SQL

Fonction retournant le nombre total de commandes.

## ✔️ Trigger SQL

Validation automatique de la quantité lors d’un ajout dans la table des commandes.

---

# 📈 Dashboard Business Intelligence

Le dashboard interactif a été développé avec Dash et Plotly.

Il permet :

* d’afficher des KPI business,
* d’analyser le chiffre d’affaires,
* d’identifier les produits les plus performants,
* d’analyser les ventes par catégorie,
* d’afficher des graphiques interactifs,
* d’observer l’évolution du chiffre d’affaires dans le temps.

---

# 📊 KPI disponibles

* Nombre de clients
* Nombre de commandes
* Chiffre d’affaires total
* Panier moyen
* Quantité totale vendue
* Produit le plus vendu

---

# 📉 Visualisations disponibles

* Histogramme du chiffre d’affaires
* Diagramme circulaire des ventes
* Courbe d’évolution du chiffre d’affaires
* Tableau interactif des produits

---

# ▶️ Installation

## Installer les dépendances

```bash
pip install -r requirements.txt
```

## Lancer le dashboard

```bash
py sql/dashboard.py
```

---

# 📌 Analyse Business

Les analyses montrent :

* les catégories les plus rentables,
* les produits les plus vendus,
* les tendances de ventes,
* la répartition des ventes par catégorie,
* l’évolution du chiffre d’affaires.

---

# 👨‍💻 Auteur

Projet réalisé par Sacha Garrel.
