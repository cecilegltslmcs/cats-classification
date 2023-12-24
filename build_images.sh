#!/bin/bash
# Script to build Docker images for a Cats Breeds Classifier application.

# Exit script if any command returns a non-zero status
set -e

# Define image tags
MODEL_TAG="cats-classifier-model:001"
BACKEND_TAG="cats-classifier-backend:001"
FRONTEND_TAG="cats-classifier-frontend:001"

# Build Docker image for the model
echo "🖼️   Building docker image for model..."
docker build --no-cache -t $MODEL_TAG -f image-model.dockerfile .

# Change to the api directory
cd api/

# Build Docker image for the backend
echo "🖼️   Building docker image for backend..."
docker build --no-cache -t $BACKEND_TAG -f image-backend.dockerfile .

# Build Docker image for the frontend
echo "🖼️   Building docker image for frontend..."
docker build --no-cache -t $FRONTEND_TAG -f image-frontend.dockerfile .
