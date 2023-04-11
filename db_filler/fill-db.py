import sys
import requests

file_name = sys.argv[1]

file = open(file_name, 'r')
for line in file:
   split_line = line.split('\n')
   user_info = split_line[0].split(',')
   user = {
      "user_id": user_info[0],
      "name": user_info[1],
      "email": user_info[2],
      "points": 0 
   }
   url = "http://localhost:5000/users/"+user_info[0]
   res = requests.post(url, json=user)
   print(res)