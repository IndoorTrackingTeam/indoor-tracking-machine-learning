FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir pandas numpy thinc==8.2.5 requests autogluon==1.1.1 --use-deprecated=legacy-resolver

COPY model_training_service.py .

CMD ["python", "model_training_service.py"]
