from latterouter import db
import uuid

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    points = db.Column(db.Integer)

    def __init__(self, email, region):
        self.id = '-'.join(region, uuid.UUID())
        self.email = email


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    