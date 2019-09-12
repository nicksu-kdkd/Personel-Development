resource "null_resource" "kubeconfig" {
  provisioner "local-exec" {
    command = "gcloud container clusters get-credentials ${ var.k8s_name } --zone ${ var.location } --project ${ var.project_name }"
  }

  depends_on = [google_container_cluster.k8_cluster, google_container_node_pool.np]
}

resource "null_resource" "helmInit" {
  provisioner "local-exec" {
    command = "curl -O ${ var.helm_address }/${ var.helm_pkg } && tar -zxf ${ var.helm_pkg } && find . -type f -name 'helm' -exec mv {} /usr/local/bin \\; && helm init"
  }

  depends_on = [google_container_cluster.k8_cluster, google_container_node_pool.np, kubernetes_cluster_role_binding.tillerRoleBinding]
}