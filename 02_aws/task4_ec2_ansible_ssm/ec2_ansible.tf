# Create key pair

# Generate a new SSH key pair
resource "tls_private_key" "example" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

# Create the key pair in AWS using the generated public key
resource "aws_key_pair" "deploy_by_ansible" {
  key_name   = var.ssh_key_name
  public_key = tls_private_key.example.public_key_openssh
}

# Save the private key to a file
resource "local_file" "private_key" {
  filename = "${path.module}/my_key_for_ansible.pem"
  content  = tls_private_key.example.private_key_pem
  file_permission = "0600" # Secure permissions for the private key
}

# Create instance
resource "aws_instance" "web_server" {
  ami           = var.instance_ami
  instance_type = var.instance_type
  key_name = aws_key_pair.deploy_by_ansible.key_name
  subnet_id = module.net.ec2_ansible_subnet_id # Subnet where the instance will be deployed
  vpc_security_group_ids = [aws_security_group.web_server_sg.id] # Attach the security group
  tags = {
    Name = "WebServer_Ansible"
  }
}

# Security Group for EC2 instance
resource "aws_security_group" "web_server_sg" {
  vpc_id = module.net.main_vpc_id

  dynamic "ingress" {
    for_each = var.sg_ports_for_internet
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      description = "Allow all request from anywhere"
      cidr_blocks = ["0.0.0.0/0"]
      ipv6_cidr_blocks = ["::/0"]
    }
  }

  egress {
    from_port = 0
    to_port   = 0
    protocol = "-1" # Allow all output traffic
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "WebServerSecurityGroup"
  }
}