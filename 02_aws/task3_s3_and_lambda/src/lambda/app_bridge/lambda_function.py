import boto3
import json
import logging

# Initialize the S3 client
s3_client = boto3.client('s3')

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Log the incoming event for debugging purposes
    logger.info("Received event: %s", json.dumps(event, indent=2))

    # Check if the event is from EventBridge
    if 'source' in event and event['source'] == 'aws.s3':
        logger.info("Triggered by EventBridge event")

        # Specify the bucket name
        bucket_name = "aws-s3-bucket-for-snd-and-lambda-vbazh1"

        try:
            # List objects in the bucket and count them
            response = s3_client.list_objects_v2(Bucket=bucket_name)
            object_count = response.get('KeyCount', 0)

            # Log the number of objects in the bucket
            logger.info(f"Bucket {bucket_name} contains {object_count} objects.")
        except Exception as e:
            logger.error(f"Error counting objects in bucket {bucket_name}: {e}")
    else:
        logger.warning("Event was not triggered by EventBridge.")
