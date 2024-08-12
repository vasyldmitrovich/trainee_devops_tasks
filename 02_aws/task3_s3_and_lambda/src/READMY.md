This terraform scenario

Create s3 bucket 
upload files to this bucket
and bucket make notification

sns triggered to bucket when in bucket uploaded .log file

sns call lambda function

which get object from bucket
rename name and put to s3 bucket.