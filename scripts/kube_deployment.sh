#!/bin/bash
#Script to deployment in a local cluster with Kind or Kubernetes

set -e

# Change to the kube-config directory
cd ../kube-config

# Define docker images to load in cluster
model_image="cats-classifier-model:001"
backend_image="cats-classifier-backend:001"
frontend_image="cats-classifier-frontend:001"

# Choose tool to create Kubernetes local cluster
echo "🧰  Choose your tool: "
echo "0️⃣  Kind | 1️⃣   Minikube"
read -r distribution

# Create local cluster and load docker images
echo "📦  Creating local cluster..."
if [ "$distribution" -eq 0 ]; then
    kind create cluster
    echo "📦  Cluster created!"
    echo "🖼️  Loading local images in cluster..."
    kind load docker-image "$model_image"
    kind load docker-image "$backend_image"
    kind load docker-image "$frontend_image"
    echo "🖼️  Docker images loaded in cluster!"
elif [ "$distribution" -eq 1 ]; then
    minikube start --cpus 4
    echo "📦  Cluster created!"
    echo "🖼️  Loading local images in cluster..."
    minikube image load "$model_image"
    minikube image load "$backend_image"
    minikube image load "$frontend_image"
    echo "🖼️  Docker images loaded in cluster!"
else
    echo "🚫  Invalid distribution choice. Exiting..."
    exit 1
fi

# Save directory localisation
kube_config=$(pwd)

# Create deployments and services
echo "📟  Launching deployments and services..."
for file in "$kube_config"/*.yaml; do
    if [ -f "$file" ]; then
        echo "📦   Creating resources from file: $file"
        kubectl apply -f "$file"
    fi
done

sleep 10

# Print pods & services
echo "----- PODS -----"
kubectl get pod

echo "----- SERVICES -----"
kubectl get service

echo "🟢  Deployments and services ready to use!"
