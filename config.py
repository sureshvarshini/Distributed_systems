import json
import os
from flask import jsonify
import requests

# Load the configuration from the JSON file
with open("routes.json", "r") as f:
    config = json.load(f)

AVAILABLE_REGIONS = ('EUW', 'EUE')
REGION = os.environ.get("REGION")
API_PORT = config[REGION]['api_port']
MARIA_PORT = config[REGION]['maria_port']
MONGO_PORT = config[REGION]['mongo_port']
REDIS_PORT = config[REGION]['redis_port']

def redirect_request_to_region(request_method:str, url:str, region_code:str, payload:dict):
    new_api_port = config[region_code]['api_port']
    new_url = url.replace(str(API_PORT), str(new_api_port))
    new_url = new_url.replace('localhost', 'host.docker.internal')
    print(new_url)
    if request_method == 'POST':
        requests.post(new_url, json=payload)
    if request_method == 'PUT':
        requests.put(new_url, json=payload)
    if request_method == 'GET':
        requests.get(new_url, json=payload)