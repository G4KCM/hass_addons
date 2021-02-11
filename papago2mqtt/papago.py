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
lst = tree.findall('.//{http://www.papouch.com/xml/papago/act}sns')
for item in lst:
    sensorname = item.attrib['name'] 
    client.publish("homeassistant/sensor/papago_"+sensorname.lower().replace(" ", "_")+"_temp/config", "{\"name\":\"Papago "+ sensorname +" Temperature\",\"platform\":\"mqtt\",\"state_topic\":\"/papago/temps.json\",\"unit_of_measurement\":\"°C\",\"value_template\":\"{{ value_json."+sensorname.lower().replace(" ", "_")+"_temp }}\"}" ,qos=0,retain=True)
    client.publish("homeassistant/sensor/papago_"+sensorname.lower().replace(" ", "_")+"_hum/config", "{\"name\":\"Papago "+ sensorname +" Humidity\",\"platform\":\"mqtt\",\"state_topic\":\"/papago/temps.json\",\"unit_of_measurement\":\"%\",\"value_template\":\"{{ value_json."+sensorname.lower().replace(" ", "_")+"_hum }}\"}" ,qos=0,retain=True)

def settemps():
    opener = urllib.request.build_opener()
    jsonstring = "{" 
    tree = ET.parse(opener.open("http://%s/fresh.xml" % PAPAGOIP))
    for sensor in tree.iter('{http://www.papouch.com/xml/papago/act}sns'):
        sensorname = sensor.attrib['name'].lower().replace(" ", "_")
        if len(jsonstring) > 1:
            jsonstring += ","
        jsonstring += "\""+sensorname+"_temp\":"
        jsonstring += "\""+sensor.attrib['val']+"\""
        jsonstring += ",\""+sensorname+"_hum\":"
        jsonstring += "\""+sensor.attrib['val2']+"\""
    jsonstring += "}"
    client.publish("/papago/temps.json", payload=jsonstring, qos=0, retain=True)

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(settemps, 'interval', seconds=REFRESHSECONDS)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass