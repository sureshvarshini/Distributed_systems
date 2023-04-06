import argparse
import requests

if __name__ =="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--shop', type=str)
    parser.add_argument('--region', type=str)
    parser.add_argument('--id', type=str)
    args = parser.parse_args()
    
    print("Hello! Welcome to "+args.shop+" in the "+args.region+" region!")

    print("Checking points balnce for you...")

    #API Request
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    data = response.json()
    print(data)