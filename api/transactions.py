from latterouter import app
from flask import request

@app.route("/transaction/add", methods=["POST"])
def add_transaction():
    pass