terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  required_version = ">= 1.5"
}

provider "aws" {
  region  = var.AWS_REGION
  profile = "default"
}

module "net" {
  source          = "./net/"
  availability_zone = var.availability_zone

}


