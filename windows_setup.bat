rem Create and initialize a Python Virtual Environment
echo "Creating virtual env - .env"
virtualenv .env

echo "starting virtualenv - .env"
call .env\Scripts\activate.bat

rem Create a directory to put things in
echo "Creating 'setup' directory"
mkdir setup

rem Move the relevant files into setup directory
echo "Moving creds.json and function file(s) to setup dir"
xcopy .\creds.json .\setup\creds.json /Q /R /Y
F
xcopy .\sparrow_kms.py setup\ /Q /R /Y
xcopy .\sparrow_nokms.py setup\ /Q /R /Y
cd .\setup

rem Install requirements 
echo "pip installing requirements from requirements file in target directory"
pip install -r ..\requirements.txt -t .

rem Prepares the deployment package
echo "Setting up your 7zip PATH - This assumes the installation location of 7zip is in C:\Program Files\7-Zip\"
set PATH=%PATH%;C:\Program Files\7-Zip\

echo "Zipping package"
7z a -r ..\package.zip .\* 

rem Remove the setup directory used
echo "Removing setup directory and virtual environment"
cd ..
rd /Q /S .\setup
call .env\Scripts\deactivate.bat
rd /Q /S .\.env

rem changing dirs back to dir from before
echo "Opening folder containg function package - 'package.zip'"
explorer .