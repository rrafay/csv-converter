from flask import Flask
from markupsafe import escape
from flask import jsonify
import requests
import csv

app = Flask(__name__)

@app.route("/path/<path:pin>")
def show_subpath(pin):
    url = f'https://docs.google.com/spreadsheets/d/e/{pin}/pub?output=csv'
    r = requests.get(url)

    text = r.text.splitlines('')

    reader = csv.DictReader(text, fieldnames=None)
    data = []
    for row in reader:
        data.append(row)

    return jsonify(data)