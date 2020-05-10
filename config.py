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
