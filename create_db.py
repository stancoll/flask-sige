from dotenv import load_dotenv
load_dotenv()
from models.user_model import create_user_table
from models.consommation_model import create_consumption_table
from models.production_model import create_production_table
from models.alert_model import create_alert_table
from models.appareil_model import create_appareil_table
from config import get_db_connection


def setup_database():
    conn = get_db_connection()
    cursor = conn.cursor()

    create_user_table(cursor)
    create_consumption_table(cursor)
    create_appareil_table(cursor)
    create_production_table(cursor)
    create_alert_table(cursor)

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Base de données créée avec succès.")

if __name__ == "__main__":
    setup_database()
