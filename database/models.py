from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import uuid
from pymongo import MongoClient
from datetime import datetime
from latterouter import redis_client


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


def get_user(id):
    found_user = User.query.filter_by(user_id=id).first()
    data = {}
    data['user_id'] = found_user.user_id
    data['email'] = found_user.email
    data['points'] = found_user.points
    return data


def add_user(user_data):
    user_details = User(email=user_data["email"], region=user_data["region"])
    db.session.add(user_details)
    db.session.commit()
    return user_details.user_id

def update_user(user_data):
    found_user = User.query.filter_by(user_id=id).first()
    found_user.from_dict(user_data, new_user = False)
    db.session.commit()
    return {'user_id': found_user.user_id}

def add_transaction(data):
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    item = {'user_id':data['user_id'], 'date': now, 'order_details': data['order_details']}
    id = transactions.insert_one(item)
    return id

def get_transactions(user_id):
    return list(transactions.find({"user_id":user_id}))

def get_user_points(user_id):
    # Get from redis cache
    points = redis_client.get_from_cache(user_id)
    if points is not None:
        data = {'user_id': user_id, 'points': points}
    else:
        user = User.query.filter_by(user_id=id).first()
        data = {'user_id': user.user_id, 'points': user.points}
    return data

def update_user_points(user_id, data):
    user = get_user_points(user_id)
    if data['action'] == 'deduct':
        user.points -= data['points']
    if data['action'] == 'add':
        user.points += data['points']
    db.session.commit()

    # Update redis cache
    redis_client.add_to_cache(user.user_id, user.points)

    return {'user_id': user.user_id, 'points': user.points}