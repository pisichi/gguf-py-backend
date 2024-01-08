from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app_url = os.getenv("APP_URL")
port = int(os.getenv("PORT"))


def add_route(route, method, handler):
    app.route(route, methods=[method])(handler)

from controllers import llama_controller as controller
add_route('/generate', 'POST', controller.generate)


if __name__ == '__main__':
    app.run(host=app_url, port=port)
