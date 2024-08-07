# Policy for topic for using s3 notification
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

# Add subscription to run lambda function
resource "aws_sns_topic_subscription" "topic_lambda" {
  endpoint = var.lambda_arn
  protocol = "lambda"
  topic_arn = aws_sns_topic.topic_sns_run_lambda.arn
}
