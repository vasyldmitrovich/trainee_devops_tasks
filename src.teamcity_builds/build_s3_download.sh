#!/bin/bash

# Download JAR from S3
aws s3api get-object --bucket aws-s3-bucket-for-snd-and-lambda-vbazh1 --key calculator-service-0.0.1-SNAPSHOT.jar
# Check if the file was downloaded
if [ -f "./your-file.jar" ]; then
    echo "JAR downloaded successfully!"
else
    echo "Failed to download JAR from S3" >&2
    exit 1
fi
