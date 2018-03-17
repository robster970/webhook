#!/bin/bash

CONTAINER_ID=$(docker ps -a | grep -v Exit | grep 'sierra-trading' | awk '{print $1}')
docker pull robster970/sierra-nginx:latest
echo "Stopping container id: " $CONTAINER_ID
docker stop $CONTAINER_ID
docker rm $CONTAINER_ID
docker run --name sierra-trading -p 80:5000 -d --restart=always -t robster970/sierra-nginx:latest
docker ps -a
