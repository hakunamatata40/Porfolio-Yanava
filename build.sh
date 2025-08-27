#!/usr/bin/env bash
# set -o errexit  # Optionnel pour arrêter sur erreur

echo "BUILD START"
pip install -r requirements.txt
echo "Running collectstatic..."
python manage.py collectstatic --noinput --clear
echo "Running migrate..."
python manage.py migrate
if [ $? -eq 0 ]; then
    echo "Build completed successfully"
else
    echo "Build failed"
    exit 1
fi
echo "BUILD END"