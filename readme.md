# Polygon Stock Market API Framework

This framework is built using python and docker to test the REST API endpoints
that correlate to the market data from the US Stock exchange provided by 
[polygon](https://polygon.io/docs/stocks/getting-started) 

### TO-DO
- Build Docker structure (DONE)
  - Write one test to run against docker env 
  - Create shell script to streamline this process (done)
  - Figure out how to automatically delete dangling images when shell script is run
- Create helper classes & utilities (WIP)
  - Need to build a request wrapper