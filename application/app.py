from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

from views.students import StudentsListView, StudentsSingleView

api.add_resource(StudentsListView, '/students')
api.add_resource(StudentsSingleView, '/students/<int:id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
