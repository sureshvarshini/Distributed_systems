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
    parser.add_argument('--name', type=str)
    parser.add_argument('--email', type=str)
    parser.add_argument('--change', type=str)
    args = parser.parse_args()
    
    print("Hello! Welcome to "+args.shop+" in the "+args.region+" region!")

    print("Updating your account details to the system...")

    # API Request
    region = config[args.region]["api_port"]
    json_o = {"user_id": args.id}

    if args.change == "name":
        json_o["name"] = args.name
    elif args.change == "email":
        json_o["email"] = args.email
    else:
        json_o["name"] = args.name
        json_o["email"] = args.email

    response = requests.put(f"http://127.0.0.1:{str(region)}/users/{args.id}", json=json_o)
    print(response.json())