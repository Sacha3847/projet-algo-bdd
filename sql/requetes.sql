USE ecommerce_db;

-- 1. WHERE
SELECT * 
FROM clients
WHERE pays = 'France';

-- 2. ORDER BY
SELECT * 
FROM produits
ORDER BY prix DESC;

-- 3. LIMIT
SELECT * 
FROM produits
LIMIT 3;

-- 4. GROUP BY
SELECT categorie, COUNT(*) AS nb_produits
FROM produits
GROUP BY categorie;

-- 5. HAVING
SELECT categorie, AVG(prix) AS prix_moyen
FROM produits
GROUP BY categorie
HAVING AVG(prix) > 500;

-- 6. Jointure 3 tables
SELECT clients.nom AS client,
       produits.nom AS produit,
       commandes.date_commande
FROM clients
JOIN commandes 
ON clients.id = commandes.client_id
JOIN commande_produits
ON commandes.id = commande_produits.commande_id
JOIN produits
ON commande_produits.produit_id = produits.id;

-- 7. Sous-requête
SELECT nom, prix
FROM produits
WHERE prix > (
    SELECT AVG(prix)
    FROM produits
);

-- 8. VIEW
CREATE VIEW vue_clients_commandes AS
SELECT clients.nom,
       commandes.date_commande
FROM clients
JOIN commandes
ON clients.id = commandes.client_id;

-- 9. Fonction simple
DELIMITER //

CREATE FUNCTION total_commandes()
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE total INT;

    SELECT COUNT(*)
    INTO total
    FROM commandes;

    RETURN total;
END //

DELIMITER ;

SELECT clients.nom, commandes.date_commande
FROM clients
JOIN commandes
ON clients.id = commandes.client_id;

SELECT categorie, COUNT(*) AS total
FROM produits
GROUP BY categorie;

CREATE VIEW vue_commandes_clients AS
SELECT clients.nom, commandes.date_commande
FROM clients
JOIN commandes
ON clients.id = commandes.client_id;

