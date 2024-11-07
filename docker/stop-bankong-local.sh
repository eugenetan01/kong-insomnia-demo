#!/bin/bash


# docker-compose -f docker-compose-gateway-bankong-combined_local.yaml down
docker-compose -f docker-compose-gateway-bankong-combined_local_portchange.yaml down

for file in $(ls logs)
do
  truncate -s 0 logs/$file
done

docker container rm $(docker container ls -aq) --force
docker volume prune --force
docker network prune --force
docker image prune --force
