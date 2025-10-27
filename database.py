import mysql.connector
import os

def get_db_connection():
    """
    Connexion à MySQL avec variables d'environnement
    pour fonctionner en local ET sur Render
    """
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "3306")),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "bd-sige"),
            ssl_disabled=False,  # Important pour Aiven
            connection_timeout=10
        )
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Erreur de connexion à la base de données : {err}")
        raise