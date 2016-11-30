#!/bin/bash

# Create and initialize a Python Virtual Environment
echo "Creating virtual env - .env"
virtualenv .env && echo "source virtual env - .env" && source .env/bin/activate

# create a directory to put things in
echo "Creating 'setup' dir"
mkdir setup

# Move that stuff into setup
echo "Moving creds.json and function file(s) to setup dir"
cp creds.json setup/creds.json
cp sparrow_*.py setup/
cd ./setup

# Install requirements 
echo "pip installing requirements"
pip install -r ../requirements.txt -t .

# Prepares the deployment package
echo "Zipping package"
zip -r ../package.zip ./* 

# Remove the dir used
cd ..
rm -rf ./setup
deactivate
rm -rf ./.env
# changing dirs back to dir from before
echo "Opening folder containg function package - 'package.zip'"
open .