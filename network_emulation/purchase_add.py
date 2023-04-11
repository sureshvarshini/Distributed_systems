from __future__ import annotations

import argparse
import requests
from abc import ABC, abstractmethod
from typing import Any

from business_logic.Director import Director
from business_logic.ConcreteBuilder1 import ConcreteBuilder1


def switch(builder, region, defaultPoint):
    if region == "ire":
        builder.produce_part_a()
    if region == "fran":
        builder.produce_part_b()
    if region == "ind":
        builder.produce_part_c()
    if region == "rom":
        builder.produce_part_d()
    if region == "spa":
        builder.produce_part_a()
        builder.produce_part_a()

    return builder.product.computePointsScheme(defaultPoint)


def constructObject(points):
    jsonObject = {"action": "<add>", "points": points}
    return jsonObject


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--shop', type=str)
    parser.add_argument('--region', type=str)
    parser.add_argument('--id', type=str)
    parser.add_argument('--order', type=str)
    args = parser.parse_args()

    print("Hello! Welcome to " + args.shop + " in the " + args.region + " region!")

    print("Here's a " + args.order)
    print("Adding points for your purchase...")
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

    url = "https://jsonplaceholder.typicode.com/posts/" + points
    # may need to add data instead of json
    response = requests.post(url, json=jsonObject)
    data = response.json()
    print(data)
