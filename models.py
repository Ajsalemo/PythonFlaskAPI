from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BMWCarModel(db.Model):
    __tablename__ = "BMWCarTable"

    id = db.Column(db.Integer, primary_key=True)
    Production = db.Column(db.String)
    Model = db.Column(db.String)
    Type = db.Column(db.String)
    Displacement = db.Column(db.String)
    Engine_Type = db.Column(db.String)
    Power = db.Column(db.String)
    Body = db.Column(db.String)
    Production_Number = db.Column(db.String)
    Image = db.Column(db.String)

    def __init__(self, Production, Model, Type, Displacement, Engine_Type, Power, Body, Production_Number, Image):
        self.id = id
        self.Production = Production
        self.Model = Model
        self.Type = Type
        self.Displacement = Displacement
        self.Engine_Type = Engine_Type
        self.Power = Power
        self.Body = Body
        self.Production_Number = Production_Number
        self.Image = Image

    def __repr__(self):
        return f"{self.Production}:{self.Model}"
