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
  region     = var.instance_region
  profile = "default"
}

resource "aws_lambda_function" "my_lambda_1" {
#  filename         = "./function.zip"
  filename         = "./lambda_function_app2.zip"
#  function_name    = "my_lambda_function"
  function_name    = "my_lambda_function_app2"
  role             = aws_iam_role.lambda_exec.arn
#  role             = var.lambda_arn_role
#  handler          = "app.lambda_handler"
  handler          = "lambda_function.lambda_handler"
#  source_code_hash = filebase64sha256("./function.zip")
  source_code_hash = filebase64sha256("./lambda_function_app2.zip")
  runtime          = "python3.12"
}

resource "aws_iam_role" "lambda_exec" {
  name = "lambda_exec_role1"

  assume_role_policy = jsonencode({#resourde data data aws_iam_policy_document use
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole",
      Effect = "Allow",
      Sid    = "",
      Principal = {
        Service = "lambda.amazonaws.com"
      },
    }],
  })
}

resource "aws_iam_role_policy_attachment" "lambda_exec_policy" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}
