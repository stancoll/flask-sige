def create_alert_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alertes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            type VARCHAR(50),
            message TEXT,
            niveau VARCHAR(20),
            date DATETIME,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)