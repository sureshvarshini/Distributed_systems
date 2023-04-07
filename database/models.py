from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import uuid
import json
from pymongo import MongoClient
from datetime import datetime


db = SQLAlchemy()
client = MongoClient('localhost', 3002,username='root', password='pass')
mdb = client.flask_db
transactions = mdb.transactions


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    points = db.Column(db.Integer)
    def __init__(self, email, region):
        self.user_id = "-" + region +str(uuid.uuid4())
        self.email = email
        self.points = 0


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(120))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    def __init__(self, user_id):
        self.user_id = user_id


def getUser(id):
    found_user = User.query.filter_by(user_id=id).first()
    data = {}
    data['user_id'] = found_user.user_id
    data['email'] = found_user.email
    data['points'] = found_user.points
    return json.dumps(data)


def addUser(request):
    user_details = User(email=request.json.get("email"), region=request.json.get("region"))
    db.session.add(user_details)
    db.session.commit()
    return user_details.user_id

def updateUser(id, points):
    found_user = User.query.filter_by(user_id=id).first()
    found_user.points = points
    db.session.add(found_user)
    db.session.commit()
    return str(found_user.points)


def addTransaction(user_id):
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    print(now)
    item = {'user_id':user_id, 'date': now}
    transactions.insert_one(item)
    return user_id

def getTransactions(user_id):
    
    return json.dumps(list(transactions.find({"user_id":user_id})), default=str)