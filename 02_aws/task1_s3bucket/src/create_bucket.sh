#!/bin/bash

BUCKET_NAME="my-versioned-bucket-vbazh1989-v3"
ROLE_NAME="MyS3AccessRole"
POLICY_NAME="S3AccessPolicy"
PROFILE_NAME="task1s3"

# Create bucket
aws s3api create-bucket --bucket $BUCKET_NAME --region us-east-1

# Include versioning
aws s3api put-bucket-versioning --bucket $BUCKET_NAME --versioning-configuration Status=Enabled

# Add life lifecycle policy
aws s3api put-bucket-lifecycle-configuration --bucket $BUCKET_NAME --lifecycle-configuration file://./s3/lifecycle-policy.json

# Adding crypt AES256
aws s3api put-bucket-encryption --bucket $BUCKET_NAME --server-side-encryption-configuration file://./s3/server-side-encryption.json

# Add access to role
aws s3api put-bucket-policy --bucket $BUCKET_NAME --policy file://./s3/bucket-policy.json

# Upload objects to bucket
aws s3api put-object --bucket $BUCKET_NAME --key my_file1.txt --body "$(pwd)/files/file1.txt"
aws s3api put-object --bucket $BUCKET_NAME --key my_file2.txt --body "$(pwd)/files/file2.txt"
aws s3api put-object --bucket $BUCKET_NAME --key my_file3.txt --body "$(pwd)/files/file3.txt"

# Create role and add policy to role
aws iam create-role --role-name $ROLE_NAME --assume-role-policy-document file://./role/trust-policy.json
aws iam put-role-policy --role-name $ROLE_NAME --policy-name $POLICY_NAME --policy-document file://./role/access-policy.json

# Config AWS CLI for assume role, add profile task1s3

# Wait for 3 minutes
#echo "Waiting for 15 sec..."
#sleep 30

# AFTER THAT run script to rename objects in bucket
./script.sh $BUCKET_NAME $PROFILE_NAME