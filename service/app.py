from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class output(Resource):
    def get(self):
        return {'message': 'Hallo, ich bin ON'}, 200

class nochmal(Resource):
    def get(self):
        return {'message': 'Hallo, ich bin nochmal'}, 200

api.add_resource(output, "/test")
api.add_resource(nochmal, "/hoffe")


if __name__ == '__main__':
    app.run()
