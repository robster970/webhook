#!/bin/bash

CONTAINER_NAME="sierra-nginx"

docker pull robster970/sierra-nginx:latest
CONTAINER_ID=$(docker ps -a | grep -v Exit | grep 'sierra-nginx' | awk '{print $1}')
echo "Stopping container id: " $CONTAINER_ID
docker stop $CONTAINER_ID
docker rm $CONTAINER_ID
docker run  -p 80:5000 -d --restart=always -t robster970/sierra-nginx:latest
docker ps -a
