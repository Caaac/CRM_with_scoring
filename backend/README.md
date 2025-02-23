# Backend commands

***

### A short guide to the backend with a description of the basic commands for django and venv

***

## Django commands

***
Create project

```
django-admin startproject backend .
```
Create app (Don't foget register app in settings)

```
python manage.py startapp api
```

import created table

```
python manage.py inspectdb > ./api/models.py
```

Migrations

```
python manage.py makemigrations
```
```
python manage.py migrate
```

Get ORM
```
python manage.py inspectdb > models.py
```

Run Server

```
python manage.py runserver
```

***

## Venv commands

Create venv

```
python -m venv venv
```
Activate venv

> Windows
```
venv\Scripts\activate
```
> MacOS
```
source venv/bin/activate
```

Deactivate venv

```
deactivate
```
Get depandants

```
pip freeze
```
Make a file with depandants

```
pip freeze > requirements.txt
```
Install all depandants in venv

```
pip install -r requirements.txt
```
