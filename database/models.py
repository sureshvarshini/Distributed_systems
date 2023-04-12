from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import uuid
from pymongo import MongoClient, errors
from datetime import datetime
from cache.redis_cache import RedisClient

db = SQLAlchemy()
client = MongoClient(host='mongodb', port=27017, username='root', password='pass')
# Connect to database - db
mdb = client["db"]
# Connect to collections - transactions
transactions = mdb["transactions"]
print("Connected to MONGODB")
# Connect to redis
redis_client = RedisClient()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(120))
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    points = db.Column(db.Integer)
    def __init__(self, userid, name, email):
        self.user_id = userid
        self.name = name
        self.email = email
        self.points = 0


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(120))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    def __init__(self, user_id):
        self.user_id = user_id


def get_user_info(id):
    print('Fetching user data from Mariadb.', flush=True)
    found_user = User.query.filter_by(user_id=id).first()
    data = {}
    data['user_id'] = found_user.user_id
    data['email'] = found_user.email
    data['points'] = found_user.points
    return data


def add_user(user_data):
    print('Adding new user data to mariadb.', flush=True)
    user_details = User(email=user_data["email"], name=user_data["name"], userid=user_data["user_id"])
    db.session.add(user_details)
    db.session.commit()
    return user_details.user_id

def update_user(user_data):
    print('Updating user data to mariadb.', flush=True)
    found_user = User.query.filter_by(user_id=user_data["user_id"]).first()
    if "email" in user_data:
        found_user.email = user_data["email"]
    if "name" in user_data:
        found_user.name = user_data["name"]
    if "points" in user_data:
        found_user.points = user_data["points"]
    # found_user.from_dict(user_data, new_user = False)
    db.session.commit()
    return {'updated_user': found_user.user_id}

def add_transaction(data):
    print('Adding user transactions to Mongodb.', flush=True)
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    item = {'user_id':data['user_id'], 'date': now, 'order_details': data['order_details']}
    id = transactions.insert_one(item)
    return id

def get_transactions(user_id):
    print('Fetching user transactions from Mongodb.', flush=True)
    return list(transactions.find({"user_id":user_id}))

def get_user_points(user_id):
    # Get from redis cache
    points = redis_client.get_from_cache(user_id)
    if points is not None:
        print('Fetching user points from redis cache.', flush=True)
        data = {'user_id': user_id, 'points': points}
    else:
        print('Fetching user points from mariadb.', flush=True)
        user = User.query.filter_by(user_id=user_id).first()
        data = {'user_id': user.user_id, 'points': user.points}
    return data

def update_user_points(user_id, data):
    user = get_user_points(user_id)
    if data['action'] == 'deduct':
        user.points -= data['points']
    if data['action'] == 'add':
        user.points += data['points']
    print('Updating user points to mariadb.', flush=True)
    db.session.commit()

    # Update redis cache
    print('Updating user points to redis cache.', flush=True)
    redis_client.add_to_cache(user.user_id, user.points)

    return {'user_id': user.user_id, 'points': user.points}