import os
from flask import Flask,sessions
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))
# print(basedir)
# print(__file__) -- basic.py
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db) # connect the application to database


class User(db.Model):

    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    dob = db.Column(db.Date)
    sex = db.Column(db.Text)

    def __init__(self,name,age,dob,sex):
        self.name = name
        self.age = age
        self.dob = dob
        self.sex = sex

    def __repr__(self):
        return f"Student Name :{self.name}\n Age :{self.age}\n DOB :{self.dob}\n sex : {self.sex}"



