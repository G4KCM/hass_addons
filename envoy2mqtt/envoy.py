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

client.publish(topic= "homeassistant/sensor/envoy_solar_l1_power/config", payload= "{\"name\":\"Envoy Solar Power L1\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"kW\",\"value_template\":\"{%if is_state('sun.sun', 'below_horizon')%}{{0|float(0)}}{%else%}{{ value_json['production']['ph-a']['p']|float/1000|round(2)}}{%endif%}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_solar_l2_power/config", payload= "{\"name\":\"Envoy Solar Power L2\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"kW\",\"value_template\":\"{%if is_state('sun.sun', 'below_horizon')%}{{0|float(0)}}{%else%}{{ value_json['production']['ph-b']['p']|float/1000|round(2)}}{%endif%}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_solar_l3_power/config", payload= "{\"name\":\"Envoy Solar Power L3\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"kW\",\"value_template\":\"{%if is_state('sun.sun', 'below_horizon')%}{{0|float(0)}}{%else%}{{ value_json['production']['ph-c']['p']|float/1000|round(2)}}{%endif%}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_solar_total_power/config", payload= "{\"name\":\"Envoy Solar Power Total\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"W\",\"value_template\":\"{%if is_state('sun.sun', 'below_horizon')%}{{0|float(0)}}{%else%}{{ (value_json['production']['ph-a']['p']|float + value_json['production']['ph-b']['p']|float + value_json['production']['ph-c']['p']|float)/1000|round(2) }}{%endif%}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_solar_l1_voltage/config", payload= "{\"name\":\"Envoy Solar Voltage L1\",\"device_class\":\"voltage\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"V\",\"value_template\":\"{{ value_json['production']['ph-a']['v']|float|round(2)}}\",\"icon\":\"mdi:flash-triangle-outline\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_solar_l2_voltage/config", payload= "{\"name\":\"Envoy Solar Voltage L2\",\"device_class\":\"voltage\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"V\",\"value_template\":\"{{ value_json['production']['ph-b']['v']|float|round(2)}}\",\"icon\":\"mdi:flash-triangle-outline\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_solar_l3_voltage/config", payload= "{\"name\":\"Envoy Solar Voltage L3\",\"device_class\":\"voltage\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"V\",\"value_template\":\"{{ value_json['production']['ph-c']['v']|float|round(2)}}\",\"icon\":\"mdi:flash-triangle-outline\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_solar_l1_current/config", payload= "{\"name\":\"Envoy Solar Current L1\",\"device_class\":\"current\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"A\",\"value_template\":\"{{ value_json['production']['ph-a']['i']|float|round(2)}}\",\"icon\":\"mdi:flash-auto\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_solar_l2_current/config", payload= "{\"name\":\"Envoy Solar Current L2\",\"device_class\":\"current\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"A\",\"value_template\":\"{{ value_json['production']['ph-b']['i']|float|round(2)}}\",\"icon\":\"mdi:flash-auto\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_solar_l3_current/config", payload= "{\"name\":\"Envoy Solar Current L3\",\"device_class\":\"current\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"A\",\"value_template\":\"{{ value_json['production']['ph-c']['i']|float|round(2)}}\",\"icon\":\"mdi:flash-auto\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_solar_l1_frequency/config", payload= "{\"name\":\"Envoy Solar Frequency L1\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"Hz\",\"value_template\":\"{{ value_json['production']['ph-a']['f']|float|round(2)}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_solar_l2_frequency/config", payload= "{\"name\":\"Envoy Solar Frequency L2\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"Hz\",\"value_template\":\"{{ value_json['production']['ph-b']['f']|float|round(2)}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_solar_l3_frequency/config", payload= "{\"name\":\"Envoy Solar Frequency L3\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"Hz\",\"value_template\":\"{{ value_json['production']['ph-c']['f']|float|round(2)}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_grid_l1_power/config", payload= "{\"name\":\"Envoy Grid Power L1\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"kW\",\"value_template\":\"{{ value_json['net-consumption']['ph-a']['p']|float/1000|round(2)}}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_grid_l2_power/config", payload= "{\"name\":\"Envoy Grid Power L2\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"kW\",\"value_template\":\"{{ value_json['net-consumption']['ph-b']['p']|float/1000|round(2)}}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_grid_l3_power/config", payload= "{\"name\":\"Envoy Grid Power L3\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"kW\",\"value_template\":\"{{ value_json['net-consumption']['ph-c']['p']|float/1000|round(2)}}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_grid_total_power/config", payload= "{\"name\":\"Envoy Grid Power Total\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"W\",\"value_template\":\"{{ (value_json['net-consumption']['ph-a']['p']|float + value_json['net-consumption']['ph-b']['p']|float + value_json['net-consumption']['ph-c']['p']|float)/1000|round(2) }}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_grid_l1_voltage/config", payload= "{\"name\":\"Envoy Grid Voltage L1\",\"device_class\":\"voltage\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"V\",\"value_template\":\"{{ value_json['net-consumption']['ph-a']['v']|float|round(2)}}\",\"icon\":\"mdi:flash-triangle-outline\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_grid_l2_voltage/config", payload= "{\"name\":\"Envoy Grid Voltage L2\",\"device_class\":\"voltage\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"V\",\"value_template\":\"{{ value_json['net-consumption']['ph-b']['v']|float|round(2)}}\",\"icon\":\"mdi:flash-triangle-outline\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_grid_l3_voltage/config", payload= "{\"name\":\"Envoy Grid Voltage L3\",\"device_class\":\"voltage\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"V\",\"value_template\":\"{{ value_json['net-consumption']['ph-c']['v']|float|round(2)}}\",\"icon\":\"mdi:flash-triangle-outline\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_grid_l1_current/config", payload= "{\"name\":\"Envoy Grid Current L1\",\"device_class\":\"current\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"A\",\"value_template\":\"{{ value_json['net-consumption']['ph-a']['i']|float|round(2)}}\",\"icon\":\"mdi:flash-auto\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_grid_l2_current/config", payload= "{\"name\":\"Envoy Grid Current L2\",\"device_class\":\"current\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"A\",\"value_template\":\"{{ value_json['net-consumption']['ph-b']['i']|float|round(2)}}\",\"icon\":\"mdi:flash-auto\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_grid_l3_current/config", payload= "{\"name\":\"Envoy Grid Current L3\",\"device_class\":\"current\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"A\",\"value_template\":\"{{ value_json['net-consumption']['ph-c']['i']|float|round(2)}}\",\"icon\":\"mdi:flash-auto\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_grid_l1_frequency/config", payload= "{\"name\":\"Envoy Grid Frequency L1\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"Hz\",\"value_template\":\"{{ value_json['net-consumption']['ph-a']['f']|float|round(2)}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_grid_l2_frequency/config", payload= "{\"name\":\"Envoy Grid Frequency L2\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"Hz\",\"value_template\":\"{{ value_json['net-consumption']['ph-b']['f']|float|round(2)}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_grid_l3_frequency/config", payload= "{\"name\":\"Envoy Grid Frequency L3\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"Hz\",\"value_template\":\"{{ value_json['net-consumption']['ph-c']['f']|float|round(2)}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l1_power/config", payload= "{\"name\":\"Envoy Total Power L1\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"kW\",\"value_template\":\"{{ value_json['total-consumption']['ph-a']['p']/1000|float|round(2)}}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l2_power/config", payload= "{\"name\":\"Envoy Total Power L2\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"kW\",\"value_template\":\"{{ value_json['total-consumption']['ph-b']['p']/1000|float|round(2)}}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l3_power/config", payload= "{\"name\":\"Envoy Total Power L3\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"kW\",\"value_template\":\"{{ value_json['total-consumption']['ph-c']['p']/1000|float|round(2)}}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_power/config", payload= "{\"name\":\"Envoy Total Power\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"W\",\"value_template\":\"{{ (value_json['total-consumption']['ph-a']['p']|float + value_json['total-consumption']['ph-b']['p']|float + value_json['total-consumption']['ph-c']['p']|float)/1000|round(2) }}\",\"icon\":\"mdi:flash\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l1_voltage/config", payload= "{\"name\":\"Envoy Total Voltage L1\",\"device_class\":\"voltage\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"V\",\"value_template\":\"{{ value_json['total-consumption']['ph-a']['v']|float|round(2)}}\",\"icon\":\"mdi:flash-triangle-outline\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l2_voltage/config", payload= "{\"name\":\"Envoy Total Voltage L2\",\"device_class\":\"voltage\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"V\",\"value_template\":\"{{ value_json['total-consumption']['ph-b']['v']|float|round(2)}}\",\"icon\":\"mdi:flash-triangle-outline\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l3_voltage/config", payload= "{\"name\":\"Envoy Total Voltage L3\",\"device_class\":\"voltage\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"V\",\"value_template\":\"{{ value_json['total-consumption']['ph-c']['v']|float|round(2)}}\",\"icon\":\"mdi:flash-triangle-outline\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l1_current/config", payload= "{\"name\":\"Envoy Total Current L1\",\"device_class\":\"current\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"A\",\"value_template\":\"{{ value_json['total-consumption']['ph-a']['i']|float|round(2)}}\",\"icon\":\"mdi:flash-auto\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l2_current/config", payload= "{\"name\":\"Envoy Total Current L2\",\"device_class\":\"current\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"A\",\"value_template\":\"{{ value_json['total-consumption']['ph-b']['i']|float|round(2)}}\",\"icon\":\"mdi:flash-auto\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l3_current/config", payload= "{\"name\":\"Envoy Total Current L3\",\"device_class\":\"current\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"A\",\"value_template\":\"{{ value_json['total-consumption']['ph-c']['i']|float|round(2)}}\",\"icon\":\"mdi:flash-auto\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l1_frequency/config", payload= "{\"name\":\"Envoy Total Frequency L1\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"Hz\",\"value_template\":\"{{ value_json['total-consumption']['ph-a']['f']|float|round(2)}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l2_frequency/config", payload= "{\"name\":\"Envoy Total Frequency L2\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"Hz\",\"value_template\":\"{{ value_json['total-consumption']['ph-b']['f']|float|round(2)}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_total_l3_frequency/config", payload= "{\"name\":\"Envoy Total Frequency L3\",\"device_class\":\"power\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/realtime.json\",\"unit_of_measurement\":\"Hz\",\"value_template\":\"{{ value_json['total-consumption']['ph-c']['f']|float|round(2)}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)

client.publish(topic= "homeassistant/sensor/envoy_solar_daily_production/config", payload= "{\"name\":\"Envoy Solar Daily Production\",\"device_class\":\"energy\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/production.json\",\"unit_of_measurement\":\"kWh\",\"value_template\":\"{{ value_json['production'][1]['whToday']|float/1000|round(2)}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_solar_weekly_production/config", payload= "{\"name\":\"Envoy Solar Weekly Production\",\"device_class\":\"energy\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/production.json\",\"unit_of_measurement\":\"kWh\",\"value_template\":\"{{ value_json['production'][1]['whLastSevenDays']|float/1000|round(2)}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)
client.publish(topic= "homeassistant/sensor/envoy_solar_lifetime_production/config", payload= "{\"name\":\"Envoy Solar Lifetime Production\",\"device_class\":\"energy\",\"platform\":\"mqtt\",\"state_class\":\"measurement\",\"state_topic\":\"/envoy/production.json\",\"unit_of_measurement\":\"kWh\",\"value_template\":\"{{ value_json['production'][1]['whLifetime']|float/1000|round(2)}}\",\"icon\":\"mdi:current-ac\"}",qos=0,retain=True)


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

user = 'installer'
auth = HTTPDigestAuth(user, ENVOYPASS)
marker = b'data: '
loops=1

def scrape_streams():
    while True:
        try:
            url = 'http://%s/stream/meter' % ENVOYIP
            stream = requests.get(url, auth=auth, stream=True, timeout=5)
            for line in stream.iter_lines():
                if line.startswith(marker):
                    data = json.loads(line.replace(marker, b''))
                    json_string = json.dumps(data)
                    #pp.pprint(json_string)
                                    
                    client.publish(topic= '/envoy/realtime.json' , payload= json_string, qos=0 )
        
            if (loops == 3):
                url = 'http://%s/production.json' % ENVOYIP
                jsonproduction = requests.get(url, auth=auth, verify=False)
                if (jsonproduction.status_code == 200):                
                    client.publish(topic= '/envoy/production.json' , payload= jsonproduction.json(), qos=0 )
                loops = 0
            loops += 1
            time.sleep(5)
        except requests.exceptions.RequestException as e:
            print(dt_string, ' Exception fetching stream data: %s' % e)

def main():
    stream_thread = threading.Thread(target=scrape_streams)
    stream_thread.start()

if __name__ == '__main__':
    main()