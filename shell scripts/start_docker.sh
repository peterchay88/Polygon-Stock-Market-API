#!/bin/bash

# Creating the docker image
echo "-----------------------------------------"
echo "Spinning up docker container and image"
echo "-----------------------------------------"
echo

docker build -t polygon_api:latest ../

