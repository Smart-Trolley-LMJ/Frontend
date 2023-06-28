import random

class RC522():
    def __init__(self) -> None:
        self.text = 'This is an rfid tag'
        self.id = 1
        self.isscanned = False

    def read(self):
        scanned = random.choice([True,False])
        print("RFID Scanned status", scanned)
        if scanned:
            return self.id, self.text
        return 0,''