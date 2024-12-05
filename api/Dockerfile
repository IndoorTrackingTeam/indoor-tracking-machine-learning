# Stage 1: Build dependencies
FROM python:3.11-slim as build

RUN apt-get update && apt-get install -y --no-install-recommends \

    build-essential \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt --no-cache-dir

# Stage 2: Final runtime
FROM python:3.11-slim

WORKDIR /app

COPY --from=build /app /app

COPY . /app

CMD ["python", "main.py"]
