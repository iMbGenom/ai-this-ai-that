#!/bin/bash

source venv/bin/activate
python src/train_model.py
PYTHONPATH=./src uvicorn main:app --reload --app-dir src --port 8000
