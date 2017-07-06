import config
import netUtil
import json
import ast
import service
from flask import Flask
from flask_restful import reqparse, Resource, Api

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('data')

@app.route("/ping")
def ping():
    return "XtremeYZ is Online."

class Accelerometer(Resource):
    def post(self):
        args = parser.parse_args()

        jsonData = json.load(args.data)

        return 'Invalid Command', 400

class TrainingState(Resource):
    def post(self):
        args = parser.parse_args()

        jsonData = json.load(args.data)
        
        print(jsonData)
        return 'Invalid Command', 400


class ProductionState(Resource):
    def post(self):
        args = parser.parse_args()

        jsonData = json.load(args.data)

        return 'Invalid Command', 400

api.add_resource(Accelerometer, '/accelerometer')
api.add_resource(TrainingState, '/trainingstate')
api.add_resource(ProductionState, '/productionstate')

if __name__ == "__main__":
    app.run(debug=True)