#!/bin/bash

VENV_NAME="my_virtual_env"

python3 -m venv $VENV_NAME
source $VENV_NAME/bin/activate
pip install -r requirements.txt
echo "Virtual environment $VENV_NAME is set up and dependencies are installed."
python3 app.py
