# Main file where the script is compiled together

import paho.mqtt.client as mqtt
import time
import requests
import json
from pprint import pprint
from config import server, database, username, password, driver, cnxn, cursor, API_KEY, NET_ID, SERIAL_CAM, broker, topic, AUTH_TOKEN
import pyodbc
global url_link

# connection notification that the script is running
def on_connect(client, userdata, flags, rc):
    print("connected with code: " + str(rc))
    client.subscribe(topic) #Subscribe to desired topic, this is where the camera will listen to the publisher


# On message response, trigger the code
def on_message(client, userdata, msg):
    # print(str(msg.payload))
    global m_decode
    m_decode = str(msg.payload.decode("utf-8", "ignore"))
    print(m_decode)
    if m_decode == "1":  # if message "1" is triggered, then the script will execute the code below in sequence

        snapshot()



# Takes a snapshot from the camera
def snapshot():


    headers = {
        'X-Cisco-Meraki-API-Key': API_KEY, }

    try:
        response = requests.post(
            'https://api.meraki.com/api/v0/networks/' + NET_ID + '/cameras/' + SERIAL_CAM + '/snapshot',
            headers=headers)
    except requests.exceptions.RequestException as e:
        print("Error: %s" % (e))

    data = response.json()
    url_link = data['url']
    print(url_link)
    
    time.sleep(5)
    downloadpic(url_link)
    time.sleep(3)
    #api()


# Downloads the snapshot from the camera
def downloadpic(link):
    Picture_request = requests.get(link)
    print(Picture_request)
    if Picture_request.status_code == 200:
        with open(r"meraki.jpg", 'wb') as f:
            f.write(Picture_request.content)
            
            api()

    
# Opens the picture to read the license plate
def api():
    with open(r'meraki.jpg', 'rb') as fp:
        response = requests.post(
            'https://platerecognizer.com/api/plate-reader/',
            files=dict(upload=fp),
            headers={'Authorization': AUTH_TOKEN})

    data = response.json()
    # Extracts the plate number and timestamp from the API, and populated the data in the desired table of azure SQL DB
    for l in data["results"]:
        pprint(l['plate'])
        pprint(data)
        
        Base = "INSERT INTO {DB PATH} (PlateNumber, arrivalTime) VALUES ('{}', '{}')" 
        query = Base.format(str(l['plate']), str(data['timestamp']))
        
        cursor.execute(query)
        
    
       
        cnxn.commit()
print("Insertion is completed")

# Connects the broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)

client.loop_forever()