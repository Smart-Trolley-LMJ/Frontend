import random
import json

# with open("./json/image.json", "r") as file:



class RC522():
    def __init__(self) -> None:
        self.id = -1
        self.isscanned = False

        self.data = ["84981e68-6da4-427b-a667-e7457b45824c","a140b29c-9ced-4342-a4e1-a288d51fe51a",
                     "fb7e9e52-0b72-400b-b771-04ed81d4e481","fb7e9e52-0b72-400b-b771-04ed81d4e481","5294986d-2361-45a9-abe1-b5386f95ff23",
                     "7d7759dc-88fd-4d76-81a9-7583a9c33b67","5294986d-2361-45a9-abe1-b5386f95ff23",]

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
        