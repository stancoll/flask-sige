from flask import jsonify
from config import get_db_connection

def get_simulation_month(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT categorie, SUM(consommationQuotidienne) AS total
        FROM appareils
        WHERE user_id = %s AND est_actif = TRUE
        GROUP BY categorie
    """, (user_id,))

    rows = cursor.fetchall()

    repartition = {row["categorie"]: row["total"] for row in rows}
    consommation = sum(row["total"] for row in rows)

    # Appareils actifs (optionnel)
    cursor.execute("""
        SELECT * FROM appareils
        WHERE user_id = %s AND est_actif = TRUE
    """, (user_id,))
    appareils_actifs = cursor.fetchall()

    conn.close()

    return jsonify({
        "consommation": consommation,
        "repartition": repartition,
        "appareilsActifs": appareils_actifs
    })
