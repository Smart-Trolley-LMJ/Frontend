import os
from Custom_Widgets.Widgets import *
from UI.Images.ui_interface import Ui_MainWindow
from Pages.Inventory.food import foodPage
from Pages.Inventory.alcohol import alcoholPage
from Pages.Inventory.nonAlcohol import NonAlcoholPage
from Pages.Inventory.toiletries import toiletriesPage
from Pages.Inventory.cosmetics import cosmeticsPage


CURRENT_WORKING_DIRECTORY = os.getcwd()



class Inventories():
    def __init__(self, json_data, ui):
        self.foodData = [item for item in json_data if "food" in item["category"].lower()]
        self.alcoholData = [item for item in json_data if "alcoholic" in item["category"].lower()]
        self.nonAlcoholData = [item for item in json_data if "non-alcoholic" in item["category"].lower()]
        # self.cosmeticsData = [item for item in json_data if "cosmetics" in item["category"].lower()]
        # self.toiletriesData = [item for item in json_data if "toiletries "in item["category"].lower()]

        self.food = foodPage(self.foodData, ui)
        self.alcohol = alcoholPage(self.alcoholData, ui)
        self.nonAlcohol = NonAlcoholPage(self.nonAlcoholData, ui)
        # self.toiletries = toiletriesPage(self.toiletriesData, ui)
        # self.cosmetics = cosmeticsPage(self.cosmeticsData, ui)


        