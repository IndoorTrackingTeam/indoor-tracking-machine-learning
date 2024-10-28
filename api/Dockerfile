us-east1-docker.pkg.dev/seventh-azimuth-433221-r8/ar-backend/machine-learning-api-prod:latest

RUN rm -rf /app && mkdir -p /app
WORKDIR /app
COPY . /app

CMD ["python", "main.py"]