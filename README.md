## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Features](#Features)  
* [Test accounts](#test-accounts)  
* [Setup](#setup)         

## General info
This is a simple academic project. The created web application allows to view, add and edit movies and reviews.

## Technologies
Project is created with:
* Python v3.9.5
* Django v3.2.2
* SQLite v3.35.5
* Bootstrap v4

## Features
* Login - /accounts/login/
* Registration - /accounts/register/
* Contact - /contact/
* Detailed information about movies - /details/id/
* Possibility to add videos - only for staff - /addmovies/
* Possibility to edit movies - only for staff - /editmovies/id/
* Admin panel based on django-admin - /admin/

## Test accounts

Admin user
```
Login: admin
Password: admin
```
Normal user
```
Login: DemoAccount
Password: Password123
```

## Setup
```
$ git clone https://github.com/Dwarg/movieweb-django.git
$ cd movieweb-django
$ pip install -r requirements.txt
$ python manage.py makemigrations (optional)
$ python manage.py migrate (optional)
$ python manage.py runserver
```
