# Distributed_systems
IMPLEMENTING A GLOBALLY-ACCESSIBLE DISTRIBUTED SERVICE - Loyalty card scheme in global café

# Running the application through docker
- Install docker
    - For fresh start on prevously installed docker.

        ```docker system prune```
        
        *NOTE: This command will remove all previous images and containers. Execute with caution.*
- Create docker network.

    ```docker network create -d bridge app-network```
- Run docker build command for each region .yml file. This command will install all the modules required by the application. *(Do this command for all specified regions.)*.

    ```docker-compose -f docker-compose-<region>.yml build```
- Compose up to start the application. *(Do this command for all specified regions.)*.

    ```docker-compose -f docker-compose-<region>.yml up```

    You should be able see all the containers up and application running at ports.

# Exposed APIs
## User registration management system
- */users/{id}* -> (POST, PUT, GET)

    - Add, update and fetch consumer detials by id
    - Sample POST payload:
    
    ```json
        {
            "email": "test-user-6@example.com",
            "name": "test-user-ire006",
            "user_id": "ire006",
            "region": "EUW/EUE"
        }  
    ```   
    - Sample PUT payload:

    ```json
        {
            "name": "test-user-ire006-new-name",
            "user_id": "ire006"
        }  
    ```  
## Loyalty points management system
- */users/{id}/points* -> (GET, PUT)
    - Fetch and update loyalty points by consumer id

    - Sample PUT payload to add points:

    ```json
        {
            "action": "add",
            "points": 13
        } 
    ```
    - Sample PUT payload to deduct points:

    ```json
        {
            "action": "deduct",
            "points": 7
        } 
    ```
## Transaction history management system
- */transactions/{id}* ->  (GET, POST)
    - Fetch and add consumer order transactions

    - Sample POST payload:

    ```json
        {
            "user_id": "ire004",
            "order_details": "latte"
        } 
    ```
