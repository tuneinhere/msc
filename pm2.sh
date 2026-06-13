#!/bin/bash

SERVICE_NAME=$(basename "$(pwd)")
REPO_DIR="$(pwd)"
VENV_DIR="$REPO_DIR/venv"

echo "📦 Cek Node.js & PM2..."

# install Node.js kalau belum ada
if ! command -v node &> /dev/null
then
    echo "⬇️ Install Node.js..."
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt-get install -y nodejs
else
    echo "ℹ️ Node.js sudah ada"
fi

# install PM2 kalau belum ada
if ! command -v pm2 &> /dev/null
then
    echo "⬇️ Install PM2..."
    sudo npm install -g pm2
else
    echo "ℹ️ PM2 sudah ada"
fi

echo "📦 Setup virtual environment..."

if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
    echo "✅ Venv dibuat"
else
    echo "ℹ️ Venv sudah ada"
fi

source "$VENV_DIR/bin/activate"
pip install --upgrade pip
pip install -r requirements.txt

# load .env kalau ada
if [ -f ".env" ]; then
    export $(grep -v '^#' .env | xargs)
    echo "📄 .env loaded"
fi

echo "🚀 Menjalankan dengan PM2..."


pm2 delete "$SERVICE_NAME" 2>/dev/null

pm2 start "$VENV_DIR/bin/python" \
    --name "$SERVICE_NAME" \
    --cwd "$INSTALL_DIR" \
    -- -u -m FsubPremBot

pm2 save
pm2 startup

echo "✅ Berhasil jalan!"
pm2 status