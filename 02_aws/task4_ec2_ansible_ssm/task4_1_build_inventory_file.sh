#!/bin/bash

# Check argument
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <first_instance_ip> <second_instance_ip> <private_key_path>"
    exit 1
fi

FIRST_IP=$1
SECOND_IP=$2
PRIVATE_KEY_PATH=$3
INVENTORY_FILE="task4_1_ec2_inventory.ini"

# Create or update inventory file
cat > $INVENTORY_FILE <<EOL
[ec2webservers]
my_first_ec2_instance ansible_host=$FIRST_IP ansible_user=ubuntu ansible_ssh_private_key_file=$PRIVATE_KEY_PATH
my_second_ec2_instance ansible_host=$SECOND_IP ansible_user=ubuntu ansible_ssh_private_key_file=$PRIVATE_KEY_PATH
EOL

echo "Inventory file $INVENTORY_FILE has been updated."
