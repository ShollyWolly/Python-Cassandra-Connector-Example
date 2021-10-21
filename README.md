# Python-Cassandra-Connector-Example
A simple connection to a cassandra DB using the Python Driver


## Introduction
This is a example of a simple connection to a local Cassandra Database. The Database is simulated in a Docker-Compose file, so you can test it's behavior locally regarding replication.
Of Cause that is not meant for a production enviroment, just for local testing.

## Data
The Data doesn't have any valid meaning. it's just to demonstrate what you can do with Cassandra and how you could set the DB up. The coordinates are just random numbers representing x, y, z. 

## Setting it up
You should not have to do much, you need to install pandas and the python driver via pip in order for the code to work. (pip3 install pands || pip3 install cassandra-driver)
The Cassandra Database can be started by simply typing the command "docker-compose up" in the "CassandraDB" folder (you of cause need to have docker installed for that).

## DB volumes:
I exposed 2 volumes for the DataBase. First one being the actual data, since you never would want to lose that ever. 
The 2nd being the configuration files so you have maximum control what you want to do with the CassandraDB.
The folder "cassandra-4.0.1_vanilla_config" contains the vanilla configuration. You can manually reset the DB that was if something goes wrong.
