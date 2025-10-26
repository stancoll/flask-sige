# from flask import Blueprint
# from controllers.appareil_controller import (
#     ajouter_appareil,
#     get_appareils,
#     update_appareil,
#     delete_appareil
# )

# appareil_bp = Blueprint("appareils", __name__)

# # ➕ Ajouter un appareil
# @appareil_bp.route("/add", methods=["POST"])
# def add_appareil():
#     return ajouter_appareil()

# # 📥 Récupérer les appareils d’un utilisateur (par token)
# @appareil_bp.route("/list", methods=["GET"])
# def fetch_appareils():
#     return get_appareils()

# # ✏️ Mettre à jour un appareil spécifique (par id)
# @appareil_bp.route("/<int:appareil_id>", methods=["PUT"])
# def edit_appareil(appareil_id):
#     return update_appareil(appareil_id)

# # ❌ Supprimer un appareil spécifique (par id)
# @appareil_bp.route("/<int:appareil_id>", methods=["DELETE"])
# def remove_appareil(appareil_id):
#     return delete_appareil(appareil_id)

# @appareil_bp.route("/", methods=["GET"])
# def list_appareils():
#     return get_appareils()




from flask import Blueprint, jsonify, request
from controllers.appareil_controller import (
    ajouter_appareil,
    get_appareils,
    update_appareil,
    delete_appareil
)
from utils.jwt_utils import decode_token

appareil_bp = Blueprint("appareils", __name__)

# ➕ Ajouter un appareil
@appareil_bp.route("/add", methods=["POST"])
def add_appareil():
    try:
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if not token:
            return jsonify({"error": "Token manquant"}), 401
            
        payload = decode_token(token)
        if not payload:
            return jsonify({"error": "Token invalide"}), 401
            
        return ajouter_appareil()
    except Exception as e:
        return jsonify({"error": f"Erreur lors de l'ajout de l'appareil: {str(e)}"}), 500

# 📥 Récupérer les appareils d'un utilisateur (par token)
@appareil_bp.route("/list", methods=["GET"])
def fetch_appareils():
    try:
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if not token:
            return jsonify({"error": "Token manquant"}), 401
            
        payload = decode_token(token)
        if not payload:
            return jsonify({"error": "Token invalide"}), 401
            
        return get_appareils()
    except Exception as e:
        return jsonify({"error": f"Erreur lors de la récupération des appareils: {str(e)}"}), 500

# ✏️ Mettre à jour un appareil spécifique (par id)
@appareil_bp.route("/<int:appareil_id>", methods=["PUT"])
def edit_appareil(appareil_id):
    try:
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if not token:
            return jsonify({"error": "Token manquant"}), 401
            
        payload = decode_token(token)
        if not payload:
            return jsonify({"error": "Token invalide"}), 401
            
        return update_appareil(appareil_id)
    except Exception as e:
        return jsonify({"error": f"Erreur lors de la mise à jour de l'appareil: {str(e)}"}), 500

# ❌ Supprimer un appareil spécifique (par id)
@appareil_bp.route("/<int:appareil_id>", methods=["DELETE"])
def remove_appareil(appareil_id):
    try:
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if not token:
            return jsonify({"error": "Token manquant"}), 401
            
        payload = decode_token(token)
        if not payload:
            return jsonify({"error": "Token invalide"}), 401
            
        return delete_appareil(appareil_id)
    except Exception as e:
        return jsonify({"error": f"Erreur lors de la suppression de l'appareil: {str(e)}"}), 500

# ✅ Ajouter la route manquante pour le frontend
@appareil_bp.route("/", methods=["GET"])
def list_appareils():
    try:
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if not token:
            return jsonify({"error": "Token manquant"}), 401
            
        payload = decode_token(token)
        if not payload:
            return jsonify({"error": "Token invalide"}), 401
            
        return get_appareils()
    except Exception as e:
        return jsonify({"error": f"Erreur lors de la récupération des appareils: {str(e)}"}), 500