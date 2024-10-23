FROM python:3.10-alpine

WORKDIR /app

RUN apk add --no-cache build-base

COPY ./src /app/src
COPY main.py .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r "requirements.txt"

RUN apt-get update && apt-get install -y \
    build-essential \
    libopenblas-dev \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir thinc==8.2.5 autogluon

CMD ["python", "main.py"]