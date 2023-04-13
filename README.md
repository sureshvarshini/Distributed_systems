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

    ```docker-compose -f .\docker-compose-ire.yml -f .\docker-compose-fra.yml -f .\docker-compose-ind.yml -f .\docker-compose-spa.yml -f .\docker-compose-rom.yml build```
- Compose up to start the application. *(Do this command for all specified regions.)*.

    ```docker-compose -f .\docker-compose-ire.yml -f .\docker-compose-fra.yml -f .\docker-compose-ind.yml -f .\docker-compose-spa.yml -f .\docker-compose-rom.yml up```

    You should be able see all the containers up and application running at ports.
- Compose down to stop the application. *(Do this command for all specified regions.)*.

    ```docker-compose -f .\docker-compose-ire.yml -f .\docker-compose-fra.yml -f .\docker-compose-ind.yml -f .\docker-compose-spa.yml -f .\docker-compose-rom.yml down```

# Server Home Page - by region
## Ireland
- *http://localhost:5010/index*

        IRE - Latte
## France
- *http://localhost:5011/index*

        FRA - Latte

## Spain
- *http://localhost:5000/index*

        SPA - Latte

## India
- *http://localhost:5012/index*

        IND - Latte

## Romania
- *http://localhost:5013/index*

        ROM - Latte

# Exposed APIs
## User registration management system
- */users/{id}* -> (POST, PUT, GET)

    - Add, update and fetch consumer detials by id
    - Sample POST payload:
    
    ```json
        {
            "email": "test-user-6@example.com",
            "name": "test-user-ire006",
            "region": "IRE/FRA/SPA/IND/ROM"
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
# Running simulations with TMUX
- TMUX comes with any Linux distribution or can be installed with the Cygwin package manager.

- Open a Cygwin terminal and cd to the network_emulation directory.

- Run the command: ```.scenarios/<scenario_name>```

Where secenario_name is the filename of the selected scenario definition. e.g. base_scenario, this will start a new tmux session and the simulation will start to process.

- Run the command ```tmux attach``` to enter the tmux session.

- Press ctrl+b then w to observe all the windows in a list. A smaller view will show what is being processed on the current window. This will be the occurring transaction.

- To exit tmux, select a window in the list and enter the command ```tmux kill-server```. This will exit and kill the simulation and return you to the normal terminal.

