#!/bin/bash

cd ../kube-config

echo "🧰  Choose your distribution: "
echo "0️⃣   Kind | 1️⃣   Minikube"
read distribution

echo "📦  Creating local cluster..."
if [ "$distribution" -eq 0 ]; then
    kind create cluster
    echo "📦  Cluster created!"
    echo "🖼️  Loading local images in cluster..."
    kind load docker-image cats-classifier-model:001
    kind load docker-image cats-classifier-backend:001
    kind load docker-image cats-classifier-frontend:001
    echo "🖼️  Docker images loaded in cluster!"
elif [ "$distribution" -eq 1 ]; then
    minikube start --cpus 4
    echo "📦  Cluster created!"
    echo "🖼️  Loading local images in cluster..."
    minikube image load cats-classifier-model:001
    minikube image load cats-classifier-backend:001
    minikube image load cats-classifier-frontend:001
    echo "🖼️  Docker images loaded in cluster!"
else
    echo "🚫  Invalid distribution choice. Exiting..."
    exit 1
fi

kube_config=$(pwd)


echo "📟  Launching deployments and services..."
for file in "$kube_config"/*.yaml; do
    if [ -f "$file" ]; then
        echo "📦   Creating resources from file: $file"
        kubectl apply -f "$file"
    fi
done

echo "🟢  Deployments and services ready to use!"
