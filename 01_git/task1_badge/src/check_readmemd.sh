#!/bin/bash

# The file being checked
FILE="README.md"

# Status badge for GitHub Actions
BADGENAME="Check README"
BADGE="![$BADGENAME](https://github.com/vasyldmitrovich/trainee_devops_tasks/actions/workflows/git_task1.yml/badge.svg)"
TIMESTAMP=$(date '+%A %d/%m/%Y %H:%M:%S %Z')
TOP_LANGUAGE="https://img.shields.io/github/languages/top/vasyldmitrovich/trainee_devops_tasks"

echo "Running the script whether the file exists or not"

# Timestamp
echo "Current timestamp: $TIMESTAMP"

# Check file existence
if [ ! -f "$FILE" ]; then
    echo "Error: $FILE file not found!"
    exit 1
fi

# Function to insert badge at specific line
insert_badge() {
    sed -i "$1i $BADGE #Num:$GITHUB_RUN_NUMBER $TOP_LANGUAGE" "$FILE"
}

# Function to insert action block at specific line
insert_action_block() {
    sed -i "$1i ### Action\n$BADGE #Num:$GITHUB_RUN_NUMBER $TOP_LANGUAGE\n\nEnd!" "$FILE"
}

# Check if there is an existing "### Action" block
# Find the starting line number of the "### Action" block
ACTION_BLOCK_START=$(grep -n "### Action" "$FILE" | cut -d: -f1)
# Find the ending line number of the "### Action" block (denoted by '---')
ACTION_BLOCK_END=$(grep -n "^End!" "$FILE" | grep -A1 "^${ACTION_BLOCK_END}" | tail -n1 | cut -d: -f1)

if [ -n "$ACTION_BLOCK_START" ] && [ -n "$ACTION_BLOCK_END" ]; then
    # If the "### Action" block exists, check if the badge is already present
    if sed -n "${ACTION_BLOCK_START},${ACTION_BLOCK_END}p" "$FILE" | grep -q "$BADGENAME"; then
        sed -i "$ACTION_BLOCK_START,$ACTION_BLOCK_END{/$BADGENAME/d}" $FILE
        insert_badge "$((ACTION_BLOCK_START + 1))"
        echo "Badge already exists in the Action block, but insert new badge."
    else
        # Insert the badge after the start of the "### Action" block if it's not already there
        insert_badge "$((ACTION_BLOCK_START + 1))"
        echo "Badge inserted in the Action block."
    fi
else
    # Check for "## Task List" header
    TASK_LIST_LINE=$(grep -n "## Task List" "$FILE" | cut -d: -f1)

    if [ -n "$TASK_LIST_LINE" ]; then
        # Check if an action block already exists before the Task List
        PREVIOUS_LINE=$((TASK_LIST_LINE - 1))
        if ! sed -n "${PREVIOUS_LINE}p" "$FILE" | grep -q "### Action"; then
            # Insert the "### Action" block before the "## Task List" header
            insert_action_block "$PREVIOUS_LINE"
            echo "Action block inserted before Task List."
        else
            echo "Action block already exists before Task List."
        fi
    else
        # Append the "### Action" block to the end of the file if neither headers are found
        echo -e "\n### Action\n$BADGE #Num:$GITHUB_RUN_NUMBER $TOP_LANGUAGE\n\nEnd!" >> "$FILE"
        echo "Action block and badge appended to the end of the file."
    fi
fi

echo "README.md file is updated with the status badge."
exit 0