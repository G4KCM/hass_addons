import os
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
import paho.mqtt.client as mqtt

MQTTBROKERHOST = sys.argv[1]
MQTTBROKERPORT = int(sys.argv[2])
MQTTUSERNAME = sys.argv[3]
MQTTPASSWORD = sys.argv[4]
PAPAGOIP = sys.argv[5]
REFRESHSECONDS = int(sys.argv[6])

client = mqtt.Client()
client.username_pw_set(MQTTUSERNAME, MQTTPASSWORD)
client.connect_async(MQTTBROKERHOST, MQTTBROKERPORT, 60)
client.loop_start()

try:
    opener = urllib.request.build_opener()
    tree = ET.parse(opener.open("http://%s/fresh.xml" % PAPAGOIP))
    dev = tree.find('.//{http://www.papouch.com/xml/papago/act}status').attrib['location']
    lst = tree.findall('.//{http://www.papouch.com/xml/papago/act}sns')
    for item in lst:
        id = item.attrib['id']
        sensorname = item.attrib['name']
        client.publish("homeassistant/sensor/"+dev+"/temp"+id+"/config", "{\"name\":\""+sensorname+" Temperature\",\"device_class\":\"temperature\",\"state_topic\":\"papago/"+sensorname.lower().replace(" ", "_")+"/state\",\"availability_topic\":\"papago/online\",\"value_template\": \"{{ value_json.temperature}}\",\"unit_of_measurement\":\"°C\",\"unique_id\":\""+dev+"_T_"+id+"\", \"device\": {\"identifiers\":[\""+dev+"\"], \"name\":\""+dev+"\", \"manufacturer\":\"Papouch\", \"model\":\"Papago 2TH WIFI\"},\"payload_available\":\"1\",\"payload_not_available\":\"0\"}" ,qos=0,retain=True)
        client.publish("homeassistant/sensor/"+dev+"/hum"+id+"/config", "{\"name\":\""+sensorname+" Humidity\",\"device_class\":\"humidity\",\"state_topic\":\"papago/"+sensorname.lower().replace(" ", "_")+"/state\",\"availability_topic\":\"papago/online\",\"value_template\": \"{{ value_json.humidity}}\",\"unit_of_measurement\":\"%\",\"unique_id\":\""+dev+"_H_"+id+"\", \"device\": {\"identifiers\":[\""+dev+"\"], \"name\":\""+dev+"\", \"manufacturer\":\"Papouch\", \"model\":\"Papago 2TH WIFI\"},\"payload_available\":\"1\",\"payload_not_available\":\"0\"}" ,qos=0,retain=True)

    client.publish("papago/online", payload="1", qos=0, retain=True)
    while True:
        opener = urllib.request.build_opener()
        tree = ET.parse(opener.open("http://%s/fresh.xml" % PAPAGOIP))
        for sensor in tree.iter('{http://www.papouch.com/xml/papago/act}sns'):
            sensorname = sensor.attrib['name'].lower().replace(" ", "_")
            jsonstring = "{\"temperature\":\""+sensor.attrib['val']+"\", \"humidity\":\""+sensor.attrib['val2']+"\"}"
            client.publish("papago/"+sensorname+"/state", payload=jsonstring, qos=0, retain=True)
        time.sleep(REFRESHSECONDS)
except Exception as e:
    print("Error retrieving papago data: "+e)
finally:
    print("going into finally now")
    time.sleep(5)
    client.publish("papago/online", payload="0", qos=0, retain=True)
    print("should have published online here")
