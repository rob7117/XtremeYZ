from models import db
from models import *
from datetime import datetime
import netUtil
import json
from sklearn.svm import SVC
from sklearn.externals import joblib
import numpy

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
    print str(json['x']) + "x  " + str(json['y']) + "y   "
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
    results = list(db.session.query(AccelerometerData).filter_by(user_id=user.id).order_by(AccelerometerData.time.desc()).limit(15))

    svm = SVC()
    svm = joblib.load('/home/kilmoore/svm.pkl')
    x = numpy.array([])
    vallist = []
    arrayvals = numpy.array([])
    for result in results:        
	print "PROCESSING - " + str(result.x) + "x  "+ str(result.y)+ "y  " + str(result.z)+ "z"
	value = numpy.array([int(result.x), int(result.y), int(result.z)])
       
    	x = svm.predict(value)
	
	vallist.append(x[0])
    sitcount = 0
    standcount = 0
    for prediction in vallist:
	if "sitting" in prediction:
	    sitcount += 1
	if "walking" in prediction:
	    standcount += 1

    if standcount > 8:
	    message = "{} is not at their desk!".format(name)
    elif sitcount > 8: 
	    message = "{} is at their desk!".format(name)
    else:
	    message = "{} may or may not be at their desk, I'm not sure :(".format(name)
    netUtil.sendMessage(message, None)
    print vallist
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
