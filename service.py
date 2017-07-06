from models import db
from models import *
from datetime import datetime
import netUtil

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

def atDesk(variables):
    if not len(variables) == 1:
        return 'Incorrect number of arguments provided', 400
    username = variables[0]
    user = db.session.query(User).filter_by(name=username).first()
    if user == None:
        return 'User not found', 404

    # TODO:
    # Query accelerometer data

    message = "{} is at their desk!".format(username)
    print(message)
    netUtil.sendMessage(message, None)

    return 200
