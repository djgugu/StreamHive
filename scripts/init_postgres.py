import psycopg2

def create_postgres_db():
    conn = psycopg2.connect(
        dbname="postgres",  # Standard-Datenbank zum Connecten
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    conn.autocommit = True
    cur = conn.cursor()
    print("Connected")

    # Neue DB erstellen
    cur.execute("DROP DATABASE IF EXISTS streamhivedb;")
    cur.execute("CREATE DATABASE streamhivedb;")
    cur.close()
    conn.close()

    # Mit neuer DB verbinden
    conn = psycopg2.connect(
        dbname="streamhivedb",  # Standard-Datenbank zum Connecten
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    print("Connected")

    cur = conn.cursor()

    # Users + Profile
    cur.execute("""
    CREATE TABLE Users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) UNIQUE NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        role VARCHAR(50) NOT NULL DEFAULT 'user'
    );
    """)
    cur.execute("""
    CREATE TABLE UserProfiles (
        id SERIAL PRIMARY KEY,
        user_id INT REFERENCES Users(id) ON DELETE CASCADE,
        name VARCHAR(100),
        bio TEXT,
        profile_image TEXT
    );
    """)

    # Videos + Metadaten
    cur.execute("""
    CREATE TABLE Videos (
        id SERIAL PRIMARY KEY,
        user_id INT REFERENCES Users(id) ON DELETE CASCADE,
        title VARCHAR(200) NOT NULL,
        description TEXT,
        upload_date DATE,
        duration INT,
        tags TEXT[]
    );
    """)
    cur.execute("""
    CREATE TABLE VideoInteractions (
        id SERIAL PRIMARY KEY,
        video_id INT REFERENCES Videos(id) ON DELETE CASCADE,
        likes INT DEFAULT 0,
        dislikes INT DEFAULT 0,
        views INT DEFAULT 0
    );
    """)

    # Playlists
    cur.execute("""
    CREATE TABLE Playlists (
        id SERIAL PRIMARY KEY,
        user_id INT REFERENCES Users(id) ON DELETE CASCADE,
        name VARCHAR(100) NOT NULL
    );
    """)
    cur.execute("""
    CREATE TABLE PlaylistVideos (
        playlist_id INT REFERENCES Playlists(id) ON DELETE CASCADE,
        video_id INT REFERENCES Videos(id) ON DELETE CASCADE,
        PRIMARY KEY (playlist_id, video_id)
    );
    """)

    # Abonnements
    cur.execute("""
    CREATE TABLE Subscriptions (
        follower_id INT REFERENCES Users(id) ON DELETE CASCADE,
        followed_id INT REFERENCES Users(id) ON DELETE CASCADE,
        PRIMARY KEY (follower_id, followed_id)
    );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("✅ PostgreSQL: StreamHiveDb mit Tabellen erstellt.")

if __name__ == "__main__":
    create_postgres_db()
