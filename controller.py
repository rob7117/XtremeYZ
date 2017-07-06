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

if __name__ == "__main__":
    app.run(debug=True)