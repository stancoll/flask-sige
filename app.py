from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Import des blueprints
from routes.simulation_routes import simulation_bp
from routes.appareils_routes import appareil_bp
from routes.alert_routes import alert_bp
from routes.energy_routes import energy_bp
from routes.user_routes import user_bp
from routes.auth_routes import auth_bp  

# Charger le fichier .env
load_dotenv()

app = Flask(__name__)

# ✅ Récupération de la clé secrète
SECRET = os.getenv('SECRET_KEY') or os.getenv('JWT_SECRET_KEY')

# ✅ Vérifie que la clé existe — sinon erreur claire
if not SECRET:
    raise RuntimeError("⚠️ SECRET_KEY ou JWT_SECRET_KEY manquant dans le fichier .env")

# ✅ Configure la clé dans Flask et pour JWT
app.config['SECRET_KEY'] = SECRET
app.config['JWT_SECRET_KEY'] = SECRET  # important si tu utilises Flask-JWT-Extended

# Activer CORS
CORS(app)

# Enregistre les routes
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(energy_bp, url_prefix="/energy")
app.register_blueprint(simulation_bp, url_prefix="/simulation")
app.register_blueprint(appareil_bp, url_prefix="/appareils")
app.register_blueprint(alert_bp, url_prefix="/alerts")
app.register_blueprint(user_bp, url_prefix="/user")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(debug=False, host="0.0.0.0", port=port)
