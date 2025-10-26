from flask import Blueprint, request
from controllers.alert_controller import get_alerts
from utils.jwt_utils import decode_token

alert_bp = Blueprint("alerts", __name__)

@alert_bp.route("/", methods=["GET"])
def alerts():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    payload = decode_token(token)
    if not payload:
        return {"error": "Token invalide"}, 401
    return get_alerts(payload["id"])


# from flask import Blueprint, request, jsonify
# from controllers.alert_controller import get_alerts
# from utils.jwt_utils import decode_token

# alert_bp = Blueprint("alerts", __name__)

# @alert_bp.route("/", methods=["GET"])
# def alerts():
#     try:
#         token = request.headers.get("Authorization", "").replace("Bearer ", "")
#         if not token:
#             return jsonify({"error": "Token manquant"}), 401
            
#         payload = decode_token(token)
#         if not payload:
#             return jsonify({"error": "Token invalide"}), 401
            
#         result = get_alerts(payload["id"])
#         return result
#     except Exception as e:
#         return jsonify({"error": f"Erreur serveur lors de la récupération des alertes: {str(e)}"}), 500