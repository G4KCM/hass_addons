#!/usr/bin/with-contenv bashio
CONFIG_PATH=/data/options.json

MQTTBROKERHOST=$(bashio::services mqtt "host")
MQTTBROKERPORT=$(bashio::services mqtt "port")
MQTTUSERNAME=$(bashio::services mqtt "username")
MQTTPASSWORD=$(bashio::services mqtt "password")
ALPHA2IPS=$(jq --raw-output ".alpha2ips" $CONFIG_PATH)
REFRESHSECONDS=$(jq --raw-output ".refreshseconds" $CONFIG_PATH)

python3 -u ./alpha2.py $MQTTBROKERHOST $MQTTBROKERPORT $MQTTUSERNAME $MQTTPASSWORD $ALPHA2IPS $REFRESHSECONDS
