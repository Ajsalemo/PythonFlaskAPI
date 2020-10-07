import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, abort
from flask_migrate import Migrate

from models import BMWCarModel, db

# Load dotenv
load_dotenv()


# Environment variables
# Local
POSTGRES_USERNAME = os.getenv('POSTGRES_USERNAME')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DATABASE = os.getenv('POSTGRES_DATABASE')
# Production
AZURE_POSTGRES_USERNAME = os.getenv('AZURE_POSTGRES_USERNAME')
AZURE_POSTGRES_PASSWORD = os.getenv('AZURE_POSTGRES_PASSWORD')
AZURE_POSTGRES_HOST = os.getenv('AZURE_POSTGRES_HOST')
AZURE_POSTGRES_PORT = os.getenv('AZURE_POSTGRES_PORT')
AZURE_POSTGRES_DATABASE = os.getenv('AZURE_POSTGRES_DATABASE')

app = Flask(__name__)

local_conn_str = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"
prod_conn_str = f"postgresql://{AZURE_POSTGRES_USERNAME}:{AZURE_POSTGRES_PASSWORD}@{AZURE_POSTGRES_HOST}:{AZURE_POSTGRES_PORT}/{AZURE_POSTGRES_DATABASE}"

app.config['SQLALCHEMY_DATABASE_URI'] = prod_conn_str
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
    return jsonify({"all_models": all_models_array})


# Return all generational types
# Format ex - "E46"
@app.route('/api/v1/cars/model_types')
def all_model_types():
    all_model_types = BMWCarModel.query.all()
    all_model_type_array = []
    for t in all_model_types:
        all_model_type_array.append(t.Type)
    return jsonify({"all_models": all_model_type_array})


# Return all models based on the parameter passed
@app.route('/api/v1/cars/models/<model>')
def get_model(model):
    specific_model = BMWCarModel.query.filter_by(Model=model).all()
    specific_model_array = [
        {
            "id": m.id,
            "Year": m.Production,
            "Model": m.Model,
            "Type": m.Type,
            "Engine_Type": m.Engine_Type,
            "Power": m.Power,
            "Body": m.Body,
            "Production_Number": m.Production_Number
        } for m in specific_model
    ]
    return jsonify({ "model": specific_model_array })


# Return all models based on the parameter passed
@app.route('/api/v1/cars/types/<gen_type>')
def get_type(gen_type):
    # Convert the passed parameter to uppcase to match the data in the CSV
    specific_type = BMWCarModel.query.filter_by(Type=gen_type.upper()).all()
    specific_type_array = [
        {
            "id": t.id,
            "Year": t.Production,
            "Model": t.Model,
            "Type": t.Type,
            "Engine_Type": t.Engine_Type,
            "Power": t.Power,
            "Body": t.Body,
            "Production_Number": t.Production_Number
        } for t in specific_type
    ]
    return jsonify({ "type": specific_type_array })


# Return all models based on the ID parameter
@app.route('/api/v1/cars/<int:id>')
def get_car_by_id(id):
    specific_id = BMWCarModel.query.filter_by(id=id).all()
    specific_id_array = [
        {
            "id": i.id,
            "Year": i.Production,
            "Model": i.Model,
            "Type": i.Type,
            "Engine_Type": i.Engine_Type,
            "Power": i.Power,
            "Body": i.Body,
            "Production_Number": i.Production_Number
        } for i in specific_id
    ]
    return jsonify({ "response": specific_id_array })



# Error handlers
# Return a JSON response for a HTTP 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({ "error": "The requested resource does not exist." }), 404

# Error handlers
# Return a JSON response for a HTTP 500
@app.errorhandler(500)
def not_found(error):
    return jsonify({ "error": "An application error occurred." }), 500


# Error handlers
# Return a JSON response for a HTTP 502
@app.errorhandler(502)
def not_found(error):
    return jsonify({ "error": "Bad Gateway." }), 502


# Error handlers
# Return a JSON response for a HTTP 504
@app.errorhandler(504)
def not_found(error):
    return jsonify({ "error": "A Gateway timeout has occurred." }), 504