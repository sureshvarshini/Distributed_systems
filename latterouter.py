from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


# App instance
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
# DB instance
db = SQLAlchemy()
db.init_app(app)

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