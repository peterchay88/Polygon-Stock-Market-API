#!/bin/bash

# Creating the docker image
echo "-----------------------------------------"
echo "Spinning up docker container and image"
echo "-----------------------------------------"
echo
echo "Checking to see if polygon_api:latest already exists"
echo "If it does removing it"
#docker rmi polygon_api:latest
docker build --no-cache -t polygon_api:latest .

# If a container named stock_market_framework exists. Stop it and then remove it.
echo "-----------------------------------------"
echo "If container stock_market_framework already exists stop it and then delete it"
echo
echo "Please Wait..."
echo "-----------------------------------------"
echo
docker stop stock_market_framework
docker rm stock_market_framework

# Creating Docker container
docker run \
  --name stock_market_framework \
  -p 8000:8000 \
  --restart unless-stopped \
  -v framework:/automation \
  --env-file secrets.env \
  -it polygon_api:latest /bin/bash


