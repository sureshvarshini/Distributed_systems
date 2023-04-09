from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from api import api
from database.models import mdb, db, User, getUser, addUser, updateUser, addTransaction, getTransactions


# App instance
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pass@localhost:3001/db'
app.register_blueprint(api, url_prefix="/api")
# DB instance
db.init_app(app)


with app.app_context():
    db.create_all()

print(app.url_map)



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/users/<string:id>", methods=['GET'])
def get_user_by_id(id):
    return getUser(id) 

@app.route("/api/users/", methods=['POST'])
def add_user():
    return addUser(request)

@app.route("/api/users//<int:points>", methods=['PUT'])
def update_user_by_id(id, points):
    return updateUser(id, points)
    
@app.route("/transaction/add/<string:id>", methods=["POST"])
def add_transaction(id):
    return addTransaction(id)
    
@app.route("/transaction/get/<string:id>", methods=["GET"])
def get_transaction(id):
    return getTransactions(id)
        
