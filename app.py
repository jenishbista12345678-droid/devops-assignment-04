import os
from flask import Flask, jsonify


app = Flask(__name__)


# Read environment variables (fall back to example values if missing)
APP_MESSAGE = os.getenv('APP_MESSAGE', 'Hello — set APP_MESSAGE env var')
APP_HEALTH = os.getenv('APP_HEALTH', 'healthy')


@app.route('/')
def index():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Flask App</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #74ebd5 0%, #ACB6E5 100%);
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                color: #333;
                text-align: center;
            }}
            h1 {{
                font-size: 2.5em;
                margin-bottom: 0.5em;
            }}
            p {{
                font-size: 1.2em;
            }}
        </style>
    </head>
    <body>
        <h1>Flask App — Home</h1>
        <p><strong>Message:</strong> {APP_MESSAGE}</p>
        <p>Visit <a href="/health">/health</a> to check app health.</p>
    </body>
    </html>
    """


@app.route('/health')
def health():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Health Check</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f7fa;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                color: #333;
            }}
            h1 {{
                color: #4CAF50;
            }}
            p {{
                font-size: 1.2em;
            }}
        </style>
    </head>
    <body>
        <h1>Application Health</h1>
        <p>Status: <strong>{APP_HEALTH}</strong></p>
        <a href="/">← Back to Home</a>
    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)