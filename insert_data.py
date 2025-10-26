from config import get_db_connection
from utils.password_utils import hash_password
from models.appareil_model import insert_appareil

def insert_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Créer un utilisateur test
    email = "test@example.com"
    password = hash_password("motdepasse")

    cursor.execute("INSERT INTO users (email, mot_de_passe) VALUES (%s, %s)", (email, password))
    user_id = cursor.lastrowid  # ← ID utilisé pour les données suivantes

    # 2. Ajouter une consommation
    cursor.execute("""
        INSERT INTO consommation (user_id, valeur, type, date)
        VALUES (%s, %s, %s, NOW())
    """, (user_id, 2500, "chauffage"))

    # 3. Ajouter une production
    cursor.execute("""
        INSERT INTO production (user_id, valeur, date)
        VALUES (%s, %s, NOW())
    """, (user_id, 1500))

    # 4. Ajouter un appareil via modèle
    insert_appareil(cursor, {
        "user_id": user_id,
        "nom": "Climatiseur",
        "categorie": "chauffage",
        "consommationQuotidienne": 3.5,
        "puissanceWatt": 1200,
        "est_actif": True
    })

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Données de test insérées avec succès.")

if __name__ == "__main__":
    insert_data()
