from flask import jsonify
from config import get_db_connection

def get_alerts(user_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT id, type, message, niveau, date 
            FROM alertes 
            WHERE user_id = %s 
            ORDER BY date DESC
        """, (user_id,))
        
        data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        print("Erreur lors de la récupération des alertes :", e)
        return jsonify({"error": "Erreur serveur"}), 500
    finally:
        cursor.close()
        conn.close()
