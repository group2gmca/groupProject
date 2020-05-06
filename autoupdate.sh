#! /bin/bash


touch /home/poley1971/logs
docker stack deploy -c /home/poley1971/groupProject/docker-compose.yml prize >> /home/poley1971/logs


#alt path to test
#docker stack deploy –c /home/poley1971/groupProject/docker-compose.yml

