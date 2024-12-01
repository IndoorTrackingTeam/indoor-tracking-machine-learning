FROM us-east1-docker.pkg.dev/indoor-tracking-team/ar-backend/machine-learning-api-prod:latest

RUN rm -rf /app && mkdir -p /app
WORKDIR /app
COPY . /app

CMD ["python", "main.py"]