FROM python:3.9-slim

ARG ARG_GITHUB_ENV
ENV GITHUB_ENV={GITHUB_ENV}

RUN apt-get update && apt-get install -y \
    build-essential \
    libopenblas-dev \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --no-cache-dir numpy==1.22.4 pandas==2.1.1 requests autogluon thinc==8.2.5

COPY model_training_service.py .

CMD ["python", "model_training_service.py"]
