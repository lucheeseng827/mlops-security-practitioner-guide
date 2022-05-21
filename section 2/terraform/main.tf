
terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "3.90.0"
    }
  }

  backend "local" {
    hostname     = "app.terraform.io"
    organization = "xxxx"

    workspaces {
      name = "gke-xxxx"
    }
  }
}

provider "google" {
  project     = var.project_id
  region      = var.gcp_region
}

#GOOGLE_CREDENTIALS