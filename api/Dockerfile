FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    libblas-dev \
    liblapack-dev \
    gfortran \
    cmake \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --upgrade pip setuptools wheel --no-cache-dir
RUN pip install fastapi --no-cache-dir
RUN pip install uvicorn --no-cache-dir
RUN pip install pydantic --no-cache-dir
RUN pip install pandas==2.1.1 --no-cache-dir
RUN pip install numpy>=1.22.4 --no-cache-dir
RUN pip install thinc==8.2.5 --no-cache-dir
RUN pip install autogluon==1.1.1 --no-cache-dir
RUN pip install pytest-cov --no-cache-dir
RUN pip install httpx --no-cache-dir

COPY . /app

CMD ["python", "main.py"]
