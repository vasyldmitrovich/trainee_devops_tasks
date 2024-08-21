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

# ----------  When in s3 add file lambda run, change name of file and put new file in s3  ----------

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

# Create an EventBridge Schedule that triggers every 15 minutes using cron expression
resource "aws_scheduler_schedule" "every_15_minutes_schedule" {
  name        = "every-15-minutes-schedule"
  schedule_expression = "cron(0/15 * * * ? *)"  # This cron expression represents every 15 minutes

  # Define the target Lambda function
  target {
    arn = aws_lambda_function.lambda_bridge.arn
    role_arn = var.eventbridge_scheduler_role_arn  # Role to allow EventBridge to invoke the Lambda function

    # Optional: Input to the Lambda function
    input = jsonencode({
      "source" = "aws.events",
      "detail-type" = "Scheduled Event"
    })
  }

  # Define time zone (optional)
  flexible_time_window {
    mode = "OFF"  # No flexible time window, triggers exactly every 15 minutes
  }
}

# Grant permission for EventBridge Scheduler to invoke the Lambda function
resource "aws_lambda_permission" "allow_eventbridge_lambda_bridge" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_bridge.arn
  principal     = "scheduler.amazonaws.com"
  source_arn    = aws_scheduler_schedule.every_15_minutes_schedule.arn
}



# ----------  Get parameter from event or env variable  ----------

# Third lambda getting parameter and do Debug of Info log
resource "aws_lambda_function" "lambda_logger" {
  function_name = "lambda_function_app_logger"
  role          = var.lambda_basic_execution_arn
  filename      = "${path.module}/app_versioning_alias/lambda_function_app_logger.zip"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.12"
  source_code_hash = filebase64sha256("${path.module}/app_versioning_alias/lambda_function_app_logger.zip")

  environment {
    variables = {
      LOG_LEVEL = var.log_level
    }
  }
}

# ----------  Use aliases in lambda  ----------

resource "aws_lambda_function" "lambda_logger_workspaces" {
  function_name = "lambda_function_app_versioning_workspaces"#Add parametrization of resources not hardcode
  role          = var.lambda_basic_execution_arn
  filename      = "${path.module}/app_versioning_workspaces/lambda_function_app_versioning_workspaces.zip"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.12"
  source_code_hash = filebase64sha256("${path.module}/app_versioning_workspaces/lambda_function_app_versioning_workspaces.zip")
  publish       = true

  # Log level depend from workspace
  environment {
    variables = {
      LOG_LEVEL = terraform.workspace == "test" ? "DEBUG" : "INFO"
    }
  }
}

# Alias for dev, pointing to the latest version
resource "aws_lambda_alias" "dev_alias" {
  name             = "dev"
  function_name    = aws_lambda_function.lambda_logger_workspaces.arn
  function_version = "$LATEST"  # LATEST version
}

# Alias for prod, pointing to first version
resource "aws_lambda_alias" "prod_alias" {
  name             = "prod"
  function_name    = aws_lambda_function.lambda_logger_workspaces.arn
  function_version = "1"  # Use a specific version number here
}



# Use s3 notification unless gateway

