from models import db
from models import *
from datetime import datetime
import netUtil
import json

def enterTrainingState(json):
    user = db.session.query(User).filter_by(name=json['user']).first()
    if int(json['state']) == 0:
        state = False
    else:
        state = True
    trainingData = TrainingData(user.id, datetime.now(), state)
    db.session.add(trainingData)
    db.session.commit()

def enterAccelerometerdata(json):
    user = db.session.query(User).filter_by(name=json['user']).first()
    accelerometerdata = AccelerometerData(user.id, datetime.now(), json['x'], json['y'], json['z'])
    db.session.add(accelerometerdata)
    db.session.commit()

def createUser(json):
    user = User(json['name'])
    db.session.add(user)
    db.session.commit()

def atDesk(name):
    user = db.session.query(User).filter_by(name=name).first()
    if user == None:
        netUtil.sendMessage('{} is not in our system'.format(name), None)
        return 'User not found', 404

    # TODO:
    # Query accelerometer data

    message = "{} is at their desk!".format(name)
    netUtil.sendMessage(message, None)

    return 200

def report():
    with open("alerts.json") as json_file:
        alerts = json.load(json_file)
        message = alerts['report_status'].format(10, "20 minutes", "8hrs")
        netUtil.sendMessage(None, message)

    return 200

def alert():
    with open("alerts.json") as json_file:
        alerts = json.load(json_file)
        message = alerts['alarm_home']
        netUtil.sendMessage(None, message)

    return 200