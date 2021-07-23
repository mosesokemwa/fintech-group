import json

from application.app import db
from application.models.application import Stream, Student

print('recreating DB tables')
db.drop_all()
db.create_all()

print('adding dummy data')

streams_data = json.loads(open('streams.json').read())
students_data = json.loads(open('students.json').read())


for stream in streams_data:
    db.session.add(Stream(**stream))

for student in students_data:
    db.session.add(Student(**student))


db.session.commit()
