output "s3_sns_lambda_role_arn" {
  value = aws_iam_role.s3_sns_lambda.arn
}

output "s3_lambda_role_arn" {
  value = aws_iam_role.lambda_role.arn
}