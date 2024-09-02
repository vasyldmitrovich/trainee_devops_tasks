variable "AWS_REGION" {
  default = "eu-west-1"
}

variable "availability_zone" {
  default = "eu-west-1a"
}

variable "instance_type" {
  description = "The instance type to use for the EC2 instance"
  type        = string
  default     = "t2.micro"
}

variable "instance_ami" {
  description = "The AMI ID to use for the EC2 instance"
  type        = string
  default     = "ami-0c1c30571d2dae5c9"
}

variable "sg_ports_for_internet" {
  type = list(number)
  default = [80, 443, 22] # 22 -> ssh, 80 -> http, 443 -> https
}

variable "ssh_key_name" {
  default = "key_for_ansible"

}