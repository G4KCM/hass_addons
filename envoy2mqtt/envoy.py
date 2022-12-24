import os
import sys
import json
import requests
import threading
from requests.auth import HTTPDigestAuth
import pprint
from datetime import datetime
import time
import paho.mqtt.client as mqtt

MQTTBROKERHOST = sys.argv[1]
MQTTBROKERPORT = int(sys.argv[2])
MQTTUSERNAME = sys.argv[3]
MQTTPASSWORD = sys.argv[4]
ENVOYIP = sys.argv[5]
ENVOYPASS = sys.argv[6]

client = mqtt.Client()
client.username_pw_set(MQTTUSERNAME, MQTTPASSWORD)
client.connect_async(MQTTBROKERHOST, MQTTBROKERPORT, 60)
client.loop_start()
time.sleep(5)

client.publish(topic= "homeassistant/sensor/envoy_production_l1_power/config", payload= "{\"name\":\"Solar Power L1\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"W\",\"value_template\":\"{%if is_state('sun.sun', 'below_horizon')%}{{0|float(0)}}{%else%}{{ value_json['production']['ph-a']['p']|float}}{%endif%}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_production_l2_power/config", payload= "{\"name\":\"Solar Power L2\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"W\",\"value_template\":\"{%if is_state('sun.sun', 'below_horizon')%}{{0|float(0)}}{%else%}{{ value_json['production']['ph-b']['p']|float}}{%endif%}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_production_l3_power/config", payload= "{\"name\":\"Solar Power L3\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"W\",\"value_template\":\"{%if is_state('sun.sun', 'below_horizon')%}{{0|float(0)}}{%else%}{{ value_json['production']['ph-c']['p']|float}}{%endif%}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_production_total_power/config", payload= "{\"name\":\"Solar Power Total\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"W\",\"value_template\":\"{%if is_state('sun.sun', 'below_horizon')%}{{0|float(0)}}{%else%}{{ value_json['production']['ph-a']['p']|float + value_json['production']['ph-b']['p']|float + value_json['production']['ph-c']['p']|float }}{%endif%}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_production_l1_voltage/config", payload= "{\"name\":\"Solar Voltage L1\",\"device_class\":\"voltage\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"V\",\"value_template\":\"{{ value_json['production']['ph-a']['v']|float}}\",\"icon\":\"mdi:flash-triangle-outline\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_production_l2_voltage/config", payload= "{\"name\":\"Solar Voltage L2\",\"device_class\":\"voltage\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"V\",\"value_template\":\"{{ value_json['production']['ph-b']['v']|float}}\",\"icon\":\"mdi:flash-triangle-outline\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_production_l3_voltage/config", payload= "{\"name\":\"Solar Voltage L3\",\"device_class\":\"voltage\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"V\",\"value_template\":\"{{ value_json['production']['ph-c']['v']|float}}\",\"icon\":\"mdi:flash-triangle-outline\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_production_l1_current/config", payload= "{\"name\":\"Solar Current L1\",\"device_class\":\"current\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"A\",\"value_template\":\"{{ value_json['production']['ph-a']['i']|float}}\",\"icon\":\"mdi:flash-auto\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_production_l2_current/config", payload= "{\"name\":\"Solar Current L2\",\"device_class\":\"current\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"A\",\"value_template\":\"{{ value_json['production']['ph-b']['i']|float}}\",\"icon\":\"mdi:flash-auto\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_production_l3_current/config", payload= "{\"name\":\"Solar Current L3\",\"device_class\":\"current\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"A\",\"value_template\":\"{{ value_json['production']['ph-c']['i']|float}}\",\"icon\":\"mdi:flash-auto\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_production_l1_frequency/config", payload= "{\"name\":\"Solar Frequency L1\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"Hz\",\"value_template\":\"{{ value_json['production']['ph-a']['f']|float}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_production_l2_frequency/config", payload= "{\"name\":\"Solar Frequency L2\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"Hz\",\"value_template\":\"{{ value_json['production']['ph-b']['f']|float}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_production_l3_frequency/config", payload= "{\"name\":\"Solar Frequency L3\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"Hz\",\"value_template\":\"{{ value_json['production']['ph-c']['f']|float}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_consumption_l1_power/config", payload= "{\"name\":\"Grid Power L1\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"W\",\"value_template\":\"{{ value_json['net-consumption']['ph-a']['p']|float}}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_consumption_l2_power/config", payload= "{\"name\":\"Grid Power L2\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"W\",\"value_template\":\"{{ value_json['net-consumption']['ph-b']['p']|float}}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_consumption_l3_power/config", payload= "{\"name\":\"Grid Power L3\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"W\",\"value_template\":\"{{ value_json['net-consumption']['ph-c']['p']|float}}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_consumption_total_power/config", payload= "{\"name\":\"Grid Power Total\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"W\",\"value_template\":\"{{ value_json['net-consumption']['ph-a']['p']|float + value_json['net-consumption']['ph-b']['p']|float + value_json['net-consumption']['ph-c']['p']|float }}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_consumption_l1_voltage/config", payload= "{\"name\":\"Grid Voltage L1\",\"device_class\":\"voltage\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"V\",\"value_template\":\"{{ value_json['net-consumption']['ph-a']['v']|float}}\",\"icon\":\"mdi:flash-triangle-outline\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_consumption_l2_voltage/config", payload= "{\"name\":\"Grid Voltage L2\",\"device_class\":\"voltage\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"V\",\"value_template\":\"{{ value_json['net-consumption']['ph-b']['v']|float}}\",\"icon\":\"mdi:flash-triangle-outline\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_consumption_l3_voltage/config", payload= "{\"name\":\"Grid Voltage L3\",\"device_class\":\"voltage\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"V\",\"value_template\":\"{{ value_json['net-consumption']['ph-c']['v']|float}}\",\"icon\":\"mdi:flash-triangle-outline\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_consumption_l1_current/config", payload= "{\"name\":\"Grid Current L1\",\"device_class\":\"current\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"A\",\"value_template\":\"{{ value_json['net-consumption']['ph-a']['i']|float}}\",\"icon\":\"mdi:flash-auto\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_consumption_l2_current/config", payload= "{\"name\":\"Grid Current L2\",\"device_class\":\"current\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"A\",\"value_template\":\"{{ value_json['net-consumption']['ph-b']['i']|float}}\",\"icon\":\"mdi:flash-auto\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_consumption_l3_current/config", payload= "{\"name\":\"Grid Current L3\",\"device_class\":\"current\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"A\",\"value_template\":\"{{ value_json['net-consumption']['ph-c']['i']|float}}\",\"icon\":\"mdi:flash-auto\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_consumption_l1_frequency/config", payload= "{\"name\":\"Grid Frequency L1\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"Hz\",\"value_template\":\"{{ value_json['net-consumption']['ph-a']['f']|float}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_consumption_l2_frequency/config", payload= "{\"name\":\"Grid Frequency L2\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"Hz\",\"value_template\":\"{{ value_json['net-consumption']['ph-b']['f']|float}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_consumption_l3_frequency/config", payload= "{\"name\":\"Grid Frequency L3\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"Hz\",\"value_template\":\"{{ value_json['net-consumption']['ph-c']['f']|float}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l1_power/config", payload= "{\"name\":\"Total Power L1\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"W\",\"value_template\":\"{{ value_json['total-consumption']['ph-a']['p']|float}}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l2_power/config", payload= "{\"name\":\"Total Power L2\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"W\",\"value_template\":\"{{ value_json['total-consumption']['ph-b']['p']|float}}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l3_power/config", payload= "{\"name\":\"Total Power L3\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"W\",\"value_template\":\"{{ value_json['total-consumption']['ph-c']['p']|float}}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_power/config", payload= "{\"name\":\"Total Power\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"W\",\"value_template\":\"{{ value_json['total-consumption']['ph-a']['p']|float + value_json['total-consumption']['ph-b']['p']|float + value_json['total-consumption']['ph-c']['p']|float }}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l1_voltage/config", payload= "{\"name\":\"Total Voltage L1\",\"device_class\":\"voltage\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"V\",\"value_template\":\"{{ value_json['total-consumption']['ph-a']['v']|float}}\",\"icon\":\"mdi:flash-triangle-outline\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l2_voltage/config", payload= "{\"name\":\"Total Voltage L2\",\"device_class\":\"voltage\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"V\",\"value_template\":\"{{ value_json['total-consumption']['ph-b']['v']|float}}\",\"icon\":\"mdi:flash-triangle-outline\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l3_voltage/config", payload= "{\"name\":\"Total Voltage L3\",\"device_class\":\"voltage\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"V\",\"value_template\":\"{{ value_json['total-consumption']['ph-c']['v']|float}}\",\"icon\":\"mdi:flash-triangle-outline\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l1_current/config", payload= "{\"name\":\"Total Current L1\",\"device_class\":\"current\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"A\",\"value_template\":\"{{ value_json['total-consumption']['ph-a']['i']|float}}\",\"icon\":\"mdi:flash-auto\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l2_current/config", payload= "{\"name\":\"Total Current L2\",\"device_class\":\"current\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"A\",\"value_template\":\"{{ value_json['total-consumption']['ph-b']['i']|float}}\",\"icon\":\"mdi:flash-auto\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l3_current/config", payload= "{\"name\":\"Total Current L3\",\"device_class\":\"current\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"A\",\"value_template\":\"{{ value_json['total-consumption']['ph-c']['i']|float}}\",\"icon\":\"mdi:flash-auto\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l1_frequency/config", payload= "{\"name\":\"Total Frequency L1\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"Hz\",\"value_template\":\"{{ value_json['total-consumption']['ph-a']['f']|float}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l2_frequency/config", payload= "{\"name\":\"Total Frequency L2\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"Hz\",\"value_template\":\"{{ value_json['total-consumption']['ph-b']['f']|float}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l3_frequency/config", payload= "{\"name\":\"Total Frequency L3\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/json\",\"unit_of_measurement\":\"Hz\",\"value_template\":\"{{ value_json['total-consumption']['ph-c']['f']|float}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

user = 'installer'
auth = HTTPDigestAuth(user, ENVOYPASS)
marker = b'data: '

def scrape_stream():
    while True:
        try:
            url = 'http://%s/stream/meter' % ENVOYIP
            stream = requests.get(url, auth=auth, stream=True, timeout=5)
            for line in stream.iter_lines():
                if line.startswith(marker):
                    data = json.loads(line.replace(marker, b''))
                    json_string = json.dumps(data)
                    #pp.pprint(json_string)
                                    
                    client.publish(topic= '/envoy/json' , payload= json_string, qos=0 )
                    time.sleep(4)
        except requests.exceptions.RequestException as e:
            print(dt_string, ' Exception fetching stream data: %s' % e)

def main():
    stream_thread = threading.Thread(target=scrape_stream)
    #    stream_thread.setDaemon(True)
    stream_thread.start()

if __name__ == '__main__':
    main()