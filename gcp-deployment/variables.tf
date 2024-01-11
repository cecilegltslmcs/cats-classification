variable "project_id" {
  description = "The project ID to host the cluster in"
  default = "cats-breeds-classifier"
}
variable "cluster_name" {
  description = "The name for the GKE cluster"
  default     = "cats-classifier"
}
variable "env_name" {
  description = "The environment for the GKE cluster"
  default     = "prod"
}
variable "region" {
  description = "The region to host the cluster in"
  default     = "europe-west1"
}

variable "artifact_id"{
  description = "The name of the artifact registry"
  default     = "cats-classifier"
}

variable "network" {
  description = "The VPC network created to host the cluster in"
  default     = "gke-network"
}
variable "subnetwork" {
  description = "The subnetwork created to host the cluster in"
  default     = "gke-subnet"
}
variable "ip_range_pods_name" {
  description = "The secondary ip range to use for pods"
  default     = "ip-range-pods"
}
variable "ip_range_services_name" {
  description = "The secondary ip range to use for services"
  default     = "ip-range-services"
}
