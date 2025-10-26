from flask import jsonify
from config import get_db_connection

def get_current_energy(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM consommation WHERE user_id = %s ORDER BY date DESC LIMIT 1", (user_id,))
    conso = cursor.fetchone()
    cursor.execute("SELECT * FROM production WHERE user_id = %s ORDER BY date DESC LIMIT 1", (user_id,))
    prod = cursor.fetchone()
    return jsonify({"consommation": conso, "production": prod})

def get_energy_history(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM consommation WHERE user_id = %s ORDER BY date DESC LIMIT 30", (user_id,))
    data = cursor.fetchall()
    return jsonify(data)
