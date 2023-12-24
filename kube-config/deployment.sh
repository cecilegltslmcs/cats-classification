#!/bin/bash

echo "Choose your distribution: "
echo "0: Kind | 1: Minikube"
read distribution

echo "Creating local cluster..."
if [ "$distribution" -eq 0 ]; then
    kind create cluster
    echo "Cluster created!"
    echo "Loading local images in cluster..."
    kind load docker-image cats-classifier-model:001
    kind load docker-image cats-classifier-backend:001
    kind load docker-image cats-classifier-frontend:001
    echo "Docker images loaded in cluster!"
elif [ "$distribution" -eq 1 ]; then
    minikube start --cpus 8
    echo "Cluster created!"
    echo "Loading local images in cluster..."
    minikube image load cats-classifier-model:001
    minikube image load cats-classifier-backend:001
    minikube image load cats-classifier-frontend:001
    echo "Docker images loaded in cluster!"
else
    echo "Invalid distribution choice. Exiting..."
    exit 1
fi

kube_config=$(pwd)


echo "Launching deployment and service..."
for file in "$kube_config"/*.yaml; do
    if [ -f "$file" ]; then
        echo "Create for file: $file"
        kubectl apply -f "$file"
    fi
done
echo "Deployments and services ready to use!"
