#!/bin/bash

# Parameters
BUCKET="my-versioned-bucket-vbazh1989"
PREFIX="new-prefix/"

# Local temp directory
TEMP_DIR="./tmp/s3_objects"
mkdir -p "$TEMP_DIR"

# Get list of all object in bucket
OBJECTS=$(aws s3api list-objects --bucket "$BUCKET" --query 'Contents[].Key' --output text --profile task1s3)

# Go throws all objects
for OBJECT in $OBJECTS; do
    # Download objects
    aws s3 cp "s3://$BUCKET/$OBJECT" "$TEMP_DIR/$OBJECT" --profile task1s3

    # Rename
    echo "Random string: $(openssl rand -base64 12)" >> "$TEMP_DIR/$OBJECT"

    # Upload objects to S3
    aws s3 cp "$TEMP_DIR/$OBJECT" "s3://$BUCKET/$PREFIX$OBJECT" --profile task1s3

    # Delete local object
    rm "$TEMP_DIR/$OBJECT"
done

# Delete temporary directory
rmdir "$TEMP_DIR"

