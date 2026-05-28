CREATE DATABASE ecommerce_db;

USE ecommerce_db;

CREATE TABLE clients (
    id INT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    ville VARCHAR(100),
    pays VARCHAR(100)
);

CREATE TABLE produits (
    id INT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    categorie VARCHAR(100),
    prix DECIMAL(10,2) NOT NULL
);

CREATE TABLE commandes (
    id INT PRIMARY KEY,
    client_id INT,
    date_commande DATE,
    FOREIGN KEY (client_id) REFERENCES clients(id)
);

CREATE TABLE commande_produits (
    commande_id INT,
    produit_id INT,
    quantite INT NOT NULL,
    PRIMARY KEY (commande_id, produit_id),

    FOREIGN KEY (commande_id) REFERENCES commandes(id),
    FOREIGN KEY (produit_id) REFERENCES produits(id)
);
