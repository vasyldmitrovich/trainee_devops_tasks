aws s3api create-bucket --bucket my-versioned-bucket-vbazh1989 --region us-east-1

# Include versioning
aws s3api put-bucket-versioning --bucket my-versioned-bucket-vbazh1989 --versioning-configuration Status=Enabled

# Add life lifecycle policy
aws s3api put-bucket-lifecycle-configuration --bucket my-versioned-bucket-vbazh1989 --lifecycle-configuration file://./02_aws/task1_s3bucket/src/s3/lifecyclepolicy.json

# Adding crypt AES256
aws s3api put-bucket-encryption --bucket my-versioned-bucket-vbazh1989 --server-side-encryption-configuration file://./02_aws/task1_s3bucket/src/s3/server_side_encryption.json

# Apload objects to bucket
aws s3api put-object --bucket my-versioned-bucket-vbazh1989 --key my_file1.txt --body C:\Users\vbazh\IdeaProjects\trainee_devops_tasks\02_aws\task1_s3bucket\src\files\file1.txt
aws s3api put-object --bucket my-versioned-bucket-vbazh1989 --key my_file2.txt --body C:\Users\vbazh\IdeaProjects\trainee_devops_tasks\02_aws\task1_s3bucket\src\files\file2.txt
aws s3api put-object --bucket my-versioned-bucket-vbazh1989 --key my_file3.txt --body C:\Users\vbazh\IdeaProjects\trainee_devops_tasks\02_aws\task1_s3bucket\src\files\file3.txt

# Create role and add policy to role
aws iam create-role --role-name MyS3AccessRole --assume-role-policy-document file://./02_aws/task1_s3bucket/src/role/trust-policy.json
aws iam put-role-policy --role-name MyS3AccessRole --policy-name S3AccessPolicy --policy-document file://./02_aws/task1_s3bucket/src/role/access-policy.json


# Config AWS CLI for assume role, add profile task1s3

# AFTER THAT run script to rename objects in bucket
chmod +x ./02_aws/task1_s3bucket/src/script.sh
./02_aws/task1_s3bucket/src/script.sh