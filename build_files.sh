#!/bin/bash
echo "BUILD START"
# Upgrade pip
python3 -m pip install --upgrade pip
# Install dependencies
python3 -m pip install -r requirements.txt
echo "Running collectstatic..."
python3 manage.py collectstatic --noinput --clear --verbosity 3
if [ $? -eq 0 ]; then
    echo "collectstatic completed successfully"
else
    echo "collectstatic failed"
    exit 1
fi
echo "BUILD END"