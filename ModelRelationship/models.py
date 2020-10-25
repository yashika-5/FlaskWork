import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__name__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Student(db.Model):

    __tablename__ = 'students'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)

    # one to many
    # students to many books
    books = db.relationship('Book',backref='student',lazy='dynamic')

    # one to onee
    # one student to one college
    colleges = db.relationship('College',backref='student',uselist=False)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if self.colleges:
            return f"Student name is {self.name} and college name is {self.colleges.name}"
        else:
            return f"Student name is {self.name} and has no college yet!"

    def report_books(self):
        print("Here are my books")
        for book in self.books:
            print(book.book_name)


class Book(db.Model):

    __tablename__ = 'books'

    id = db.Column(db.Integer,primary_key=True)
    book_name = db.Column(db.Text)
    student_id = db.Column(db.Integer,db.ForeignKey('students.id'))

    def __init__(self,book_name,student_id):
        self.book_name = book_name
        self.student_id = student_id



class College(db.Model):

    __tablename__ = 'colleges'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    student_id = db.Column(db.Integer,db.ForeignKey('students.id'))

    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id

