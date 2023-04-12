from latterouter import app
from flask import request, jsonify
from database.models import add_user, update_user, update_user_points, get_user_points, get_user_info

@app.route("/users/<string:id>", methods=['POST', 'PUT'])
def points_data(id):
    if request.method == 'POST':
        # Adding new user
        data = request.get_json()
        try:
            user_id = add_user(data)
            if user_id is not None:
                response = jsonify({'id': user_id, 'message': 'Sucessfully created.'})
                response.status_code = 200
            else:
                response = jsonify({'error': 'User with given details already registered.'})
                response.status_code = 400
            return response
        except:
            response = jsonify({'error': 'User with given details already registered.'})
            response.status_code = 400
            return response

    
    else:
        # Update user
        data = request.get_json()
        user = update_user(data, id)
        if user is not None:
            response = jsonify({'id': user.user_id, 'message': 'Sucessfully updated.'})
            response.status_code = 200
            return response
        else:
            response = jsonify({'error': 'User not found'})
            response.status_code = 404
            return response

@app.route("/users/<string:userid>", methods=["GET"])
def get_user(userid):
    if request.method == 'GET':
        user = get_user_info(userid)
        if user is not None:
            response = jsonify(user.as_dict())
            response.status_code = 200
        else:
            response = jsonify({'error': 'User not found'})
            response.status_code = 404
        return response
    else:
        response = jsonify({'error': 'Invalid request method'})
        return response

@app.route("/users/<string:id>/points", methods=["GET", 'PUT'])
def user_points(id):
    if request.method == 'GET':
        response = jsonify(get_user_points(id))
        response.status_code = 200
        return response
    elif request.method == 'PUT':
        data = request.get_json()
        response = update_user_points(id, data)
        if 'error' in response:
            response = jsonify(response)
            response.status_code = 400
        return response