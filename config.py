import json
import os
from flask import jsonify
import requests

# Load the configuration from the JSON file
with open("routes.json", "r") as f:
    config = json.load(f)

AVAILABLE_REGIONS = ('IRE', 'FRA', 'SPA', 'IND', 'ROM')
REGION = os.environ.get("REGION")
API_PORT = config[REGION]['api_port']
MARIA_ADDRESS = config[REGION]['maria_address']
MONGO_ADDRESS = config[REGION]['mongo_address']
REDIS_ADDRESS = config[REGION]['redis_address']

def redirect_request_to_region(request_method:str, url:str, region_code:str, payload:dict = None):
    new_api_port = config[region_code]['api_port']
    new_url = url.replace(str(API_PORT), str(new_api_port))
    new_url = new_url.replace('localhost', region_code.lower() + '-app')
    print(new_url, flush=True)
    if request_method == 'POST':
        requests.post(new_url, json=payload)
    if request_method == 'PUT':
        requests.put(new_url, json=payload)
    if request_method == 'GET':
        requests.get(new_url, json=payload)