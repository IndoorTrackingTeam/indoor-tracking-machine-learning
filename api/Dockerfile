FROM us-east1-docker.pkg.dev/seventh-azimuth-433221-r8/ar-backend/machine-learning-api-prod@sha256:316075c466256bd028a64974eb0a54d4bea4dd586b926960fade2eccbbaadd9d

RUN rm -rf /app
RUN mkdir /app
WORKDIR /app

COPY ./src /app/src
COPY main.py .

CMD ["python", "main.py"]