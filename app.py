import json
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == '_main_':
    app.run(debug=True)
