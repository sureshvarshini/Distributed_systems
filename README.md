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
    
