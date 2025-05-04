#!/bin/bash

SERVER_NAME=${PGADMIN_SERVER_NAME:-"Main DB Server"}
DB_HOST=${DB_HOST:-"db"}
DB_PORT=${DB_PORT:-5432}
DB_NAME=${POSTGRES_DB:-"postgres"}
DB_USER=${POSTGRES_USER:-"postgres"}
SSL_MODE=${PGADMIN_SSL_MODE:-"prefer"}
SERVERS_JSON_PATH=/var/lib/pgadmin/servers.json


echo "🛠️ Generating servers.json for pgAdmin at $SERVERS_JSON_PATH..."

cat > "$SERVERS_JSON_PATH" <<EOF
{
  "Servers": {
    "1": {
      "Name": "$SERVER_NAME",
      "Group": "Servers",
      "Host": "$DB_HOST",
      "Port": $DB_PORT,
      "MaintenanceDB": "$DB_NAME",
      "Username": "$DB_USER",
      "SSLMode": "$SSL_MODE"
    }
  }
}
EOF

echo "✅ pgAdmin server config generated!"

sh /entrypoint.sh

tail -f /dev/null
