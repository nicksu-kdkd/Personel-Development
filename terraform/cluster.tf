resource "google_container_cluster" "k8_cluster" {
  name     = "${ var.k8s_name }"
  location = "${ var.location }"

  # Required and should not be changed, as we are deploying without a default node pool
  remove_default_node_pool = true
  initial_node_count = 1

  # Keep the empty vaule to disable basic auth or GKE will generate a passwd for admin user 
  master_auth {
    username = ""
    password = ""

    client_certificate_config {
      issue_client_certificate = false
    }
  }

  addons_config {
    http_load_balancing {
      disabled = "${ var.load_balancing_disabled }"
    }

    horizontal_pod_autoscaling {
      disabled = "${ var.autoscaling_disabled }"
    }

    kubernetes_dashboard {
      disabled = "${ var.dashboard_disabled }"
    }
  }
}