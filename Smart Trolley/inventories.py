import os
from Custom_Widgets.Widgets import *
from UI.Images.ui_interface import Ui_MainWindow
from Pages.Inventory.food import foodPage
from Pages.Inventory.alcohol import DrinkPage
from Pages.Inventory.clothes import ClothesPage
from Pages.Inventory.gadgets import gadgetsPage
from Pages.Inventory.cosmetics import cosmeticsPage
from Pages.Inventory.health import healthPage


CURRENT_WORKING_DIRECTORY = os.getcwd()



class Inventories():
    def __init__(self, json_data, ui):
        self.foodData = [item for item in json_data if "food" in item["category"].lower()]
        self.drinkData = [item for item in json_data if "drinks" in item["category"].lower()]
        self.clothesData = [item for item in json_data if "clothes" in item["category"].lower()]
        self.cosmeticsData = [item for item in json_data if "cosmetics" in item["category"].lower()]
        self.gadgetsData = [item for item in json_data if "electronics "in item["category"].lower()]
        self.healthData = [item for item in json_data if "health "in item["category"].lower()]

        self.food = foodPage(self.foodData, ui)
        self.drinks = DrinkPage(self.drinkData, ui) # Alcohol is now drinks
        self.clothes = ClothesPage(self.clothesData, ui) # Non Alcohol is now clothes\
        self.cosmetics = cosmeticsPage(self.cosmeticsData, ui)
        self.gadgets = gadgetsPage(self.gadgetsData, ui)
        self.health = healthPage(self.healthData, ui)
        


        