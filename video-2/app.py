import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "development")

@app.route("/")
def home():
    return jsonify(
        message="Welcome from Tawla w Shay to Kubernetes Arabic Course",
        environment=APP_ENV
    )

@app.route("/health")
def health():
    return jsonify(status="healthy")

@app.route("/version")
def version():
    return jsonify(version="1.0.0")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)