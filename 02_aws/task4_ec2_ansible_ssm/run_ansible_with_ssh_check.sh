#!/bin/bash

# Arguments passed to the script
WEB_SERVER_IP=$1
PRIVATE_KEY_PATH=$2

# Maximum number of retries
max_retries=10
retry_count=0
ssh_ready=false

while [ $retry_count -lt $max_retries ]; do
  # Check if SSH is available
  nc -z -v -w5 $WEB_SERVER_IP 22
  if [ $? -eq 0 ]; then
    echo "SSH is available, running Ansible Playbook"
    ssh_ready=true
    break
  else
    echo "SSH is not available, waiting for 30 seconds..."
    sleep 30
    retry_count=$((retry_count + 1))
  fi
done

# If SSH is available, run the Ansible Playbook
if [ "$ssh_ready" = true ]; then
  ansible-playbook -i "${WEB_SERVER_IP}," -u ubuntu --private-key $PRIVATE_KEY_PATH playbook.yml
else
  echo "SSH is not available after $max_retries attempts, exiting."
  exit 1
fi
