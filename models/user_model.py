def create_user_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(191) NOT NULL,
            email VARCHAR(191) NOT NULL UNIQUE,
            mot_de_passe VARCHAR(255) NOT NULL,
            objectif_mensuel FLOAT DEFAULT 0,
            tarif_kwh FLOAT DEFAULT 0,
            seuil_alerte FLOAT DEFAULT 0,
            theme_sombre BOOLEAN DEFAULT FALSE,
            notifications_actives BOOLEAN DEFAULT TRUE
        );
    """)
