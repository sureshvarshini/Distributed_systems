import argparse
import requests
import json

# Load the configuration from the JSON file
with open("../routes.json", "r") as f:
    config = json.load(f)

if __name__ =="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--shop', type=str)
    parser.add_argument('--region', type=str)
    parser.add_argument('--id', type=str)
    args = parser.parse_args()
    
    print("Hello! Welcome to "+args.shop+" in the "+args.region+" region!")

    print("Getting your account details...")

    #API Request
    region = config[args.region]["api_port"]
    response = requests.get(f"http://localhost:{str(region)}/users/{args.id}")
    data = response.json()
    print(data)