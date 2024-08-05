#!/bin/bash
set -e

cd ./app2
# Clear and create temp directory
rm -rf lambda_package
mkdir lambda_package

# Install dependency in temp directory
poetry install --no-dev
poetry run pip install --target=lambda_package .

# Copy code project to temp dir
#cp -r proj lambda_package/
cp ./lambda_function.py lambda_package/

# Create archive
cd ./lambda_package
#zip -r9 ../lambda_function_app2.zip .
7z a -r ../../lambda_function_app2.zip ./*

cd ../
# Clear
rm -rf ./lambda_package
