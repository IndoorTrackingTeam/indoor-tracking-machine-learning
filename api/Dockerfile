FROM python:3.9-alpine

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libopenblas-dev \
    libatlas-base-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip --no-cache-dir \
    && pip install -r "requirements.txt" --no-cache-dir \
    && pip install --no-cache-dir thinc==8.2.5 autogluon

COPY ./src /app/src
COPY main.py .
COPY requirements.txt .

CMD ["python", "main.py"]