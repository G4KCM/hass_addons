#!/usr/bin/with-contenv bashio

MQTTBROKERHOST=$(bashio::services mqtt "host")
MQTTBROKERPORT=$(bashio::services mqtt "port")
MQTTUSERNAME=$(bashio::services mqtt "username")
MQTTPASSWORD=$(bashio::services mqtt "password")

python3 -u ./davis.py $MQTTBROKERHOST $MQTTBROKERPORT $MQTTUSERNAME $MQTTPASSWORD
