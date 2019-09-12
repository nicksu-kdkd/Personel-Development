resource "google_container_node_pool" "np" {
  name       = "${ var.node_pool_name }"
  location    = "${ var.location }"
  cluster   = "${ var.k8s_name }"
  node_count = "${ var.node_number }"

  node_config {
    preemptible = "${ var.preemptible }"
    machine_type = "${ var.machine_type }"

    oauth_scopes = [
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring",
    ]
  }

  depends_on = [google_container_cluster.k8_cluster]
}

