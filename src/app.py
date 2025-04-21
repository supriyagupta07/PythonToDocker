from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Hello, I am Supriya! </h1>
    <p>I am inside a Docker container!</p>
    <p>This is my Dockerized Flask app</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

