#!/bin/bash

if  [ $# -eq 0 ]; then
  echo "please provide a test case id to run OR specify all to run all"
elif [ "$1" = "all" ]; then
  docker exec -it stock_market_framework pytest
elif [ $# -eq 1 ]; then
  docker exec -it stock_market_framework pytest -m $1
fi




