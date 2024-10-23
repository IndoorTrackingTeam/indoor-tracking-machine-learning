FROM python:3.9-slim

WORKDIR /app

RUN pip install uv
RUN uv venv && uv pip install autogluon
RUN pip install --no-cache-dir pandas numpy thinc==8.2.5 requests

COPY model_training_service.py .

CMD ["python", "model_training_service.py"]
