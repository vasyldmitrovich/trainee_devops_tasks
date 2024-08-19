# First lambda triggered by SNS
resource "aws_lambda_function" "lambda" {
  filename      = "${path.module}/app/lambda_function_app.zip"
  function_name = "lambda_function_app"
  role          = var.s3_sns_lambda_role_arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.12"
  source_code_hash = filebase64sha256("${path.module}/app/lambda_function_app.zip")
}

resource "aws_lambda_permission" "with_sns" {
  statement_id  = "AllowExecutionFromSNS"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda.arn
  principal     = "sns.amazonaws.com"
  source_arn    = var.sns_topic_arn
}

# ----------   ----------

#Second lambda triggered by s3
resource "aws_lambda_function" "lambda_bridge" {
  filename      = "${path.module}/app_bridge/lambda_function_app_bridge.zip"
  function_name = "lambda_function_app_bridge"
  role          = var.s3_lambda_role_arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.12"
  source_code_hash = filebase64sha256("${path.module}/app_bridge/lambda_function_app_bridge.zip")
}

resource "aws_lambda_permission" "with_s3_lambda_bridge" {
  statement_id  = "AllowExecutionFromS3"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_bridge.arn
  principal     = "s3.amazonaws.com"
  source_arn    = var.bucket_arn
}

# ----------   ----------

# Third lambda getting parameter and do Debar of Info log
resource "aws_lambda_function" "lambda_logger" {
  function_name = "lambda_function_app_logger"
  role          = var.lambda_basic_execution_arn
  filename = "${path.module}/app_versioning_alias/lambda_function_app_logger.zip"
  handler = "lambda_function.lambda_handler"
  runtime = "python3.12"
  source_code_hash = filebase64sha256("${path.module}/app_versioning_alias/lambda_function_app_logger.zip")

  environment {
    variables = {
      LOG_LEVEL = var.log_level
    }
  }
}