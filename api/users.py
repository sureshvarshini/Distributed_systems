from latterouter import app
from api import api
from flask import request, jsonify
from database.models import add_user, update_user, update_user_points, get_user_points, get_user

@app.route("/users/<int:id>", methods=['GET', 'POST', 'PUT'])
def user(id):
    if request.method == 'POST':
        # Adding new user
        data = request.get_json()
        user_id = add_user(data)
        if user_id is not None: 
            response = jsonify({'id': user_id})
            response.status_code = 200
            return response
        else:
            response = jsonify({'error': 'User not found'})
            response.status_code = 404
            return response
    
    elif request.method == 'GET':
        # Get user from id
        response = jsonify(get_user(id))
        response.status_code = 200
        return response
    
    else:
        # Update user
        data = request.get_json()
        user_id = update_user(data)
        if user_id is not None: 
            response = jsonify({'id': user_id})
            response.status_code = 200
            return response
        else:
            response = jsonify({'error': 'Error adding user'})
            response.status_code = 500
            return response

@app.route("/user/<int:id>/points", methods=["GET", 'PUT'])
def user_points(id):
    if request.method == 'GET':
        response = jsonify(get_user_points(id))
        response.status_code = 200
        return response
    elif request.method == 'PUT':
        data = request.get_json()
        response = jsonify(update_user_points(data))
        return response