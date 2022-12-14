# Django Rest Framework


[![N|Solid](https://user-images.githubusercontent.com/61903698/188264476-cd5f36d4-04ac-4198-842b-c5d1f1ecd3fd.png)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

The Django REST framework (DRF) is a toolkit built on top of the Django web framework that reduces the amount of code you need to write to create REST interfaces.

## About
This Django Rest FrameWork project having 3 types of views

- normal views
- Class Based View
- Mixin View and Generic Views

## Features

- Simplicity, flexibility, quality, and test coverage of source code.
- Powerful serialization engine compatible with both ORM and non-ORM data sources.
- Pluggable and easy to customise emitters, parsers, validators and authenticators.
- Generic classes for CRUD operations.


## Installation

Django Rest Frame_work requires


Install the dependencies by using the following command.

```sh
pip install djangorestframework
```

add the frame work in settings file...

```sh
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'API',
    'rest_framework',
    'rest_framework_swagger',
]
```

## Server

for start the django server use the following command

```sh
python manage.py runserver
```

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## License

MIT
