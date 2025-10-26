# from flask import jsonify
# from config import get_db_connection

# def get_profile(user_id):
#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)

#     try:
#         cursor.execute("""
#             SELECT id, nom, email, objectif_mensuel, tarif_kwh, seuil_alerte, theme_sombre, notifications_actives
#             FROM users WHERE id = %s
#         """, (user_id,))
#         user = cursor.fetchone()

#         if user:
#             return jsonify(user), 200
#         else:
#             return jsonify({"error": "Utilisateur introuvable"}), 404
#     except Exception as e:
#         return jsonify({"error": f"Erreur lors de la récupération : {str(e)}"}), 500
#     finally:
#         cursor.close()
#         conn.close()


# def update_profile(user_id, data):
#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)  # ✅ pour accès par nom

#     try:
#         cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
#         existing = cursor.fetchone()
#         if not existing:
#             return jsonify({"error": "Utilisateur introuvable"}), 404

#         # ✅ On récupère par nom au lieu d'indices (plus sûr)
#         nom = data.get("nom", existing["nom"])
#         email = data.get("email", existing["email"])
#         objectif = data.get("objectif_mensuel", existing["objectif_mensuel"])
#         tarif = data.get("tarif_kwh", existing["tarif_kwh"])
#         seuil = data.get("seuil_alerte", existing["seuil_alerte"])
#         theme = data.get("theme_sombre", existing["theme_sombre"])
#         notifications = data.get("notifications_actives", existing["notifications_actives"])

#         cursor.execute("""
#             UPDATE users
#             SET nom = %s,
#                 email = %s,
#                 objectif_mensuel = %s,
#                 tarif_kwh = %s,
#                 seuil_alerte = %s,
#                 theme_sombre = %s,
#                 notifications_actives = %s
#             WHERE id = %s
#         """, (
#             nom, email, objectif, tarif, seuil, theme, notifications, user_id
#         ))

#         conn.commit()
#         return jsonify({"message": "Profil mis à jour avec succès"}), 200

#     except Exception as e:
#         conn.rollback()
#         return jsonify({"error": f"Erreur lors de la mise à jour : {str(e)}"}), 500
#     finally:
#         cursor.close()
#         conn.close()
from flask import jsonify
from config import get_db_connection

def get_profile(user_id):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT id, nom, email, objectif_mensuel, tarif_kwh, seuil_alerte, theme_sombre, notifications_actives
            FROM users WHERE id = %s
        """, (user_id,))
        user = cursor.fetchone()

        if user:
            return jsonify(user), 200
        else:
            return jsonify({"error": "Utilisateur introuvable"}), 404
            
    except Exception as e:
        return jsonify({"error": f"Erreur lors de la récupération du profil: {str(e)}"}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def update_profile(user_id, data):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        existing = cursor.fetchone()
        if not existing:
            return jsonify({"error": "Utilisateur introuvable"}), 404

        nom = data.get("nom", existing["nom"])
        email = data.get("email", existing["email"])
        objectif = data.get("objectif_mensuel", existing["objectif_mensuel"])
        tarif = data.get("tarif_kwh", existing["tarif_kwh"])
        seuil = data.get("seuil_alerte", existing["seuil_alerte"])
        theme = data.get("theme_sombre", existing["theme_sombre"])
        notifications = data.get("notifications_actives", existing["notifications_actives"])

        # Vérifier si l'email est déjà utilisé par un autre utilisateur
        if email != existing["email"]:
            cursor.execute("SELECT id FROM users WHERE email = %s AND id != %s", (email, user_id))
            if cursor.fetchone():
                return jsonify({"error": "Cet email est déjà utilisé par un autre utilisateur"}), 409

        cursor.execute("""
            UPDATE users
            SET nom = %s,
                email = %s,
                objectif_mensuel = %s,
                tarif_kwh = %s,
                seuil_alerte = %s,
                theme_sombre = %s,
                notifications_actives = %s
            WHERE id = %s
        """, (
            nom, email, objectif, tarif, seuil, theme, notifications, user_id
        ))

        conn.commit()
        return jsonify({"message": "Profil mis à jour avec succès"}), 200

    except Exception as e:
        if conn:
            conn.rollback()
        return jsonify({"error": f"Erreur lors de la mise à jour du profil: {str(e)}"}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()