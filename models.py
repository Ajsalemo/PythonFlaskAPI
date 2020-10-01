from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BMWCarModel(db.Model):
    __tablename__ = "BMWCarTable"

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String())
    model = db.Column(db.String())
    year = db.Column(db.Integer())
    horsepower = db.Column(db.Integer())

    def __init__(self, make, model, year, horsepower):
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.horsepower = horsepower
        
    def __repr__(self):
        return f"{self.make}:{self.model}"