from controller import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xyz@localhost/xyz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a base model for other database tables to inherit
class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)

class User(Base):
    __tablename__ = 'users'

    name = db.Column(db.String(64))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Name %r>' % self.name

class AccelerometerData(Base):
    __tablename__ = 'accelerometerdata'

    user_id = db.Column(db.Integer)
    time = db.Column(db.DateTime)
    x = db.Column(db.Float)
    y = db.Column(db.Float)
    z = db.Column(db.Float)
    train = db.Column(db.Boolean)
    calculated = db.Column(db.Boolean)

    def __init__(self, user_id, time, x, y, z):
        self.user_id = user_id
        self.time = time
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return '<Name %r>' % self.id

class TrainingData(Base):
    __tablename__ = 'trainingdata'

    user_id = db.Column(db.Integer)
    time = db.Column(db.DateTime)
    state = db.Column(db.Boolean)

    def __init__(self, user_id, time, state):
        self.user_id = user_id
        self.time = time
        self.state = state

    def __repr__(self):
        return '<Name %r>' % self.id

class ProductionData(Base):
    __tablename__ = 'productiondata'

    user_id = db.Column(db.Integer)
    time = db.Column(db.DateTime)
    state = db.Column(db.Boolean)

    def __init__(self, user_id, time, state):
        self.user_id = user_id
        self.time = time
        self.state = state

    def __repr__(self):
        return '<Name %r>' % self.id