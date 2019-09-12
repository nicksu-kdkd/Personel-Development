variable "project_name" {
  type = string
  description = "The project to deploy to"
  default = "upheld-garage-218509"
}

variable "project_region" {
  type = string
  description = "The region to deploy to"
  default = "us-central1"
}

variable "project_zone" {
  type = string
  description = "The zone to deploy to"
  default = "us-central1-c"
}

variable "k8s_name" {
  type = string
  description = "The name of the kubernetes cluster"
  default = "k8s-cluster"
}

variable "dashboard_disabled" {
  type = bool
  description = "Whether or not to disable the kubernetes dashboard"
  default = true
}

variable "autoscaling_disabled" {
  type = bool
  description = "Whether or not to disable the horizontal pod auto scaling"
  default = false
}

variable "load_balancing_disabled" {
  type = bool
  description = "Whether or not to disable the http load balancing"
  default = false
}