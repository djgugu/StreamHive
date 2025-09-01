#!/bin/bash

# Stoppe das Script bei Fehlern
set -e

echo "🚀 Starte Initialisierung..."

# Schritt 1: Python Abhängigkeiten installieren
echo "📦 Installiere Python Abhängigkeiten..."
pip install -r requirements.txt

# Schritt 2: PostgreSQL Initialisierung
echo "🗄️ Initialisiere PostgreSQL..."
python init_postgres.py

# Schritt 3: MongoDB Initialisierung
echo "🍃 Initialisiere MongoDB..."
python init_mongo.py

echo "✅ Alles erfolgreich initialisiert!"
