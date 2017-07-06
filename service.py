from models import db
from models import *
from datetime import datetime

def enterTrainingState(json):
    user = db.session.query(User).filter_by(name=json['user']).first()
    trainingData = TrainingData(user.id, datetime.now().time(), json['user'])
    db.session.add(trainingData)
    db.session.commit()