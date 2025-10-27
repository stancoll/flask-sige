from dotenv import load_dotenv
load_dotenv()

from database import get_db_connection
from models.user_model import create_user_table
from models.consommation_model import create_consumption_table
from models.production_model import create_production_table
from models.alert_model import create_alert_table
from models.appareil_model import create_appareil_table

def init_remote_database():
    """Initialise la base de données distante (Aiven)"""
    print("🚀 Initialisation de la base de données distante...")
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        print("📋 Création des tables...")
        create_user_table(cursor)
        print("  ✅ Table users créée")
        
        create_consumption_table(cursor)
        print("  ✅ Table consommation créée")
        
        create_production_table(cursor)
        print("  ✅ Table production créée")
        
        create_appareil_table(cursor)
        print("  ✅ Table appareils créée")
        
        create_alert_table(cursor)
        print("  ✅ Table alertes créée")

        conn.commit()
        cursor.close()
        conn.close()
        
        print("\n✅ Base de données distante initialisée avec succès !")
        
    except Exception as e:
        print(f"\n❌ Erreur lors de l'initialisation : {e}")

if __name__ == "__main__":
    init_remote_database()