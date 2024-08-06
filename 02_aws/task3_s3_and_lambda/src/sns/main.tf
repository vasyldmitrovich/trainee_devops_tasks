# Policy
data "aws_iam_policy_document" "topic" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["s3.amazonaws.com"]
    }

    actions   = ["SNS:Publish"]
    resources = ["arn:aws:sns:*:*:s3-event-notification-topic"]

    condition {
      test     = "ArnLike"
      variable = "aws:SourceArn"
      values   = [var.bucket_arn]
    }
  }
}

# Create SNS topic
resource "aws_sns_topic" "topic_sns_run_lambda" {
  name   = "s3-event-notification-topic"
  policy = data.aws_iam_policy_document.topic.json
}

resource "aws_sns_topic_subscription" "topic_lambda" {
  endpoint = aws_lambda_function.lambda.arn
  protocol = "lambda"
  topic_arn = aws_sns_topic.topic_sns_run_lambda.arn
}

resource "aws_lambda_function" "lambda" {
  filename         = "./lambda_function_app2.zip"
  function_name    = "lambda_function_app2"
  role             = var.s3_sns_lambda_role_arn
  handler          = "lambda_function.lambda_handler"
  runtime          = "python3.12"
  source_code_hash = filebase64sha256("./lambda_function_app2.zip")

}

resource "aws_lambda_permission" "with_sns" {
  statement_id = "AllowExecutionFromSNS"
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda.arn
  principal = "sns.amazonaws.com"
  source_arn = aws_sns_topic.topic_sns_run_lambda.arn
}
