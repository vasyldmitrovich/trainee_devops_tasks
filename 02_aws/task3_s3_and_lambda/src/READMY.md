This terraform scenario have some tasks

__Lavbda which triggered to sns__
Create s3 bucket 
upload files to this bucket
and bucket make notification

sns triggered to bucket when in bucket uploaded .log file

sns call lambda function

which get object from bucket
rename name and put to s3 bucket

__Lambda which triggered to s3 and event bridge__

__Lambda with different version__

Vars in terraform<br>
<img src="/02_aws/task3_s3_and_lambda/src/vars_in_terraform.png" style="width: 600px; height: 350px;"><br>