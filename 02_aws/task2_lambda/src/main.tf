provider "aws" {
  region = "us-east-1"
}

resource "aws_lambda_function" "my_lambda" {
  filename         = "./function.zip"
  function_name    = "my_lambda_function"
  role             = aws_iam_role.lambda_exec.arn
  handler          = "app.handler"
  source_code_hash = filebase64sha256("./function.zip")
  runtime          = "python3.8"
}

resource "aws_iam_role" "lambda_exec" {
  name = "lambda_exec_role"

  assume_role_policy = jsonencode({
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
