import unittest
import json
from app import app

class TestFlaskAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello(self):
        response = self.app.get('/hello')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Hello, World!')

    def test_echo(self):
        data = {'key': 'value'}
        response = self.app.post('/echo', json=data)
        received_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(received_data, data)

if __name__ == '__main__':
    unittest.main()
