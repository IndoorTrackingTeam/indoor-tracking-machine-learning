FROM python:3.9-alpine

WORKDIR /app

COPY ./src /app/src
COPY main.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r "requirements.txt"

CMD ["python", "main.py"]