# # Define the API Gateway REST API
# resource "aws_api_gateway_rest_api" "api" {
#   name = "my_api"
# }
#
# # Define the API Gateway resource for the "latest" alias of the Lambda function
# resource "aws_api_gateway_resource" "resource_latest" {
#   rest_api_id = aws_api_gateway_rest_api.api.id
#   parent_id   = aws_api_gateway_rest_api.api.root_resource_id
#   path_part   = "latest"
# }
#
# # Define the API Gateway resource for the "v1" version of the Lambda function
# resource "aws_api_gateway_resource" "resource_v1" {
#   rest_api_id = aws_api_gateway_rest_api.api.id
#   parent_id   = aws_api_gateway_rest_api.api.root_resource_id
#   path_part   = "v1"
# }
#
# # Create a GET method for the "latest" resource
# resource "aws_api_gateway_method" "get_method_latest" {
#   rest_api_id   = aws_api_gateway_rest_api.api.id
#   resource_id   = aws_api_gateway_resource.resource_latest.id
#   http_method   = "GET"
#   authorization = "NONE"
# }
#
# # Create a GET method for the "v1" resource
# resource "aws_api_gateway_method" "get_method_v1" {
#   rest_api_id   = aws_api_gateway_rest_api.api.id
#   resource_id   = aws_api_gateway_resource.resource_v1.id
#   http_method   = "GET"
#   authorization = "NONE"
# }
#
# # Integrate the "latest" Lambda alias with the API Gateway for the "latest" resource
# resource "aws_api_gateway_integration" "lambda_integration_latest" {
#   rest_api_id             = aws_api_gateway_rest_api.api.id
#   resource_id             = aws_api_gateway_resource.resource_latest.id
#   http_method             = aws_api_gateway_method.get_method_latest.http_method
#   integration_http_method = "POST"
#   type                    = "AWS_PROXY"
#   uri                     = "arn:aws:apigateway:${var.INSTANCE_REGION}:lambda:path/2015-03-31/functions/${aws_lambda_alias.dev_alias.arn}/invocations"
# }
#
# # Integrate the "v1" Lambda version with the API Gateway for the "v1" resource
# resource "aws_api_gateway_integration" "lambda_integration_v1" {
#   rest_api_id             = aws_api_gateway_rest_api.api.id
#   resource_id             = aws_api_gateway_resource.resource_v1.id
#   http_method             = aws_api_gateway_method.get_method_v1.http_method
#   integration_http_method = "POST"
#   type                    = "AWS_PROXY"
#   uri                     = "arn:aws:apigateway:${var.INSTANCE_REGION}:lambda:path/2015-03-31/functions/${aws_lambda_function.lambda_logger_workspaces.arn}:1/invocations"
# }
#
# # Grant API Gateway permission to invoke the "latest" Lambda alias
# resource "aws_lambda_permission" "api_gateway_permission_latest" {
#   statement_id  = "AllowAPIGatewayInvokeLatest"
#   action        = "lambda:InvokeFunction"
#   function_name = aws_lambda_function.lambda_logger_workspaces.function_name
#   principal     = "apigateway.amazonaws.com"
#   source_arn    = "${aws_api_gateway_rest_api.api.execution_arn}/*/latest"
# }
#
# # Grant API Gateway permission to invoke the "v1" Lambda version
# resource "aws_lambda_permission" "api_gateway_permission_v1" {
#   statement_id  = "AllowAPIGatewayInvokeV1"
#   action        = "lambda:InvokeFunction"
#   function_name = aws_lambda_function.lambda_logger_workspaces.function_name
#   principal     = "apigateway.amazonaws.com"
#   source_arn    = "${aws_api_gateway_rest_api.api.execution_arn}/*/v1"
# }
#
# # Define a deployment for the API Gateway - Production
# resource "aws_api_gateway_deployment" "api_deployment_prod" {
#   rest_api_id = aws_api_gateway_rest_api.api.id
#   stage_name  = "prod"
#
#   depends_on = [
#     aws_api_gateway_integration.lambda_integration_latest,
#     aws_api_gateway_integration.lambda_integration_v1,
#     aws_api_gateway_method.get_method_latest,
#     aws_api_gateway_method.get_method_v1,
#   ]
# }
#
# # Define a deployment for the API Gateway - Test
# resource "aws_api_gateway_deployment" "api_deployment_test" {
#   rest_api_id = aws_api_gateway_rest_api.api.id
#   stage_name  = "test"
#
#   depends_on = [
#     aws_api_gateway_integration.lambda_integration_latest,
#     aws_api_gateway_integration.lambda_integration_v1,
#     aws_api_gateway_method.get_method_latest,
#     aws_api_gateway_method.get_method_v1,
#   ]
# }
#
# # Define a stage for the API Gateway - Production
# resource "aws_api_gateway_stage" "api_stage_prod" {
#   stage_name    = "prod"
#   rest_api_id   = aws_api_gateway_rest_api.api.id
#   deployment_id = aws_api_gateway_deployment.api_deployment_prod.id
# }
#
# # Define a stage for the API Gateway - Test
# resource "aws_api_gateway_stage" "api_stage_test" {
#   stage_name    = "test"
#   rest_api_id   = aws_api_gateway_rest_api.api.id
#   deployment_id = aws_api_gateway_deployment.api_deployment_test.id
# }