from flask import Flask
from controllers.llama_controller import generate_text
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
port = int(os.getenv("PORT"))

@app.route('/generate', methods=['POST'])
def generate_route():
    return generate_text()

if __name__ == '__main__':
    app.run(port=port)