# Polygon Stock Market API Framework

This framework is built using python and docker to test the REST API endpoints
that correlate to the market data from the US Stock exchange provided by 
[polygon](https://polygon.io/docs/stocks/getting-started) 

### prerequisites:
Docker \
Python \
Account created with polygon


This framework was intended to be run inside a docker container. Make sure you have docker running in the background 
and run the following command to spin up the image and container
```commandline
bash start_docker.sh
```
Once you run this command you will be inside the docker container and will be able to run the tests via the pytest
commands. The container is designed to be mounted with the framework so any changes you make on your local machine in 
the `framework` folder should reflect in the docker container. 

For any changes that are made to files outside the 
`framework` folder you will need to exit the container and re-run the start docker shel script for these changes to
take effect.

## How to run tests

In order to run the tests you will need to use the `start_docker.sh` script with provided arguments.
```commandline
bash start_docker.sh <argument>
```
List of available arguments:

`all` - Runs all test cases \
`Specifc Test ID` - Runs specific test cases marked by pytest marker. (E.G tcid01 runs test marked with tcid01)

Once the tests are done running a report will be written to the /framework/reports directory.