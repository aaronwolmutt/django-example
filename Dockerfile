FROM python:3.8-alpine

# Update alpine package manager, install C compilers, 
# postgres libraries, and Python dependencies
RUN apk update && \
    apk add build-base python3-dev postgresql-dev libpq && \
    pip install -U pip && \
    pip install Django && \
    pip install psycopg2

COPY manage.py ./app/

WORKDIR /app/

COPY golf_scorecard/ ./golf_scorecard/

COPY golfscores/ ./golfscores/

# Run the database migrations
# Creates postgres schema specified in Models.py
RUN python manage.py makemigrations && \
    python manage.py migrate && \ 
    python manage.py test

ENTRYPOINT ["python", "manage.py", "runserver"]