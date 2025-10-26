# from flask import Blueprint, request
# from controllers.simulation_controller import get_simulation_month
# from utils.jwt_utils import decode_token

# simulation_bp = Blueprint("simulation", __name__)

# @simulation_bp.route("/month", methods=["GET"])
# def simulation_month():
#     token = request.headers.get("Authorization", "").replace("Bearer ", "")
#     payload = decode_token(token)
#     if not payload:
#         return {"error": "Token invalide"}, 401
#     return get_simulation_month(payload["id"])

from flask import Blueprint, request, jsonify
from controllers.simulation_controller import get_simulation_month
from utils.jwt_utils import decode_token

simulation_bp = Blueprint("simulation", __name__)

@simulation_bp.route("/month", methods=["GET"])
def simulation_month():
    try:
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if not token:
            return jsonify({"error": "Token manquant"}), 401
            
        payload = decode_token(token)
        if not payload:
            return jsonify({"error": "Token invalide"}), 401
            
        result = get_simulation_month(payload["id"])
        return result
    except Exception as e:
        return jsonify({"error": f"Erreur serveur lors de la simulation: {str(e)}"}), 500