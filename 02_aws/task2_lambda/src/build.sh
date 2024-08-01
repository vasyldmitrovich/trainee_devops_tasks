#!/bin/bash
cd ./app
#pip install poetry
#poetry export -f requirements.txt --output requirements.txt --without-hashes
mkdir package
pip install --target ./package -r requirements.txt
cd package
#zip -r ../function.zip .
7z a -r ../../function.zip ./*
cd ../
#zip function.zip app.py db.py
7z a -tzip ../function.zip app.py db.py