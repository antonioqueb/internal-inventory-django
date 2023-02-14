FROM python:3.9-alpine3.14

ENV PYTHONUNBUFFERED 1

WORKDIR /backendinv

RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps \
    && rm -rf /var/cache/apk/*

COPY . .
