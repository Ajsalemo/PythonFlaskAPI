from flask import Flask, render_template, jsonify

from models import json_db

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

# v1 API routes 
@app.route('/api/v1/test_endpoint')
def test_endpoint():
    return jsonify(json_db)
