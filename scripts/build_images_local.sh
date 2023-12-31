#!/bin/bash
# Script to build Docker images for a Cats Breeds Classifier application.

set -e

cd ..

# Define image tags
model_tag="cats-classifier-model:001"
backend_tag="cats-classifier-backend:001"
frontend_tag="cats-classifier-frontend:001"

# Define Dockerfile names
model_dockerfile="image-model.dockerfile"
backend_dockerfile="image-backend.dockerfile"
frontend_dockerfile="image-frontend.dockerfile"

# Build Docker image for the model
echo "🖼️   Building Docker image for model..."
docker build --no-cache -t "$model_tag" -f "$model_dockerfile" .

# Change to the api directory
cd api/

# Build Docker image for the backend
echo "🖼️   Building Docker image for backend..."
docker build --no-cache -t "$backend_tag" -f "$backend_dockerfile" .

# Build Docker image for the frontend
echo "🖼️   Building Docker image for frontend..."
docker build --no-cache -t "$frontend_tag" -f "$frontend_dockerfile" .

# Print information about the built Docker images
docker image ls | grep "cats-classifier"
