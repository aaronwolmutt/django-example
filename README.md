# Golf score card

This is an example CRUD application written in Django and PostgresSQL where users can manage their golf scores and calculate their handicaps, hole averages, and other views.

## Docker build and service orchestration

Compose is used to orchestrate a Postgres and single Django application service. Orchestrating the services will execute the runtimes of Postgres and an Alpine Linux container running Django. Upon executing the runtime, Django will perform any database migrations as well as intitialize the schema provided in the Models.py file.

To build and execute the app use: 
```bash
$ docker-compose up -d
```
View the UWGI server logs: 
```bash 
$ docker logs app-01_1
```

## Local development & using Debug mode

Run the Postgres server on localhost: 
```bash
$ docker-compose up psql -d
```
Check for model changes:
```bash
$ python manage.py makemigrations
```
Apply the database migrations:
```bash
$ python manage.py migrate
```
Run the tests:
```
$ python manage.py test
```
Start the Django server:
```bash
$ python manage.py runserver
```
