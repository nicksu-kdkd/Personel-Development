variable "location" {
  type = string
  description = "The location of the node pool"
  default = "asia-east1-a"
}

variable "node_pool_name" {
  type = string
  description = "The name of the node pool"
  default = "k8s-node-pool"
}

variable "node_number" {
  type = number
  description = "How manay nodes inside the node pool"
  default = 1
}

variable "machine_type" {
  type = string
  description = "The machine_type of the nodes vm"
  default = "f1-micro"
}

variable "preemptible" {
  type = bool
  description = "Whether the nodes vm can be preemptive"
  default = true
}