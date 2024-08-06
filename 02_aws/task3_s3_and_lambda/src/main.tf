terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  required_version = ">= 1.2.0"
}

provider "aws" {
  region     = var.INSTANCE_REGION
  profile = "default"
}

module "lambda" {
  source = "./lambda/"
  s3_sns_lambda_role_arn = module.role.s3_sns_lambda_role_arn
  sns_topic_arn = module.sns.sns_topic_arn
}

module "role" {
  source = "./role/"
}

module "s3" {
  source = "./s3/"
  sns_topic_art = module.sns.sns_topic_arn
}

module "sns" {
  source = "./sns/"
  bucket_id = module.s3.s3_for_sns_and_lambda_id
  bucket_arn = module.s3.s3_for_sns_and_lambda_arn
}



