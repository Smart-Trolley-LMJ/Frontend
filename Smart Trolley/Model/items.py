import requests
from typing import NamedTuple
import os

class StoreItems():
    # The API endpoint
    def __init__(self) -> None:
        # url = "https://smtrolley.onrender.com/inventories/"
        self.response_json = []
        self.url = os.environ.get("URL")
        url = f"{self.url}/inventories/"
        try:
            self.response = requests.get(url)
            self.response_json = self.response.json()
        except:
            print("An error occurred in retrieving items from the database")
        # print(self.response_json['products'][0])
        
class Product(NamedTuple):
    date_added: str
    name: str
    price: float
    quantity: int
    category: str
    product_id: str
    description: str
    image: str
    weight: float

# # The API endpoint
# url = "https://smtrolley.onrender.com/inventories"

# # A GET request to the API
# response = requests.get(url)

# # Print the response
# response_json = response.json()
# names = [product['category'] for product in response_json]
# print(set(names))# The API endpoint
