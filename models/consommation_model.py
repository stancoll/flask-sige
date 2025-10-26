def create_consumption_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS consommation (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            valeur FLOAT,
            type VARCHAR(50),
            date DATETIME,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)