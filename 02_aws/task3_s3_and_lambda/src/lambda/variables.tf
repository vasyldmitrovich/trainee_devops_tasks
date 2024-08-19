variable "s3_sns_lambda_role_arn" {}

variable "sns_topic_arn" {}

variable "bucket_arn" {}

variable "s3_lambda_role_arn" {}

variable "lambda_basic_execution_arn" {}

variable "log_level" {
  type    = string
  default = "INFO"
}