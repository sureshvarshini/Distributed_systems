import sys
from random import randint
region = sys.argv[1]

f_names = ["liam", "noah", "oliver", "elijah", "james", "william", "ben", "lucas", "henry", "theo", "olivia", "emma", "ava", "isabella", "mia", "flora", "clover", "daisy", "ella", "lucy"]
l_names = ["smith", "brown", "jones", "miller", "moore", "lunt", "allen", "green", "baker", "gomez", "mcardle", "henry", "fletcher"]
emails = ["@gmail.com", "@yahoo.com", "@hotmail.com"]
users = []


for i in range(1000):
    first_name = f_names[randint(0, len(f_names)-1)]
    last_name = l_names[(randint(0, len(l_names)-1))]
    email = first_name +str(i)+emails[randint(0, len(emails)-1)]
    user = str(region +str(i +100000))+","+first_name+" "+last_name+","+email
    users.append(user)

with open('region_'+region+".txt",  'w') as f:
    for user in users:
        f.write(user)
        f.write("\n")


