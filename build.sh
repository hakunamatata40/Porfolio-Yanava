#!/bin/bash

# Installer les dépendances Python
pip install -r requirements.txt

# Collecter les fichiers statiques
python manage.py collectstatic --noinput