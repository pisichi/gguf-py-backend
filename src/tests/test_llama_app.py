# tests/test_llama_app.py
import sys
sys.path.append('E:\\Textgen\\llama-backend')  # Replace with the actual path to your project's root directory

import unittest
from flask import json
from src.app import app

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

        data = json.loads(response.get_data(as_text=True))
        self.assertIn('output', data)

if __name__ == '__main__':
    unittest.main()
