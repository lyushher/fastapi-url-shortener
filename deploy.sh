#!/bin/bash

cd /home/ubuntu/app

echo "🔄 Pulling latest changes..."
docker compose down
docker compose pull
docker compose up -d --build

echo "✅ Deployment complete."
