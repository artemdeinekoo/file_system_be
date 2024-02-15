# Setup project

- fill environments files
- run project

## Fill environment
1. run - > cp .env.sample .env



## Start project

run:
     - > python3 -m venv venv
     - > venv/Scripts/activate
     - > pip install -r requirements.txt
     - > python manage.py makemigrations
     - > python manage.py migrate
     - > python manage.py runserver 0.0.0.0:8000

