#!/bin/bash
cd ./app
poetry export -f requirements.txt --output requirements.txt --without-hashes
pip install --target ./package -r requirements.txt
cd package
zip -r9 ../function.zip .
cd ../
zip -g function.zip app.py db.py