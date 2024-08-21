Using Terraform Workspaces to manage environments:

In your terminal:

Create and activate the workspace for test:

```bash

terraform workspace new test
terraform workspace select test
```
Apply the Terraform configuration:

```bash

terraform apply
```
Switch to prod and run the same commands:

```bash

terraform workspace new prod
terraform workspace select prod
terraform apply
```

Testing

API Gateway:
Run a GET request via Postman or curl to the appropriate API Gateway endpoint that calls the Lambda function.
Verify that the CloudWatch logs show the appropriate logging level (INFO or DEBUG) depending on the environment.