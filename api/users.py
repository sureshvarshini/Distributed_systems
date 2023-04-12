from latterouter import app
from flask import request, jsonify
from database.models import add_user, update_user, update_user_points, get_user_points, get_user_info

@app.route("/users/<string:id>", methods=['POST', 'PUT'])
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

@app.route("/user/<string:userid>", methods=["GET"])
def get_user(userid):
    if request.method == 'GET':
        user = get_user_info(userid)
        response = jsonify(user)
        response.status_code = 200
        return response
    else:
        response = jsonify({'error': 'Invalid request method'})
        return response

@app.route("/user/<string:id>/points", methods=["GET", 'PUT'])
def user_points(id):
    if request.method == 'GET':
        response = jsonify(get_user_points(id))
        response.status_code = 200
        return response
    elif request.method == 'PUT':
        data = request.get_json()
        response = jsonify(update_user_points(id, data))
        return response