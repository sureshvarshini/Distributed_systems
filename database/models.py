from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import update
from flask import jsonify
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
    user_id = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    points = db.Column(db.Integer)

    def __init__(self, userid, name, email):
        self.user_id = userid
        self.name = name
        self.email = email
        self.points = 0

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

def get_user_info(id):
    print('Fetching user data from Mariadb.', flush=True)
    found_user = User.query.filter_by(user_id=id).first()
    return found_user


def add_user(user_data):
    print('Adding new user data to mariadb.', flush=True)
    user_details = User(email=user_data["email"], name=user_data["name"], userid=user_data["user_id"])
    db.session.add(user_details)
    db.session.commit()
    print('Updating new user with 0 points to redis cache.', flush=True)
    redis_client.add_to_cache(user_data["user_id"], 0)
    return user_details.user_id

def update_user(user_data, id):
    print('Updating user data to mariadb.', flush=True)
    found_user = User.query.filter_by(user_id=id).first()
    if found_user is not None:
        if "email" in user_data:
            found_user.email = user_data["email"]
        if "name" in user_data:
            found_user.name = user_data["name"]
        if "points" in user_data:
            found_user.points = user_data["points"]
        db.session.commit()
    return found_user

def add_transaction(data):
    print('Adding user transactions to Mongodb.', flush=True)
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    item = {'user_id':data['user_id'], 'date': now, 'order_details': data['order_details']}
    id = transactions.insert_one(item)
    return str(id.inserted_id)

def get_transactions(user_id):
    print('Fetching user transactions from Mongodb.', flush=True)
    return list(transactions.find({"user_id":user_id}))

def get_user_points(user_id):
    # Get from redis cache
    points = redis_client.get_from_cache(user_id)
    print(type(points))
    if points is not None:
        print('Fetching user points from redis cache.', flush=True)
        data = {'user_id': user_id, 'points': int(points)}
    else:
        print('Fetching user points from mariadb.', flush=True)
        data = jsonify(db.first_or_404(db.select(User).filter_by(user_id=id)))
    return data

def update_user_points(user_id, data):
    points_data = get_user_points(user_id)
    user = get_user_info(user_id)
    points_to_deduct = data['points']
    print(points_data, flush=True)
    if data['action'] == 'deduct':
        if points_data['points'] - points_to_deduct < 0:
            response = {'error': 'Insufficient points. Could not deduct'}
            return response
        points_data['points'] -= points_to_deduct
    elif data['action'] == 'add':
        points_data['points'] += points_to_deduct
    print(f'Updating user points to mariadb.', flush=True)
    user.points = points_data['points']
    db.session.commit()

    # Update redis cache
    print('Updating user points to redis cache.', flush=True)
    redis_client.add_to_cache(points_data['user_id'], points_data['points'])

    return {'user_id': points_data['user_id'], 'points': points_data['points']}