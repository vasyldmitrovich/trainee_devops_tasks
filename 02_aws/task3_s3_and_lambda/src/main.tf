terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  required_version = ">= 1.5.0, < 2.0.0"
}

provider "aws" {
  region  = var.INSTANCE_REGION
  profile = "default"
}

module "lambda" {
  source                 = "./lambda/"
  s3_sns_lambda_role_arn = module.role.s3_sns_lambda_role_arn
  sns_topic_arn          = module.sns.sns_topic_arn
}

module "role" {
  source                    = "./role/"
  s3_for_sns_and_lambda_arn = module.s3.s3_for_sns_and_lambda_arn
  s3_for_sns_and_lambda_id  = module.s3.s3_for_sns_and_lambda_id
  #TODO: Add role name for creating any another role
  #FIXME: need fix this thing
}

module "s3" {
  source        = "./s3/"
  sns_topic_arn = module.sns.sns_topic_arn
}

module "sns" {
  source     = "./sns/"
  bucket_id  = module.s3.s3_for_sns_and_lambda_id
  bucket_arn = module.s3.s3_for_sns_and_lambda_arn
  lambda_arn = module.lambda.lambda_arn
}



