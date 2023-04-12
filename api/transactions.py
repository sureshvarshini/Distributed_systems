from latterouter import app
from flask import request, jsonify
from database.models import add_transaction, get_transactions


@app.route("/transactions/<int:id>", methods=['POST'])
def transactions(id):
    if request.method == 'POST':
        data = request.get_json()
        transaction_id = add_transaction(data)
        response = jsonify({'transaction_id': transaction_id})
        return response
    else:
        response = jsonify({'error': 'Invalid request method'})
        return response


@app.route("/transactions/<string:userid>", methods=["GET"])
def get_user_transactions(userid):
    if request.method == 'GET':
        transactions = get_transactions(userid)
        response = jsonify(transactions)
        return response
    else:
        response = jsonify({'error': 'Invalid request method'})
        return response
