def create_appareil_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appareils (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            nom VARCHAR(100),
            categorie VARCHAR(50),
            consommationQuotidienne FLOAT,
            puissanceWatt INT,
            est_actif BOOLEAN DEFAULT TRUE,
            date_ajout DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)

def insert_appareil(cursor, appareil_data):
    cursor.execute("""
        INSERT INTO appareils (user_id, nom, categorie, consommationQuotidienne, puissanceWatt, est_actif)
        VALUES (%s, %s, %s, %s, %s, %s);
    """, (
        appareil_data["user_id"],
        appareil_data["nom"],
        appareil_data["categorie"],
        appareil_data["consommationQuotidienne"],
        appareil_data["puissanceWatt"],
        appareil_data.get("est_actif", True), 
    ))