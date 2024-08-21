output "s3_sns_lambda_role_arn" {
  value = aws_iam_role.s3_sns_lambda.arn
}

output "s3_lambda_role_arn" {
  value = aws_iam_role.lambda_role.arn
}

output "lambda_basic_execution_arn" {
  value = aws_iam_role.lambda_basic_execution.arn
}

output "eventbridge_scheduler_role_arn" {
  value = aws_iam_role.eventbridge_scheduler_role.arn
}