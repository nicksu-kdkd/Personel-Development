variable "helm_address" {
  type = string
  description = "The download link of helm binary"
  default = "https://get.helm.sh"
}

variable "helm_pkg" {
  type = string
  description = "The name of the helm pkg to download"
  default = "helm-v2.14.2-darwin-amd64.tar.gz"
}

variable "helm_user" {
  type = string
  description = "The user to own the helm service"
  default = "tiller"
}
