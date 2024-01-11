output "artifact_id" {
  description = "Repository name"
  value       = "${google_artifact_registry_repository.repo.id}"
}

output "cluster_name" {
  description = "Cluster name"
  value       = "${module.gke.name}"
}
