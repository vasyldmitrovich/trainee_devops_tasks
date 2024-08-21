#!/bin/bash

# Function to create a Lambda deployment package
create_lambda_package() {
    local zip_file="$1"
    local project_path="$2"
    local lambda_function_file="$3"

    cd $project_path

    # Delete old zip archive if it exists
    if [ -f "$zip_file" ]; then
        rm "$zip_file"
    fi

    # Install dependencies into a temporary package directory
    pip install --target "$project_path/package" -r "$project_path/requirements.txt"

    # Create zip archive of the package
    cd "$project_path/package"
    zip -r9 "../$zip_file" .

    # Add the Lambda function to the archive
    cd "$project_path"
    zip -g "$zip_file" "$lambda_function_file"

    # Delete the temporary package directory
    rm -rf "$project_path/package"

    echo "Lambda package created: $zip_file"
}

# Variables for zip file name and project path
ZIP_FILE1="lambda_function_app.zip"
PROJECT_PATH1="$(pwd)/app"
LAMBDA_FILE1="lambda_function.py"

ZIP_FILE2="lambda_function_app_bridge.zip"
PROJECT_PATH2="$(pwd)/app_bridge"
LAMBDA_FILE2="lambda_function.py"

ZIP_FILE3="lambda_function_app_logger.zip"
PROJECT_PATH3="$(pwd)/app_versioning_alias"
LAMBDA_FILE3="lambda_function.py"

ZIP_FILE4="lambda_function_app_versioning_workspaces.zip"
PROJECT_PATH4="$(pwd)/app_versioning_workspaces"
LAMBDA_FILE4="lambda_function.py"

# Call the function with the provided arguments
create_lambda_package "$ZIP_FILE1" "$PROJECT_PATH1" "$LAMBDA_FILE1"
create_lambda_package "$ZIP_FILE2" "$PROJECT_PATH2" "$LAMBDA_FILE2"
create_lambda_package "$ZIP_FILE3" "$PROJECT_PATH3" "$LAMBDA_FILE3"
create_lambda_package "$ZIP_FILE4" "$PROJECT_PATH4" "$LAMBDA_FILE4"
