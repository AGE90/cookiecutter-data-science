#!/bin/bash
set -e

echo "🔧 Installing dependencies..."
poetry install --with dev,test,data-science,viz

echo "📁 Copying environment files..."
cp -n .env.example .env || true

echo "✅ Setup complete."