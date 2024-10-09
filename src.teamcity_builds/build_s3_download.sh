#!/bin/bash

# Download JAR from S3
aws s3 cp s3://aws-s3-bucket-for-snd-and-lambda-vbazh1/calculator-service-0.0.1-SNAPSHOT.jar ./your-file.jar

# Check if the file was downloaded
if [ -f "./your-file.jar" ]; then
    echo "JAR downloaded successfully!"
else
    echo "Failed to download JAR from S3" >&2
    exit 1
fi
