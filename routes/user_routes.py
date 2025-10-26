# from flask import Blueprint, request, jsonify
# from controllers.user_controller import get_profile, update_profile
# from utils.jwt_utils import decode_token

# user_bp = Blueprint("user", __name__)

# @user_bp.route("/profile", methods=["GET"])
# def profile():
#     token = request.headers.get("Authorization", "").replace("Bearer ", "")
#     payload = decode_token(token)
#     if not payload:
#         return jsonify({"error": "Token invalide"}), 401
#     return get_profile(payload["id"])


# @user_bp.route("/profile", methods=["PUT"])
# def update():
#     token = request.headers.get("Authorization", "").replace("Bearer ", "")
#     payload = decode_token(token)
#     if not payload:
#         return jsonify({"error": "Token invalide"}), 401

#     data = request.get_json()
#     if not data:
#         return jsonify({"error": "Aucune donnée reçue"}), 400

#     return update_profile(payload["id"], data)


# # ✅ Utilise aussi update_profile pour les paramètres
# @user_bp.route("/settings", methods=["PUT"])
# def update_user_settings():
#     token = request.headers.get("Authorization", "").replace("Bearer ", "")
#     payload = decode_token(token)
#     if not payload:
#         return jsonify({"error": "Token invalide"}), 401

#     data = request.get_json()
#     if not data:
#         return jsonify({"error": "Aucune donnée reçue"}), 400

#     return update_profile(payload["id"], data)
from flask import Blueprint, request, jsonify
from controllers.user_controller import get_profile, update_profile
from utils.jwt_utils import decode_token

user_bp = Blueprint("user", __name__)

@user_bp.route("/profile", methods=["GET"])
def profile():
    try:
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if not token:
            return jsonify({"error": "Token manquant"}), 401
            
        payload = decode_token(token)
        if not payload:
            return jsonify({"error": "Token invalide"}), 401
            
        return get_profile(payload["id"])
    except Exception as e:
        return jsonify({"error": f"Erreur serveur lors de la récupération du profil: {str(e)}"}), 500


@user_bp.route("/profile", methods=["PUT"])
def update():
    try:
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if not token:
            return jsonify({"error": "Token manquant"}), 401
            
        payload = decode_token(token)
        if not payload:
            return jsonify({"error": "Token invalide"}), 401

        data = request.get_json()
        if not data:
            return jsonify({"error": "Aucune donnée reçue"}), 400

        return update_profile(payload["id"], data)
    except Exception as e:
        return jsonify({"error": f"Erreur serveur lors de la mise à jour du profil: {str(e)}"}), 500


@user_bp.route("/settings", methods=["PUT"])
def update_user_settings():
    try:
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if not token:
            return jsonify({"error": "Token manquant"}), 401
            
        payload = decode_token(token)
        if not payload:
            return jsonify({"error": "Token invalide"}), 401

        data = request.get_json()
        if not data:
            return jsonify({"error": "Aucune donnée reçue"}), 400

        return update_profile(payload["id"], data)
    except Exception as e:
        return jsonify({"error": f"Erreur serveur lors de la mise à jour des paramètres: {str(e)}"}), 500