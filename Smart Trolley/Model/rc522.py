import random
import json

# with open("./json/image.json", "r") as file:
#         data = json.load(file)

data = []
class RC522():
    def __init__(self) -> None:
        self.id = 0
        self.isscanned = False

    def read(self):
        # scanned = random.choice([True,False])
        current_item = data[self.id]
        # self.text = json.dumps(current_item)
        self.id = self.id + 1 if self.id < 9 else 0
        print(self.id, "here")
        scanned = True
        print("RFID Scanned status", scanned)
        input("Just wait a bit so I know you are running in the background.....\n")
        
        return self.id, self.text
        