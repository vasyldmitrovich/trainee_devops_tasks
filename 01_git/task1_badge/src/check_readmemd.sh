#!/bin/bash

# The file being checked
FILE="README.md"

# Status badge for GitHub Actions
BADGENAME="Check README"
BADGE="![$BADGENAME](https://github.com/vasyldmitrovich/trainee_devops_tasks/actions/workflows/git_task1.yml/badge.svg)"
TIMESTAMP=$(date '+%A %d/%m/%Y %H:%M:%S %Z')

LANGUAGES_JSON=$(curl -L \
                -H "Accept: application/vnd.github+json" \
                -H "Authorization: Bearer $GITHUB_TOKEN" \
                -H "X-GitHub-Api-Version: 2022-11-28" \
                https://api.github.com/repos/vasyldmitrovich/trainee_devops_tasks/languages)
# Calculate the primary language and its percentage
TOTAL_BYTES=$(echo $LANGUAGES_JSON | jq '. | map(values) | add')
PRIMARY_LANGUAGE=$(echo $LANGUAGES_JSON | jq -r 'to_entries | max_by(.value) | .key')
PRIMARY_LANGUAGE_BYTES=$(echo $LANGUAGES_JSON | jq -r --arg lang "$PRIMARY_LANGUAGE" '.[$lang]')
PRIMARY_LANGUAGE_PERCENTAGE=$(awk "BEGIN {printf \"%.2f\", ($PRIMARY_LANGUAGE_BYTES/$TOTAL_BYTES)*100}")
# Create a badge URL using Shields.io
LANGUAGE_BADGE="![Primary Language](https://img.shields.io/badge/$PRIMARY_LANGUAGE-$PRIMARY_LANGUAGE_PERCENTAGE%25-blue)"

# A pattern to check the version (for example, a version in the format v1.0.0)
VERSION_PATTERN="v[0-9]+\.[0-9]+\.[0-9]+"

echo "Running the script whether the file exists or not"
# Timestamp
echo "Current timestamp: $TIMESTAMP"

# Check file existence
if [ ! -f "$FILE" ]; then
    echo "Error: $FILE file not found!"
    exit 1
fi

# A function to search for a version in a file
check_version_in_file() {
    local file=$1
    local pattern=$2
    local version_line

    version_line=$(grep -E "$pattern" "$file")

    if [ -z "$version_line" ]; then
        echo "Error: No version matching the pattern '$pattern' found in the file."
        exit 1
    else
        echo "Version found: $version_line"
        # Selection of the version itself from the line
        local version
        version=$(echo $version_line | grep -oE "$pattern")
        echo "Extracted version: $version"
    fi
}

check_version_in_file $FILE $VERSION_PATTERN

# Function to insert badge at specific line
insert_badge() {
    sed -i "$1i $BADGE   Num:$GITHUB_RUN_NUMBER   Primary Language: $LANGUAGE_BADGE" "$FILE"
}

# Function to insert action block at specific line
insert_action_block() {
    sed -i "$1i ### Action\n$BADGE   Num:$GITHUB_RUN_NUMBER   Primary Language: $LANGUAGE_BADGE\n\nEnd!" "$FILE"
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
        echo "\n" >> "$FILE"
        # Find the last line of the file
        LAST_LINE=$(wc -l < "$FILE")

        # Append the "### Action" block to the end of the file if neither headers are found
        insert_action_block "$LAST_LINE"

        echo "Action block and badge appended to the end of the file."
    fi
fi

echo "README.md file is updated with the status badge."
exit 0