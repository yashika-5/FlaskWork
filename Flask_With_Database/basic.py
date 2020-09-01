import os
from flask import Flask,sessions
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))
# print(basedir)
# print(__file__) -- basic.py
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):

    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    dob = db.Column(db.Date)

    def __init__(self,name,age,dob):
        self.name = name
        self.age = age
        self.dob = dob

    def __repr__(self):
        return f"Student Name :{self.name}\n Age :{self.age}\n DOB :{self.dob}"



