* Why this script
To automatically deploy a GKE cluster in google cloud and provision a helm server for auto deployment

* Must do before this script
1. A valid gcp account
Go to this page [Create a service account key](https://console.cloud.google.com/apis/credentials/serviceaccountkey?project=upheld-garage-218509&folder&organizationId) to create and download a json credential, then either you can provide the credential to terraform by exposing the path to the environmental variable `GOOGLE_CLOUD_KEYFILE_JSON` or put it in the `credential` of `main.tf`
2. gcloud command
[How to install gcloud command](https://cloud.google.com/sdk/gcloud/)
3. A google cloud project
[How to create a project](https://cloud.google.com/appengine/docs/standard/nodejs/building-app/creating-project)
4. Terraform 
[How to install Terraform](https://learn.hashicorp.com/terraform/getting-started/install.html)

* How this script works
There are 2 types of scripts in this repo:
| Name | Description |
| ------ | ----------- |
| main.tf| descript which cloud provider will be use and the default region and zone, as well as the credential |
| cluster.tf| descript how the GKE cluster will be deploy, the default node poll will be removed and a dedicate node poll will be created|
| node.tf| descript how a dedicated node poll will be created|
| helm.tf| pull the kubernetes credential and download the latest helm binary and initilize a helm server|
| *-variables.tf | declared the variables used by the deployment |


* How to deploy
** Run init to intialize the terraform environment
```bash
~/D/P/terraform> terraform init

Initializing the backend...

Initializing provider plugins...
- Checking for available provider plugins...
- Downloading plugin for provider "google" (terraform-providers/google) 2.10.0...
- Downloading plugin for provider "null" (terraform-providers/null) 2.1.2...

The following providers do not have any version constraints in configuration,
so the latest version was installed.

To prevent automatic upgrades to new major versions that may contain breaking
changes, it is recommended to add version = "..." constraints to the
corresponding provider blocks in configuration, with the constraint strings
suggested below.

* provider.google: version = "~> 2.10"
* provider.null: version = "~> 2.1"

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```


** Run plan to know what will be updated during change
``` bash
~/D/P/terraform> terraform plan -out k8-cluster.plan
Refreshing Terraform state in-memory prior to plan...
The refreshed state will be used to calculate this plan, but will not be
persisted to local or remote state storage.


------------------------------------------------------------------------

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_container_cluster.k8_cluster will be created
  + resource "google_container_cluster" "k8_cluster" {
      + additional_zones            = (known after apply)
      + cluster_autoscaling         = (known after apply)
      + cluster_ipv4_cidr           = (known after apply)
      + enable_binary_authorization = (known after apply)
      + enable_kubernetes_alpha     = false
      + enable_legacy_abac          = false
      + enable_tpu                  = (known after apply)
      + endpoint                    = (known after apply)
      + id                          = (known after apply)
      + initial_node_count          = 1
      + instance_group_urls         = (known after apply)
      + ip_allocation_policy        = (known after apply)
      + location                    = "asia-east1-a"
      + logging_service             = (known after apply)
      + master_version              = (known after apply)
      + monitoring_service          = (known after apply)
      + name                        = "k8s-cluster"
      + network                     = "default"
      + node_locations              = (known after apply)
      + node_version                = (known after apply)
      + project                     = (known after apply)
      + region                      = (known after apply)
      + remove_default_node_pool    = true
      + services_ipv4_cidr          = (known after apply)
      + subnetwork                  = (known after apply)
      + zone                        = (known after apply)

      + addons_config {
          + horizontal_pod_autoscaling {
              + disabled = false
            }

          + http_load_balancing {
              + disabled = false
            }

          + kubernetes_dashboard {
              + disabled = true
            }

          + network_policy_config {
              + disabled = (known after apply)
            }
        }

      + master_auth {
          + client_certificate     = (known after apply)
          + client_key             = (sensitive value)
          + cluster_ca_certificate = (known after apply)

          + client_certificate_config {
              + issue_client_certificate = false
            }
        }

      + network_policy {
          + enabled  = (known after apply)
          + provider = (known after apply)
        }

      + node_config {
          + disk_size_gb      = (known after apply)
          + disk_type         = (known after apply)
          + guest_accelerator = (known after apply)
          + image_type        = (known after apply)
          + labels            = (known after apply)
          + local_ssd_count   = (known after apply)
          + machine_type      = (known after apply)
          + metadata          = (known after apply)
          + min_cpu_platform  = (known after apply)
          + oauth_scopes      = (known after apply)
          + preemptible       = (known after apply)
          + service_account   = (known after apply)
          + tags              = (known after apply)

          + sandbox_config {
              + sandbox_type = (known after apply)
            }

          + taint {
              + effect = (known after apply)
              + key    = (known after apply)
              + value  = (known after apply)
            }

          + workload_metadata_config {
              + node_metadata = (known after apply)
            }
        }

      + node_pool {
          + initial_node_count  = (known after apply)
          + instance_group_urls = (known after apply)
          + max_pods_per_node   = (known after apply)
          + name                = (known after apply)
          + name_prefix         = (known after apply)
          + node_count          = (known after apply)
          + version             = (known after apply)

          + autoscaling {
              + max_node_count = (known after apply)
              + min_node_count = (known after apply)
            }

          + management {
              + auto_repair  = (known after apply)
              + auto_upgrade = (known after apply)
            }

          + node_config {
              + disk_size_gb      = (known after apply)
              + disk_type         = (known after apply)
              + guest_accelerator = (known after apply)
              + image_type        = (known after apply)
              + labels            = (known after apply)
              + local_ssd_count   = (known after apply)
              + machine_type      = (known after apply)
              + metadata          = (known after apply)
              + min_cpu_platform  = (known after apply)
              + oauth_scopes      = (known after apply)
              + preemptible       = (known after apply)
              + service_account   = (known after apply)
              + tags              = (known after apply)

              + sandbox_config {
                  + sandbox_type = (known after apply)
                }

              + taint {
                  + effect = (known after apply)
                  + key    = (known after apply)
                  + value  = (known after apply)
                }

              + workload_metadata_config {
                  + node_metadata = (known after apply)
                }
            }
        }
    }

  # google_container_node_pool.np will be created
  + resource "google_container_node_pool" "np" {
      + cluster             = "k8s-cluster"
      + id                  = (known after apply)
      + initial_node_count  = (known after apply)
      + instance_group_urls = (known after apply)
      + location            = "asia-east1-a"
      + max_pods_per_node   = (known after apply)
      + name                = "k8s-node-pool"
      + name_prefix         = (known after apply)
      + node_count          = 1
      + project             = (known after apply)
      + region              = (known after apply)
      + version             = (known after apply)
      + zone                = (known after apply)

      + management {
          + auto_repair  = (known after apply)
          + auto_upgrade = (known after apply)
        }

      + node_config {
          + disk_size_gb      = (known after apply)
          + disk_type         = (known after apply)
          + guest_accelerator = (known after apply)
          + image_type        = (known after apply)
          + labels            = (known after apply)
          + local_ssd_count   = (known after apply)
          + machine_type      = "f1-micro"
          + metadata          = (known after apply)
          + oauth_scopes      = [
              + "https://www.googleapis.com/auth/logging.write",
              + "https://www.googleapis.com/auth/monitoring",
            ]
          + preemptible       = true
          + service_account   = (known after apply)
        }
    }

  # null_resource.kubeconfig will be created
  + resource "null_resource" "kubeconfig" {
      + id = (known after apply)
    }

Plan: 3 to add, 0 to change, 0 to destroy.

------------------------------------------------------------------------

This plan was saved to: k8-cluster.plan

To perform exactly these actions, run the following command to apply:
    terraform apply "k8-cluster.plan"
```


** Run apply to deploy
```bash
~/D/P/terraform> terraform apply k8-cluster.plan
google_container_cluster.k8_cluster: Creating...
google_container_cluster.k8_cluster: Still creating... [10s elapsed]
google_container_cluster.k8_cluster: Still creating... [20s elapsed]
google_container_cluster.k8_cluster: Still creating... [30s elapsed]
google_container_cluster.k8_cluster: Still creating... [40s elapsed]
google_container_cluster.k8_cluster: Still creating... [50s elapsed]
google_container_cluster.k8_cluster: Still creating... [1m0s elapsed]
google_container_cluster.k8_cluster: Still creating... [1m10s elapsed]
google_container_cluster.k8_cluster: Still creating... [1m20s elapsed]
google_container_cluster.k8_cluster: Still creating... [1m30s elapsed]
google_container_cluster.k8_cluster: Still creating... [1m40s elapsed]
google_container_cluster.k8_cluster: Still creating... [1m50s elapsed]
google_container_cluster.k8_cluster: Still creating... [2m0s elapsed]
google_container_cluster.k8_cluster: Still creating... [2m11s elapsed]
google_container_cluster.k8_cluster: Still creating... [2m21s elapsed]
google_container_cluster.k8_cluster: Still creating... [2m31s elapsed]
google_container_cluster.k8_cluster: Still creating... [2m41s elapsed]
google_container_cluster.k8_cluster: Still creating... [2m51s elapsed]
google_container_cluster.k8_cluster: Still creating... [3m1s elapsed]
google_container_cluster.k8_cluster: Still creating... [3m11s elapsed]
google_container_cluster.k8_cluster: Still creating... [3m21s elapsed]
google_container_cluster.k8_cluster: Still creating... [3m31s elapsed]
google_container_cluster.k8_cluster: Still creating... [3m41s elapsed]
google_container_cluster.k8_cluster: Still creating... [3m51s elapsed]
google_container_cluster.k8_cluster: Still creating... [4m1s elapsed]
google_container_cluster.k8_cluster: Still creating... [4m11s elapsed]
google_container_cluster.k8_cluster: Still creating... [4m21s elapsed]
google_container_cluster.k8_cluster: Creation complete after 4m22s [id=k8s-cluster]
google_container_node_pool.np: Creating...
google_container_node_pool.np: Still creating... [10s elapsed]
google_container_node_pool.np: Still creating... [20s elapsed]
google_container_node_pool.np: Still creating... [30s elapsed]
google_container_node_pool.np: Still creating... [40s elapsed]
google_container_node_pool.np: Creation complete after 49s [id=asia-east1-a/k8s-cluster/k8s-node-pool]
null_resource.kubeconfig: Creating...
null_resource.kubeconfig: Provisioning with 'local-exec'...
null_resource.kubeconfig (local-exec): Executing: ["/bin/sh" "-c" "gcloud container clusters get-credentials k8s-cluster --zone asia-east1-a --project upheld-garage-218509"]
null_resource.kubeconfig (local-exec): Fetching cluster endpoint and auth data.
null_resource.kubeconfig (local-exec): kubeconfig entry generated for k8s-cluster.
null_resource.kubeconfig: Provisioning with 'local-exec'...
null_resource.kubeconfig (local-exec): Executing: ["/bin/sh" "-c" "tar -zxf helm-v2.14.2-darwin-amd64.tar.gz && find . -type f -name 'helm' -exec mv {} /usr/local/bin \\; && helm init"]
null_resource.kubeconfig (local-exec): Creating /Users/nicksu/.helm
null_resource.kubeconfig (local-exec): Creating /Users/nicksu/.helm/repository
null_resource.kubeconfig (local-exec): Creating /Users/nicksu/.helm/repository/cache
null_resource.kubeconfig (local-exec): Creating /Users/nicksu/.helm/repository/local
null_resource.kubeconfig (local-exec): Creating /Users/nicksu/.helm/plugins
null_resource.kubeconfig (local-exec): Creating /Users/nicksu/.helm/starters
null_resource.kubeconfig (local-exec): Creating /Users/nicksu/.helm/cache/archive
null_resource.kubeconfig (local-exec): Creating /Users/nicksu/.helm/repository/repositories.yaml
null_resource.kubeconfig (local-exec): Adding stable repo with URL: https://kubernetes-charts.storage.googleapis.com
null_resource.kubeconfig: Still creating... [10s elapsed]
null_resource.kubeconfig: Still creating... [20s elapsed]
null_resource.kubeconfig: Still creating... [30s elapsed]
null_resource.kubeconfig (local-exec): Adding local repo with URL: http://127.0.0.1:8879/charts
null_resource.kubeconfig (local-exec): $HELM_HOME has been configured at /Users/nicksu/.helm.

null_resource.kubeconfig (local-exec): Tiller (the Helm server-side component) has been installed into your Kubernetes Cluster.

null_resource.kubeconfig (local-exec): Please note: by default, Tiller is deployed with an insecure 'allow unauthenticated users' policy.
null_resource.kubeconfig (local-exec): To prevent this, run `helm init` with the --tiller-tls-verify flag.
null_resource.kubeconfig (local-exec): For more information on securing your installation see: https://docs.helm.sh/using_helm/#securing-your-helm-installation
null_resource.kubeconfig: Creation complete after 35s [id=5621880508203640741]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.

The state of your infrastructure has been saved to the path
below. This state is required to modify and destroy your
infrastructure, so keep it safe. To inspect the complete state
use the `terraform show` command.

State path: terraform.tfstate
```


** How to verify the provision of GKE
*** How to verify kubernetes cluster
``` bash
~/D/P/terraform> kubectl cluster-info
Kubernetes master is running at https://35.185.148.69
GLBCDefaultBackend is running at https://35.185.148.69/api/v1/namespaces/kube-system/services/default-http-backend:http/proxy
Heapster is running at https://35.185.148.69/api/v1/namespaces/kube-system/services/heapster/proxy
KubeDNS is running at https://35.185.148.69/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
Metrics-server is running at https://35.185.148.69/api/v1/namespaces/kube-system/services/https:metrics-server:/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
~/D/P/terraform> kubectl get cs
NAME                 STATUS    MESSAGE              ERROR
etcd-1               Healthy   {"health": "true"}
scheduler            Healthy   ok
controller-manager   Healthy   ok
etcd-0               Healthy   {"health": "true"}
```

*** How to verify helm server
```bash
~/D/P/terraform> helm repo list
NAME    URL
stable  https://kubernetes-charts.storage.googleapis.com
local   http://127.0.0.1:8879/charts
~/D/P/terraform> helm version
Client: &version.Version{SemVer:"v2.14.2", GitCommit:"a8b13cc5ab6a7dbef0a58f5061bcc7c0c61598e7", GitTreeState:"clean"}
Server: &version.Version{SemVer:"v2.14.2", GitCommit:"a8b13cc5ab6a7dbef0a58f5061bcc7c0c61598e7", GitTreeState:"clean"}
```


** Run show to show current state of Terraform
Before deployment, there should be nothing managed by Terraform, so the result of `terraform show` is null
```bash
~/D/P/terraform> terraform show

```
But after a successfully deployment, the result should tell us what has been managing by Terraform
```bash
~/D/P/terraform> terraform show
# google_container_cluster.k8_cluster:
resource "google_container_cluster" "k8_cluster" {
    additional_zones         = []
    cluster_autoscaling      = []
    cluster_ipv4_cidr        = "10.12.0.0/14"
    enable_kubernetes_alpha  = false
    enable_legacy_abac       = false
    endpoint                 = "35.185.148.69"
    id                       = "k8s-cluster"
    initial_node_count       = 1
    instance_group_urls      = []
    ip_allocation_policy     = []
    location                 = "asia-east1-a"
    logging_service          = "logging.googleapis.com"
    master_version           = "1.12.8-gke.10"
    monitoring_service       = "monitoring.googleapis.com"
    name                     = "k8s-cluster"
    network                  = "projects/upheld-garage-218509/global/networks/default"
    node_locations           = []
    node_version             = "1.12.8-gke.10"
    project                  = "upheld-garage-218509"
    remove_default_node_pool = true
    services_ipv4_cidr       = "10.15.240.0/20"
    subnetwork               = "projects/upheld-garage-218509/regions/asia-east1/subnetworks/default"
    zone                     = "asia-east1-a"

    addons_config {
        horizontal_pod_autoscaling {
            disabled = false
        }

        http_load_balancing {
            disabled = false
        }

        kubernetes_dashboard {
            disabled = true
        }

        network_policy_config {
            disabled = true
        }
    }

    master_auth {
        cluster_ca_certificate = "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURERENDQWZTZ0F3SUJBZ0lSQU1mdXlFK0RqVjhBS0c3WndXV1hEaXN3RFFZSktvWklodmNOQVFFTEJRQXcKTHpFdE1Dc0dBMVVFQXhNa016ZG1NalJrTnpFdE9URmpZUzAwTURVM0xXSXlZak10TkRBM05EYzRaVFkwTWpZNApNQjRYRFRFNU1EY3hOREV6TXpJME1Gb1hEVEkwTURjeE1qRTBNekkwTUZvd0x6RXRNQ3NHQTFVRUF4TWtNemRtCk1qUmtOekV0T1RGallTMDBNRFUzTFdJeVlqTXROREEzTkRjNFpUWTBNalk0TUlJQklqQU5CZ2txaGtpRzl3MEIKQVFFRkFBT0NBUThBTUlJQkNnS0NBUUVBaXVSSnh6WFhjTnU4N0lKQ2xuaXpmUUtWSHM5ZXVOaXN1c2NIMy9CSwpWWlEza0xUS3BsUllJdGFxZkJUaGYwNVpsU2ovQnFFcjhpempncDJRVFBIVGxXZTVzMDM3UlZXQ3JDaUxqd1ZzCk5OSVMrN1hsaWh3YWhPQTJjdDVEdDFJVENiaHFFQitrVkVWaUJ6Y0pTN3IyR2Z1b3Y3TDVtekJFL3JFUUliR2wKbHk2ZlYwd2NzOHV2aE9hWWVCY2FnMDdOQmk2NVRPVXJEUkt3aUxlWVNKaEQxbXR2dkhLdzJkSk5YRWdoUEVmdQpwUm5PRTZDTzRNdXpVZmdSYlBVZCt2aWYrS3VoZDNNTFloR0oyN2FjNXQ1dmxORHhST0Vha2xwN0FZRDFONkl1Cm44cnh5L25hQm5tUmV4WXZjS2l6eVQwZklMRThrODBlMWR0OTlnSHFRbWxUV3dJREFRQUJveU13SVRBT0JnTlYKSFE4QkFmOEVCQU1DQWdRd0R3WURWUjBUQVFIL0JBVXdBd0VCL3pBTkJna3Foa2lHOXcwQkFRc0ZBQU9DQVFFQQpDVGZQL3c4SWVBL0dXT2RPa3lONHYzaE5qb2hJVU4rdnRvNFN6ZVFkZHhhS2hxVVJQUjB2YXlOZXlNWWNyZWI4Ck5DbDV0d1NwMzVRTWxwTjhITTEyWGlOUjhoUDdIbHQycUZrZkFiOXM2eU80SkdKeEFNNVFCNjkxY0Q2ZjZWNkQKUDg1M0NzT29lQ1JkUkNibmlzT05Jd0hON0ZpU3o3MUNUNVZzWUsyTXdna2xZUmxxdnpic3RmTmR3NFR6Vi9JVwpHQXU5NmlRZFlpRThXb3N0bVRaUmdyb1diRFM1YVBKVFVKZ01tdnVLbm1Ud0ZhV0E3UzRCNll3TE54S3NjRHFLCjQ5RlZOME4wSE1MSGNsTnlaS1VWMFZuZ3NQTVhrYW1kTXRYNTk3NkYzblVMWmpOVVplNTJQUThYd0RqdTg4NHMKY1B2SEppY1d2TE9IWFZHSzVneWNaQT09Ci0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0K"

        client_certificate_config {
            issue_client_certificate = false
        }
    }

    network_policy {
        enabled  = false
        provider = "PROVIDER_UNSPECIFIED"
    }
}

# google_container_node_pool.np:
resource "google_container_node_pool" "np" {
    cluster             = "k8s-cluster"
    id                  = "asia-east1-a/k8s-cluster/k8s-node-pool"
    initial_node_count  = 1
    instance_group_urls = [
        "https://www.googleapis.com/compute/v1/projects/upheld-garage-218509/zones/asia-east1-a/instanceGroupManagers/gke-k8s-cluster-k8s-node-pool-e6837464-grp",
    ]
    location            = "asia-east1-a"
    name                = "k8s-node-pool"
    node_count          = 1
    project             = "upheld-garage-218509"
    version             = "1.12.8-gke.10"
    zone                = "asia-east1-a"

    management {
        auto_repair  = false
        auto_upgrade = false
    }

    node_config {
        disk_size_gb      = 100
        disk_type         = "pd-standard"
        guest_accelerator = []
        image_type        = "COS"
        labels            = {}
        local_ssd_count   = 0
        machine_type      = "f1-micro"
        metadata          = {
            "disable-legacy-endpoints" = "true"
        }
        oauth_scopes      = [
            "https://www.googleapis.com/auth/logging.write",
            "https://www.googleapis.com/auth/monitoring",
        ]
        preemptible       = true
        service_account   = "default"
    }
}

# null_resource.kubeconfig:
resource "null_resource" "kubeconfig" {
    id = "5621880508203640741"
}
```


** Run destroy to destroy all the resources managed by Terraform
```bash
~/D/P/terraform> terraform destroy
google_container_cluster.k8_cluster: Refreshing state... [id=k8s-cluster]
google_container_node_pool.np: Refreshing state... [id=asia-east1-a/k8s-cluster/k8s-node-pool]
null_resource.kubeconfig: Refreshing state... [id=5621880508203640741]

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # google_container_cluster.k8_cluster will be destroyed
  - resource "google_container_cluster" "k8_cluster" {
      - additional_zones         = [] -> null
      - cluster_autoscaling      = [] -> null
      - cluster_ipv4_cidr        = "10.12.0.0/14" -> null
      - enable_kubernetes_alpha  = false -> null
      - enable_legacy_abac       = false -> null
      - endpoint                 = "35.185.148.69" -> null
      - id                       = "k8s-cluster" -> null
      - initial_node_count       = 1 -> null
      - instance_group_urls      = [
          - "https://www.googleapis.com/compute/v1/projects/upheld-garage-218509/zones/asia-east1-a/instanceGroups/gke-k8s-cluster-k8s-node-pool-e6837464-grp",
        ] -> null
      - ip_allocation_policy     = [] -> null
      - location                 = "asia-east1-a" -> null
      - logging_service          = "logging.googleapis.com" -> null
      - master_version           = "1.12.8-gke.10" -> null
      - monitoring_service       = "monitoring.googleapis.com" -> null
      - name                     = "k8s-cluster" -> null
      - network                  = "projects/upheld-garage-218509/global/networks/default" -> null
      - node_locations           = [] -> null
      - node_version             = "1.12.8-gke.10" -> null
      - project                  = "upheld-garage-218509" -> null
      - remove_default_node_pool = true -> null
      - resource_labels          = {} -> null
      - services_ipv4_cidr       = "10.15.240.0/20" -> null
      - subnetwork               = "projects/upheld-garage-218509/regions/asia-east1/subnetworks/default" -> null
      - zone                     = "asia-east1-a" -> null

      - addons_config {
          - horizontal_pod_autoscaling {
              - disabled = false -> null
            }

          - http_load_balancing {
              - disabled = false -> null
            }

          - kubernetes_dashboard {
              - disabled = true -> null
            }

          - network_policy_config {
              - disabled = true -> null
            }
        }

      - master_auth {
          - cluster_ca_certificate = "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURERENDQWZTZ0F3SUJBZ0lSQU1mdXlFK0RqVjhBS0c3WndXV1hEaXN3RFFZSktvWklodmNOQVFFTEJRQXcKTHpFdE1Dc0dBMVVFQXhNa016ZG1NalJrTnpFdE9URmpZUzAwTURVM0xXSXlZak10TkRBM05EYzRaVFkwTWpZNApNQjRYRFRFNU1EY3hOREV6TXpJME1Gb1hEVEkwTURjeE1qRTBNekkwTUZvd0x6RXRNQ3NHQTFVRUF4TWtNemRtCk1qUmtOekV0T1RGallTMDBNRFUzTFdJeVlqTXROREEzTkRjNFpUWTBNalk0TUlJQklqQU5CZ2txaGtpRzl3MEIKQVFFRkFBT0NBUThBTUlJQkNnS0NBUUVBaXVSSnh6WFhjTnU4N0lKQ2xuaXpmUUtWSHM5ZXVOaXN1c2NIMy9CSwpWWlEza0xUS3BsUllJdGFxZkJUaGYwNVpsU2ovQnFFcjhpempncDJRVFBIVGxXZTVzMDM3UlZXQ3JDaUxqd1ZzCk5OSVMrN1hsaWh3YWhPQTJjdDVEdDFJVENiaHFFQitrVkVWaUJ6Y0pTN3IyR2Z1b3Y3TDVtekJFL3JFUUliR2wKbHk2ZlYwd2NzOHV2aE9hWWVCY2FnMDdOQmk2NVRPVXJEUkt3aUxlWVNKaEQxbXR2dkhLdzJkSk5YRWdoUEVmdQpwUm5PRTZDTzRNdXpVZmdSYlBVZCt2aWYrS3VoZDNNTFloR0oyN2FjNXQ1dmxORHhST0Vha2xwN0FZRDFONkl1Cm44cnh5L25hQm5tUmV4WXZjS2l6eVQwZklMRThrODBlMWR0OTlnSHFRbWxUV3dJREFRQUJveU13SVRBT0JnTlYKSFE4QkFmOEVCQU1DQWdRd0R3WURWUjBUQVFIL0JBVXdBd0VCL3pBTkJna3Foa2lHOXcwQkFRc0ZBQU9DQVFFQQpDVGZQL3c4SWVBL0dXT2RPa3lONHYzaE5qb2hJVU4rdnRvNFN6ZVFkZHhhS2hxVVJQUjB2YXlOZXlNWWNyZWI4Ck5DbDV0d1NwMzVRTWxwTjhITTEyWGlOUjhoUDdIbHQycUZrZkFiOXM2eU80SkdKeEFNNVFCNjkxY0Q2ZjZWNkQKUDg1M0NzT29lQ1JkUkNibmlzT05Jd0hON0ZpU3o3MUNUNVZzWUsyTXdna2xZUmxxdnpic3RmTmR3NFR6Vi9JVwpHQXU5NmlRZFlpRThXb3N0bVRaUmdyb1diRFM1YVBKVFVKZ01tdnVLbm1Ud0ZhV0E3UzRCNll3TE54S3NjRHFLCjQ5RlZOME4wSE1MSGNsTnlaS1VWMFZuZ3NQTVhrYW1kTXRYNTk3NkYzblVMWmpOVVplNTJQUThYd0RqdTg4NHMKY1B2SEppY1d2TE9IWFZHSzVneWNaQT09Ci0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0K" -> null

          - client_certificate_config {
              - issue_client_certificate = false -> null
            }
        }

      - network_policy {
          - enabled  = false -> null
          - provider = "PROVIDER_UNSPECIFIED" -> null
        }

      - node_config {
          - disk_size_gb      = 100 -> null
          - disk_type         = "pd-standard" -> null
          - guest_accelerator = [] -> null
          - image_type        = "COS" -> null
          - labels            = {} -> null
          - local_ssd_count   = 0 -> null
          - machine_type      = "f1-micro" -> null
          - metadata          = {
              - "disable-legacy-endpoints" = "true"
            } -> null
          - oauth_scopes      = [
              - "https://www.googleapis.com/auth/logging.write",
              - "https://www.googleapis.com/auth/monitoring",
            ] -> null
          - preemptible       = true -> null
          - service_account   = "default" -> null
          - tags              = [] -> null
        }

      - node_pool {
          - initial_node_count  = 1 -> null
          - instance_group_urls = [
              - "https://www.googleapis.com/compute/v1/projects/upheld-garage-218509/zones/asia-east1-a/instanceGroupManagers/gke-k8s-cluster-k8s-node-pool-e6837464-grp",
            ] -> null
          - max_pods_per_node   = 0 -> null
          - name                = "k8s-node-pool" -> null
          - node_count          = 1 -> null
          - version             = "1.12.8-gke.10" -> null

          - management {
              - auto_repair  = false -> null
              - auto_upgrade = false -> null
            }

          - node_config {
              - disk_size_gb      = 100 -> null
              - disk_type         = "pd-standard" -> null
              - guest_accelerator = [] -> null
              - image_type        = "COS" -> null
              - labels            = {} -> null
              - local_ssd_count   = 0 -> null
              - machine_type      = "f1-micro" -> null
              - metadata          = {
                  - "disable-legacy-endpoints" = "true"
                } -> null
              - oauth_scopes      = [
                  - "https://www.googleapis.com/auth/logging.write",
                  - "https://www.googleapis.com/auth/monitoring",
                ] -> null
              - preemptible       = true -> null
              - service_account   = "default" -> null
              - tags              = [] -> null
            }
        }
    }

  # google_container_node_pool.np will be destroyed
  - resource "google_container_node_pool" "np" {
      - cluster             = "k8s-cluster" -> null
      - id                  = "asia-east1-a/k8s-cluster/k8s-node-pool" -> null
      - initial_node_count  = 1 -> null
      - instance_group_urls = [
          - "https://www.googleapis.com/compute/v1/projects/upheld-garage-218509/zones/asia-east1-a/instanceGroupManagers/gke-k8s-cluster-k8s-node-pool-e6837464-grp",
        ] -> null
      - location            = "asia-east1-a" -> null
      - name                = "k8s-node-pool" -> null
      - node_count          = 1 -> null
      - project             = "upheld-garage-218509" -> null
      - version             = "1.12.8-gke.10" -> null
      - zone                = "asia-east1-a" -> null

      - management {
          - auto_repair  = false -> null
          - auto_upgrade = false -> null
        }

      - node_config {
          - disk_size_gb      = 100 -> null
          - disk_type         = "pd-standard" -> null
          - guest_accelerator = [] -> null
          - image_type        = "COS" -> null
          - labels            = {} -> null
          - local_ssd_count   = 0 -> null
          - machine_type      = "f1-micro" -> null
          - metadata          = {
              - "disable-legacy-endpoints" = "true"
            } -> null
          - oauth_scopes      = [
              - "https://www.googleapis.com/auth/logging.write",
              - "https://www.googleapis.com/auth/monitoring",
            ] -> null
          - preemptible       = true -> null
          - service_account   = "default" -> null
          - tags              = [] -> null
        }
    }

  # null_resource.kubeconfig will be destroyed
  - resource "null_resource" "kubeconfig" {
      - id = "5621880508203640741" -> null
    }

Plan: 0 to add, 0 to change, 3 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

null_resource.kubeconfig: Destroying... [id=5621880508203640741]
null_resource.kubeconfig: Destruction complete after 0s
google_container_node_pool.np: Destroying... [id=asia-east1-a/k8s-cluster/k8s-node-pool]
google_container_node_pool.np: Still destroying... [id=asia-east1-a/k8s-cluster/k8s-node-pool, 10s elapsed]
google_container_node_pool.np: Still destroying... [id=asia-east1-a/k8s-cluster/k8s-node-pool, 20s elapsed]
google_container_node_pool.np: Still destroying... [id=asia-east1-a/k8s-cluster/k8s-node-pool, 30s elapsed]
google_container_node_pool.np: Still destroying... [id=asia-east1-a/k8s-cluster/k8s-node-pool, 40s elapsed]
google_container_node_pool.np: Still destroying... [id=asia-east1-a/k8s-cluster/k8s-node-pool, 50s elapsed]
google_container_node_pool.np: Still destroying... [id=asia-east1-a/k8s-cluster/k8s-node-pool, 1m0s elapsed]
google_container_node_pool.np: Still destroying... [id=asia-east1-a/k8s-cluster/k8s-node-pool, 1m10s elapsed]
google_container_node_pool.np: Still destroying... [id=asia-east1-a/k8s-cluster/k8s-node-pool, 1m20s elapsed]
google_container_node_pool.np: Still destroying... [id=asia-east1-a/k8s-cluster/k8s-node-pool, 1m30s elapsed]
google_container_node_pool.np: Still destroying... [id=asia-east1-a/k8s-cluster/k8s-node-pool, 1m40s elapsed]
google_container_node_pool.np: Destruction complete after 1m49s
google_container_cluster.k8_cluster: Destroying... [id=k8s-cluster]
google_container_cluster.k8_cluster: Still destroying... [id=k8s-cluster, 10s elapsed]
google_container_cluster.k8_cluster: Still destroying... [id=k8s-cluster, 20s elapsed]
google_container_cluster.k8_cluster: Still destroying... [id=k8s-cluster, 30s elapsed]
google_container_cluster.k8_cluster: Still destroying... [id=k8s-cluster, 40s elapsed]
google_container_cluster.k8_cluster: Still destroying... [id=k8s-cluster, 50s elapsed]
google_container_cluster.k8_cluster: Still destroying... [id=k8s-cluster, 1m0s elapsed]
google_container_cluster.k8_cluster: Still destroying... [id=k8s-cluster, 1m10s elapsed]
google_container_cluster.k8_cluster: Still destroying... [id=k8s-cluster, 1m20s elapsed]
google_container_cluster.k8_cluster: Still destroying... [id=k8s-cluster, 1m30s elapsed]
google_container_cluster.k8_cluster: Still destroying... [id=k8s-cluster, 1m40s elapsed]
google_container_cluster.k8_cluster: Still destroying... [id=k8s-cluster, 1m50s elapsed]
google_container_cluster.k8_cluster: Still destroying... [id=k8s-cluster, 2m0s elapsed]
google_container_cluster.k8_cluster: Still destroying... [id=k8s-cluster, 2m10s elapsed]
google_container_cluster.k8_cluster: Still destroying... [id=k8s-cluster, 2m20s elapsed]
google_container_cluster.k8_cluster: Still destroying... [id=k8s-cluster, 2m30s elapsed]
google_container_cluster.k8_cluster: Destruction complete after 2m40s

Destroy complete! Resources: 3 destroyed.
```


** Verify the destroy result
*** By Terraform
```bash
~/D/P/terraform> terraform show

```

*** By kubectl
```bash
~/D/P/terraform> kubectl get cs
error: the server doesnt have a resource type "cs"
```

*** By Helm
```bash
~/D/P/terraform> helm version
Client: &version.Version{SemVer:"v2.14.2", GitCommit:"a8b13cc5ab6a7dbef0a58f5061bcc7c0c61598e7", GitTreeState:"clean"}
Error: Get https://35.185.148.69/api/v1/namespaces/kube-system/pods?labelSelector=app%3Dhelm%2Cname%3Dtiller: net/http: TLS handshake timeout
```