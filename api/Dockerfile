FROM python:3.11-slim

WORKDIR /app

RUN apk update && apk add --no-cache \
    build-base \
    openblas-dev \
    linux-headers \
    bash

COPY ./src /app/src
COPY main.py .
COPY requirements.txt .

RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r "requirements.txt" --no-cache-dir


CMD ["python", "main.py"]