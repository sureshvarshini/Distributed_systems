from __future__ import annotations

import argparse
import requests
from abc import ABC, abstractmethod
from typing import Any
import json

# Load the configuration from the JSON file
with open("../routes.json", "r") as f:
    config = json.load(f)

import sys
sys.path.append('../business_logic')
from Director import Director
from ConcreteBuilder1 import ConcreteBuilder1


def switch(builder, region, defaultPoint):
    if region == "IRE":
        builder.produce_part_a()
    if region == "FRA":
        builder.produce_part_b()
    if region == "IND":
        builder.produce_part_c()
    if region == "ROM":
        builder.produce_part_d()
    if region == "SPA":
        builder.produce_part_a()
        builder.produce_part_a()

    return builder.product.computePointsScheme(defaultPoint)


def constructObject(points):
    jsonObject = {"action": "deduct", "points": points}
    return jsonObject


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--region', type=str)
    parser.add_argument('--id', type=str)
    parser.add_argument('--order', type=str)
    args = parser.parse_args()

    print("Hello!")

    print("Here's a " + args.order)
    print("Deducting points for your purchase...")
    print("Updating transaction history")

    # API Request
    # add business logic points, with json payload
    # myobj = { "action": "<deduct/add>", "points": 25}
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    defaultPoints = 1
    points = switch(builder, args.region, defaultPoints)
    jsonObject = constructObject(points)
    print(jsonObject)

    region = config[args.region]["api_port"]

    url = "http://localhost:"+str(region)+"/users/" + args.id + "/" + "points"
    # may need to add data instead of json
    response = requests.put(url,json=jsonObject)
    data = response.json()
    print(data)

    #Update Transaction History
    id = 1 #What should this be?
    url = 'http://localhost:'+str(region)+'/transactions/' + str(id)
    response = requests.post(url,json={"user_id": args.id, "order_details": args.order})
    print(response)
    #data = response.json()
    #print(data)