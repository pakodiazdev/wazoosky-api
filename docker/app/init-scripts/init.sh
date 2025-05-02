#!/bin/bash

# 🐍 Verifica si ya están instaladas las dependencias
if [ -d "$HOME/.local/lib/python3.11/site-packages" ] && [ "$(ls -A $HOME/.local/lib/python3.11/site-packages)" ]; then
    echo "✅ Python dependencies already installed. Skipping pip install."
else
    echo "📦 Installing Python dependencies..."
    pip install --user -r requirements.txt
fi

# 🧠 Scripts utilitarios
bash /init-scripts/sync-vscode-settings.sh
bash /init-scripts/art.sh

# 🐘 Espera a que PostgreSQL esté disponible
echo "⏳ Waiting for PostgreSQL..."
until pg_isready -h db -p 5432 > /dev/null 2>&1; do
  sleep 1
done
echo "✅ PostgreSQL is up."

set -e

echo "⏳ Checking if PostgreSQL schema is empty..."

EXISTING_TABLES=$(PGPASSWORD=$POSTGRES_PASSWORD psql -U $POSTGRES_USER -d $POSTGRES_DB -h db -tAc "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'public';" || echo "error")

if ! [[ "$EXISTING_TABLES" =~ ^[0-9]+$ ]]; then
  echo "❌ Could not check database tables. Got: '$EXISTING_TABLES'"
  exit 1
fi

if [ "$EXISTING_TABLES" -eq "0" ]; then
    echo "📂 Database is empty. Running initial migrations..."
    python manage.py migrate

    echo "🌱 Running seeders..."
    python manage.py seed_users --total 75
else
    echo "📦 Database already has $EXISTING_TABLES tables. Skipping migration and seed."
fi

# Git Configuration

git config --global core.autocrlf input

python manage.py runserver 0.0.0.0:8000 & tail -f /dev/null

