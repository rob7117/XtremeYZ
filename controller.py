import config
import netUtil
import json
import ast
import service
from flask import Flask, request
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
        json_data = request.get_json(force=True)

        service.enterAccelerometerdata(json_data)

        print(json_data)

        return 200

class TrainingState(Resource):
    def post(self):
        json_data = request.get_json(force=True)

        service.enterTrainingState(json_data)

        return 200

class ProductionState(Resource):
    def post(self):
        json_data = request.get_json(force=True)

        return 'Invalid Command', 400

class User(Resource):
    def post(self):
        json_data = request.get_json(force=True)

        service.createUser(json_data)

        return 200
class Command(Resource):
    def post(self):
        #if config.bot['id'] not in jsonData["mentionedPeople"]:
        json_data = request.get_json(force=True)
        print(json_data)
        print(json_data)
        message = netUtil.getMessage(json_data['data']['id'])
        text = message['text'].replace("\'", "\"")
        words = text.split()
        command = words[0]

        # Open Commands
        if command.lower() == "report":
            return service.atDesk()
        
            #return service.atDesk(command)

        return 200


api.add_resource(Command, '/command')
api.add_resource(User, '/user')
api.add_resource(Accelerometer, '/accelerometer')
api.add_resource(TrainingState, '/trainingstate')
api.add_resource(ProductionState, '/productionstate')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')