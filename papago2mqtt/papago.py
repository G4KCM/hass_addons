import os
import sys
import json
import urllib.request
import xml.etree.ElementTree as ET
import paho.mqtt.client as mqtt
from apscheduler.schedulers.blocking import BlockingScheduler

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

opener = urllib.request.build_opener()
tree = ET.parse(opener.open("http://%s/fresh.xml" % PAPAGOIP))
dev = tree.find('.//{http://www.papouch.com/xml/papago/act}status').attrib['location']
lst = tree.findall('.//{http://www.papouch.com/xml/papago/act}sns')
for item in lst:
    id = item.attrib['id']
    sensorname = item.attrib['name']
    client.publish("homeassistant/sensor/"+dev+"/temp"+id+"/config", "{\"name\":\""+sensorname+" Temperature\",\"device_class\":\"temperature\",\"state_topic\":\"papago/"+sensorname.lower().replace(" ", "_")+"/state\",\"value_template\": \"{{ value_json.temperature}}\",\"unit_of_measurement\":\"°C\",\"unique_id\":\""+dev+"_T_"+id+"\", \"device\": {\"identifiers\":[\""+dev+"\"], \"name\":\""+dev+"\", \"manufacturer\":\"Papouch\", \"model\":\"Papago 2TH WIFI\"}}" ,qos=0,retain=True)
    client.publish("homeassistant/sensor/"+dev+"/hum"+id+"/config", "{\"name\":\""+sensorname+" Humidity\",\"device_class\":\"humidity\",\"state_topic\":\"papago/"+sensorname.lower().replace(" ", "_")+"/state\",\"value_template\": \"{{ value_json.humidity}}\",\"unit_of_measurement\":\"%\",\"unique_id\":\""+dev+"_H_"+id+"\", \"device\": {\"identifiers\":[\""+dev+"\"], \"name\":\""+dev+"\", \"manufacturer\":\"Papouch\", \"model\":\"Papago 2TH WIFI\"}}" ,qos=0,retain=True)

def settemps():
    opener = urllib.request.build_opener()
    tree = ET.parse(opener.open("http://%s/fresh.xml" % PAPAGOIP))
    for sensor in tree.iter('{http://www.papouch.com/xml/papago/act}sns'):
        sensorname = sensor.attrib['name'].lower().replace(" ", "_")
        jsonstring = "{\"temperature\":\""+sensor.attrib['val']+"\", \"humidity\":\""+sensor.attrib['val2']+"\"}"
        client.publish("papago/"+sensorname+"/state", payload=jsonstring, qos=0, retain=True)

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(settemps, 'interval', seconds=REFRESHSECONDS)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass