from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from api import api

# App instance
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
app.register_blueprint(api, url_prefix="/api")
# DB instance
db = SQLAlchemy()
db.init_app(app)

print(app.url_map)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/users/details/<int:id>", methods=['GET'])
def get_user_by_id(id):
    pass

@app.route("/api/users/update/<int:id>", methods=['POST'])
def update_user_by_id(id):
    user_details = request.json['user']
    # Push to db
    
@app.route("/transaction/add", methods=["POST"])
def add_transaction():
    pass