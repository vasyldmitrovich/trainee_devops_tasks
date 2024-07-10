#!/bin/bash

# Parameters
BUCKET="my-versioned-bucket-vbazh1989"
PREFIX="new-prefix"

# Local temp directory
TEMP_DIR="./tmp/s3_objects"
mkdir -p "$TEMP_DIR"
echo $(pwd)

# Get list of all objects in bucket
OBJECTS=$(aws s3api list-objects --bucket "$BUCKET" --query 'Contents[].Key' --output text --profile task1s3)
echo "Objects in bucket: $OBJECTS"

# Go through all objects
for OBJECT in $OBJECTS; do
    # Download objects
    aws s3 cp "s3://$BUCKET/$OBJECT" "$TEMP_DIR/$OBJECT" --profile task1s3
    echo "Downloaded $OBJECT to $TEMP_DIR/$OBJECT"

    # Create random string
    RANDOM_STRING="_$(openssl rand -base64 12 | tr -dc 'a-zA-Z0-9')_"
    echo "Random string: $RANDOM_STRING"

    # Upload objects to S3
    aws s3 cp "$TEMP_DIR/$OBJECT" "s3://$BUCKET/$PREFIX$RANDOM_STRING$OBJECT" --profile task1s3
    echo "Uploaded $TEMP_DIR/$OBJECT to s3://$BUCKET/$PREFIX$RANDOM_STRING$OBJECT"

    # Delete local object
    rm "$TEMP_DIR/$OBJECT"
done

# Delete temporary directory
rmdir "$TEMP_DIR"
echo "Deleted temporary directory $TEMP_DIR"
