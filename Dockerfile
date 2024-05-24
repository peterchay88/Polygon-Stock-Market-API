FROM python:3.11.4

# installing nano
RUN apt-get update && apt-get install -y nano

# Creating a folder named automation
RUN mkdir /automation
