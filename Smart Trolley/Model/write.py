#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import json

reader = SimpleMFRC522()

with open("../json/image.json", "r") as file:
        data = json.load(file)

for item in data:
    try:
            item = json.dumps(item)
            text = input('New data:')
            print("Now place your tag to write")
            reader.write(item)
            print("Written")
    finally:
            GPIO.cleanup()