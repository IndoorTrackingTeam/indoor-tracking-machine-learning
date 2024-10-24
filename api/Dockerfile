FROM python:3.9-alpine

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libopenblas-dev \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/*

COPY ./src /app/src
COPY main.py .
COPY requirements.txt .

RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r "requirements.txt" --no-cache-dir

RUN pip install --no-cache-dir thinc==8.2.5 autogluon

CMD ["python", "main.py"]