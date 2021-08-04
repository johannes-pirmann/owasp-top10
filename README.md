# Setup
## Create an environment
git clone git@github.com:johannes-pirmann/owasp-top10.git

cd owasp_top10

python3 -m venv venv

## Activate the environment
. venv/bin/activate

## Install the requirements
pip3 install -r requirements.txt

## Setup the database
python3 db.py

## Run the application
run flask

# DEMO
## XSS
