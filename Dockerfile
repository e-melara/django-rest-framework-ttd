FROM python:3.11.2-slim-buster
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ=America/El_Salvador

RUN apt-get update \
    && apt-get install -y libpq-dev python3-dev \
    && apt-get install -y build-essential

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .