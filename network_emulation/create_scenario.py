import random

# Define the list of regions
regions = ["IRE", "FRA", "ROM", "SPA"]

# Read the list of ids from a file and store them in a list
with open("ids.txt") as f:
    ids = f.readlines()
ids = [x.strip() for x in ids]

# Define the list of orders
orders = ["Water", "HotChocolate", "Tea", "Latte", "Cappuccino", "Americano", "Croissant"]

# Define the list of functions
functions = [
    "purchase_add.py",
    "purchase_deduct.py",
    "read_points.py",
    "read_transaction_history.py",
    "read_user_details.py",
    "update_user_details.py",
]

detail_change = ["email","name","both"]

shops = ["1","2","3","4","5"]

new_detail_count = 0

# Define the number of iterations
num_iterations = 100

# Loop through the iterations and print the strings
for i in range(num_iterations):
    # Generate a random shop number between 1 and 20
    shop_number = random.randint(1, 20)
    # Choose a random region from the list
    region = random.choice(regions)
    # Choose a random id from the list
    id = random.choice(ids)
    # Choose a random order from the list
    order = random.choice(orders)
    # Choose a random function from the list
    function = random.choice(functions)
    # Choose random shop
    shop = random.choice(shops)
    # Print the string
    if function == "purchase_add.py":
        print(f"tmux send-keys -t Shops:s{shop_number} 'python {function} --shop {shop} --region {region} --id {id} --order {order}'")
    elif function == "purchase_deduct.py":
        print(f"tmux send-keys -t Shops:s{shop_number} 'python {function} --region {region} --id {id} --order {order}'")
    elif function == "update_user_details.py":
        change = random.choice(detail_change)
        print(f"tmux send-keys -t Shops:s{shop_number} 'python {function} --region {region} --id {id} --name new_name{new_detail_count} --email new_email{new_detail_count}@example.com --change {change}'")
        new_detail_count+=1
    else:
        print(f"tmux send-keys -t Shops:s{shop_number} 'python {function} --region {region} --id {id}'")
    
    # Every random number of iterations, sleep for a random amount of time
    if random.randint(1, 3) == 1:
        sleep_time = random.randint(2, 18)
        print(f"tmux send-keys -t Shops:s{shop_number} 'Sleep {sleep_time}'")
