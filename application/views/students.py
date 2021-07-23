from flask_restful import Resource
from app import db

class StudentsListView(Resource):
    def get(self):
        """ Simple search endpoint that returns log messages. """

        statement = """select * from students"""

        ret_value = []
        for r in db.engine.execute(statement):
            student_as_dict = dict(r)
            student_as_dict['created'] = str(student_as_dict['created'])
            ret_value.append(student_as_dict)

        return ret_value


class StudentsSingleView(Resource):

    def get(self, id):
        """ Simple search endpoint that returns log messages. """

        statement = """select * from students where '%s'""" % (id)

        ret_value = []
        for r in db.engine.execute(statement):
            student_as_dict = dict(r)
            student_as_dict['created'] = str(student_as_dict['created'])
            ret_value.append(student_as_dict)

        return ret_value

    def put(self, id):
        """ Simple search endpoint that returns log messages. """

        statement = """select * from students where '%s'""" % (id)

        ret_value = []
        for r in db.engine.execute(statement):
            student_as_dict = dict(r)
            student_as_dict['created'] = str(student_as_dict['created'])
            ret_value.append(student_as_dict)

        return ret_value



