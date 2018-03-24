#!/bin/bash

current_date_time="`date +%Y-%m-%d:%H-%M-%S`";
echo $current_date_time;

CONTAINER_ID=$(docker ps -a | grep -v Exit | grep 'sierra-trading' | awk '{print $1}')

docker pull robster970/sierra-nginx:latest

echo "Stopping container id: " $CONTAINER_ID
docker stop $CONTAINER_ID
docker rm $CONTAINER_ID

docker run -e "HOME=/home" -v $HOME/.aws:/home/.aws --name sierra-trading -p 80:5000 -d --restart=always -t robster970/sierra-nginx:latest
docker ps -a

docker system prune -f
df -k
