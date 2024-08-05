//resource "aws_iam_role" "lambda_exec" {
//  name = "lambda_exec_role1"
//
//  assume_role_policy = jsonencode({#resourde data data aws_iam_policy_document use
//    Version = "2012-10-17",
//    Statement = [{
//      Action = "sts:AssumeRole",
//      Effect = "Allow",
//      Sid    = "",
//      Principal = {
//        Service = "lambda.amazonaws.com"
//      },
//    }],
//  })
//}

//resource "aws_iam_role_policy_attachment" "lambda_exec_policy" {
//  role       = aws_iam_role.lambda_exec.name
//  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
//}

data "aws_iam_policy_document" "s3_sns_lambda" {
  statement {
    effect = "Allow"
  }
}