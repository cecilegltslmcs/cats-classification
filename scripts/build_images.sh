#!/bin/bash
# Script to build Docker images for a Cats Breeds Classifier application.

set -e

cd ..

# Define Docker registry
HOST_NAME="europe-west1-docker.pkg.dev/cats-breeds-classifier/cats-classifier"
GCP_PROJECT_NAME="cats-breeds-classifier"

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
docker build --no-cache --pull -t "$model_tag" -f "$model_dockerfile" .
docker tag $model_tag $HOST_NAME/$GCP_PROJECT_NAME/$model_tag

# Change to the api directory
cd api/

# Build Docker image for the backend
echo "🖼️   Building Docker image for backend..."
docker build --no-cache --pull -t "$backend_tag" -f "$backend_dockerfile" .
docker tag $backend_tag $HOST_NAME/$GCP_PROJECT_NAME/$backend_tag

# Build Docker image for the frontend
echo "🖼️   Building Docker image for frontend..."
docker build --no-cache --pull -t "$frontend_tag" -f "$frontend_dockerfile" .
docker tag $frontend_tag $HOST_NAME/$GCP_PROJECT_NAME/$frontend_tag

# Print information about the built Docker images
docker image ls | grep "cats-classifier"

docker image push $HOST_NAME/$GCP_PROJECT_NAME/$model_tag
docker image push $HOST_NAME/$GCP_PROJECT_NAME/$backend_tag
docker image push $HOST_NAME/$GCP_PROJECT_NAME/$frontend_tag
