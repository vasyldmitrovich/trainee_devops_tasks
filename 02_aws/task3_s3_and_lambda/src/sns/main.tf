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

# Create s3 Bucket notification
resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = var.bucket_id

  topic {
    events = ["s3:ObjectCreated:*"]
    topic_arn = aws_sns_topic.topic_sns_run_lambda.arn
    filter_suffix = ".log"
  }
}