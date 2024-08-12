#!/bin/bash

# Name of archive
ZIP_FILE="lambda_function_app.zip"

# Delete old zip archive
if [ -f "$ZIP_FILE" ]; then
    rm "$ZIP_FILE"
fi

# Install dependency
pip install --target ./package -r ./app/requirements.txt

# Create zip-archive
cd package
zip -r9 ../"$ZIP_FILE" .

# Add lambda function to archive
cd ../app/
zip -g "../$ZIP_FILE" lambda_function.py
cd ..

# Delete temporary directory
rm -rf package

echo "Lambda package created: $ZIP_FILE"
