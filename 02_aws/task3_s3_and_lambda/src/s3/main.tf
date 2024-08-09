# Create s3 Bucket
resource "aws_s3_bucket" "bucket_for_sns_and_lambda" {
  bucket = "aws-s3-bucket-for-snd-and-lambda-vbazh"
}

# Upload files to s3 Bucket
resource "aws_s3_object" "provision_source_files" {
  bucket = aws_s3_bucket.bucket_for_sns_and_lambda.id
  for_each = fileset("${path.module}/data_for_s3/", "*")
  key    = each.value
  source = "${path.module}/data_for_s3/${each.value}"
  etag = filemd5("${path.module}/data_for_s3/${each.value}")
}

# Create s3 Bucket notification
resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = aws_s3_bucket.bucket_for_sns_and_lambda.id

  topic {
    events = ["s3:ObjectCreated:*"]
    topic_arn     = var.sns_topic_art
    filter_suffix = ".log"
  }
}