from app import db
from datetime import datetime

class Stream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stream = db.Column(db.String())


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    stream_id = db.Column(db.Integer, primary_key=True)

