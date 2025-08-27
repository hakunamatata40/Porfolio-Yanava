#!/bin/bash
echo "BUILD START"
python3.11 -m pip install --upgrade pip
python3.11 -m pip install -r requirements.txt
echo "Running collectstatic..."
python3.11 manage.py collectstatic --noinput --clear --verbosity 3
if [ $? -eq 0 ]; then
    echo "collectstatic completed successfully"
else
    echo "collectstatic failed"
    exit 1
fi
echo "BUILD END"