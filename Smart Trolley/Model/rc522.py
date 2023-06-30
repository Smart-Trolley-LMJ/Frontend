import random
import time

class RC522():
    def __init__(self) -> None:
        self.text = 'This is an rfid tag'
        self.id = random.randint(1,3)
        self.isscanned = False

    def read(self):
        scanned = random.choice([True,False])
        print("RFID Scanned status", scanned)
        input("Just wait a bit so I know you are running in the background.....\n")
        if scanned:
            return self.id, self.text
        return 1,'Waakye'