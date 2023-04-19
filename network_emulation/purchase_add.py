from __future__ import annotations

import argparse
import requests
from abc import ABC, abstractmethod
from typing import Any
import json

import sys

sys.path.append('../business_logic')
from Director import Director
from ConcreteBuilder1 import ConcreteBuilder1
from ConcreteBuilder2 import ConcreteBuilder2
from ConcreteBuilder3 import ConcreteBuilder3
from ConcreteBuilder4 import ConcreteBuilder4
from ConcreteBuilder5 import ConcreteBuilder5

# Load the configuration from the JSON file
with open("../routes.json", "r") as f:
    config = json.load(f)

def switchShop(builder, shop, defaultPoint):
    if shop == "Cafe1":
        builder.produce_part_a()
    if shop == "Cafe2":
        builder.produce_part_b()
    if shop == "Cafe3":
        builder.produce_part_c()
    if shop == "Cafe4":
        builder.produce_part_d()
    if shop == "Cafe5":
        builder.produce_part_a()
        builder.produce_part_a()

    return builder.product.computePointsScheme(defaultPoint)


def switchBuilder(region, director):
    if region == "IRE":
        director.builder = ConcreteBuilder1()
    if region == "FRA":
        director.builder = ConcreteBuilder2()
    if region == "IND":
        director.builder = ConcreteBuilder3()
    if region == "ROM":
        director.builder = ConcreteBuilder4()
    if region == "SPA":
        director.builder = ConcreteBuilder5()

    return director.builder


def constructObject(points):
    jsonObject = {"action": "add", "points": points}
    return jsonObject


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--shop',type=str)
    parser.add_argument('--region', type=str)
    parser.add_argument('--id', type=str)
    parser.add_argument('--order', type=str)
    args = parser.parse_args()

    print("Hello!")

    print("Here's a " + args.order)
    print("Adding points for your purchase...")

    # API Request
    # add business logic points, with json payload
    # myobj = { "action": "<deduct/add>", "points": 25}
    director = Director()
    director.builder = switchBuilder(args.region, director)

    defaultPoints = 1
    points = switchShop(director.builder, args.shop, defaultPoints)
    jsonObject = constructObject(points)
    #print(jsonObject)

    region = config[args.region]["api_port"]

    # Add points
    url = "http://localhost:"+str(region)+"/users/" + args.id + "/" + "points"
    response = requests.put(url, json=jsonObject)
    data = response.json()
    print(data)

    print("Updating transaction history...")
    #Update Transaction History
    id = 1 #What should this be?
    url = 'http://localhost:'+str(region)+'/transactions/' + str(id)
    response = requests.post(url,json={"user_id": args.id, "order_details": args.order})
    print(response)
    #data = response.json()
    #print(data)
