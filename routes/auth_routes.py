# from flask import Blueprint, request, jsonify
# import bcrypt  # type: ignore
# import jwt
# import os
# from config import get_db_connection

# auth_bp = Blueprint("auth", __name__)

# @auth_bp.route("/test", methods=["GET"])
# def test():
#     return jsonify({"message": "auth ok"}), 200

# @auth_bp.route("/register", methods=["POST"])
# def register():
#     data = request.get_json()
#     nom = data.get("nom")
#     email = data.get("email")
#     mot_de_passe = data.get("mot_de_passe")

#     if not email or not mot_de_passe or not nom:
#         return jsonify({"error": "Champs manquants"}), 400

#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
#     if cursor.fetchone():
#         cursor.close()
#         conn.close()
#         return jsonify({"error": "Utilisateur déjà existant"}), 409

#     hashed = bcrypt.hashpw(mot_de_passe.encode(), bcrypt.gensalt()).decode()

#     try:
#         cursor.execute(
#             "INSERT INTO users (nom, email, mot_de_passe) VALUES (%s, %s, %s)",
#             (nom, email, hashed)
#         )
#         conn.commit()
#         return jsonify({"message": "Inscription réussie"}), 201
#     except Exception as e:
#         conn.rollback()
#         return jsonify({"error": f"Erreur lors de l'inscription: {str(e)}"}), 500
#     finally:
#         cursor.close()
#         conn.close()

# # ✅ AJOUTE LA ROUTE LOGIN ICI
# @auth_bp.route("/login", methods=["POST"])
# def login():
#     data = request.get_json()
#     email = data.get("email")
#     mot_de_passe = data.get("mot_de_passe")

#     if not email or not mot_de_passe:
#         return jsonify({"error": "Champs manquants"}), 400

#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
#     user = cursor.fetchone()

#     if not user or not bcrypt.checkpw(mot_de_passe.encode(), user["mot_de_passe"].encode()):
#         return jsonify({"error": "Email ou mot de passe invalide"}), 401

#     payload = {
#         "id": user["id"],
#         "email": user["email"],
#         "nom": user["nom"]
#     }

#     token = jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm="HS256")
#     return jsonify({"token": token}), 200
from flask import Blueprint, request, jsonify
import bcrypt
import jwt
import os
from config import get_db_connection

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/test", methods=["GET"])
def test():
    try:
        return jsonify({"message": "auth ok"}), 200
    except Exception as e:
        return jsonify({"error": f"Erreur serveur: {str(e)}"}), 500

@auth_bp.route("/register", methods=["POST"])
def register():
    conn = None
    cursor = None
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Aucune donnée reçue"}), 400
            
        nom = data.get("nom")
        email = data.get("email")
        mot_de_passe = data.get("mot_de_passe")

        if not email or not mot_de_passe or not nom:
            return jsonify({"error": "Champs manquants: nom, email et mot_de_passe requis"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        if cursor.fetchone():
            return jsonify({"error": "Utilisateur déjà existant"}), 409

        hashed = bcrypt.hashpw(mot_de_passe.encode(), bcrypt.gensalt()).decode()

        cursor.execute(
            "INSERT INTO users (nom, email, mot_de_passe) VALUES (%s, %s, %s)",
            (nom, email, hashed)
        )
        conn.commit()
        return jsonify({"message": "Inscription réussie"}), 201
        
    except Exception as e:
        if conn:
            conn.rollback()
        return jsonify({"error": f"Erreur lors de l'inscription: {str(e)}"}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@auth_bp.route("/login", methods=["POST"])
def login():
    conn = None
    cursor = None
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Aucune donnée reçue"}), 400
            
        email = data.get("email")
        mot_de_passe = data.get("mot_de_passe")

        if not email or not mot_de_passe:
            return jsonify({"error": "Email et mot_de_passe requis"}), 400

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if not user:
            return jsonify({"error": "Email ou mot de passe invalide"}), 401

        if not bcrypt.checkpw(mot_de_passe.encode(), user["mot_de_passe"].encode()):
            return jsonify({"error": "Email ou mot de passe invalide"}), 401

        payload = {
            "id": user["id"],
            "email": user["email"],
            "nom": user["nom"]
        }

        secret_key = os.getenv("SECRET_KEY") or os.getenv("JWT_SECRET_KEY")
        if not secret_key:
            return jsonify({"error": "Configuration serveur invalide"}), 500

        token = jwt.encode(payload, secret_key, algorithm="HS256")
        return jsonify({"token": token, "user": {"id": user["id"], "nom": user["nom"], "email": user["email"]}}), 200
        
    except Exception as e:
        return jsonify({"error": f"Erreur lors de la connexion: {str(e)}"}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()