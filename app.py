import os
from flask import Flask, jsonify


app = Flask(__name__)


# Read environment variables (fall back to example values if missing)
APP_MESSAGE = os.getenv('APP_MESSAGE', 'Hello — set APP_MESSAGE env var')
APP_HEALTH = os.getenv('APP_HEALTH', 'healthy')


@app.route('/')
def index():
    return f"{APP_MESSAGE}\n"


@app.route('/health')
def health():
    return jsonify(status=APP_HEALTH)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)