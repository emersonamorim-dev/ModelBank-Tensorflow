FROM python:3.8

RUN pip install psycopg2 pandas sklearn tensorflow kafka-python dotenv

WORKDIR /app

COPY main.py .

CMD ["python", "main.py"]
