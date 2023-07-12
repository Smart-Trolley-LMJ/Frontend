import os
from Custom_Widgets.Widgets import QWidget, QGridLayout, QLabel, QPixmap
from UI.Images.ui_interface import Ui_MainWindow
from Model.items import Product
import json
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
        pixmap = QPixmap('UI\Images\\food and drinks\\coca cola.jpeg')
        self.ui.label_68.setPixmap(pixmap)
        self.ui.label_69.setText((f'<html><head/><body><p><span style=" font-size:10pt;">{data["name"]}</span></p><p><span style=" font-size:10pt;">GHS{data["price"]}</span></p></body></html>'))

class foodPage(QWidget):
    def __init__(self, json_data: Product, ui):
        super(QWidget, self).__init__()
        self.ui : Ui_MainWindow = ui
        self.data = json_data
        self.grid = QGridLayout()
        # self.ui.foodScrollArea.setLayout(self.grid)
        self.ui.FoodScrollAreaWidgetContents.setLayout(self.grid)
        self.display_grid(self.data)
        # self.ui.searchBar.textChanged.connect(self.filter_data)
    
        


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

        # for item in filtered_data:

        #     # Create QPixmap from image path
        #     pixmap = QPixmap(item['image'])

        #     # Create QLabel for the image
        #     image_label = QLabel()
        #     image_label.setPixmap(pixmap)
        #     self.grid.addWidget(image_label, row, column)

        #     # Create QLabel for the text
        #     text_label = QLabel(json.dumps(item))
        #     self.grid.addWidget(text_label, row+1, column)

        #     column += 1

        #     # If the current row is filled, move to the next row and reset column to 0
        #     if column == 3:
        #         column = 0
        #         row += 2

    def filter_data(self):
        search_text = self.ui.searchBar.toPlainText().lower()
        filtered_data = [item for item in self.data if search_text in item["name"].lower()]
        # print(filtered_data)
        self.display_grid(filtered_data)
        