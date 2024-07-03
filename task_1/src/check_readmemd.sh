#!/bin/bash

# The file being checked
FILE="README.md"
# Status badge for GitHub Actions
BADGE="![Check README](https://github.com/vasyldmitrovich/trainee_devops_tasks/actions/workflows/task1.yml/badge.svg)"

echo "Running the script whether the file exists or not"

# Timestamp
echo "Current timestamp: $(date)"

# Check file
if [ ! -f $FILE ]; then
    echo "Error: $FILE file not found!"
    exit 1
fi

# Deleting the old status badge, if it exists
sed -i '/!\[Check README\]/d' README.md

# Adding a new status badge after text
sed -i "/### Task 1/a $BADGE $(date +%A %d/%m/%Y %H:%M:%S %Z)" README.md
#echo -e "$(cat README.md)\n$(date) $BADGE\n" > README.md

echo "README.md file is updated with the status badge."
exit 0