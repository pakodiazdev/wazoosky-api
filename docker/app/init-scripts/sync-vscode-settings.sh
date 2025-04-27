#!/bin/sh

BASE="/app/.vscode/settings.dist.json"
TARGET="/app/.vscode/settings.json"

echo "🔧 Synchronizing VS Code configuration..."

# Verificar que exista el archivo base
if [ ! -f "$BASE" ]; then
    echo "❌ Base file $BASE not found."
    exit 1
fi

# Leer y parsear el base
DIST_CONTENT=$(cat "$BASE")
if ! echo "$DIST_CONTENT" | jq empty > /dev/null 2>&1; then
    echo "❌ Error parsing $BASE"
    exit 1
fi

# Inicializar current vacío
CURRENT_CONTENT="{}"

# Si existe settings.json, leerlo
if [ -f "$TARGET" ]; then
    CURRENT_CONTENT=$(cat "$TARGET")
    if ! echo "$CURRENT_CONTENT" | jq empty > /dev/null 2>&1; then
        echo "⚠️  Invalid settings.json, it will be completely overwritten."
        CURRENT_CONTENT="{}"
    fi
fi

# Merge: las keys de settings.json pisan las de settings.dist.json
MERGED_CONTENT=$(jq -s '.[0] * .[1]' <(echo "$DIST_CONTENT") <(echo "$CURRENT_CONTENT"))

# Guardar el archivo final
echo "$MERGED_CONTENT" | jq '.' > "$TARGET"

echo "✅ settings.json updated successfully!"
