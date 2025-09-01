from pymongo import MongoClient

def create_mongo_db():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["StreamHiveDb"]

    # Users mit Profil
    users = db["Users"]
    users.insert_one({
        "username": "demo_user",
        "email": "demo@example.com",
        "password": "hashed_password",
        "profile": {
            "name": "Demo User",
            "bio": "Hallo, ich bin neu hier!",
            "profile_image": "path/to/image.png"
        },
        "role": "user"  # admin oder user
    })

    # Videos mit Metadaten
    videos = db["Videos"]
    videos.insert_one({
        "user_id": "demo_user_id",
        "title": "Erstes Video",
        "description": "Das ist mein erstes Video",
        "upload_date": "2025-08-28",
        "duration": 120,
        "tags": ["fun", "demo"],
        "interactions": {
            "likes": 0,
            "dislikes": 0,
            "views": 0
        }
    })

    # Playlists
    playlists = db["Playlists"]
    playlists.insert_one({
        "user_id": "demo_user_id",
        "name": "Meine Playlist",
        "videos": []
    })

    # Abonnements
    subscriptions = db["Subscriptions"]
    subscriptions.insert_one({
        "follower_id": "demo_user_id",
        "followed_id": "another_user_id"
    })

    print("✅ MongoDB: StreamHiveDb wurde erstellt mit Collections.")

if __name__ == "__main__":
    create_mongo_db()
