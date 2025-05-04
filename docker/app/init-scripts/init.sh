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

# 🧪 Verifica si la base de datos de pruebas existe, y créala si no
echo "🔎 Checking if test database '$POSTGRES_TEST_DB' exists..."
DB_EXISTS=$(PGPASSWORD=$POSTGRES_PASSWORD psql -U $POSTGRES_USER -h db -d $POSTGRES_DB -tAc "SELECT 1 FROM pg_database WHERE datname = '$POSTGRES_TEST_DB';")

if [ "$DB_EXISTS" != "1" ]; then
    echo "🧪 Test database not found. Creating '$POSTGRES_TEST_DB'..."
    PGPASSWORD=$POSTGRES_PASSWORD createdb -U $POSTGRES_USER -h db $POSTGRES_TEST_DB
    echo "✅ Test database created."
else
    echo "📂 Test database '$POSTGRES_TEST_DB' already exists. Skipping creation."
fi

# 🧠 Verifica si la base principal está vacía y aplica migraciones
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
    python manage.py seed_users --total 575
else
    echo "📦 Database already has $EXISTING_TABLES tables. Skipping migration and seed."
fi

# ⚙️ Configuración Git
git config --global core.autocrlf input

# 🚀 Inicia servidor
python manage.py runserver 0.0.0.0:8000 & tail -f /dev/null
