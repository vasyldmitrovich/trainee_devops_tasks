#!/bin/bash

# Stopping run script if will be error
set -e

# Variables
TF_DIR="./"          # Folder where is terraform scenario
ANSIBLE_PLAYBOOK1="./config_instance/playbook.yml" # Ansible playbook1
ANSIBLE_PLAYBOOK2="./config_instance/task4_1_playbook.yml" # Ansible playbook2
INVENTORY_FILE="./config_instance/task4_1_ec2_inventory.ini"
USER="ubuntu"                 # Name of user for ssh connection

# Function for checking command
command_exists() {
  command -v "$1" >/dev/null 2>&1
}

# Checking is Terraform or not
if ! command_exists terraform; then
  echo "Terraform not installed. Install Terraform for contining."
  exit 1
fi

# Checking is Ansible or not
if ! command_exists ansible-playbook; then
  echo "Ansible  not installed. Install Ansible for contining."
  exit 1
fi

# Go to directory where is terraform scenario
cd $TF_DIR

# 1. Initialization of Terraform
echo "Initialization of Terraform..."
terraform init

# 2. Applying Terraform scenario
echo "Run Terraform apply..."
terraform apply -auto-approve

# 3. Get IP-address of EC2 instance1 and name of private key
echo "Get IP-address of EC2 instance1 and name of private key..."
WEB_SERVER1_IP=$(terraform output -raw web_server1_public_ip) # Public IP of first instance
PRIVATE_KEY_PATH=$(terraform output -raw private_key_filename) # Path to private SSH key

# Checking the presence of an SSH key
if [ ! -f "$PRIVATE_KEY_PATH" ]; then
  echo "File with private key not found for path: $PRIVATE_KEY_PATH"
  exit 1
fi

if [ -z "$WEB_SERVER1_IP" ]; then
  echo "Could not get IP-address of EC2 instance1. Verify that Terraform has successfully brought up the infrastructure."
  exit 1
fi

# 4. Check connection to EC2 instance1 by SSH
echo "Check connection to EC2 instance1 by SSH..."
sleep 5
# Maximum number of retries
max_retries=10
retry_count=0
ssh_ready=false

while [ $retry_count -lt $max_retries ]; do
  # Check if SSH is available
  nc -z -v -w5 $WEB_SERVER1_IP 22
  if [ $? -eq 0 ]; then
    echo "SSH is available, running Ansible Playbook"
    ssh_ready=true
    break
  else
    echo "SSH is not available, waiting for 10 seconds..."
    sleep 10
    retry_count=$((retry_count + 1))
  fi
done

# 5. Run Ansible playbook1
echo "Run Ansible playbook for configurate EC2 instance1..."
# If SSH is available, run the Ansible Playbook
if [ "$ssh_ready" = true ]; then
  ansible-playbook -i "${WEB_SERVER1_IP}," -u $USER -e 'ansible_ssh_common_args="-o StrictHostKeyChecking=no"' --private-key $PRIVATE_KEY_PATH $ANSIBLE_PLAYBOOK1
else
  echo "SSH is not available after $max_retries attempts, exiting."
  exit 1
fi

# 6. Run Ansible playbook2
echo "Run Ansible playbook for configurate EC2 instance2..."
WEB_SERVER2_IP=$(terraform output -raw web_server2_public_ip) # Public IP of second instance

# Create or update inventory file
cat > $INVENTORY_FILE <<EOL
[ec2webservers]
my_first_ec2_instance ansible_host=$WEB_SERVER1_IP ansible_user=$USER ansible_ssh_private_key_file=$PRIVATE_KEY_PATH
my_second_ec2_instance ansible_host=$WEB_SERVER2_IP ansible_user=$USER ansible_ssh_private_key_file=$PRIVATE_KEY_PATH
EOL
echo "Inventory file $INVENTORY_FILE has been updated."

ansible-playbook -i $INVENTORY_FILE -e 'ansible_ssh_common_args="-o StrictHostKeyChecking=no"' $ANSIBLE_PLAYBOOK2

echo "Deploy is finished!"
