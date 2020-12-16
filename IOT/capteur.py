#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
from pprint import pprint
import json
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIR_PIN = 9
GPIO.setup(PIR_PIN, GPIO.IN)
with open('/etc/SmartClassroom/config.json') as json_file:
     data=json.load(json_file)
print('Starting up the PIR Module (click on STOP to exit)')
time.sleep(1)
print ('Ready')
v=data['MeteoTextFile']
file=open(v,"r")
i=file.read()
os.popen('espeak -p 1 -a 1000 -g 10 -v fr+f3 "'+i+'" --stdout | aplay')
time.sleep(1)
