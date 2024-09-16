# Get the Assume Role Policy JSON for SSM
data "aws_iam_policy_document" "ssm_assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
  }
}

# Create an IAM Role for SSM
resource "aws_iam_role" "ssm_role" {
  name               = "ssmAutomationRole"
  assume_role_policy = data.aws_iam_policy_document.ssm_assume_role_policy.json
}

# Use a data resource to get the ARN of the AmazonSSMFullAccess policy
data "aws_iam_policy" "ssm_full_access" {
  arn = "arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforSSM"
}

# Attach the AmazonSSMFullAccess policy to the role
resource "aws_iam_role_policy_attachment" "ssm_role_policy" {
  role       = aws_iam_role.ssm_role.name
  policy_arn = data.aws_iam_policy.ssm_full_access.arn
}

data "aws_iam_policy" "ssm_full_access1" {
  arn = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
}
# Attach the AmazonSSMFullAccess policy to the role
resource "aws_iam_role_policy_attachment" "ssm_role_policy1" {
  role       = aws_iam_role.ssm_role.name
  policy_arn = data.aws_iam_policy.ssm_full_access1.arn
}

resource "aws_iam_instance_profile" "ssm_instance_profile" {
  name = "SSMInstanceProfile"
  role = aws_iam_role.ssm_role.name
}

# Read JSON file content
data "local_file" "ssm_document_json" {
  filename = "${path.module}/config_instance/ssm_document.json"
}

# Create an SSM Document
resource "aws_ssm_document" "run_script" {
  name    = "RunScript"
  document_type = "Command"  # For AWS-RunShellScript type documents
  content = data.local_file.ssm_document_json.content
}

# Associate the SSM Document with the EC2 instance
resource "aws_ssm_association" "example" {
  name = aws_ssm_document.run_script.name
#  name = aws_ssm_document.example.name

  targets {
    key = "InstanceIds"
    values = [aws_instance.web_server.id]
  }
}
