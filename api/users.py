from latterouter import app
from api import api
from flask import request

@app.route("/users/details/<int:id>", methods=['GET'])
def get_user(id):
    pass

@app.route("/users/update/<int:id>", methods=['POST'])
def update_user(id):
    user_details = request.json['user']
    # Push to db
    
