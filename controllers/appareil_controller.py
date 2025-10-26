from flask import request, jsonify
from config import get_db_connection
from models.appareil_model import insert_appareil
from utils.jwt_utils import decode_token

# ➕ Ajouter un appareil
def ajouter_appareil():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    payload = decode_token(token)

    if not payload:
        return jsonify({"error": "Token invalide"}), 401

    user_id = payload["id"]
    data = request.get_json()

    nom = data.get("nom")
    categorie = data.get("categorie")
    consommation = data.get("consommationQuotidienne")
    puissance = data.get("puissanceWatt")
    est_actif = data.get("est_actif", True)

    if not nom or not categorie or consommation is None or puissance is None:
        return jsonify({"error": "Champs manquants"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        insert_appareil(cursor, {
            "user_id": user_id,
            "nom": nom,
            "categorie": categorie,
            "consommationQuotidienne": consommation,
            "puissanceWatt": puissance,
            "est_actif": est_actif
        })
        conn.commit()
        return jsonify({"message": "Appareil ajouté"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()


# 📥 Récupérer les appareils de l’utilisateur connecté
def get_appareils():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    payload = decode_token(token)

    if not payload:
        return jsonify({"error": "Token invalide"}), 401

    user_id = payload["id"]

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM appareils WHERE user_id = %s", (user_id,))
        appareils = cursor.fetchall()
        return jsonify(appareils), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()


# ✏️ Mettre à jour un appareil
def update_appareil(appareil_id):
    data = request.get_json()

    champs = []
    valeurs = []

    for champ in ["nom", "categorie", "consommationQuotidienne", "puissanceWatt", "est_actif"]:
        if champ in data:
            champs.append(f"{champ} = %s")
            valeurs.append(data[champ])

    if not champs:
        return jsonify({"error": "Aucune donnée à mettre à jour"}), 400

    valeurs.append(appareil_id)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f"""
            UPDATE appareils SET {', '.join(champs)} WHERE id = %s
        """, valeurs)
        conn.commit()
        return jsonify({"message": "Appareil mis à jour"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()


# ❌ Supprimer un appareil
def delete_appareil(appareil_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM appareils WHERE id = %s", (appareil_id,))
        conn.commit()
        return jsonify({"message": "Appareil supprimé"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()
