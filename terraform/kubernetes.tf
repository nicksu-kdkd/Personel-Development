provider "kubernetes" {}

resource "kubernetes_service_account" "tiller" {
  metadata {
    name = "${ var.helm_user }"
    namespace = "kube-system"
  }

  depends_on = [null_resource.kubeconfig]
}

resource "kubernetes_cluster_role_binding" "tillerRoleBinding" {
  metadata {
    name = "tiller-rule"
  }

  role_ref {
    api_group = "rbac.authorization.k8s.io"
    kind      = "ClusterRole"
    name      = "cluster-admin"
  }

  subject {
    kind      = "ServiceAccount"
    name      = "${ kubernetes_service_account.tiller.metadata.0.name }"
    namespace = "${ kubernetes_service_account.tiller.metadata.0.namespace }"
  }

  depends_on = [kubernetes_service_account.tiller]
}

