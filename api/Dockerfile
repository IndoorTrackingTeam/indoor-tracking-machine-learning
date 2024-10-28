FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    libblas-dev \
    liblapack-dev \
    gfortran \
    && rm -rf /var/lib/apt/lists/*

COPY ./src /app/src
COPY main.py .
COPY requirements.txt .
COPY AutogluonModels /app/AutogluonModels

RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r "requirements.txt" --no-cache-dir

CMD ["python", "main.py"]