from flask import Flask, jsonify, render_template

from models import json_db

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


# v1 API routes
@app.route('/api/v1/test_endpoint/all')
def test_endpoint():
    return jsonify(json_db)


@app.route('/api/v1/test_endpoint/books/<int:i>')
def get_book_by_id(i):
    try:
        return jsonify(json_db[i])
    except IndexError:
        return jsonify({"Error": "Index or book does not exist."})


@app.route('/api/v1/test_endpoint/authors/all')
def get_all_authors():
    author = []
    for a in json_db:
        print(a['author'])
        author.append(a['author'])
    return jsonify({"authors": author})
