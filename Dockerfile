FROM python:3.12-alpine

WORKDIR /app

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN \
 apk add --no-cache make && \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN python -m pip install -r requirements.txt --no-cache-dir

