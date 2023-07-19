import os
from Custom_Widgets.Widgets import QWidget, QGridLayout, QLabel, QPixmap
from UI.Images.ui_interface import Ui_MainWindow
from Model.items import Product
import json
import requests
CURRENT_WORKING_DIRECTORY = os.getcwd()
from UI.Images.item_card import Ui_ItemCard  # Import the generated Python code for the item card UI


class ItemCard(QWidget):
    def __init__(self, data):
        super().__init__()
        self.ui = Ui_ItemCard()
        self.ui.setupUi(self)
        self.populate_data(data)
        
        

    def populate_data(self, data):
        # Set the data values to the widgets in the item card frame
        self.image_data = requests.get(data["image_url"]).content
        pixmap = QPixmap()
        pixmap.loadFromData(self.image_data)
        self.ui.label_68.setPixmap(pixmap)
        self.ui.label_69.setText((f'<html><head/><body><p><span style=" font-size:10pt;">{data["description"]}</span></p><p><span style=" font-size:10pt;">GHS{data["price"]}</span></p></body></html>'))

class NonAlcoholPage(QWidget):
    def __init__(self, json_data: Product, ui):
        super(QWidget, self).__init__()
        self.ui : Ui_MainWindow = ui
        self.data = json_data
        self.grid = QGridLayout()
        # self.ui.foodScrollArea.setLayout(self.grid)
        self.ui.DrinksScrollAreaWidgetContents.setLayout(self.grid)
        self.display_grid(self.data)
        self.ui.lineEdit_2.setText('')
        self.ui.lineEdit_2.textChanged.connect(self.filter_data)
    
        


    def display_grid(self, filtered_data):
        row = 0
        column = 0

        # Clear the layout
        for i in reversed(range(self.grid.count())):
            item = self.grid.itemAt(i)
            widget = item.widget()
            if widget:
                self.grid.removeWidget(widget)
                widget.setParent(None)
            # Iterate over the JSON data and create duplicated item card frames
        for item_data in filtered_data:
            item_card = ItemCard(item_data)
            self.grid.addWidget(item_card, row, column)
            column += 1

            if column == 3:
                column = 0
                row += 1

    def filter_data(self):
        search_text = self.ui.lineEdit_2.text().lower()
        filtered_data = [item for item in self.data if search_text in item["description"].lower()]
        self.display_grid(filtered_data)
        