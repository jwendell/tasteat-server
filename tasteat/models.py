from db import db


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
