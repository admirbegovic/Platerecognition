# Meraki MV Sense Plate Recognizer
The goal of this project is to automatically detect the license plate on a car by the MV72 camera and save the results to an SQL DB.

# License
This license is free, enables our customers and partners to do everything they need to do with the code, but also provides Cisco the limitations and protections we need in order to keep the policy and process requirements for sample code sharing as lightweight and streamlined as possible.

# Installation
Requirements: Python 3, Active Azure SQL DB, Microsoft SQL Server Management Sutdio, Meraki MV sense API, MQTT Broker, MQTT.fx, platerecognizer API.

1. You need to have python 3 installed on your PC to run the script
2. An active SQL DB is needed to store the information
3. Registration on platerecognizer.com is required for the API token (with an optional paid subscription if you need more lookups) 
4. Make sure that MV sense API is enabled on the camera and add an MQTT broker
5. Download MQTT.fx client. We will use the client to connected to the broker and trigger the running script with a command
6. Enter the required information and credentials in the config.py file (open it with a text editor, e.g notepad++)
7. Save the config.py file and run the script (main.py)
8. Launch the MQTT.fx client. Connect to the broker, type in the topic that the camera is subscribing on in the narrow field. Type 1 and publish the command
9. Use SQL management studio to query the DB for the insertion


Note: Scripts are expected to be executed in a trusted environment with proper security settings


