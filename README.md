# Setup
## Create an environment
git clone xyz
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