#!/bin/bash

custom_datetime=$(date +"%Y_%m_%d_%H:%M:%S")

if  [ $# -eq 0 ]; then
  echo "please provide a test case id to run OR specify all to run all"
elif [ "$1" = "all" ]; then
  docker exec -it stock_market_framework pytest
elif [ $# -eq 1 ]; then
  docker exec  -it stock_market_framework pytest -m $1 \
  --html /framework/tests/reports/results_$1_$custom_datetime.html \
  --self-contained-html \
  --color=yes
fi




