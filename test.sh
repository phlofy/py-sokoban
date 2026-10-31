#!/bin/bash
python3 -m venv .venv && source ./.venv/bin/activate
python3 -m pip install -r test_requirements.txt
PYTHONPATH=. pytest tests/*
deactivate
rm -rf ./.venv
