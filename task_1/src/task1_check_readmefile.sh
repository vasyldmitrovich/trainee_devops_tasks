#!/bin/bash

echo "Start script witch check is file Readme.md or not"

# Timestamp
echo "Current timestamp: $(date)"

# Check README.md file
if [ ! -f "README.md" ]; then
    echo "Error: README.md file not found!"
    exit 1
fi

echo "README.md file is present."
exit 0