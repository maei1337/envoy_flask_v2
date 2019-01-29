from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class output(Resource):
    def get(self):
        return {'message': 'Hallo, ich bin Service1'}, 200

class nochmal(Resource):
    def get(self, name):
        return {'message': 'Hallo, ich bin {} und laufe auf Service 1'.format(name)}, 200


api.add_resource(output, "/service1/test")
api.add_resource(nochmal, "/service1/test/<string:name>")


if __name__ == '__main__':
    app.run()
