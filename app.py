from flask import Flask, jsonify, render_template
from flask_migrate import Migrate

from models import BMWCarModel, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ajsalemo:Dudebug1992@localhost:5432/bmw_database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def home():
    return render_template('home.html')


# v1 API routes
@app.route('/api/v1/test_endpoint/all')
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
