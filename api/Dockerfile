FROM python:3.11-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    libblas-dev \
    liblapack-dev \
    gfortran \
    cmake \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Definir diretório de trabalho
WORKDIR /app

# Atualizar pip, setuptools e wheel
RUN pip install --upgrade pip setuptools wheel --no-cache-dir

# Instalar dependências individuais
RUN pip install fastapi --no-cache-dir
RUN pip install uvicorn --no-cache-dir
RUN pip install pydantic --no-cache-dir
RUN pip install pandas==2.1.1 --no-cache-dir
RUN pip install numpy>=1.22.4 --no-cache-dir
RUN pip install thinc==8.2.5 --no-cache-dir
RUN pip install pytest-cov --no-cache-dir
RUN pip install httpx --no-cache-dir

# Instalar onnx e protobuf antes do autogluon
RUN pip install protobuf==3.20.3 --no-cache-dir
RUN pip install onnx==1.14.0 --no-cache-dir

# Instalar autogluon
RUN pip install autogluon==1.1.1 --no-cache-dir

# Copiar o código para dentro do container
COPY . /app

# Comando padrão para executar o app
CMD ["python", "main.py"]