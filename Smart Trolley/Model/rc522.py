import random
import json

# with open("./json/image.json", "r") as file:



class RC522():
    def __init__(self) -> None:
        self.id = -1
        self.isscanned = False

        self.data = ["ea590116-2b4d-4b8d-b3e5-6f42c35dec03"
                     ,"e2edf332-be6f-4974-a439-567e1d38c9c8",
"ea590116-2b4d-4b8d-b3e5-6f42c35dec03",
"52fed6b3-8ff2-43c1-ad0f-c1c61ecf1b13",
"780e7534-62fb-4c55-acc6-166e57b7ada8",
"6cee019c-b5b6-41c1-a542-6c160370de30",
"79ec490a-5ea6-4c76-86c8-7b795106d8e0",
"143846de-2f57-42d9-896e-bc4eec4864eb",
"16e7d259-450b-4ad3-8183-1f5d93563bac",
]

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
        