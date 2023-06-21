
from os import getcwd
from UI.Images.ui_interface import Ui_MainWindow
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *

CURRENT_WORKING_DIRECTORY = getcwd()
products = [{
    "image_path": "nutrisnax.jfif",
    "label": "nutrisnax",
    "category": "food and drinks",
    "location": "Aisle ",
    "cost": "10.00"
},
{
    "image_path": "coca cola.jfif",
    "label": "Coke",
    "category": "food and drinks",
    "location": "Aisle ",
    "cost": "10.00"
}]

class Budget():
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        # Add item to list
        self.ui.addToListBtn.clicked.connect(self.add_item)

    def add_item(self, name):
        row_count = self.ui.shoppingTable.rowCount()
        name = self.ui.item_edit.displayText()
        quantity = int(self.ui.quantity_edit.displayText())
        unit_cost = 5
        cost = quantity * unit_cost

        # Check if the item already exists in the table
        for row in range(row_count):
            item_name = self.ui.shoppingTable.item(row, 0).text()
            if item_name == name:
                # Item already exists, increment quantity and recalculate cost
                current_quantity = int(self.ui.shoppingTable.item(row, 1).text())
                new_quantity = current_quantity + quantity
                self.ui.shoppingTable.setItem(row, 1, QTableWidgetItem(str(new_quantity)))

                # current_cost = int(self.ui.shoppingTable.item(row, 4).text())
                new_cost = new_quantity * unit_cost
                self.ui.shoppingTable.setItem(row, 2, QTableWidgetItem(str(new_cost)))
                return

        # Item does not exist, add a new row to the table
        self.ui.shoppingTable.setRowCount((row_count + 1))
        self.ui.shoppingTable.setItem(row_count, 0, QTableWidgetItem(name))
        self.ui.shoppingTable.setItem(row_count, 1, QTableWidgetItem(str(quantity)))
        self.ui.shoppingTable.setItem(row_count, 2, QTableWidgetItem(str(unit_cost)))
        # self.ui.shoppingTable.setItem(row_count, 4, QTableWidgetItem(str(cost)))

        # Clear text boxes
        self.ui.item_edit.setText("")
        self.ui.quantity_edit.setText("")


