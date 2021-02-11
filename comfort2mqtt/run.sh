#!/usr/bin/with-contenv bashio
CONFIG_PATH=/data/options.json

MQTTBROKERHOST=$(bashio::services mqtt "host")
MQTTBROKERPORT=$(bashio::services mqtt "port")
MQTTUSERNAME=$(bashio::services mqtt "username")
MQTTPASSWORD=$(bashio::services mqtt "password")
COMFORTIP=$(jq --raw-output ".comfortip" $CONFIG_PATH)
COMFORTPORT=$(jq --raw-output ".comfortport" $CONFIG_PATH)
COMFORTPIN=$(jq --raw-output ".comfortpin" $CONFIG_PATH)
python3 -u ./comfort2.py $MQTTBROKERHOST $MQTTBROKERPORT $MQTTUSERNAME $MQTTPASSWORD $COMFORTIP $COMFORTPORT $COMFORTPIN
