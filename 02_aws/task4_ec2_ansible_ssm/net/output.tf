#
output "main_vpc_id" {
  description = "The ID of the VPC where the Security Group will be created"
  value       = aws_vpc.main_vpc.id
}
output "ec2_ansible_subnet_id" {
  description = "The ID of the subnet where the EC2 instance will be launched"
  value       = aws_subnet.ec2_ansible_subnet.id
}