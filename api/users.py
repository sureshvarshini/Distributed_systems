from latterouter import app
from flask import request, jsonify
from database.models import add_user, update_user, update_user_points, get_user_points, get_user_info
from config import REGION, AVAILABLE_REGIONS, redirect_request_to_region

@app.route("/users/<string:id>", methods=['POST', 'PUT'])
def points_data(id):
    if request.method == 'POST':
        # Adding new user
        data = request.get_json()
        if 'region' not in data or data['region'] not in AVAILABLE_REGIONS:
            response = jsonify({'error': 'Region missing or invalid region provided.'})
            response.status_code = 400
            return response
        try:
            user_id = add_user(data)
            print(user_id, flush=True)
            if user_id is not None:
                response = jsonify({'id': user_id, 'message': 'Sucessfully created.'})
                response.status_code = 200
            else:
                response = jsonify({'error': 'Unable to create'})
                response.status_code = 400
            return response
        except Exception as e:
            print(e)
            response = jsonify({'error': f'Exception occured while creating user. {str(e)}'})
            response.status_code = 400
            return response 
    else:
        # Update user
        user_region = id[:3]
        data = request.get_json()
        print(user_region, flush=True)
        if user_region != REGION:
            print(REGION, flush=True)
            print(request.url, flush=True)
            response = redirect_request_to_region(request.method, request.url, user_region, data)
            return response
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
        user_region = userid[:3]
        if user_region != REGION:
            print(REGION, flush=True)
            print(request.url, flush=True)
            response = redirect_request_to_region(request.method, request.url, user_region)
            return response
        user = get_user_info(userid)
        if user is not None:
            response = jsonify(user.as_dict())
            response.status_code = 200
        else:
            response = jsonify({'error': 'User not found'})
            response.status_code = 404
        return response

@app.route("/users/<string:id>/points", methods=["GET", 'PUT'])
def user_points(id):
    user_region = id[:3]
    if request.method == 'GET':
        print(user_region, flush=True)
        if user_region != REGION:
            print(REGION, flush=True)
            print(request.url, flush=True)
            response = redirect_request_to_region(request.method, request.url, user_region)
            return response
        response = jsonify(get_user_points(id))
        response.status_code = 200
        return response
    elif request.method == 'PUT':
        data = request.get_json()
        data = request.get_json()
        print(user_region, flush=True)
        if user_region != REGION:
            print(REGION, flush=True)
            print(request.url, flush=True)
            response = redirect_request_to_region(request.method, request.url, user_region, data)
            return response
        response = update_user_points(id, data)
        if 'error' in response:
            response = jsonify(response)
            response.status_code = 400
        return response