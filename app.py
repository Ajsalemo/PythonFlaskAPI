from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
from flask import json
from flask_migrate import Migrate
from models import BMWCarModel, db

# Load dotenv
load_dotenv()

import os

# Environment variables
POSTGRES_USERNAME = os.getenv('POSTGRES_USERNAME')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DATABASE = os.getenv('POSTGRES_DATABASE')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def home():
    return render_template('home.html')


# v1 API routes
# Return all columns an assiociated information for the stored cars in Postgres
@app.route('/api/v1/cars/all')
def test_endpoint():
    all_results = BMWCarModel.query.all()
    results = [
        {
            "id": result.id,
            "Production": result.Production,
            "Model": result.Model,
            "Type": result.Type,
            "Displacement": result.Displacement,
            "Engine_Type": result.Engine_Type,
            "Power": result.Power,
            "Body": result.Body,
            "Production_Number": result.Production_Number
        } for result in all_results]
    return jsonify({"all_cars": results})


# Return all models wih their production year
# Format ex. - "2000-2006 M3"
@app.route('/api/v1/cars/all_models')
def all_models():
    all_models = BMWCarModel.query.all()
    all_models_array = []
    for m in all_models:
        all_models_array.append(f"{m.Production} {m.Model}")
    return jsonify({ "all_models": all_models_array })


# Return all generational types
# Format ex - "E46"
@app.route('/api/v1/cars/model_types')
def all_model_types():
    all_model_types = BMWCarModel.query.all()
    all_model_type_array = []
    for t in all_model_types:
        all_model_type_array.append(t.Type)
    return jsonify({ "all_models": all_model_type_array })


# TODO
# Return all models based on the parameter passed
@app.route('/api/v1/cars/model/<model>')
def get_model(model):
    return jsonify({ "model": model })
