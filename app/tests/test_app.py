# app/tests/test_app.py
import unittest
import json
from app.app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Hello, World!')

    def test_check_number_high(self):
        data = {'integer': 150}
        response = self.app.post('/check_number', json=data)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode())
        self.assertEqual(result['integer'], data['integer'])
        self.assertEqual(result['value'], 'high')

    def test_check_number_low(self):
        data = {'integer': 50}
        response = self.app.post('/check_number', json=data)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode())
        self.assertEqual(result['integer'], data['integer'])
        self.assertEqual(result['value'], 'low')

    def test_invalid_input(self):
        data = {'non_integer': 'invalid'}
        response = self.app.post('/check_number', json=data)
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode())
        self.assertEqual(result['error'], 'Invalid input')

if __name__ == '__main__':
    unittest.main()
