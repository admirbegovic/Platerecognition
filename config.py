#
#	Copyright (c) 2020 Cisco and/or its affiliates.
#
#	This software is licensed to you under the terms of the Cisco Sample
#	Code License, Version 1.1 (the "License"). You may obtain a copy of the
#	License at
#
#		       https://developer.cisco.com/docs/licenses
#
#	All use of the material herein must be in accordance with the terms of
#	the License. All rights not expressly granted by the License are
#	reserved. Unless required by applicable law or agreed to separately in
#	writing, software distributed under the License is distributed on an "AS
#	IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#	or implied.
#

import pyodbc
import paho.mqtt.client as mqtt
# Credentials for your DB goes here
server = ''
database = ''
username = ''
password = ''
        
## Connects and makes it possible to query the DB by using the credentials from the config file
driver='{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

# Meraki camera credentials, insert values inside ''
API_KEY = ''
NET_ID = ''
SERIAL_CAM = ''
        
        
## MQTT settings for the broker & topic subscribe. Type in the broker IP in '' for broker and desired topic you want the camera to subscribe to

broker = ''

topic = ''

# Plate recognition API settings

AUTH_TOKEN = ''
