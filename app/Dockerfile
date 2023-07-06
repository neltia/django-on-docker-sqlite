FROM python:3.9
WORKDIR /app
COPY . .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# apt dependencies
RUN apt-get update

# requirements install
RUN pip install -r requirements.txt

# static file
RUN python manage.py collectstatic --noinput
