FROM python:3.9-alpine

WORKDIR /app

RUN pip install  --no-cache-dir setuptools wheel
RUN pip install --no-cache-dir thinc==8.2.5 autogluon

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