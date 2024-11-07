#!/bin/bash

# TRANSACT_CONTAINER=$(docker container ls|grep transaction | awk '{print $1})

docker-compose -f docker-compose-gateway-bankong-combined_local_portchange.yaml stop bankong-backend-transactions
docker-compose -f docker-compose-gateway-bankong-combined_local_portchange.yaml rm -f bankong-backend-transactions
docker-compose -f course-dev/docker-compose-gateway-bankong-combined_local_portchange.yaml up -d bankong-backend-transactions



# docker container rm $(docker container ls -aq) --force
# docker volume prune --force
# docker network prune --force
# docker image prune --force
