import requests
from typing import NamedTuple

class StoreItems():
    # The API endpoint
    def __init__(self) -> None:
        url = "https://smtrolley.onrender.com/inventories/"
        self.response = requests.get(url)
        self.response_json = self.response.json()
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
