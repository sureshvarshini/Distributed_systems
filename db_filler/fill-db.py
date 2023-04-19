import sys
import requests
import random
import json

# Load the configuration from the JSON file
with open("../routes.json", "r") as f:
    config = json.load(f)


files = {
   "FRA": "region_fran.txt",
   "IND": "region_ind.txt",
   "IRE": "region_ire.txt",
   "SPA": "region_spa.txt",
   "ROM": "region_rom.txt"
}


for i in range(50):
   random_region = random.choice(list(files.keys()))
   random_file = files[random_region]

   with open(random_file,'r') as file:
      random_line = random.choice(file.readlines())
      split_line = random_line.split('\n')
      user_info = split_line[0].split(',')
      user = {
         "email": user_info[2],
         "name": user_info[1],
         "region": random_region
      }
      region_port = str(config[random_region]['api_port'])
      url = f"http://localhost:{region_port}/users/0"
      try:
         res = requests.post(url, json=user)
         user_id = res.json()['id']
         print(res.json()['id'])
      except:
         "DB already contains user"
      #url = "http://localhost:"+str(region_port)+"/users/" + user_id+ "/" + "points"