import random
import json

# with open("./json/image.json", "r") as file:



class RC522():
    def __init__(self) -> None:
        self.id = -1
        self.isscanned = False
        





# 7bb9fc34-be0d-4c1d-b07f-d3f53dbf4cad
# a872b89f-fd6c-43b4-96cf-885450135449
# ba137151-25c1-4460-af60-7823add63263
# c342cf11-4d81-4427-8c95-edc3d28f8e88
# c545824d-80d0-49d8-8693-8a0859e3961c
# ee11fda6-f763-49f7-97c5-566ede0fbd36

        self.data = ["64687fd6-27f5-4451-8d2b-311406ee88e6"
                     ,"b9e5e9c3-cc5c-4d59-9355-ce4f8065f69c",
"18aa126d-ea8a-432a-adf7-84285d3f3daf",
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
        