from dotenv import load_dotenv
load_dotenv()

from config import get_db_connection
from utils.password_utils import hash_password
from models.appareil_model import insert_appareil

def insert_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    nom = "Utilisateur Test"
    email = "test@example.com"
    password = hash_password("motdepasse")

    # 🔎 Vérifie si l'utilisateur existe déjà
    cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        user_id = existing_user[0]
        print(f"⚠️ L'utilisateur '{email}' existe déjà (id={user_id}), aucune insertion faite.")
    else:
        # 🧩 Crée un nouvel utilisateur
        cursor.execute("""
            INSERT INTO users (nom, email, mot_de_passe) 
            VALUES (%s, %s, %s)
        """, (nom, email, password))
        user_id = cursor.lastrowid
        print(f"✅ Nouvel utilisateur inséré : {email} (id={user_id})")

        # 🪫 Ajoute une consommation
        cursor.execute("""
            INSERT INTO consommation (user_id, valeur, type, date)
            VALUES (%s, %s, %s, NOW())
        """, (user_id, 2500, "chauffage"))

        # ⚡ Ajoute une production
        cursor.execute("""
            INSERT INTO production (user_id, valeur, date)
            VALUES (%s, %s, NOW())
        """, (user_id, 1500))

        # 🧰 Ajoute un appareil via modèle
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

    print("\n✅ Script terminé avec succès.")
    print(f"📧 Email : {email}")
    print(f"🔑 Mot de passe : motdepasse")

if __name__ == "__main__":
    insert_data()
