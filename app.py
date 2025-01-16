from flask import Flask, render_template, jsonify
from markupsafe import escape
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def sendData():
    return jsonify({"message":"hello world"})

@app.route('/<url>')
def convert(url):
    return jsonify({"data":url})

app.run('127.0.0.1',8000)