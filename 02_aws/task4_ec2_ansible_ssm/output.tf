#
output "web_server1_public_ip" {
  value = aws_instance.web_server.public_ip
}

output "web_server2_public_ip" {
  value = aws_instance.web_server2.public_ip
}

output "private_key_filename" {
  value = local_file.private_key.filename
}