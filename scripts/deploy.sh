kube_config = ../kube-config

echo "📟  Launching deployments and services..."
for file in "$kube_config"/*.yaml; do
  if [ -f "$file" ]; then
    echo "📦   Creating resources from file: $file"
    kubectl apply -f "$file"
  fi
done
