#!/bin/bash


# export PUBLICIP=$(curl -s http://checkip.amazonaws.com)
export PUBLICIP=localhost
export KONG_ADMIN_API_URI=http://$PUBLICIP:8001
export KONG_ADMIN_GUI_URL=http://$PUBLICIP:8002
export KONG_PORTAL_GUI_HOST=$PUBLICIP:8003
export KONG_PORTAL_API_URL=http://$PUBLICIP:8004
# sudo setfacl -m user:ubuntu:rw /var/run/docker.sock

cd /Users/johnfitzpatrick/GitHub/kong-for-developers/bankong/docker

export KONG_LICENSE_DATA=$(cat license.json)

for file in $(ls logs)
do
  truncate -s 0 logs/$file
done

# docker-compose -f docker-compose-gateway-bankong-combined_local.yaml up -d
docker-compose -f docker-compose-gateway-bankong-combined_local_portchange.yaml up -d

echo Kong Gateway is on $KONG_ADMIN_GUI_URL
echo Kong Developer Portal is $PUBLICIP:8003
echo BanKonG GUI is on $PUBLICIP:29080
echo BanKonG API is on $PUBLICIP:8181

# http -h POST http://localhost:8001/licenses payload=@license.json

