import json
import boto3
import random
import string
import urllib.parse

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        print("Received event: " + json.dumps(event, indent=2))

        # Retrieve the SNS message
        sns_message = record['Sns']['Message']

        try:
            # Parse the SNS message to extract the S3 event details
            s3_event = json.loads(sns_message)
            bucket_name = s3_event['Records'][0]['s3']['bucket']['name']
            object_key = s3_event['Records'][0]['s3']['object']['key']

            # Decode the object key to handle special characters
            object_key = urllib.parse.unquote_plus(object_key)

            print(f"Bucket Name: {bucket_name}")
            print(f"Object Key: {object_key}")

            download_path = f"/tmp/{object_key.split('/')[-1]}"

            # Download the file from S3
            s3_client.download_file(bucket_name, object_key, download_path)

            # Generate a new key with a random suffix
            random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            new_object_key = f"{object_key.split('.')[0]}_{random_suffix}.log_txt"

            # Upload the file back to S3 with the new name
            s3_client.upload_file(download_path, bucket_name, new_object_key)

            print(f"File {object_key} from {bucket_name} was renamed to {new_object_key} and uploaded back to S3.")

        except json.JSONDecodeError:
            print(f"Unable to parse SNS message: {sns_message}")
        except s3_client.exceptions.ClientError as e:
            if e.response['Error']['Code'] == '404':
                print(f"Object not found in S3: {object_key}")
            else:
                print(f"S3 ClientError: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
