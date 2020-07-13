# Kisan-Direct

## Run Locally
```
python -m venv .env
# Windows
.\.env\Scripts\activate

pip install -r requirements.txt 

python manage.py runserver
```

## Project Creation
```
python -m venv .env

# Linux
# source .env/bin/activate

# Windows
.\.env\Scripts\activate

python -m pip install --upgrade pip
pip install django

django-admin startproject kisan_direct .

pip freeze > requirements.txt
```

### Create Application
```
python manage.py startapp public
python manage.py startapp api
```