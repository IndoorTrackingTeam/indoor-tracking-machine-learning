FROM python:3.9

WORKDIR /app

COPY ./src /app/src
COPY main.py .
COPY requirements.txt .

RUN pip install -r "requirements.txt"

CMD ["python", "main.py"]