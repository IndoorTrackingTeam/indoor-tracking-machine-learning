FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY model_training_service.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "model_training_service.py"]
