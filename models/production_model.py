def create_production_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS production (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            valeur FLOAT,
            date DATETIME,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)