#!/bin/bash

cd /home/ubuntu/app

echo "Pulling latest changes and rebuilding..."

docker compose down
docker compose pull
docker compose up -d --build
