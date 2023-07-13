#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import json
from time import sleep

reader = SimpleMFRC522()

with open("../json/items.json", "r") as file:
        data = json.load(file)


try:
    for item in data:
            item = json.dumps(item)
            print("Now place your tag to write")
            reader.write(item)
            sleep(2)
            print("Written")
finally:
            GPIO.cleanup()