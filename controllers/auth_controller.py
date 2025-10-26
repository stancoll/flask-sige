from flask import request, jsonify
from config import get_db_connection
import bcrypt

def register_user(data):
    nom = data.get('nom')
    email = data.get('email')
    mot_de_passe = data.get('mot_de_passe')

    if not nom or not email or not mot_de_passe:
        return jsonify({'error': 'Champs requis manquants'}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Vérifie si l'utilisateur existe déjà
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    existing_user = cursor.fetchone()
    if existing_user:
        cursor.close()
        conn.close()
        return jsonify({'error': 'Utilisateur déjà existant'}), 409

    # Hash du mot de passe
    hashed_password = bcrypt.hashpw(mot_de_passe.encode('utf-8'), bcrypt.gensalt())

    # Insertion de l'utilisateur
    try:
        cursor.execute("""
            INSERT INTO users (nom, email, mot_de_passe, objectif_mensuel, tarif_kwh, seuil_alerte, theme_sombre, notifications_actives)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            nom,
            email,
            hashed_password,
            500,     # objectif_mensuel par défaut
            2990,    # tarif_kwh par défaut
            80,      # seuil_alerte par défaut
            False,   # theme_sombre par défaut
            True     # notifications_actives par défaut
        ))
        conn.commit()
        return jsonify({'message': 'Inscription réussie'}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({'error': f'Erreur serveur : {str(e)}'}), 500
    finally:
        cursor.close()
        conn.close()
