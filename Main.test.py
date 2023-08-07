import unittest

from fraud_detection import FraudDetectionModel, DatabaseConnector, KafkaProducerWrapper


class FraudDetectionModelTest(unittest.TestCase):

    def test_init(self):
        model = FraudDetectionModel()
        self.assertIsInstance(model, FraudDetectionModel)

    def test_train(self):
        model = FraudDetectionModel()
        X_train, _, _, _ = train_test_split([[1, 2, 3], [4, 5, 6]], [1, 0], test_size=0.2, random_state=42)
        model.train(X_train, [1, 0])
        self.assertIsInstance(model.model, tf.keras.Model)

    def test_evaluate(self):
        model = FraudDetectionModel()
        X_test, _, _, _ = train_test_split([[1, 2, 3], [4, 5, 6]], [1, 0], test_size=0.2, random_state=42)
        loss, accuracy = model.evaluate(X_test, [1, 0])
        self.assertIsInstance(loss, float)
        self.assertIsInstance(accuracy, float)

    def test_predict(self):
        model = FraudDetectionModel()
        X_test, _, _, _ = train_test_split([[1, 2, 3], [4, 5, 6]], [1, 0], test_size=0.2, random_state=42)
        predictions = model.predict(X_test)
        self.assertIsInstance(predictions, np.ndarray)


class DatabaseConnectorTest(unittest.TestCase):

    def test_init(self):
        db = DatabaseConnector('localhost', 'database', 'user', 'password')
        self.assertIsInstance(db, DatabaseConnector)

    def test_get_data(self):
        db = DatabaseConnector('localhost', 'database', 'user', 'password')
        df = db.get_data('SELECT * FROM modelBank')
        self.assertIsInstance(df, pd.DataFrame)


class KafkaProducerWrapperTest(unittest.TestCase):

    def test_init(self):
        producer = KafkaProducerWrapper('localhost:9092')
        self.assertIsInstance(producer, KafkaProducerWrapper)

    def test_send(self):
        producer = KafkaProducerWrapper('localhost:9092')
        message = {'key': 'value'}
        producer.send('modelBank_topic', message)


if __name__ == '__main__':
    unittest.main()
