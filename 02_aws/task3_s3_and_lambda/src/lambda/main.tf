resource "aws_lambda_function" "lambda" {
  filename         = "${path.module}/lambda_function_app2.zip"
  function_name    = "lambda_function_app2"
  role             = var.s3_sns_lambda_role_arn
  handler          = "lambda_function.lambda_handler"
  runtime          = "python3.12"
  source_code_hash = filebase64sha256("${path.module}/lambda_function_app2.zip")

}

resource "aws_lambda_permission" "with_sns" {
  statement_id = "AllowExecutionFromSNS"
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda.arn
  principal = "sns.amazonaws.com"
  source_arn = var.sns_topic_arn
}
