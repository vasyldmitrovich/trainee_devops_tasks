output "s3_for_sns_and_lambda_id" {
  description = "S3 bucket for using in sns and lambda"
  value = aws_s3_bucket.bucket_for_sns_and_lambda.id
}

output "s3_for_sns_and_lambda_arn" {
  value = aws_s3_bucket.bucket_for_sns_and_lambda.arn
}