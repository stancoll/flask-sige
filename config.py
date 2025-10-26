# import os
# import mysql.connector
# from dotenv import load_dotenv

# load_dotenv()

# def get_db_connection():
#     return mysql.connector.connect(
#         host="127.0.0.1", 
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#         database=os.getenv("DB_NAME")
#     )
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT", 3306)
        )
        return connection
    except mysql.connector.Error as e:
        print(f" Erreur de connexion à la base de données: {e}")
        raise Exception(f"Impossible de se connecter à la base de données: {str(e)}")