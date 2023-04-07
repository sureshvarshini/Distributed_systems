# Distributed_systems
IMPLEMENTING A GLOBALLY-ACCESSIBLE DISTRIBUTED SERVICE - Loyalty card scheme in global café

# Install required packages
```pip install requirements.txt```

# Running redis as docker image - windows
- Install docker
- Run redis image docker command (Needs to done only once)

    ```docker run --name my-redis -p 6379:6379 -d redis```
- To get inside redis-container
   
    ```docker exec -it my-redis sh```
- To run redis command line

    ```redis-cli```
- To stop redis, fist list all containers

    ``` docker ps -a```
    
    and stop that container ID

    ```docker stop <container-ID>```
- To restart redis server

    ```docker start <container-ID>```
    
# Running mariadb as docker image - windows
- Install docker
- Run mariadb image docker command 

    ```docker run --name mariadb -e MYSQL_ROOT_PASSWORD=pass  -e MARIADB_DATABASE=db -p 3001:3306 -d docker.io/library/mariadb:10.3```

# Running mongodb as docker image - windows
- Run mariadb image docker command 
    ```docker run --name mongodb -e MONGO_INITDB_ROOT_USERNAME=root  -e MONGO_INITDB_ROOT_PASSWORD=pass -e MONGO_INITDB_DATABASE=db -p 3002:27017 -d docker.io/library/mariadb:10.3```
# Start flask app 
    ```pip install -r requirements.txt```
    ```python -m flask --app latterouter run```