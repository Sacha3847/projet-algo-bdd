import mysql.connector

connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sacha38470@"
)

curseur = connexion.cursor()

curseur.execute("CREATE DATABASE IF NOT EXISTS ecommerce_db")

print("Base créée avec succès !")

connexion.close()
