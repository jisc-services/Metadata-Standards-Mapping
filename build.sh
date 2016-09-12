#!/bin/bash

source venv/bin/activate
mkdir -p build/css
cp css/* build/css/
python build.py > build/index.html
