#https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/using_gke_with_terraform

##gke code 
resource "google_service_account" "gke-sa" {
  account_id   = "service-account-gke"
  display_name = "ServiceAccountGKE"
}

#public gke
resource "google_container_cluster" "primary_gke" {
  name               = "kubeflow-cluster"
  location           = "asia-southeast1"
  initial_node_count = 1
  remove_default_node_pool = true
  // node_config {
  //   # Google recommends custom service accounts that have cloud-platform scope and permissions granted via IAM Roles.
  //   service_account =  data.google_service_account.gke-sa.name
  //   #google_service_account.default.email
  //   // oauth_scopes = [
  //   //   "https://www.googleapis.com/auth/cloud-platform"
  //   // ]
  //   labels = {
  //     Name = "gke-k8s"
  //   }
  //   tags = ["k8s", "gke"]
  // }
  // timeouts {
  //   create = "30m"
  //   update = "40m"
  // }
  depends_on = [google_service_account.gke-sa,]
}


// resource "google_container_cluster" "primary" {
//   name     = google_container_cluster.primary_gke.name
//   location = google_container_cluster.primary_gke.location

//   # We can't create a cluster with no node pool defined, but we want to only use
//   # separately managed node pools. So we create the smallest possible default
//   # node pool and immediately delete it.
//   remove_default_node_pool = true
//   initial_node_count       = 1
// }

resource "google_container_node_pool" "primary_nodes" {
  name       = "my-node-pool"
  cluster    = google_container_cluster.primary_gke.id
  node_count = 1
  
  autoscaling {
    min_node_count = 1
    max_node_count = 8
  }

  node_config {
    preemptible  = true
    machine_type = "e2-medium"

    # Google recommends custom service accounts that have cloud-platform scope and permissions granted via IAM Roles.
    service_account = var.gke_service_user
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
  depends_on = [google_service_account.gke-sa,]
}
#gke module on cluster
