import os
import sys
import paho.mqtt.publish as publish

MQTTBROKERHOST = sys.argv[1]
MQTTBROKERPORT = int(sys.argv[2])
MQTTUSERNAME = sys.argv[3]
MQTTPASSWORD = sys.argv[4]

msgs = []
print("starting Davis Sensor MQTT Autodiscovery")
msgs.append({'topic': "homeassistant/sensor/davis_barometer/config", 'payload':"{\"name\":\"Davis Barometer\",\"device_class\":\"pressure\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflrtd.json\",\"unit_of_measurement\":\"mbar\",\"value_template\":\"{{ (float(value_json.bar) * 33.8639) | round(1) }}\",\"icon\":\"mdi:gauge\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_windspeedhightime/config", 'payload':"{\"name\":\"Davis Hoogste Windsnelheid Tijd\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflhilow.json\",\"value_template\":\"{{ value_json.hlwind[0] }}\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_windspeedhigh/config", 'payload':"{\"name\":\"Davis Hoogste Windsnelheid\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflhilow.json\",\"unit_of_measurement\":\"km/h\",\"value_template\":\"{{ (float(value_json.hlwind[1]) * 1.609344) | round(0) }}\",\"icon\":\"mdi:weather-windy\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_moisturehightime/config", 'payload':"{\"name\":\"Davis Hoogste Luchtvochtigheid Tijd\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflhilow.json\",\"value_template\":\"{{ value_json.hlhumout[2] }}\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_moisturehigh/config", 'payload':"{\"name\":\"Davis Hoogste Luchtvochtigheid\",\"device_class\":\"humidity\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflhilow.json\",\"unit_of_measurement\":\"%\",\"value_template\":\"{{ value_json.hlhumout[3] }}\",\"icon\":\"mdi:water-percent\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_temphightime/config", 'payload':"{\"name\":\"Davis Hoogste Temperatuur Tijd\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflhilow.json\",\"value_template\":\"{{ value_json.hltempout[2] }}\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_temphigh/config", 'payload':"{\"name\":\"Davis Hoogste Temperatuur\",\"device_class\":\"temperature\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflhilow.json\",\"unit_of_measurement\":\"°F\",\"value_template\":\"{{ value_json.hltempout[3] }}\",\"icon\":\"mdi:weather-windy\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_moisturelowtime/config", 'payload':"{\"name\":\"Davis Laagste Luchtvochtigheid Tijd\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflhilow.json\",\"value_template\":\"{{ value_json.hlhumout[0] }}\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_moisturelow/config", 'payload':"{\"name\":\"Davis Laagste Luchtvochtigheid\",\"device_class\":\"humidity\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflhilow.json\",\"unit_of_measurement\":\"%\",\"value_template\":\"{{ value_json.hlhumout[1] }}\",\"icon\":\"mdi:water-percent\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_chill/config", 'payload':"{\"name\":\"Davis Gevoelstemperatuur\",\"device_class\":\"temperature\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflrtd.json\",\"unit_of_measurement\":\"°F\",\"value_template\":\"{{ value_json.chill }}\",\"icon\":\"mdi:thermometer\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_dewpoint/config", 'payload':"{\"name\":\"Davis Dauwpunt\",\"device_class\":\"temperature\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflrtd.json\",\"unit_of_measurement\":\"°F\",\"value_template\":\"{{ value_json.cdew }}\",\"icon\":\"mdi:thermometer\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_templowtime/config", 'payload':"{\"name\":\"Davis Laagste Temperatuur Tijd\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflhilow.json\",\"value_template\":\"{{ value_json.hltempout[0] }}\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_templow/config", 'payload':"{\"name\":\"Davis Laagste Temperatuur\",\"device_class\":\"temperature\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflhilow.json\",\"unit_of_measurement\":\"°F\",\"value_template\":\"{{ value_json.hltempout[1]}}\",\"icon\":\"mdi:weather-windy\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_moisture/config", 'payload':"{\"name\":\"Davis Luchtvochtigheid\",\"device_class\":\"humidity\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflrtd.json\",\"unit_of_measurement\":\"%\",\"value_template\":\"{{ value_json.humout }}\",\"icon\":\"mdi:water-percent\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_temp/config", 'payload':"{\"name\":\"Davis Buitentemperatuur\",\"device_class\":\"temperature\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflrtd.json\",\"unit_of_measurement\":\"°F\",\"value_template\":\"{{ value_json.tempout }}\",\"icon\":\"mdi:thermometer\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_rain/config", 'payload':"{\"name\":\"Davis Regenhoveelheid\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflrtd.json\",\"unit_of_measurement\":\"mm/h\",\"value_template\":\"{{ (float(value_json.rainr) * 25.4) | round(1) }}\",\"icon\":\"mdi:weather-rainy\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_rainhour/config", 'payload':"{\"name\":\"Davis Regenhoveelheid Uur\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflrtd.json\",\"unit_of_measurement\":\"mm\",\"value_template\":\"{{ (float(value_json.rain1h) * 25.4) | round(1) }}\",\"icon\":\"mdi:weather-rainy\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_rainday/config", 'payload':"{\"name\":\"Davis Regenhoveelheid Dag\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflrtd.json\",\"unit_of_measurement\":\"mm\",\"value_template\":\"{{ (float(value_json.raind) * 25.4) | round(1) }}\",\"icon\":\"mdi:weather-rainy\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_rainmonth/config", 'payload':"{\"name\":\"Davis Regenhoveelheid Maand\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflrtd.json\",\"unit_of_measurement\":\"mm\",\"value_template\":\"{{ (float(value_json.rainmon) * 25.4) | round(1) }}\",\"icon\":\"mdi:weather-rainy\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_rainyear/config", 'payload':"{\"name\":\"Davis Regenhoveelheid Jaar\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflrtd.json\",\"unit_of_measurement\":\"mm\",\"value_template\":\"{{ (float(value_json.rainyear) * 25.4) | round(1) }}\",\"icon\":\"mdi:weather-rainy\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_solar/config", 'payload':"{\"name\":\"Davis Zonnestraling\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflrtd.json\",\"unit_of_measurement\":\"W/m²\",\"value_template\":\"{{ value_json.solar }}\",\"icon\":\"mdi:white-balance-sunny\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_et/config", 'payload':"{\"name\":\"Davis Verdamping\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflrtd.json\",\"unit_of_measurement\":\"mm\",\"value_template\":\"{{ (float(value_json.etday) * 25.4) | round(3) }}\",\"icon\":\"mdi:weather-sunset-up\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_uvindex/config", 'payload':"{\"name\":\"Davis UV Index\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflrtd.json\",\"unit_of_measurement\":\"index\",\"value_template\":\"{{ value_json.uv }}\",\"icon\":\"mdi:weather-sunny\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_winddirection/config", 'payload':"{\"name\":\"Davis Windrichting\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflrtd.json\",\"unit_of_measurement\":\"°\",\"value_template\":\"{{ value_json.winddir }}\",\"icon\":\"mdi:compass\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_windspeed/config", 'payload':"{\"name\":\"Davis Windsnelheid\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflrtd.json\",\"unit_of_measurement\":\"km/h\",\"value_template\":\"{{ (float(value_json.windspd) * 1.609344) | round(0) }}\",\"icon\":\"mdi:weather-windy\"}",'retain':True})
msgs.append({'topic': "homeassistant/sensor/davis_windspeedaverage/config", 'payload':"{\"name\":\"Davis Windsnelheid Gemiddeld\",\"platform\":\"mqtt\",\"state_topic\":\"/davis/wflrtd.json\",\"unit_of_measurement\":\"km/h\",\"value_template\":\"{{ (float(value_json.windavg2) * 1.609344) | round(0) }}\",\"icon\":\"mdi:weather-windy\"}",'retain':True})
publish.multiple(msgs, hostname=MQTTBROKERHOST, port=MQTTBROKERPORT, auth={'username':MQTTUSERNAME, 'password':MQTTPASSWORD})

print("Ending Davis Sensor MQTT Autodiscovery. Notning to do here: exiting..")