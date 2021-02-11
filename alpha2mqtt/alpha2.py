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
ALPHA2IPS = sys.argv[5]
REFRESHSECONDS = int(sys.argv[6])

client = mqtt.Client()
client.username_pw_set(MQTTUSERNAME, MQTTPASSWORD)
client.connect_async(MQTTBROKERHOST, MQTTBROKERPORT, 60)
client.loop_start()

opener = urllib.request.build_opener()
alphas = ALPHA2IPS.split(';')
for alpha in alphas:
    tree = ET.parse(opener.open("http://%s/data/static.xml" % alpha))
    lst = tree.findall('.//HEATAREA_NAME')
    for item in lst:
        client.publish("homeassistant/sensor/alpha2_"+item.text.lower()+"/config", "{\"name\":\"Alpha2 "+ item.text +" Temperature\",\"platform\":\"mqtt\",\"state_topic\":\"/alpha2/temps.json\",\"unit_of_measurement\":\"°C\",\"value_template\":\"{{ value_json."+item.text+" }}\"}" ,qos=0,retain=True)

def settemps():
    opener = urllib.request.build_opener()
    jsonstring = "{" 
    for alpha in alphas:
        tree = ET.parse(opener.open("http://%s/data/static.xml" % alpha))
        for heatarea in tree.iter('HEATAREA'):
            if len(jsonstring) > 1:
                jsonstring += ","
            for element in heatarea:
                if element.tag == "HEATAREA_NAME":
                    jsonstring += "\""+element.text+"\":"
                if element.tag == "T_ACTUAL":
                    jsonstring += "\""+element.text+"\""
    jsonstring += "}"
    client.publish("/alpha2/temps.json", payload=jsonstring, qos=0, retain=True)

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(settemps, 'interval', seconds=REFRESHSECONDS)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass