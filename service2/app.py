from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class output(Resource):
    def get(self):
        return {'message': 'Hallo, ich bin Service2'}, 200

class nochmal(Resource):
    def get(self, name):
        return {'message': 'Hallo, ich bin {} und laufe auf Service 2'.format(name)}, 200


api.add_resource(output, "/service2/test")
api.add_resource(nochmal, "/service2/test/<string:name>")


if __name__ == '__main__':
    app.run()
