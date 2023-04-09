from latterouter import app
from flask import request, jsonify
from database.models import add_transaction, get_transactions

@app.route("/transactions/<int:id>", methods=['GET', 'POST'])
def transactions(id):
    if request.method == 'POST':
        data = request.get_json()
        transaction_id = add_transaction(data)
        response = jsonify({'transaction_id': transaction_id})
        return response
    elif request.method == 'GET':
        transactions = get_transactions(id)
        response = jsonify(transactions)
        return response