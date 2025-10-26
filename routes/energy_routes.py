from flask import Blueprint, request
from controllers.energy_controller import get_current_energy, get_energy_history
from utils.jwt_utils import decode_token

energy_bp = Blueprint("energy", __name__)

@energy_bp.route("/current", methods=["GET"])
def current():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    payload = decode_token(token)
    if not payload:
        return {"error": "Token invalide"}, 401
    return get_current_energy(payload["id"])

@energy_bp.route("/history", methods=["GET"])
def history():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    payload = decode_token(token)
    if not payload:
        return {"error": "Token invalide"}, 401
    return get_energy_history(payload["id"])



# from flask import Blueprint, request, jsonify
# from controllers.energy_controller import get_current_energy, get_energy_history
# from utils.jwt_utils import decode_token

# energy_bp = Blueprint("energy", __name__)

# @energy_bp.route("/current", methods=["GET"])
# def current():
#     try:
#         token = request.headers.get("Authorization", "").replace("Bearer ", "")
#         if not token:
#             return jsonify({"error": "Token manquant"}), 401
            
#         payload = decode_token(token)
#         if not payload:
#             return jsonify({"error": "Token invalide"}), 401
            
#         result = get_current_energy(payload["id"])
#         return result
#     except Exception as e:
#         return jsonify({"error": f"Erreur serveur lors de la récupération de l'énergie actuelle: {str(e)}"}), 500

# @energy_bp.route("/history", methods=["GET"])
# def history():
#     try:
#         token = request.headers.get("Authorization", "").replace("Bearer ", "")
#         if not token:
#             return jsonify({"error": "Token manquant"}), 401
            
#         payload = decode_token(token)
#         if not payload:
#             return jsonify({"error": "Token invalide"}), 401
            
#         result = get_energy_history(payload["id"])
#         return result
#     except Exception as e:
#         return jsonify({"error": f"Erreur serveur lors de la récupération de l'historique: {str(e)}"}), 500