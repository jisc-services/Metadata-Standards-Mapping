#!/bin/bash

source venv/bin/activate
mkdir -p build/css
cp css/* build/css/
python schema_tables.py > build/index.html
