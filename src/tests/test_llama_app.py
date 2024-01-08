import unittest
from flask import json
from ..app import app  # Relative import

class TestLlamaApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_generate_route(self):
        input_data = {
            "input_text": "Q: What is the capital of France? A:",
            "max_tokens": 32
        }

        response = self.app.post('/generate', json=input_data)

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('output', data)
        self.assertIsInstance(data['output'], str)

if __name__ == '__main__':
    unittest.main()
