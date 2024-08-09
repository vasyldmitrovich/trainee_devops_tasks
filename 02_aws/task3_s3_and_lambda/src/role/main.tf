# Create the IAM role with the assume role policy
resource "aws_iam_role" "s3_sns_lambda" {
  name = "s3_sns_lambda_role"

  assume_role_policy = data.aws_iam_policy_document.s3_sns_lambda_role_policy.json
}

# Define the IAM policy document using the data source
data "aws_iam_policy_document" "s3_sns_lambda_role_policy" {
  statement {
    actions   = ["sts:AssumeRole"]
    effect    = "Allow"
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

# Attach the AWS managed policy to the IAM role
resource "aws_iam_role_policy_attachment" "lambda_exec_policy" {
  role       = aws_iam_role.s3_sns_lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Need add to this role permission get object from s3 and put object in s3