#!/bin/bash

source venv/bin/activate
pip freeze > requirements-lock.txt
mkdir -p src/generated && touch src/generated/sklearn_model.pkl
python src/train_model.py
PYTHONPATH=./src uvicorn main:app --reload --app-dir src --port 8000
