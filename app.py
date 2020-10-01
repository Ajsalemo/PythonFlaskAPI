from flask import Flask, jsonify, render_template
from flask_migrate import Migrate

from models import db, BMWCarModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://<username>:<password>@localhost:5432/<database>"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def home():
    return render_template('home.html')


# v1 API routes
@app.route('/api/v1/test_endpoint/all')
def test_endpoint():
    return jsonify({"message": "Test"})
