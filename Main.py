import os
import pyodbc
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from kafka import KafkaProducer
import json
from dotenv import load_dotenv


class FraudDetectionModel:
    def __init__(self):
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def train(self, X, y):
        self.model.fit(X, y, epochs=10)

    def evaluate(self, X, y):
        return self.model.evaluate(X, y)

    def predict(self, X):
        return self.model.predict(X)


class DatabaseConnector:
    def __init__(self, **kwargs):
        self.conn = pyodbc.connect(
            **kwargs
        )

    def get_data(self, query):
        return pd.read_sql(query, self.conn)


class KafkaProducerWrapper:
    def __init__(self, **kwargs):
        self.producer = KafkaProducer(**kwargs)

    def send(self, topic, message):
        self.producer.send(topic, message)
        self.producer.flush()


def load_dotenv():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)


def main():
    load_dotenv()

    db = DatabaseConnector(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_DATABASE'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
    )

    # Lendo os dados em um DataFrame do Pandas
    df = db.get_data('SELECT * FROM modelBank')

    # Dividindo os dados em conjuntos de treinamento e teste
    X = df[features]
    y = df[target]

    # Dividindo os dados em conjuntos de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Construindo e treinando o modelo
    model = FraudDetectionModel()
    model.train(X_train, y_train)

    model.evaluate(X_test, y_test)

    producer = KafkaProducerWrapper(
        servers=os.environ['KAFKA_SERVERS'],
        host=os.environ['DB_HOST'],
        database=os.environ['DB_DATABASE'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
    )

    # Enviando tópico Kafka
    for index, row in df.iterrows():
        message = {
            'transaction_id': row['transaction_id'],
            'is_fraud': model.predict(row[features]),
            'index': index,
        }
        producer.send('modelBank_topic', message)


if __name__ == "__main__":
    jenkins = Jenkins()
    jenkins.build('fraud_detection')



