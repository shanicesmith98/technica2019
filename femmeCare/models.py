# models.py
from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    account = db.Column(db.String(100))
    bank = db.Column(db.String(100))
    routing = db.Column(db.String(100))
    nonprofit = db.Column(db.String(100))
    total=db.Column(db.Float)

class Transaction(db.Model):
	id = db.Column(db.Integer,  primary_key=True)
	name = db.Column(db.String(100))
	user_id = db.Column(db.Integer)
	amt = db.Column(db.Float)


