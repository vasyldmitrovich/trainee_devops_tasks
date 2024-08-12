# Create the IAM role with the assume role policy
resource "aws_iam_role" "s3_sns_lambda" {
  name = "s3_sns_lambda_role1"
  assume_role_policy = data.aws_iam_policy_document.s3_sns_lambda_role_policy.json
}

# Define the IAM policy document using the data source
data "aws_iam_policy_document" "s3_sns_lambda_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]
    effect = "Allow"
    principals {
      type = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

# Attach the AWS managed policy to the IAM role
resource "aws_iam_role_policy_attachment" "lambda_exec_policy" {
  role       = aws_iam_role.s3_sns_lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Policy to allow S3 read/write access
resource "aws_iam_policy" "lambda_s3_access" {
  name        = "lambda_s3_access_policy"
  description = "Policy to allow Lambda function to read and write to the specific S3 bucket"

  policy = data.aws_iam_policy_document.policy_for_s3_from_lambda.json
}

data "aws_iam_policy_document" "policy_for_s3_from_lambda" {
  statement {
    effect = "Allow"

    actions = [
      "s3:GetObject",
      "s3:PutObject",
      "s3:ListBucket"
    ]

    resources = [
      var.s3_for_sns_and_lambda_arn,
      "${var.s3_for_sns_and_lambda_arn}/*"
    ]
  }
}

# Attach the policy to the lambda role
resource "aws_iam_role_policy_attachment" "lambda_s3_access_attachment" {
  policy_arn = aws_iam_policy.lambda_s3_access.arn
  role       = aws_iam_role.s3_sns_lambda.name
}

#Apply the bucket policy
resource "aws_s3_bucket_policy" "bucket_policy" {
  bucket = var.s3_for_sns_and_lambda_id
  policy = data.aws_iam_policy_document.bucket_policy.json
}

data "aws_iam_policy_document" "bucket_policy" {
  statement {
    effect    = "Allow"
    actions   = ["s3:GetObject", "s3:PutObject", "s3:ListBucket"]
    resources = [
      var.s3_for_sns_and_lambda_arn,                # Permission to list the bucket
      "${var.s3_for_sns_and_lambda_arn}/*"          # Permission to access objects in the bucket
    ]
    principals {
      type        = "AWS"
      identifiers = [aws_iam_role.s3_sns_lambda.arn]
    }
  }
}

