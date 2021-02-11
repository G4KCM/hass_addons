#!/usr/bin/with-contenv bashio
CONFIG_PATH=/data/options.json

MQTTBROKERHOST=$(bashio::services mqtt "host")
MQTTBROKERPORT=$(bashio::services mqtt "port")
MQTTUSERNAME=$(bashio::services mqtt "username")
MQTTPASSWORD=$(bashio::services mqtt "password")
PAPAGOIP=$(jq --raw-output ".papagoip" $CONFIG_PATH)
REFRESHSECONDS=$(jq --raw-output ".refreshseconds" $CONFIG_PATH)

python3 -u ./papago.py $MQTTBROKERHOST $MQTTBROKERPORT $MQTTUSERNAME $MQTTPASSWORD $PAPAGOIP $REFRESHSECONDS
