#!/usr/bin/with-contenv bashio
CONFIG_PATH=/data/options.json

MQTTBROKERHOST=$(bashio::services mqtt "host")
MQTTBROKERPORT=$(bashio::services mqtt "port")
MQTTUSERNAME=$(bashio::services mqtt "username")
MQTTPASSWORD=$(bashio::services mqtt "password")
ENVOYIP=$(jq --raw-output ".envoyip" $CONFIG_PATH)
ENVOYPASS=$(jq --raw-output ".envoypass" $CONFIG_PATH)
python3 -u ./envoy.py $MQTTBROKERHOST $MQTTBROKERPORT $MQTTUSERNAME $MQTTPASSWORD $ENVOYIP $ENVOYPASS
