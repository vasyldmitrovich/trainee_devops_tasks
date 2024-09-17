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
  filename        = "${path.module}/my_key_for_ansible.pem"
  content         = tls_private_key.example.private_key_pem
  file_permission = "0600" # Secure permissions for the private key
}

# Create instance
resource "aws_instance" "web_server" {
  ami                  = var.instance_ami
  instance_type        = var.instance_type
  key_name             = aws_key_pair.deploy_by_ansible.key_name
  subnet_id = module.net.ec2_ansible_subnet_id # Subnet where the instance will be deployed
  vpc_security_group_ids = [aws_security_group.web_server_sg.id] # Attach the security group
  iam_instance_profile = aws_iam_instance_profile.ssm_instance_profile.name

  tags = {
    Name = "WebServer_Ansible"
  }
}

# Security Group for EC2 instance
resource "aws_security_group" "web_server_sg" {
  vpc_id = module.net.main_vpc_id

  tags = {
    Name = "WebServerSecurityGroup"
  }
}

# Ingress rules for the security group
resource "aws_security_group_rule" "web_server_sg_ingress" {
  for_each = toset([for port in var.sg_ports_for_internet : tostring(port)])

  type              = "ingress"
  from_port         = each.value
  to_port           = each.value
  protocol          = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
  ipv6_cidr_blocks = ["::/0"]
  security_group_id = aws_security_group.web_server_sg.id
}

# Egress rule for the security group
resource "aws_security_group_rule" "web_server_sg_egress" {
  type              = "egress"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  cidr_blocks = ["0.0.0.0/0"]
  security_group_id = aws_security_group.web_server_sg.id
}

# # Run Ansible playbook after instance is ready
# resource "null_resource" "provision_ansible" {
#   depends_on = [aws_instance.web_server, local_file.private_key]
#
#   provisioner "local-exec" {
#     command = "./run_ansible_with_ssh_check.sh ${aws_instance.web_server.public_ip} ${local_file.private_key.filename}"
#   }
# }

# --- More interesting playbook ---

# Create instance
resource "aws_instance" "web_server2" {
  ami           = var.instance_ami
  instance_type = var.instance_type
  key_name      = aws_key_pair.deploy_by_ansible.key_name
  subnet_id = module.net.ec2_ansible_subnet_id # Subnet where the instance will be deployed
  vpc_security_group_ids = [aws_security_group.web_server_sg.id] # Attach the security group

  tags = {
    Name = "WebServer_Ansible2"
  }
}

# # Run Ansible playbook after instance is ready
# resource "null_resource" "provision_ansible2" {
#   depends_on = [
#     aws_instance.web_server, aws_instance.web_server2, local_file.private_key, null_resource.provision_ansible
#   ]
#
#   provisioner "local-exec" {
#     command = <<EOT
#       ./task4_1_build_inventory_file.sh ${aws_instance.web_server.public_ip} ${aws_instance.web_server2.public_ip} ${local_file.private_key.filename}
#       ansible-playbook -i task4_1_ec2_inventory.ini -e 'ansible_ssh_common_args="-o StrictHostKeyChecking=no"' task4_1_playbook.yml
#     EOT
#   }
# }

# Create EBS volume
resource "aws_ebs_volume" "web_server_volume" {
  availability_zone = aws_instance.web_server.availability_zone
  size              = 10  # Size of volume GB
  tags = {
    Name = "web-server-volume"
  }
}

# Attach EBS volume to EC2 instance
resource "aws_volume_attachment" "web_server_attachment" {
  device_name = "/dev/xvdf"  # or another free device, for example "/dev/sdh"
  volume_id   = aws_ebs_volume.web_server_volume.id
  instance_id = aws_instance.web_server.id
  force_detach = true  # If you want turn off in case conflict
}