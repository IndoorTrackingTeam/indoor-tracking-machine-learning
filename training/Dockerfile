FROM python:3.9-slim

WORKDIR /app

RUN pip install uv
RUN uv pip install autogluon
RUN pip install --no-cache-dir  pandas numpy

COPY model_training_service.py .

CMD ["python", "model_training_service.py"]
