#!/bin/bash

echo "Building docker image for model..."
docker build --no-cache -t cats-classifier-model:001 -f image-model.dockerfile .
cd api/

echo "Building docker image for backend..."
docker build --no-cache -t cats-classifier-backend:001 -f image-backend.dockerfile .

echo "Building docker image for frontend..."
docker build --no-cache -t cats-classifier-frontend:001 -f image-frontend.dockerfile .
