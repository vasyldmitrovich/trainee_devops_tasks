# Create Network

# Create VPC
resource "aws_vpc" "main_vpc" {
  cidr_block = "10.0.0.0/16" #  65.536 IPs
  tags = {
    Name = "MainVPC"
  }
}

# Create internet gateway
resource "aws_internet_gateway" "main_igw" {
  vpc_id = aws_vpc.main_vpc.id
  tags = {
    Name = "MainIGW"
  }
}

# Create public subnet for ec2 witch will be configurate by ansible
resource "aws_subnet" "ec2_ansible_subnet" {
  vpc_id                  = aws_vpc.main_vpc.id
  cidr_block = "10.0.1.0/24" # 256 IPs
  availability_zone       = var.availability_zone
  map_public_ip_on_launch = true
  tags = {
    Name = "MainSubnetForEc2Ansible"
  }
}

# Create route table
resource "aws_route_table" "main_rt" {
  vpc_id = aws_vpc.main_vpc.id
  route {
    cidr_block = "0.0.0.0/0" # Global internet
    gateway_id = aws_internet_gateway.main_igw.id
  }
  tags = {
    Name = "MainRouteTable"
  }
}

# Bind the routing table to the subnet
resource "aws_route_table_association" "main_rt_assoc" {
  route_table_id = aws_route_table.main_rt.id
  subnet_id      = aws_subnet.ec2_ansible_subnet.id
}