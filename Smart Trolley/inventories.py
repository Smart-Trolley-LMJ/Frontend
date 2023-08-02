import os
from Custom_Widgets.Widgets import *
from UI.Images.ui_interface import Ui_MainWindow
from Pages.Inventory.food import foodPage
from Pages.Inventory.alcohol import alcoholPage
from Pages.Inventory.clothes import ClothesPage
from Pages.Inventory.gadgets import gadgetsPage
from Pages.Inventory.cosmetics import cosmeticsPage


CURRENT_WORKING_DIRECTORY = os.getcwd()



class Inventories():
    def __init__(self, json_data, ui):
        self.foodData = [item for item in json_data if "food" in item["category"].lower()]
        self.drinkData = [item for item in json_data if "drinks" in item["category"].lower()]
        self.clothesData = [item for item in json_data if "clothes" in item["category"].lower()]
        self.cosmeticsData = [item for item in json_data if "cosmetics" in item["category"].lower()]
        self.gadgetsData = [item for item in json_data if "gadgets "in item["category"].lower()]

        self.food = foodPage(self.foodData, ui)
        self.alcohol = alcoholPage(self.drinkData, ui) # Alcohol is now drinks
        self.nonAlcohol = ClothesPage(self.clothesData, ui) # Non Alcohol is now clothes
        # self.toiletries = toiletriesPage(self.toiletriesData, ui)
        self.cosmetics = cosmeticsPage(self.cosmeticsData, ui)


        