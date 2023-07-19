import random
import json

# with open("./json/image.json", "r") as file:



class RC522():
    def __init__(self) -> None:
        self.id = -1
        self.isscanned = False
        self.data = ["003b5337-2b33-4249-a183-3c845508878f",
"03c44514-48a6-4c07-bfbd-d54d8c0418ba",
"0755edda-f246-459a-90e9-7c43ddf90fb2",
"0e03a34a-3e90-48f6-8dfd-446c1c9fd71c",
"0e356799-ce6b-456c-9b9f-e220f22b0b7d",
"101dbae3-0697-4f9f-ae5b-ba8817c9cd18",
"143846de-2f57-42d9-896e-bc4eec4864eb",
"16e7d259-450b-4ad3-8183-1f5d93563bac",]

    def read(self):
        # scanned = random.choice([True,False])
        # current_item = self.data[self.id]
        # self.text = json.dumps(current_item)
        self.id = self.id + 1 if self.id < 6 else 0
        print(self.id, "here")
        scanned = True
        print("RFID Scanned status", scanned)
        input("Just wait a bit so I know you are running in the background.....\n")
        
        return self.id, self.data[self.id]
        