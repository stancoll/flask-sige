def create_settings_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS parametres (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            langue VARCHAR(20),
            theme VARCHAR(20),
            unite VARCHAR(10),
            seuil_alerte FLOAT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)