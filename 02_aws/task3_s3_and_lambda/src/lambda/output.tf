output "lambda_arn" {
  value = aws_lambda_function.lambda.arn
}

output "lambda_bridge_arn" {
  value = aws_lambda_function.lambda_bridge.arn
}