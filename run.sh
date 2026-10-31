#!/bin/bash
python3 -m venv .venv && source ./.venv/bin/activate &>/dev/null
python3 -m pip install -r requirements.txt &>/dev/null
python3 src/main.py
deactivate &>/dev/null
