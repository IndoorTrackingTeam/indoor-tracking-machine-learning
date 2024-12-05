FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    libblas-dev \
    liblapack-dev \
    gfortran \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip --no-cache-dir \
    && pip install -r "requirements.txt" --no-cache-dir --disable-pip-version-check

RUN rm -rf /app && mkdir -p /app
WORKDIR /app
COPY . /app

CMD ["python", "main.py"]
