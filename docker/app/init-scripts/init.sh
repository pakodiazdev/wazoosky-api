# Check if Python site-packages has content
if [ -d "$HOME/.local/lib/python3.11/site-packages" ] && [ "$(ls -A $HOME/.local/lib/python3.11/site-packages)" ]; then
    echo "✅ Python dependencies already installed. Skipping pip install."
else
    echo "📦 Installing Python dependencies..."
    pip install --user -r requirements.txt
fi

bash /init-scripts/sync-vscode-settings.sh
bash /init-scripts/art.sh

python manage.py runserver 0.0.0.0:8000 & tail -f /dev/null

